import os
import sys
import time
import numpy as np

# Data paths
PUHTI_DATA_DIR = "/projappl/project_2018026/super_data"
LOCAL_DATA_DIR = "/Users/marina/Desktop/school/super_computing/super_data"

# This is used to achieve 60 seconds runtime for the analysis
REPEAT = 450


def get_single_value(path):
    """
    Load a .npy file and perform repeated numerical computation
    to create sufficient CPU workload.
    """
    arr = np.load(path)
    result = 0.0
    for _ in range(REPEAT):
        result += np.mean(arr * arr)
    return result

def main():
    # Select environment based on command line argument
    if len(sys.argv) > 1 and sys.argv[1].upper() == "LOCAL":
        data_dir = LOCAL_DATA_DIR
        environment = "LOCAL"
    else:
        data_dir = PUHTI_DATA_DIR
        environment = "PUHTI"

    print(f"Running analysis in {environment} environment")
    print(f"Using data directory: {data_dir}")

    # List all .npy files
    files = [
        f for f in os.listdir(data_dir)
        if f.endswith(".npy")
    ]

    if not files:
        raise RuntimeError("No .npy files found!")

    start = time.time()

    values = []
    for fname in files:
        path = os.path.join(data_dir, fname)
        value = get_single_value(path)
        values.append(value)

    total = sum(values)
    elapsed = time.time() - start

    print(f"Files processed: {len(files)}")
    print(f"Total result: {total}")
    print(f"Elapsed time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()
