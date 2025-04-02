# Setup Instructions for the "Introduction to PyTorch" Hands-On Exercises" #
The "Introduction to PyTorch" exercises include two Jupyter Notebooks named, "pytorch_tensors_problems.ipynb" and "pytorch_models_problems.ipynb".  The solutions to these exercises are located in seperate notebooks entitled, "pytorch_tensors_solution.ipynb" and "pytorch_models_solution.ipynb".  These notebooks can be used and run on either Expanse, Delta, or DeltaAI.  Instructions are presented below for accessing the JupyterLab environments on these resources.

## Login via SSH on Expanse, Delta, or DeltaAI ##
It is necessary to login via SSH to Expanse, Delta, or DeltaAI in order to download the workshop materials for use in the hands-on session.  You can access these resouces at the following addresses, where \<username\> is your usename on that resource:

- **Expanse:** `ssh <username>@login.expanse.sdsc.edu`		
- **Delta:** `ssh <username>@login.delta.ncsa.illinois.edu`
- **DeltaAI:** `ssh <username>@dtai-login.delta.ncsa.illinois.edu`

## Download the Workshop Materials ##
The following command can be run on these resources to download the workshop materials from GitHub.  This command can be run in your home directory or other filesystems available on these resources.
`git clone https://github.com/access-ci-org/AI-Unlocked-Workshop-2025.git`

## Access JupyterLab on Expanse, Delta, or DeltaAI ##
1. Navigate to the following addresses to get to the respective resources Open OnDemand Portal:

- **Expanse:**  https://portal.expanse.sdsc.edu/pun/sys/dashboard/ 
- **Delta:**  https://openondemand.delta.ncsa.illinois.edu/pun/sys/dashboard/ 
- **DeltaAI:**  https://gh-ondemand.delta.ncsa.illinois.edu/pun/sys/dashboard/

2. Follow the sign-in prompts for the respective resources.  Expanse will have you sign in using your ACCESS credentials.  Delta and DeltaAI will have you sign in using your NCSA credentials.
3. Click on the icons for "Jupyter" (Expanse) or "JupyterLab" (Delta and DeltaAI).
4. Complete the "Jupyter" or "JupyterLab" Forms.
   - On Delta or DeltaAI use the following entries:
     | Field | Delta | DeltaAI |
     | :----- | :-----: | :-----: |
     | **Name of account** | beeh-delta-gpu | beeh-dtai-gh |
     | **Partition** | gpuA100x4-interactive or gpuA40x4-interactive | ghx4 |
     | **Duration of Job** | 1:00:00 | 2:00:00 |
     | **Number of CPUs** | 16 | 72 |
     | **Amount of RAM** | 64G | < leave blank> |
     | **Number of GPUs** | 1 | 1 |
     
   - On Expnase use the following entries:
     | Field | Expanse |
     | :----- | :-----: | 
     | **Account** | TG-CIS250186 |
     | **Partition** | gpu-shared |
     | **Time limit (min)** | 60 |
     | **Number of cores** | 10 |
     | **Memory required per node (GB)** | 96 |
     | **GPUs (optional)** | 1 |
     | **Singularity Image File Location** | /cm/shared/apps/containers/singularity/pytorch/pytorch-latest.sif |
     | **Environment modules to be loaded** | singularitypro |
     | **Working directory** | home or lustre |
     | **Type** | JupyterLab |
  5. Once submitted the jobs will be queued.
     - On Delta and DeltaAI, the Interactive session card will update from "Queued" to "Running" in the upper right hand corner of the card.  Select the "Connect to Jupyter" button to connect to JupyterLab.
     - On Expanse, a new webrowser screen will load showing links to "Jupyter Sessions".  Click the link (usually the latest one - timestamp is listed to the left of the link) to connect to JupyterLab.
  6. Navigate to the AI-Unlocked-Workshop-2025/track2-Intermediate-to-Advanced/introduction-to-pytorch/notebooks folder.
  7. Open the appropriate pytorch_tensors_problems.ipynb or pytorch_models_problems.ipynb file.
   
     
