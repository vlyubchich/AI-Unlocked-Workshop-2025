**AI Unlocked Workshop — User Reference Guide**
<br>
GitHub      : <https://github.com/access-ci-org/AI-Unlocked-Workshop-2025>\
Agenda      : <https://github.com/access-ci-org/AI-Unlocked-Workshop-2025/blob/main/AI-Unlocked-workshop-agenda.pdf>\
Google Drive: <https://drive.google.com/drive/u/1/folders/1GyZu2gXQ0crcWpzEfi3AKm3GI7VdTNku>

# Accessing Workshop Resources

| Resource | SSH Login | Open OnDemand Portal |
| --- | --- | --- |
| Expanse | ssh &lt;username&gt;@login.expanse.sdsc.edu | <https://portal.expanse.sdsc.edu/> |
| Delta | ssh &lt;username&gt;@login.delta.ncsa.illinois.edu | <https://openondemand.delta.ncsa.illinois.edu/> |
| DeltaAI | ssh &lt;username&gt;@dtai-login.delta.ncsa.illinois.edu | <https://gh-ondemand.delta.ncsa.illinois.edu/> |

To clone Workshop Materials from GitHub:

git clone <https://github.com/access-ci-org/AI-Unlocked-Workshop-2025.git>

## **Jupyter Notebook Settings (Open On Demand) — Expanse**

Expanse Open On Demand Portal: <https://portal.expanse.sdsc.edu/>

Account: ukl119 or TG-CIS250186\
Partition (CPU jobs): shared\
Partition (GPU jobs): gpu-shared\
QOS (GPU jobs only): gpu-shared-eot\
QOS (compute partition): normal-eot (for short batch jobs only)\
Cores: CPU: 16 GPU: 1\
RAM: CPU: 16G GPU: up to 64G\
GPU (if used): 1\
Time Limit (min): 60\
Singularity Image File Location (for TensorFlow): /cm/shared/apps/containers/singularity/tensorflow/tensorflow-latest.sif\
Singularity Image File Location (for PyTorch): /cm/shared/apps/containers/singularity/pytorch/pytorch-latest.sif\
Modules: singularitypro\
Reservation: nairrworkshop (this reservation can be used only from April 2, 9AM – April 3, 1:30PM), any other time leave blank\

Tips for EXPANASE:  
\- Use 'shared' for all CPU-only interactive jobs.  
\- Use 'gpu-shared' + 'gpu-shared-eot' QOS for GPU jobs. Prefer short batch jobs due to limited GPU availability.  
\- Only use 'compute' partition with 'normal-eot' QOS for special short batch needs.

## **Jupyter Notebook Settings (Open On Demand) — Delta**
Delta Open on demand Portal : <https://openondemand.delta.ncsa.illinois.edu/>

## For CPU Jobs

Account: beeh-delta-cpu\
Partition: cpu-interactive\
Duration: 1:00:00\
CPUs: 16\
RAM: 64G\
GPUs: 0

## For GPU Jobs

Account: beeh-delta-gpu\
Partition: gpuA100x4-interactive or gpuA40x4-interactive\
Duration: 1:00:00\
CPUs: 16\
RAM: 64G\
GPUs: 1

## **Jupyter Notebook Settings (Open On Demand) — DeltaAI**
DeltaAI Open On Demand portal  :<https://gh-ondemand.delta.ncsa.illinois.edu/>

Account: beeh-dtai-gh\
Partition: ghx4-interactive\
Duration: 2:00:00\
CPUs: 72\
RAM: (leave blank)\
GPUs: 1
<br>


**Track2: Introduction to Pytorch**
<https://github.com/access-ci-org/AI-Unlocked-Workshop-2025/tree/main/track2-Intermediate-to-Advanced/introduction-to-pytorch>\
Lab Notes : <https://github.com/access-ci-org/AI-Unlocked-Workshop-2025/blob/main/track2-Intermediate-to-Advanced/introduction-to-pytorch/setup-instructions.md>

**Track2 : Introduction to Tensorflow**
<https://github.com/access-ci-org/AI-Unlocked-Workshop-2025/tree/main/track2-Intermediate-to-Advanced/introduction-to-tensorflow>\
Lab notes:
<https://github.com/access-ci-org/AI-Unlocked-Workshop-2025/blob/main/track2-Intermediate-to-Advanced/introduction-to-tensorflow/workshop-notes.md>
