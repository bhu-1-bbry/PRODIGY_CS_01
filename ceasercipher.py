def caesar_cipher(text, shift, mode):
    result = ""

    # If decrypting, reverse the shift
    if mode == 'd':
        shift = -shift

    for char in text:
        if char.isalpha():  # Check if character is a letter
            # Handle uppercase and lowercase separately
            base = ord('A') if char.isupper() else ord('a')
            
            # Apply shift using modulo for wrap-around
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Keep spaces and special characters unchanged
            result += char

    return result


# Taking user input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

# Calling the function
output = caesar_cipher(message, shift, choice)

# Display result
print("Result:", output)