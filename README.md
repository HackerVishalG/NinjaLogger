# 🥷 NinjaLogger - Stealthy Recon & Keylogging for Ethical Hackers

![NinjaLogger Banner](![alt text](image.png))

**NinjaLogger** is a **powerful, stealthy, and fully-featured keylogger** designed for **ethical hacking**, **red teaming**, and **research purposes only**. Equipped with keystroke logging, clipboard capture, microphone and screen capture, and system fingerprinting, NinjaLogger provides robust recon capabilities.

> ⚠️ **DISCLAIMER**: This tool is intended strictly for educational and ethical penetration testing use with explicit authorization. Unauthorized use is illegal.

---

## 🚀 Features

- 🔐 **Keystroke Logging**  
- 📋 **Clipboard Data Capture**  
- 🎙️ **Microphone Audio Recording**  
- 📸 **Screenshot Capture**  
- 💻 **System Information Gathering**  
- 🌐 **Public & Private IP Detection**  
- 🔒 **AES Encryption (Fernet)**  
- 📧 **Email Exfiltration (Gmail SMTP)**  
- 🧹 **File Cleanup for OPSEC**

---

## 📁 Project Structure

NinjaLogger/
├── keylogger.py # Main logger script
├── requirements.txt # Dependencies
├── README.md # Project Documentation
├── LICENSE # Open Source License
└── output/
├── key_log.txt
├── screenshot.png
├── audio_info.wav
└── *.enc # Encrypted artifacts


---

## ⚙️ Tech Stack

| Module         | Purpose                          |
|----------------|----------------------------------|
| `pynput`       | Keyboard event listener          |
| `sounddevice`  | Audio capture                    |
| `Pillow`       | Screenshot capture               |
| `requests`     | Public IP + HTTP                 |
| `cryptography` | Fernet encryption                |
| `smtplib`      | Email sending via SMTP           |
| `pywin32`      | Clipboard access on Windows      |
| `scipy`        | Audio file writing               |

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/NinjaLogger.git
cd NinjaLogger
pip install -r requirements.txt

✅ Usage

python keylogger.py

📜 License

This project is licensed under the MIT License.
👨‍💻 Author

HackerxTommy — @HackerVishalG
For ethical and educational use only.
🧠 Educational Use Only

NinjaLogger is a tool for learning, research, and red teaming simulations. Any use beyond legal ethical boundaries is strictly prohibited.