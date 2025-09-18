#!/bin/bash
#SBATCH --job-name=hpl_cronos
#SBATCH --output=hpl_%j.out
#SBATCH --error=hpl_%j.err
#SBATCH --nodes=6
#SBATCH --ntasks-per-node=1
#SBATCH --time=02:00:00

# Cargar módulos si usás environment modules (opcional)
# module load mpi/openmpi

# Ir al directorio donde está xhpl y HPL.dat
cd $SLURM_SUBMIT_DIR

# Ejecutar el benchmark
mpirun xhpl
