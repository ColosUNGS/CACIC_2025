#!/bin/bash
#SBATCH --output=hpl_%j.out
#SBATCH --error=hpl_%j.err
#SBATCH --nodes=6
#SBATCH --ntasks-per-node=1
#SBATCH --time=04:00:00

# Cargar módulos si usás environment modules (opcional)
# module load mpi/openmpi

# Ejecutar el benchmark
mpirun ./xhpl
