import os
import random

# Path to the super_data folder on Puhti
DATA_DIR = "/projappl/project_2018026/super_data"

def main():
    # List all .npy files
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".npy")]

    # Count files
    file_count = len(files)
    print(f"Found {file_count} .npy files in super_data.")

    # Ensure there are at least 10 files to sample
    if file_count < 10:
        raise RuntimeError("super_data contains fewer than 10 .npy files!")

    # Select 10 random files
    selected = random.sample(files, 10)

    print("\nRandomly selected 10 files:")
    for f in selected:
        print(f" - {f}")

if __name__ == "__main__":
    main()