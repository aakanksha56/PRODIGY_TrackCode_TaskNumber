
def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            if encrypt:
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            if encrypt:
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

message = input("Enter the message to encrypt or decrypt: ")
shift_value = int(input("Enter the shift value: "))
choice = input("Encrypt (E) or Decrypt (D)? Enter E/D: ")

if choice.upper() == 'E':
    encrypted_message = caesar_cipher(message, shift_value)
    print(f"Encrypted message: {encrypted_message}")
elif choice.upper() == 'D':
    decrypted_message = caesar_cipher(message, shift_value, encrypt=False)
    print(f"Decrypted message: {decrypted_message}")
else:
    print("Invalid choice. Please enter E for encrypt or D for decrypt.")

