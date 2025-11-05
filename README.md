# 📞 Phone Number Validation CLI Tool

A simple Python command-line tool to validate phone numbers and retrieve basic, non-personal information. It uses the `phonenumbers` library.

## ⚠️ Important Disclaimer

This tool is **NOT** a tracing app. It is designed to help users identify and validate phone numbers from a technical perspective.

* This app **CANNOT** find a person's name, address, or real-time GPS location. This information is strictly protected by privacy laws and is only available to official law enforcement agencies with a legal warrant.
* The purpose of this project is to provide general, publicly available data about a number.

---

## ✨ Features

Based on the provided phone number, this script will tell you:
* **Validity:** If the number is in a valid format.
* **General Region:** The country or general area the number is from.
* **Carrier:** The mobile service provider (e.g., "Airtel", "Jio").
* **Time Zones:** The time zones associated with that number's region.

---

## 🛠️ Requirements

* [Python 3.x](https://www.python.org/)
* The `phonenumbers` Python library

---

## 🚀 How to Use

### 1. Installation

Before running the script, you must install the `phonenumbers` library.

Open your terminal or command prompt and run:
```bash
pip install phonenumbers
```

### 2. Running the Script

1.  Save the code as a Python file (e.g., `validate.py`).
2.  Run the script from your terminal:
    ```bash
    python validate.py
    ```
3.  The script will prompt you to enter a phone number.
4.  **You must include the country code** (e.g., `+91`, `+1`, etc.).

### Example Usage

Here is what you will see when you run the script:

```bash
> python validate.py

Enter phone number with country code (e.g., +91XXXXXXXXXX): +919876543210

--- Information for +919876543210 ---
Valid Number: True
General Region: India
Carrier: Airtel
Time Zones: ('Asia/Kolkata',)
```

### Error Handling

If you enter an invalid or incomplete number, the script will show an error:

```bash
> python validate.py

Enter phone number with country code (e.g., +91XXXXXXXXXX): 12345

Error: (0) The string supplied did not seem to be a phone number. Please enter a valid number with a country code (e.g., +91).
```
