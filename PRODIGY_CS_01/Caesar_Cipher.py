print(" Welcome to the Caesar Cipher Program! ")
print("This tool helps you encode or decode messages using a simple letter-shifting technique.\n")

def caesar_cipher(text, shift, action):

    result = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            offset = shift if action == 'e' else -shift
            new_char = chr((ord(char) - base + offset) % 26 + base)
            result += new_char
        else:
            result += char
    return result

def main():
    print("What would you like to do today?")
    action = input("Type 'e' to encrypt a message or 'd' to decrypt one: ").lower()

    while action not in ['e', 'd']:
        print("Oops! That’s not a valid option.")
        action = input("Please type 'e' to encrypt or 'd' to decrypt: ").lower()

    message = input("\nEnter the message you want to process: ")
    
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("That doesn't look like a number. Let's go with a default shift of 3.")
        shift = 3

    result = caesar_cipher(message, shift, action)
    action_label = "Encrypted" if action == 'e' else "Decrypted"

    print(f"\n {action_label} Message: {result}")
    print("\nThank you for using the Caesar Cipher Program! Goodbye ")

if __name__ == "__main__":
    main()
