def symmetric_decryption(encrypted_message, key):
    decrypted_message = ''
    for char in encrypted_message:
        decrypted_char = chr((ord(char) - key) % 256)
        decrypted_message += decrypted_char
    return decrypted_message
