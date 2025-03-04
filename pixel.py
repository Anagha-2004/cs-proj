import cv2
import numpy as np

def encrypt_image(image_path, key):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    encrypted_image = np.bitwise_xor(image, key)  # XOR operation for encryption
    cv2.imwrite("encrypted_image.png", encrypted_image)
    print("Encryption complete. Saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    encrypted_image = cv2.imread(encrypted_image_path)
    if encrypted_image is None:
        print("Error: Encrypted image not found!")
        return
    decrypted_image = np.bitwise_xor(encrypted_image, key)  # XOR again to decrypt
    cv2.imwrite("decrypted_image.png", decrypted_image)
    print("Decryption complete. Saved as 'decrypted_image.png'.")

# Example usage
key = 50  # XOR key (same key must be used for encryption and decryption)
encrypt_image("input_image.jpg", key)
decrypt_image("encrypted_image.png", key)
