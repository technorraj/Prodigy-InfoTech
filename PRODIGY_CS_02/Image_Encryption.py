from PIL import Image
import numpy as np
import os

print("\n=== Welcome to the Image Encryption Program ===\n")

def encrypt_image(image_path, key):
    try:
        original_image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Image not found. Please check the path and try again.")
        return

    image_array = np.array(original_image)
    
    # Apply encryption transformation
    encrypted_image_array = (image_array * key) // (key + 1)
    encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))
    
    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(f" Image encrypted successfully and saved as: {encrypted_image_path}")

def decrypt_image(image_path, key):
    try:
        encrypted_image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Encrypted image not found. Please check the path and try again.")
        return

    encrypted_image_array = np.array(encrypted_image)

    # Apply decryption transformation
    decrypted_image_array = (encrypted_image_array * (key + 1)) // key
    decrypted_image_array = np.clip(decrypted_image_array, 0, 255)
    decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))

    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(f"Image decrypted successfully and saved as: {decrypted_image_path}")

def get_valid_key():
    while True:
        try:
            key = int(input("Enter the key (positive integer): "))
            if key <= 0:
                print("⚠Key must be a positive integer greater than 0.")
                continue
            return key
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_path(prompt_message):
    while True:
        path = input(prompt_message).strip('"')
        if os.path.exists(path):
            return path
        else:
            print("File not found. Please check the path and try again.")

def main():
    while True:
        print("\nWhat would you like to do?")
        print("  [e] Encrypt an image")
        print("  [d] Decrypt an image")
        print("  [q] Quit")
        
        choice = input("Your choice: ").strip().lower()
        
        if choice == 'e':
            key = get_valid_key()
            image_path = get_valid_path("Enter the path to the image you want to encrypt: ")
            encrypt_image(image_path, key)
        elif choice == 'd':
            key = get_valid_key()
            image_path = get_valid_path("Enter the path to the encrypted image: ")
            decrypt_image(image_path, key)
        elif choice == 'q':
            print("\n Exiting the program. Thank you for using Image Encryption Program!\n")
            break
        else:
            print(" Invalid option. Please type 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()

