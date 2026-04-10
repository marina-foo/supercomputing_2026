#!/bin/bash
#SBATCH --account=project_2018026
#SBATCH --job-name=super_analysis
#SBATCH --output=super_analysis.out
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --partition=small

module load python-data
python analysis.py
