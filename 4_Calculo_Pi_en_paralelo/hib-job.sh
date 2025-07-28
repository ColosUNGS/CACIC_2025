#!/bin/bash
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=2
#SBATCH --output=mpi-out.%j
#SBATCH --error=mpi-err.%j
#SBATCH --time=00:30:00
#SBATCH --partition=cronos

export OMP_NUM_THREADS=2
cd $SLURM_SUBMIT_DIR

mpirun ./pi-hib
