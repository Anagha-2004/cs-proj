def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse shift for decryption
    
    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    
    return result

# User input
if __name__ == "__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'e':
        encrypted_text = caesar_cipher(message, shift, mode='encrypt')
        print("Encrypted Text:", encrypted_text)
    elif choice == 'd':
        decrypted_text = caesar_cipher(message, shift, mode='decrypt')
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice! Please enter 'E' or 'D'.")
