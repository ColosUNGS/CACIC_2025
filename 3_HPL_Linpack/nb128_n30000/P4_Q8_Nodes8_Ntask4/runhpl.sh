#!/bin/bash
#SBATCH --output=hpl_%j.out
#SBATCH --error=hpl_%j.err
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=4
#SBATCH --time=01:30:00

# Cargar módulos si usás environment modules (opcional)
# module load mpi/openmpi

# Ejecutar el benchmark
mpirun ./xhpl
