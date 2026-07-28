from flask import Flask, render_template, request
from config import Config
from quantum import QuantumFeatureExtractor
from models import AnomalyDetector

app = Flask(__name__)
app.config.from_object(Config)

# Initialize quantum and detection pipeline components
extractor = QuantumFeatureExtractor(shots=Config.QUANTUM_SHOTS)
detector = AnomalyDetector(
    threshold=Config.ANOMALY_THRESHOLD,
    classical_weight=Config.CLASSICAL_WEIGHT,
    quantum_weight=Config.QUANTUM_WEIGHT
)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            data = {
                "CPU Usage": float(request.form.get("cpu", 0)) / 100.0,
                "Memory Usage": float(request.form.get("memory", 0)) / 100.0,
                "Network Traffic": float(request.form.get("network", 0)) / 100.0,
                "Failed Login Attempts": float(request.form.get("logins", 0)) / 10.0,
            }

            # 1. Quantum Feature Extraction
            q_features, counts = extractor.extract(data)

            # 2. Anomaly Detection Pipeline
            prediction, anomaly_score = detector.predict(data, q_features)

            result = {
                "prediction": prediction,
                "score": round(anomaly_score, 4),
                "entropy": q_features["Entropy"],
                "purity": q_features["Purity"],
                "fidelity": q_features["Fidelity"],
                "counts": counts,
                "inputs": {
                    "CPU": int(data["CPU Usage"] * 100),
                    "Memory": int(data["Memory Usage"] * 100),
                    "Network": int(data["Network Traffic"] * 100),
                    "Logins": int(data["Failed Login Attempts"] * 10),
                }
            }
        except Exception as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(
        debug=Config.DEBUG,
        host=Config.HOST,
        port=Config.PORT
    )