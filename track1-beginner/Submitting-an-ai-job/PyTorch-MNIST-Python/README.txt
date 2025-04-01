This is a PyTorch MNIST example
https://github.com/pytorch/examples/blob/main/mnist/main.py

srun --partition=debug  --pty --account=use300 --nodes=1 --ntasks-per-node=24  --mem=32G -t 00:30:00 --wait=0 --export=ALL /bin/bash
                        
Load the Singularity module
module load singularitypro/4.1.2
 
singularity shell /cm/shared/apps/containers/singularity/pytorch/pytorch-latest.sif


