
# 📘 Journal File Operator (Python)

## 📌 Overview
This project is a **Journal File Operator** program written in Python.  
It allows users to **add**, **view**, **search**, and **delete** journal entries using **file handling** concepts.

The project is beginner-friendly and demonstrates core Python concepts such as:
- Classes and Objects
- Constructors
- Functions & Methods
- File Handling
- Exception Handling
- Date & Time usage

---

## 🧠 Concepts Used (Deep Explanation)

### 1️⃣ Class
A **class** is a blueprint for creating objects.

```python
class Journal:
    pass
```

Here, `Journal` is a class that contains all journal-related operations.

---

### 2️⃣ Object
An **object** is an instance of a class.

```python
j = Journal()
```

This object `j` is used to access all methods of the `Journal` class.

---

### 3️⃣ Constructor (`__init__`)
A constructor is used to initialize values when an object is created.

```python
def __init__(self, filename="journal.txt"):
    self.filename = filename
```

- `self.filename` stores the file name where journal entries are saved
- Default file: `journal.txt`

---

### 4️⃣ File Handling
This program uses **file handling** to store data permanently.

#### Writing to File (Append Mode)
```python
with open(self.filename, "a") as file:
    file.write(entry)
```

- `"a"` → Append mode (does not overwrite existing data)
- Used when adding new journal entries

#### Reading from File
```python
with open(self.filename, "r") as file:
    data = file.read()
```

- `"r"` → Read mode
- Used to view and search entries

---

### 5️⃣ Date & Time
The program records the date and time of each journal entry.

```python
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

This helps track **when** an entry was added.

---

### 6️⃣ Exception Handling
To avoid program crashes, `try-except` is used.

```python
try:
    # risky code
except FileNotFoundError:
    print("File not found")
```

Handles:
- File not found errors
- Invalid user input

---

## ⚙️ Features

### ✏️ Add Entry
- Takes user input
- Adds timestamp
- Saves entry to file

### 📖 View Entries
- Displays all saved journal entries

### 🔍 Search Entry
- Searches keyword inside journal file

### ❌ Delete Journal
- Clears all entries from file

---

## 🏗️ Program Structure

```text
Journal File Operator
│
├── Journal (Class)
│   ├── __init__()
│   ├── add_entry()
│   ├── view_entries()
│   ├── search_entry()
│   └── delete_entries()
│
└── main()
```

---

## ▶️ How to Run the Program

1. Make sure Python is installed
2. Save the program file
3. Open terminal / command prompt
4. Run:

```bash
python journal.py
```

---
