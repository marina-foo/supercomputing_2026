import os
import sys
import time
import numpy as np
from mpi4py import MPI

PUHTI_DATA_DIR = "/scratch/project_2018026/lojarvin/super_data"
LOCAL_DATA_DIR = "/Users/marina/Desktop/school/super_computing/super_data"

REPEAT = 450

def heavy_compute(path):
    arr = np.load(path)
    result = 0.0
    for _ in range(REPEAT):
        result += np.mean(arr * arr)
    return result

def main():
    if len(sys.argv) > 1 and sys.argv[1].upper() == "LOCAL":
        data_dir = LOCAL_DATA_DIR
        environment = "LOCAL"
    else:
        data_dir = PUHTI_DATA_DIR
        environment = "PUHTI"

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        print(f"Running analysis in {environment} environment")
        print(f"Using data directory: {data_dir}")

    if rank == 0:
        files = [
            os.path.join(data_dir, f)
            for f in os.listdir(data_dir)
            if f.endswith(".npy")
        ]
    else:
        files = None

    files = comm.bcast(files, root=0)
    local_files = files[rank::size]

    print(f"Rank {rank} processed {len(local_files)} files")

    start = time.time()

    local_sum = 0.0
    for path in local_files:
        local_sum += heavy_compute(path)

    total = comm.reduce(local_sum, op=MPI.SUM, root=0)

    if rank == 0:
        elapsed = time.time() - start
        print(f"Files processed: {len(files)}")
        print(f"Total result: {total}")
        print(f"Elapsed time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()