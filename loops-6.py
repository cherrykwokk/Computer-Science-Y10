def shift_cipher(shift, message):
    shifted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            shifted_char = char

        shifted_message += shifted_char

    return shifted_message

shift = 3
message = input("Enter text")
encrypted_message = shift_cipher(shift, message)
print(encrypted_message)