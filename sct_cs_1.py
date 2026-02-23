"""
Project Name: SCT_CS_1
Title: Caesar Cipher Encryption & Decryption
Description: A program to encrypt and decrypt text using Caesar Cipher algorithm.
Author: Deeksha P 
"""

def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26
            encrypted_text += chr(shifted + ascii_offset)
        else:
            encrypted_text += char
    
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    while True:
        print("\n========== SCT_CS_1 ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "3":
            print("Exiting program...")
            break
        
        message = input("Enter your message: ")
        
        try:
            shift = int(input("Enter shift value: "))
        except ValueError:
            print("Shift must be a number!")
            continue
        
        if choice == "1":
            print("Encrypted Message:", encrypt(message, shift))
        
        elif choice == "2":
            print("Decrypted Message:", decrypt(message, shift))
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()