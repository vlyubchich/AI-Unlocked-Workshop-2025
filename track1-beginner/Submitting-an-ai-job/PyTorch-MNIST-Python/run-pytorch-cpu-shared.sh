#!/usr/bin/env bash
#SBATCH --job-name=pytorch-cpu-shared
#### Change account below
#SBATCH --account=use300
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --time=00:30:00
#SBATCH --output=pytorch-cpu-shared.o%j.%N

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
echo $OMP_NUM_THREADS

declare -xr SINGULARITY_MODULE='singularitypro/3.11'

module purge
module load "${SINGULARITY_MODULE}"
module list
#printenv

#### We will run from the scratch directory local to the node
cd /scratch/$USER/job_$SLURM_JOBID

time -p singularity exec --bind /expanse,/scratch /cm/shared/apps/containers/singularity/pytorch/pytorch_2.2.1-openmpi-4.1.6-mofed-5.8-2.0.3.0-cuda-12.1.1-ubuntu-22.04.4-x86_64-20240412.sif python3 $SLURM_SUBMIT_DIR/main.py

#### List scratch directory
ls /scratch/$USER/job_$SLURM_JOBID
