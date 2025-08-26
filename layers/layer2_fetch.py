import os
import pandas as pd

def fetch_data(dataset_path):
    print("[INFO] Fetching CSV files from dataset...")

    # List all CSV files inside dataset_path
    csv_files = []
    for root, _, files in os.walk(dataset_path):
        for f in files:
            if f.endswith(".csv"):
                csv_files.append(os.path.join(root, f))

    if not csv_files:
        raise FileNotFoundError("No CSV files found in dataset path.")

    print(f"[INFO] Found {len(csv_files)} CSV files.")
    return csv_files

def load_data(csv_files):
    print("[INFO] Loading CSV files into pandas DataFrames...")
    dataframes = {}
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            dataframes[os.path.basename(file)] = df
            print(f"[OK] Loaded: {file} ({df.shape[0]} rows, {df.shape[1]} cols)")
        except Exception as e:
            print(f"[ERROR] Failed to load {file}: {e}")
    return dataframes

if __name__ == "__main__":
    dataset_path = input("Enter dataset path (from layer1_ingest output): ").strip()
    csv_files = fetch_data(dataset_path)
    dataframes = load_data(csv_files)
    print(f"[SUCCESS] Loaded {len(dataframes)} datasets into memory.")
