from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

def test_on_real_hardware():
    print("1. Initializing connection...")
    service = QiskitRuntimeService(channel="ibm_quantum_platform")

    # Connect to your least busy server (ibm_marrakesh)
    backend = service.least_busy(operational=True, simulator=False)
    print(f"-> Target Quantum Computer: {backend.name}")

    # 2. Build a simple test circuit (or import your project circuit)
    print("\n2. Creating Quantum Circuit...")
    qc = QuantumCircuit(2)
    qc.h(0)           # Put qubit 0 into superposition
    qc.cx(0, 1)       # Entangle qubit 0 and qubit 1
    qc.measure_all()   # Measure the result
    print(qc)

    # 3. Transpile the circuit for the target physical backend layout
    print("\n3. Transpiling circuit for hardware...")
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    isa_circuit = pm.run(qc)

    # 4. Submit job to the cloud server queue
    print("\n4. Submitting job to IBM Quantum cloud...")
    sampler = Sampler(mode=backend)
    job = sampler.run([isa_circuit], shots=1024)
    
    print(f"-> Job Submitted Successfully!")
    print(f"-> Job ID: {job.job_id()}")
    print("-> Status: Queued / Running (Waiting for real QPU execution...)")

    # 5. Wait for the real quantum processor to complete execution
    result = job.result()
    print("\n5. Job Finished!")

    # 6. Extract measurement counts
    pub_result = result[0]
    counts = pub_result.data.meas.get_counts()
    print("\n--- Physical QPU Measurement Output ---")
    print(counts)

if __name__ == "__main__":
    test_on_real_hardware()