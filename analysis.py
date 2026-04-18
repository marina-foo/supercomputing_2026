import os
import sys
import time
import numpy as np
from multiprocessing import Pool, cpu_count

# Data paths
PUHTI_DATA_DIR = "/projappl/project_2018026/super_data"
LOCAL_DATA_DIR = "/Users/marina/Desktop/school/super_computing/super_data"

# This is used to achieve 60 seconds runtime for the analysis (basline, no multiprocessing)
REPEAT = 450

def heavy_compute(path):
    """
    Load a .npy file and perform repeated numerical computation
    to generate CPU-bound workload.
    """
    arr = np.load(path)
    result = 0.0
    for _ in range(REPEAT):
        result += np.mean(arr * arr)
    return result

def main():
    # Select environment
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
        os.path.join(data_dir, f)
        for f in os.listdir(data_dir)
        if f.endswith(".npy")
    ]

    if not files:
        raise RuntimeError("No .npy files found!")

    nproc = cpu_count()
    print(f"Using multiprocessing with {nproc} processes")

    start = time.time()

    with Pool(processes=nproc) as pool:
        results = pool.map(heavy_compute, files)

    total = sum(results)
    elapsed = time.time() - start

    print(f"Files processed: {len(files)}")
    print(f"Total result: {total}")
    print(f"Elapsed time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()