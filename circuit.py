from qiskit import QuantumCircuit
from quantum.encoder import AngleEncoder

class QuantumCircuitBuilder:
    """Builds quantum circuits with angle encoding, entangling layers, and measurements."""
    def __init__(self, rotation_gate='ry', entangle=True):
        self.encoder = AngleEncoder(rotation_gate=rotation_gate)
        self.entangle = entangle

    def build_circuit(self, features, measure=True):
        qc = self.encoder.encode(features)
        n_qubits = qc.num_qubits

        if self.entangle and n_qubits > 1:
            for i in range(n_qubits - 1):
                qc.cz(i, i + 1)

        if measure:
            qc.measure_all()

        return qc

def create_quantum_circuit(features, entangle=True, measure=True):
    return QuantumCircuitBuilder(entangle=entangle).build_circuit(features, measure=measure)