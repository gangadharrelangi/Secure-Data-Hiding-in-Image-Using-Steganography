import cv2
import numpy as np
from cryptography.fernet import Fernet
from hashlib import sha256

# Generate a key for AES encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt data using AES
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Decrypt data using AES
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Generate hash for data integrity
def generate_hash(data):
    return sha256(data.encode()).hexdigest()

# Embed data into image using LSB method
def embed_data(image_path, data, key):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found. Please check the file path.")
        return
    height, width, _ = image.shape

    # Encrypt data
    encrypted_data = encrypt_data(data, key)
    binary_data = ''.join(format(byte, '08b') for byte in encrypted_data)
    data_len = len(binary_data)

    # Check if data can fit into the image
    if data_len > height * width * 3:
        print("Error: Data too large to embed in the image.")
        return

    # Embed data into LSBs
    data_index = 0
    for i in range(height):
        for j in range(width):
            for k in range(3):  # RGB channels
                if data_index < data_len:
                    image[i][j][k] = (image[i][j][k] & ~1) | int(binary_data[data_index])
                    data_index += 1

    # Save steganographic image
    output_path = "stego_image.png"
    cv2.imwrite(output_path, image)
    print(f"Data embedded successfully. Steganographic image saved as {output_path}.")

# Extract data from image using LSB method
def extract_data(image_path, key):
    # Load steganographic image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found. Please check the file path.")
        return
    height, width, _ = image.shape

    # Extract LSBs
    binary_data = ""
    for i in range(height):
        for j in range(width):
            for k in range(3):  # RGB channels
                binary_data += str(image[i][j][k] & 1)

    # Convert binary data to bytes
    encrypted_data = bytes(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))

    # Decrypt data
    try:
        decrypted_data = decrypt_data(encrypted_data, key)
        return decrypted_data
    except Exception as e:
        print("Error: Failed to decrypt data. Incorrect key or corrupted data.")
        return None

# Main function
def main():
    print("Welcome to Secure Data Hiding in Image Using Steganography!")
    print("1. Hide Data")
    print("2. Extract Data")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        # Hide Data
        image_path = input("Enter the path of the cover image: ")
        secret_data = input("Enter the secret data to hide: ")
        key = input("Enter an encryption key (leave blank to generate a new key): ")

        if not key:
            key = generate_key()
            print(f"Generated Encryption Key: {key.decode()}")
        else:
            key = key.encode()

        embed_data(image_path, secret_data, key)

    elif choice == "2":
        # Extract Data
        image_path = input("Enter the path of the steganographic image: ")
        key = input("Enter the encryption key: ").encode()

        extracted_data = extract_data(image_path, key)
        if extracted_data:
            print("Extracted Data:", extracted_data)

            # Verify data integrity
            original_hash = input("Enter the original hash (if available): ")
            if original_hash:
                extracted_hash = generate_hash(extracted_data)
                if original_hash == extracted_hash:
                    print("Data integrity verified.")
                else:
                    print("Data integrity check failed.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
