import numpy as np
from qiskit import QuantumCircuit

class AngleEncoder:
    """Encodes classical normalized telemetry vectors into qubit rotation angles."""
    def __init__(self, rotation_gate='ry'):
        self.rotation_gate = rotation_gate.lower()

    def encode(self, features):
        values = list(features.values()) if isinstance(features, dict) else list(features)
        n_qubits = len(values)
        qc = QuantumCircuit(n_qubits)

        for idx, val in enumerate(values):
            angle = float(val) * np.pi
            if self.rotation_gate == 'rx':
                qc.rx(angle, idx)
            elif self.rotation_gate == 'rz':
                qc.rz(angle, idx)
            else:
                qc.ry(angle, idx)

        return qc

def encode_angles(features, rotation_gate='ry'):
    return AngleEncoder(rotation_gate=rotation_gate).encode(features)

def encode_features(features, rotation_gate='ry'):
    return encode_angles(features, rotation_gate=rotation_gate)