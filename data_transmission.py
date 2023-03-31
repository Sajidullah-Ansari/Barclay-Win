from qiskit import QuantumCircuit, Aer, execute
from classical_key_conversion import classical_key_conversion
from symmetric_encryption import symmetric_encryption, symmetric_decryption

def data_transmission(message, shared_quantum_key):
    # Convert the quantum key to a classical key
    classical_key = classical_key_conversion(shared_quantum_key)
    
    # Encrypt the message using the classical key
    encrypted_message = symmetric_encryption(message, classical_key)
    
    # Prepare the quantum circuit to send the key
    qc = QuantumCircuit(1, 1)
    if shared_quantum_key == '1':
        qc.x(0)
    qc.measure(0, 0)
    
    # Simulate the quantum circuit and get the measurement result
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    measurement = int(list(result.get_counts())[0])
    
    # Transmit the key and the message
    if measurement == 1:
        print("Sender: Transmitting the quantum key...")
        print("Receiver: Receiving the quantum key...")
        print("Sender: Quantum key transmission complete.")
        print("Sender: Transmitting the encrypted message...")
        print("Receiver: Receiving the encrypted message...")
        print("Sender: Message transmission complete.")
        print("Receiver: Decrypting the message...")
        decrypted_message = symmetric_decryption(encrypted_message, classical_key)
        print(f"Receiver: The decrypted message is: {decrypted_message}")
    else:
        print("Sender: Sending a decoy photon...")
        print("Receiver: Detecting the decoy photon...")
        print("Receiver: Error: Security compromised!")
