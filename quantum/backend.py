from qiskit_aer import AerSimulator

class QuantumBackend:
    """Executes quantum circuits locally via Qiskit Aer Simulator."""
    def __init__(self, shots=1024, **kwargs):
        self.shots = shots
        self.simulator = AerSimulator()

    def run(self, circuit, shots=None):
        run_shots = shots if shots is not None else self.shots
        job = self.simulator.run(circuit, shots=run_shots)
        return job.result().get_counts()