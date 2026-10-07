import socket
import threading
import sqlite3
import random
import queue
import sys

HOST, PORT = "127.0.0.1", 5000
POLY = 0x04C11DB7          # CRC-32 generator polynomial
NOISE = 0.30               # probability that a frame is corrupted


# ---------- Text <-> Binary ----------
def text_to_bits(text):
    return "".join(format(b, "08b") for b in text.encode("utf-8"))


def bits_to_text(bits):
    data = bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8))
    return data.decode("utf-8", errors="replace")


# ---------- CRC generation and verification ----------
def mod2_divide(bits):
    """Modulo-2 (XOR) division of a bit string by the generator."""
    gen = (1 << 32) | POLY
    reg = 0
    for bit in bits:
        reg = (reg << 1) | int(bit)
        if reg >> 32:                 # leading bit is 1 -> XOR
            reg ^= gen
    return reg


def make_frame(text):
    data = text_to_bits(text)
    crc = mod2_divide(data + "0" * 32)       # append 32 zeros, divide
    return data + format(crc, "032b")        # frame = data + CRC


def verify_frame(frame):
    return mod2_divide(frame) == 0           # zero remainder = no error


# ---------- Noise (error injection) ----------
def add_noise(frame):
    bits = list(frame)
    for i in random.sample(range(len(bits)), random.randint(1, 4)):
        bits[i] = "1" if bits[i] == "0" else "0"
    return "".join(bits)


# ---------- Database ----------
def init_db(name):
    db = sqlite3.connect(name, check_same_thread=False)
    db.execute("""CREATE TABLE IF NOT EXISTS messages (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  message TEXT, received_crc TEXT,
                  computed_crc TEXT, status TEXT)""")
    return db


# ---------- Receiving ----------
def receive_loop(sock, db, replies, lock):
    for line in sock.makefile("r"):
        line = line.strip()
        if not line.startswith("MSG:"):
            replies.put(line)                # ACK / NAK for our message
            continue
        frame = line[4:]
        data, received = frame[:-32], frame[-32:]
        computed = format(mod2_divide(data + "0" * 32), "032b")
        ok = verify_frame(frame)
        text = bits_to_text(data)
        db.execute("INSERT INTO messages (message, received_crc, "
                   "computed_crc, status) VALUES (?, ?, ?, ?)",
                   (text, hex(int(received, 2)), hex(int(computed, 2)),
                    "VALID" if ok else "ERROR"))
        db.commit()
        if ok:
            print(f"\nFriend: {text}   [CRC OK]")
        else:
            print("\n[CRC ERROR] Corrupted message detected - NAK sent")
        print("You: ", end="", flush=True)        # redraw the prompt
        with lock:
            sock.sendall(b"ACK\n" if ok else b"NAK\n")


# ---------- Sending with retransmission ----------
def send_message(sock, text, replies, lock):
    frame = make_frame(text)
    sent = add_noise(frame) if random.random() < NOISE else frame
    for attempt in range(1, 4):
        with lock:
            sock.sendall(("MSG:" + sent + "\n").encode())
        if replies.get(timeout=5) == "ACK":
            print("[Delivered - CRC verified by receiver]")
            return
        print(f"[NAK received - retransmitting, attempt {attempt}]")
        sent = frame                         # resend the original frame
    print("[Message could not be delivered]")


# ---------- Main ----------
def main():
    role = sys.argv[1] if len(sys.argv) > 1 else "server"
    if role == "server":
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print("Waiting for a friend to connect...")
        sock, _ = server.accept()
    else:
        sock = socket.create_connection((HOST, PORT))
    db = init_db(f"crc_chat_{role}.db")
    replies, lock = queue.Queue(), threading.Lock()
    threading.Thread(target=receive_loop, daemon=True,
                     args=(sock, db, replies, lock)).start()
    print("Connected. Type a message (or 'exit' to quit).")
    while True:
        text = input("You: ")
        if text.lower() == "exit":
            break
        send_message(sock, text, replies, lock)
    sock.close()


if __name__ == "__main__":
    main()
