# 🕵️‍♀️ Text Hiding in Images using Steganography (Cybersecurity Internship Project)

This project demonstrates a basic but powerful steganography technique: **hiding secret text inside images** using the **Least Significant Bit (LSB)** method.  
It's developed as part of my **Cybersecurity Internship** to explore data hiding and privacy techniques.

![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Repo Size](https://img.shields.io/github/repo-size/suma-1506/steganography-project)
![Last Commit](https://img.shields.io/github/last-commit/suma-1506/steganography-project)
![Stars](https://img.shields.io/github/stars/suma-1506/steganography-project?style=social)

---

## 📂 Project Structure
```bash
steganography_project/
│
├── hide_text.py # Function to hide secret message inside an image
├── reveal_text.py # Function to reveal hidden message from an image
├── run_me.py # One-click script to hide & reveal the message
├── requirements.txt # Required libraries (mainly pillow)
└── sample_image.png # Your input image (any .png or .jpg)
```


---

## 🔧 How It Works

- Uses the **LSB (Least Significant Bit)** of pixel RGB values to embed binary form of the secret message.
- Appends a special **EOF marker** to detect end of message.
- Optionally supports a **password key** (currently for consistency; encryption support can be added).

---

## ✅ How to Run the Project

### 🔹 Method 1: Manual Method (Python Shell)

1. Open terminal in the project directory.
2. Start Python shell:

```bash
python
```
3. Run the following:

```bash
from hide_text import hide_text
hide_text("sample_image.png", "output_image.png", "This is the hidden message.", "mypassword123")

from reveal_text import reveal_text
print(reveal_text("output_image.png", "mypassword123"))
```
✅ Output:

```bash
Secret text hidden and saved to 'output_image.png'.
Hidden message: This is the hidden message.
```

### 🔹 Method 2: Automated Method (run_me.py)
1. Open terminal in the project folder.

2. Run:

```bash
python run_me.py
```
✅ Output:

Secret text hidden and saved to 'output_image.png'.
Hidden message: This is the hidden message.

## 🖼️ Supported Image Formats
✅ .png (Recommended)

⚠️ .jpg works, but may reduce accuracy due to compression

## 📦 Installation
Install required libraries:

```bash
pip install -r requirements.txt
```
Only one package is needed:
Pillow (for image processing)

## 🎓 Internship Takeaways
Implemented real steganography from scratch using Python

Learned about binary encoding, pixel manipulation & image formats

Practiced clean coding, modular design, and project documentation

## 🛡️ Disclaimer
This is a basic implementation meant for educational purposes during a cybersecurity internship.
It does not provide strong cryptographic security.

## ✨ Author
Suma Priya Vaddi
IBM Cybersecurity Internship, 2025


