import numpy as np
from quantum.circuit import QuantumCircuitBuilder
from quantum.backend import QuantumBackend

class QuantumFeatureExtractor:
    """Extracts state metrics including entropy, purity, and fidelity from execution counts."""
    def __init__(self, shots=1024):
        self.shots = shots
        self.backend = QuantumBackend(shots=self.shots)

    def extract(self, normalized_data):
        builder = QuantumCircuitBuilder(entangle=True)
        qc = builder.build_circuit(normalized_data, measure=True)

        counts = self.backend.run(qc)
        total_shots = sum(counts.values())
        probs = [c / total_shots for c in counts.values()]

        entropy = -sum(p * np.log2(p) for p in probs if p > 0)
        purity = sum(p**2 for p in probs)
        variance = float(np.var(probs))
        mean_val = float(np.mean(probs))
        fidelity = float(np.max(probs))

        quantum_features = {
            "Entropy": round(entropy, 4),
            "Purity": round(purity, 4),
            "Variance": round(variance, 4),
            "Mean Expectation": round(mean_val, 4),
            "Fidelity": round(fidelity, 4)
        }

        return quantum_features, counts

def extract_quantum_features(normalized_data, shots=1024):
    return QuantumFeatureExtractor(shots=shots).extract(normalized_data)