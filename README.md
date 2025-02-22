# Secure-Data-Hiding-in-Image-Using-Steganography
# Secure Data Hiding in Image Using Steganography

## Overview
This project demonstrates how to securely hide data within an image using steganography and encryption. The system uses the LSB (Least Significant Bit) method to embed data into the image and AES encryption to ensure the data remains secure. SHA-256 hashing is used to verify data integrity.

## Features
- Hide text data within an image.
- Extract hidden data from the image.
- Encrypt data using AES encryption.
- Verify data integrity using SHA-256 hashing.
- User-friendly command-line interface.

## Requirements
- Python 3.x
- Libraries: OpenCV, Pillow, NumPy, Cryptography

## Installation
1. Clone the repository:
   git clone https://github.com/gangadharrelangi/secure-data-hiding.git
    Install the required libraries:
      pip install opencv-python pillow numpy cryptography

2.Usage
Run the program:
    python secure_data_hiding.py
    Follow the on-screen instructions to:
        Hide data in an image.
        Extract data from an image.

Example
Hiding Data
    Choose option 1 (Hide Data).
    Enter the path to the cover image.
    Enter the secret data to hide.
    Provide an encryption key (or leave blank to generate a new key).
    The steganographic image will be saved as stego_image.png.

Extracting Data
    Choose option 2 (Extract Data).
    Enter the path to the steganographic image.
    Provide the encryption key.
    The extracted data will be displayed.
