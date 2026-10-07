# CRC-Data-Transfer-System

A Python-based **chatting and data transfer system** that uses **Cyclic Redundancy Check (CRC)** to detect errors during data transmission.

## 📌 Overview

The **CRC Data Transfer System** is a simple Python project that demonstrates how CRC can be integrated into a communication system.

The system allows users to exchange messages while applying **Cyclic Redundancy Check (CRC)** for error detection. Before accepting the received message, the CRC value is verified to determine whether the transmitted data has been corrupted.

This project combines the concepts of:

* 💬 Chatting
* 📡 Data Transfer
* 🔢 CRC Error Detection
* 🐍 Python Programming

## ✨ Features

* 💬 Send and receive messages
* 📡 Transfer data between users
* 🔢 Generate CRC for transmitted data
* 🔍 Verify received data using CRC
* ❌ Detect transmission errors
* 🐍 Simple Python implementation
* 🎓 Useful for understanding CRC and data communication

## 🛠️ Technologies Used

* **Language:** Python 3
* **Concept:** Cyclic Redundancy Check (CRC)
* **Domain:** Computer Networks / Data Communication

## 📂 Project Structure

```text
CRC-Data-Transfer-System/
│
├── CRC_Chat.py
└── README.md
```

The entire application is implemented in a **single Python file: `CRC_Chat.py`**.

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone https://github.com/sushmasundhar07-wq/CRC-Data-Transfer-System.git
```

### Navigate to the Project

```bash
cd CRC-Data-Transfer-System
```

### Run the Application

```bash
python CRC_Chat.py
```

If your system uses `python3`:

```bash
python3 CRC_Chat.py
```

## 🔄 How It Works

The basic communication process is:

```text
       Sender
          │
          │ Message
          ▼
   ┌───────────────┐
   │  CRC Generate │
   └───────────────┘
          │
          │ Message + CRC
          ▼
   ┌───────────────┐
   │ Data Transfer │
   └───────────────┘
          │
          ▼
   ┌───────────────┐
   │  CRC Verify   │
   └───────────────┘
          │
      ┌───┴───┐
      ▼       ▼
   Valid    Invalid
      │       │
      ▼       ▼
  Accept    Error
  Message   Detected
```

### CRC Process

1. The sender enters a message.
2. The message is converted into the required data representation.
3. CRC is calculated for the transmitted data.
4. The message and CRC information are transferred.
5. The receiver performs CRC verification.
6. If the CRC check is successful, the message is accepted.
7. If the CRC check fails, an error is detected.

## 🔢 What is CRC?

**Cyclic Redundancy Check (CRC)** is an error-detection technique used to identify accidental changes in data during transmission or storage.

CRC works by performing binary polynomial division on the data using a predefined generator.

The receiver performs the same calculation on the received data.

```text
CRC Remainder = 0
        ↓
   No Error Detected

CRC Remainder ≠ 0
        ↓
    Error Detected
```

## 💬 Chat System

This project demonstrates how CRC can be applied to a simple chatting/data-transfer scenario.

Instead of simply transferring a message:

```text
Sender → Message → Receiver
```

the system conceptually performs:

```text
Sender
   ↓
Message
   ↓
CRC Generation
   ↓
Message + CRC
   ↓
Transmission
   ↓
CRC Verification
   ↓
Receiver
```

This helps demonstrate how error detection can be incorporated into data communication.

## 🎯 Objectives

The main objectives of this project are:

* To understand the working of CRC.
* To implement CRC using Python.
* To demonstrate error detection during data transmission.
* To understand the basic concepts behind reliable data communication.
* To combine CRC with a simple chatting/data-transfer system.

## 📚 Learning Outcomes

After completing this project, you can understand:

* Cyclic Redundancy Check
* Error detection
* Binary data processing
* Data transmission concepts
* Sender-receiver communication
* Basic Python networking/programming concepts

## 🔮 Future Enhancements

The project can be extended with:

* 🌐 Real-time client-server communication
* 👥 Multiple users
* 📁 File transfer with CRC verification
* ⚠️ Automatic transmission-error simulation
* 📊 CRC calculation visualization
* 🖥️ Graphical User Interface (GUI)
* 🔐 Additional data integrity mechanisms

## 👨‍💻 Author

@SushmaSundhar07

GitHub: **sushmasundhar07-wq**

## 📄 License

This project is created for **educational purposes** to demonstrate CRC-based error detection and data communication using Python.
