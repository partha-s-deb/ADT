# layer4_anomaly.py

import os
import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest

# File paths
SPIKE_FILE = os.path.join("data", "spikes.csv")
MODEL_FILE = os.path.join("models", "isolation_forest.pkl")

def train_model(data):
    """Train Isolation Forest model and save it"""
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(data)
    joblib.dump(model, MODEL_FILE)
    print("[+] Anomaly detection model trained and saved.")

def detect_anomalies(data):
    """Load model and predict anomalies"""
    if not os.path.exists(MODEL_FILE):
        print("[!] Model not found. Training a new one...")
        train_model(data)

    model = joblib.load(MODEL_FILE)
    predictions = model.predict(data)  # -1 = anomaly, 1 = normal
    data["Anomaly"] = predictions
    return data

def main():
    if not os.path.exists(SPIKE_FILE):
        print("[!] No spike data found. Run layer3_spike.py first.")
        return

    # Load spike data
    data = pd.read_csv(SPIKE_FILE)
    features = data.select_dtypes(include=["float64", "int64"])

    # Detect anomalies
    results = detect_anomalies(features)

    # Save results
    os.makedirs("results", exist_ok=True)
    output_path = os.path.join("results", "anomalies.csv")
    results.to_csv(output_path, index=False)

    print(f"[+] Anomaly detection complete. Results saved to {output_path}")

if __name__ == "__main__":
    main()
