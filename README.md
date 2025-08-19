# 🔐 Caesar Cipher Encryption/Decryption Tool

A secure Python implementation of the Caesar Cipher algorithm with password protection and encryption storage capabilities.

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Security Notes](#security-notes)
- [Troubleshooting](#troubleshooting)

## ✨ Features

- 🔒 Encrypt messages using Caesar Cipher algorithm
- 🔓 Decrypt messages with password authentication
- 🎲 Option to use random shift values for enhanced security
- 🛡️ Strong password enforcement (8+ chars, upper/lowercase, digits, special characters)
- 💾 Secure storage of encrypted messages with associated passwords
- 🚫 Protection against incorrect password attempts

## 📋 Requirements

- Python 3.x
- No external dependencies (uses only standard Python libraries)

## 🔧 Installation

1. Clone or download the Python script to your local machine
2. Ensure Python 3.x is installed on your system
3. (Optional) Verify installation by running:
   ```bash
   python --version
   ```

## 🚀 Usage

1. Run the program:
   ```bash
   python caesar_cipher.py
   ```

2. Follow the interactive menu prompts:

### Encryption Process:
1. Select option `1` to encrypt a message
2. Enter your message when prompted
3. Choose whether to use a random shift or custom shift value (1-25)
4. Set a strong password that meets the security requirements

### Decryption Process:
1. Select option `2` to decrypt a message
2. Enter the encrypted message exactly as it was provided
3. Provide the correct password associated with the encryption

### Example Session:
```
==========================================================
🔐 Welcome to the Caesar Cipher Program Encryption and Decryption Python program 🔐
==========================================================

Options: 
1. Encrypt
2. Decrypt
3. Exit
Choose an option (1/2/3): 1

Enter the message to encrypt: Hello World!
Do you want to use a random shift? (yes/no): yes
🔢 Random Shift Generated: 17
Set your encryption password: SecurePass123!

🔒 Encryption Successful! 🔓
==================================================
Encrypted Message: Yvccf Nficu!
==================================================
```

## 🧠 How It Works

### Caesar Cipher Algorithm
- Each letter in the plaintext is shifted a fixed number of positions down the alphabet
- Non-alphabetic characters remain unchanged
- The shift value determines the encryption strength

### Password Requirements
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (!@#$%^&*(),.?":{}|<>)

### Storage Mechanism
- Encrypted messages are stored in memory with associated passwords and shift values
- Data persists only during the current session

## ⚠️ Security Notes

- This implementation is for educational purposes only
- Caesar cipher is not considered secure for modern encryption needs
- Passwords are stored in memory but not in encrypted form
- For real-world security, use industry-standard encryption algorithms

## 🔍 Troubleshooting

### Common Issues:
1. **"Encrypted message not found in storage!"**
   - Ensure you've entered the encrypted message exactly as it was provided
   - Note that the program only remembers messages encrypted during the current session

2. **"Incorrect password! Access denied."**
   - Passwords are case-sensitive; check your input carefully
   - There is no password recovery mechanism

3. **Password validation errors**
   - Ensure your password meets all complexity requirements

4. **Shift value errors**
   - Custom shift values must be integers between 1-25

### Getting Help:
If you encounter issues not covered here, please check:
- Your Python version (requires Python 3.x)
- That you're entering inputs exactly as prompted

---

**Disclaimer**: This tool is intended for educational purposes only. For actual secure communications, use professionally vetted encryption tools.
