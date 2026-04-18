#!/bin/bash
#SBATCH --account=project_2018026
#SBATCH --job-name=super_analysis
#SBATCH --output=/scratch/project_2018026/lojarvin/super_analysis_%j.out
#SBATCH --time=00:05:00
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --partition=small

module load python-data
module load gcc/11.3.0 openmpi/4.1.4

srun python analysis.py