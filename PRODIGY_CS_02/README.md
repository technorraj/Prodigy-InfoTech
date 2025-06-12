# Image Encryption & Decryption Program

This Python program provides a simple and effective way to **encrypt and decrypt image files** using a custom key. The encryption works by applying a mathematical transformation to the pixel values of the image, making it unreadable until the correct key is used for decryption.

The project uses two popular Python libraries:
- **Pillow (PIL)** for image handling
- **NumPy** for pixel-level operations

This project was created as part of an internship at **The Prodigy Infotech**, demonstrating practical implementation of basic encryption techniques on media files using pixel manipulation.

## Features

- **Image Encryption and Decryption**: Supports both operations using a specified key.
- **Key-Based Security**: Only the correct key can properly decrypt the image.
- **User Input**: Users can provide image file paths and their own encryption keys.
- **Format Support**: Works with standard image formats like `.png`, `.jpg`, etc.

## Usage

1. **Run the Program**: Execute the Python script to start the Image Encryption tool.
2. **Select Action**: Choose `'e'` to encrypt or `'d'` to decrypt an image.
3. **Enter Image Path**: Input the path to the image you want to process.
4. **Enter Key**: Provide a positive integer key (must be the same for both encryption and decryption).
5. **View Result**: 
   - Encrypted image will be saved as `encrypted_image.png`.
   - Decrypted image will be saved as `decrypted_image.png`.

