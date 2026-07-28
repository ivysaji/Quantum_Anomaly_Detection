import os

class Config:
    """System Hyperparameters and Configuration Settings for QADS."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'qads-secret-key-2026')
    DEBUG = True
    HOST = "127.0.0.1"
    PORT = 5000

    # Quantum Hyperparameters
    QUANTUM_SHOTS = 1024
    ROTATION_GATE = 'ry'
    ENABLE_ENTANGLEMENT = True

    # Classification Thresholds
    ANOMALY_THRESHOLD = 0.55
    CLASSICAL_WEIGHT = 0.6
    QUANTUM_WEIGHT = 0.4
    HIGH_CPU_THRESHOLD = 0.85
    HIGH_LOGIN_THRESHOLD = 0.50