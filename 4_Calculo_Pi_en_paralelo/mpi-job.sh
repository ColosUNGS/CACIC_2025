#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --output=mpi-out.%j
#SBATCH --error=mpi-err.%j
#SBATCH --time=00:30:00
#SBATCH --partition=cronos

cd $SLURM_SUBMIT_DIR

mpirun ./pi-mpi
