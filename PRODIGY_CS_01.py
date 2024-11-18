import random
import re

# Storage for encrypted messages and their associated passwords
encrypted_storage = {}

def caesar_cipher(text, shift, mode):
    """Encrypts or decrypts text using the Caesar Cipher algorithm."""
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result


def get_secure_shift():
    """Generates a random shift value for added security."""
    return random.randint(1, 25)


def is_strong_password(password):
    """Checks if the password meets the required security standards."""
    # Check password length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."

    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit."

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."

    return True, "Password is strong."


def main():
    print("=" * 85)
    print("🔐 Welcome to the Caesar Cipher Program Encryption and Decryption Python program 🔐")
    print("=" * 85)

    while True:
        print("\nOptions: \n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '3':
            print("⌛ Exiting the program. Stay secure!")
            break

        if choice not in ['1', '2']:
            print("⚠️ Invalid choice. Please try again.")
            continue

        if choice == '1':  # Encryption
            # Input message
            plaintext_message = input("\nEnter the message to encrypt: ").strip()
            if not plaintext_message:
                print("⚠️ Message cannot be empty!")
                continue

            # Shift configuration
            use_random_shift = input("Do you want to use a random shift? (yes/no): ").strip().lower()
            if use_random_shift == "yes":
                shift_value = get_secure_shift()
                print(f"🔢 Random Shift Generated: {shift_value}")
            else:
                try:
                    shift_value = int(input("Enter the shift value (1-25): ").strip())
                    if not (1 <= shift_value <= 25):
                        print("⚠️ Shift value must be between 1 and 25!")
                        continue
                except ValueError:
                    print("⚠️ Please enter a valid integer for the shift value.")
                    continue

                    # Password protection
                    while True:
                        password = input("Set your encryption password: ").strip()
                        is_valid, validation_message = is_strong_password(password)
                        if not is_valid:
                            print(f"⚠️ {validation_message}")
                        else:
                            break  # Exit loop if password is valid

            # Perform encryption
            encrypted_message = caesar_cipher(plaintext_message, shift_value, "encrypt")
            encrypted_storage[encrypted_message] = {"shift": shift_value, "password": password}
            print("\n🔒 Encryption Successful! 🔓")
            print("=" * 50)
            print(f"Encrypted Message: {encrypted_message}")
            print("=" * 50)

        elif choice == '2':  # Decryption
            encrypted_message = input("\nEnter the message to decrypt: ").strip()
            if encrypted_message not in encrypted_storage:
                print("⚠️ Encrypted message not found in storage!")
                continue

            # Retrieve password and shift from storage
            stored_data = encrypted_storage[encrypted_message]
            stored_password = stored_data["password"]
            shift_value = stored_data["shift"]

            # Password validation
            entered_password = input("Enter the encryption password: ").strip()
            if entered_password != stored_password:
                print("❌ Incorrect password! Access denied.")
                continue

            # Perform decryption
            decrypted_message = caesar_cipher(encrypted_message, shift_value, "decrypt")
            print("\n🔓 Decryption Successful!")
            print("=" * 50)
            print(f"Decrypted Message: {decrypted_message}")
            print("=" * 50)


if __name__ == "__main__":
    main()
