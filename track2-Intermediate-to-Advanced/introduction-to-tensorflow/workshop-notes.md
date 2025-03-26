## Hands-On Material for Introduction to TensorFlow Session

### Jupyter Notebook on Expanse

### Batch jobs on Expanse and Delta

(a) Open a terminal window via the portal on Expanse OR Delta <br>
(b) Clone the repository
```
git clone https://github.com/access-ci-org/AI-Unlocked-Workshop-2025.git
```
(c) Change to TensorFlow directory
```
cd AI-Unlocked-Workshop-2025/track2-Intermediate-to-Advanced/introduction-to-tensorflow
```
(d) Run jobs <br>
#### On Expanse: <br>
Multinode tfdist GPU Job:
```
sbatch run-clusterresolver-gpu2node.sb
```
Multinode Horovod Job:
```
sbatch run-hvd-main-cpu2.sb
```
#### On Delta: <br>
Run batch job using NGC container:
```
sbatch delta-example.sb
```
On both machines you can use "squeue -u $USER" to see the status of your job. Check for output files that get created once the job completes.
