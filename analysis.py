import os
import random
import numpy as np

# Path to the super_data directory on Puhti
DATA_DIR = "/projappl/project_2018026/super_data"

def get_single_value(path):
    arr = np.load(path)
    return float(arr.mean())

def main():
    # List all .npy files
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".npy")]

    file_count = len(files)
    print(f"Found {file_count} .npy files in super_data.")

    # Select 10 random files
    selected = random.sample(files, 10)

    print("\nSelected files:")
    for f in selected:
        print(f" - {f}")

    # Extract one numeric value from each file
    values = []
    for fname in selected:
        path = os.path.join(DATA_DIR, fname)
        value = get_single_value(path)
        values.append(value)

    # Compute sum
    total_sum = sum(values)

    print("\nExtracted values:")
    for v in values:
        print(f" {v}")

    print(f"\nSum of values: {total_sum}")

if __name__ == "__main__":
    main()