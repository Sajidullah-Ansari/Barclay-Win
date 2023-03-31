from qkd_key_generation import qkd_key_generation
from classical_key_conversion import classical_key_conversion
from symmetric_encryption import symmetric_encryption
from data_transmission import data_transmission
from symmetric_decryption import symmetric_decryption

# Generate a quantum key using QKD
qkd_key = qkd_key_generation()

# Convert the quantum key to a classical key
classical_key = classical_key_conversion(qkd_key)

# Encrypt the message using the classical key
message = 'Hello, world!'
encrypted_message = symmetric_encryption(message, classical_key)

# Transmit the encrypted message
received_message = data_transmission(encrypted_message)

# Decrypt the received message using the classical key
decrypted_message = symmetric_decryption(received_message, classical_key)

# Print the original and decrypted messages
print(f'Original message: {message}')
print(f'Encrypted message: {encrypted_message}')
print(f'Received message: {received_message}')
print(f'Decrypted message: {decrypted_message}')
