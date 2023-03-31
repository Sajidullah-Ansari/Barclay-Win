from cryptography.fernet import Fernet

def symmetric_encryption(message, key):
    """Encrypt a message using the shared classical key"""
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode('utf-8'))
    return encrypted_message

def symmetric_decryption(encrypted_message, key):
    """Decrypt an encrypted message using the shared classical key"""
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode('utf-8')
