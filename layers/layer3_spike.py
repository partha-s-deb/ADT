# layer3_spike.py

import pandas as pd
import numpy as np
import os
import sys

def detect_spikes(file_path, window_size=50, threshold=3.0):
    """
    Detect traffic spikes using rolling mean + standard deviation.
    A spike is flagged if value > mean + threshold * std.
    """

    try:
        # Load CSV
        df = pd.read_csv(file_path)

        # Pick packet/byte count column (adapt as needed for your dataset)
        if "TotPkts" in df.columns:
            traffic = df["TotPkts"]
        elif "TotBytes" in df.columns:
            traffic = df["TotBytes"]
        else:
            print("❌ Dataset missing 'TotPkts' or 'TotBytes' column.")
            return None

        # Rolling stats
        rolling_mean = traffic.rolling(window=window_size).mean()
        rolling_std = traffic.rolling(window=window_size).std()

        # Identify spikes
        spikes = traffic > (rolling_mean + threshold * rolling_std)

        # Output results
        spike_indices = np.where(spikes)[0]
        print(f"✅ Detected {len(spike_indices)} spikes in {os.path.basename(file_path)}")

        return spike_indices.tolist()

    except Exception as e:
        print(f"⚠️ Error processing {file_path}: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python layer3_spike.py <dataset_file.csv>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    spikes = detect_spikes(file_path)
    if spikes:
        print("🚨 Spike indices:", spikes[:20], "...")  # only show first 20 for readability
