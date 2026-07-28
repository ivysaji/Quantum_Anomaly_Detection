# Quantum_Anomaly_Detection
A hybrid quantum-classical web platform using Qiskit and Flask for real-time anomaly detection—built to run seamlessly on local simulators and execute on real 156-qubit IBM Quantum hardware (ibm_marrakesh).
# 🚀 Quantum Security & Anomaly Detection System (QADS)

An end-to-end, hybrid quantum-classical application that combines a real-time web telemetry dashboard with quantum circuit anomaly detection. Built using **Qiskit** and **Flask**, the platform seamlessly runs low-latency simulations on a local backend and executes transpiled circuits on physical IBM Quantum hardware (`ibm_marrakesh`).

---

## 📑 Table of Contents
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Hardware vs. Simulator Comparison](#-hardware-vs-simulator-comparison)
- [Physical Hardware Noise Analysis](#-physical-hardware-noise-analysis)
- [License](#-license)

---

## ✨ Key Features

* **Dual Execution Modes:**
  * **Local Simulator (`AerSimulator`):** High-speed, deterministic, sub-second execution ideal for real-time web application dashboards.
  * **Physical Hardware (`ibm_marrakesh`):** Direct cloud-based execution on IBM's 156-qubit Heron processor using Qiskit Runtime Primitives (`SamplerV2`).
* **Interactive Telemetry Dashboard:** Web interface built with Flask and HTML/CSS for real-time monitoring and anomaly inspection.
* **Transpilation Pipeline:** Automatic circuit optimization and pass management mapped to physical backend coupling maps.
* **Comparative Noise Benchmarking:** Quantitative evaluation comparing ideal statevector outcomes against physical NISQ hardware decoherence and readout errors.

---

## 🏗️ System Architecture

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        User Interface (Web UI)                         │
│             Real-time Metrics Dashboard & Telemetry Visualizer          │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │ HTTP API Requests
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                       Flask Engine Backend (app.py)                    │
│          Data Ingestion  ──►  Feature Mapping  ──► Encoding            │
└──────────────────┬──────────────────────────────────┬──────────────────┘
                   │                                  │
                   ▼                                  ▼
┌────────────────────────────────────┐ ┌─────────────────────────────────┐
│     Local Aer Simulator Path       │ │   Physical QPU Execution Path   │
│  • Instant response (~0.08s)       │ │  • IBM Quantum Platform Cloud   │
│  • Ideal statevector computation   │ │  • Transpilation & Optimization │


quantum-anomaly-detection/
├── .gitignore
├── README.md
├── requirements.txt
├── app.py                      # Flask Web Application (Local Simulator)
├── test_execution.py           # Physical IBM Quantum Execution Script
├── quantum/
│   ├── __init__.py
│   └── circuit.py              # Quantum circuit generation & logic
├── templates/
│   └── index.html              # Dashboard Web Interface
├── static/
│   ├── css/                    # Custom styling
│   └── js/                     # Frontend interactions
└── docs/                       # Diagrams, screenshots, and visual assets
│  • Deterministic UI benchmarking   │ │  • Target: 156-Qubit Hardware   │
└────────────────────────────────────┘ └─────────────────────────────────┘
