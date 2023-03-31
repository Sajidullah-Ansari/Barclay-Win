import hashlib

def classical_key_conversion(quantum_key):
    # Hash the quantum key using SHA-256
    sha256 = hashlib.sha256()
    sha256.update(''.join(str(bit) for bit in quantum_key).encode('utf-8'))
    hashed_key = sha256.hexdigest()

    # Convert the hashed key to a binary string
    binary_key = ''.join(format(int(c, 16), '04b') for c in hashed_key)

    # Return the binary key as a string
    return binary_key

# import hashlib

# def classical_key_conversion(quantum_key):
#     """Convert the quantum key into a classical key using the SHA256 hash function"""
#     sha256 = hashlib.sha256()
#     sha256.update(quantum_key.encode('utf-8'))
#     classical_key = sha256.digest()
#     return classical_key
