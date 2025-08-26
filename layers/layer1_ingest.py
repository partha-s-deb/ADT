import os
import kagglehub
import zipfile

def download_dataset():
    print("[INFO] Downloading dataset from Kaggle...")
    path = kagglehub.dataset_download("devendra416/ddos-datasets")
    print(f"[INFO] Dataset downloaded to: {path}")

    # Check if it's a zip file and extract
    if path.endswith(".zip"):
        extract_path = os.path.splitext(path)[0]
        print(f"[INFO] Extracting dataset to: {extract_path}")
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print("[INFO] Extraction complete.")
        return extract_path
    else:
        return path

if __name__ == "__main__":
    dataset_path = download_dataset()
    print(f"[SUCCESS] Dataset is ready at: {dataset_path}")
