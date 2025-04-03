## Hands-On Material for Introduction to TensorFlow Session

### Jupyter Notebook on Expanse
(a) Login to the Expanse portal following the directions given in the prep email & folder <br>
(b) Open a terminal window from the portal <br>
(c) Clone the repository (if not already done) <br>
```
git clone https://github.com/access-ci-org/AI-Unlocked-Workshop-2025.git
```
(d) Click on the Jupyter App and it should send you to a form <br>
(e) In the form fill out the following fields: <br>
Account: <b>ukl119</b> <br>
Partition: <b>shared</b> <br>
Time Limit: <b> 30 </b> <br>
Number of cores: <b> 4 </b> <br>
Memory Required: <b> 4 </b> <br>
GPU: <b> 0 </b> <br>
Singularity image file location: <b>/cm/shared/apps/containers/singularity/tensorflow/tensorflow-latest.sif </b> <br>
Environment modules to be loaded: <b> singularitypro </b> <br>
Reservation: <b> nairrworkshop </b> <br>
and then submit the form. You should see a status screen. Make sure the job is running, mapped, and proxied before proceeding further. Once you get the jupyter link, click on it and then navigate the folders to the tensorflow directory to find our notebook (C24_DL_MNIST_INTRO_v1soltn.ipynb). Start the notebook and follow along in the notebook.
### Jupyter Notebook on Delta
(a) Follow Paola's instructions on cloning the workshop repository (if not already done) and her instructions on spinning up a Jupyter notebook on Delta
https://github.com/access-ci-org/AI-Unlocked-Workshop-2025/blob/16d41bacae9a3c2c740add8f8217728a315c93db/track2-Intermediate-to-Advanced/Deep-Learning-vs-Machine-Learning/Delta%20Instructions%20-%20Getting%20the%20Session%20Jupyter%20Notebook%20Running.pdf
<br>
(b) Navigate to introduction-to-tensorflow folder in the cloned directory and click on the notebook.
### Batch jobs on Expanse and Delta

(a) Open a terminal window via the portal on Expanse OR Delta <br>
(b) Clone the repository (if not already done)
```
git clone https://github.com/access-ci-org/AI-Unlocked-Workshop-2025.git
```
(c) Change to TensorFlow directory
```
cd AI-Unlocked-Workshop-2025/track2-Intermediate-to-Advanced/introduction-to-tensorflow
```
(d) Run jobs <br>
#### On Expanse: <br>
Multinode Horovod Job:
```
sbatch run-hvd-main-cpu2.sb
```
Multinode tfdist GPU Job (we might run into queue limits on this one but the job is quick so can wait and retry) :
```
sbatch run-clusterresolver-gpu2node.sb
```
#### On Delta: <br>
Run batch job using NGC container:
```
sbatch delta-example.sb
```
On both machines you can use "squeue -u $USER" to see the status of your job. Check for output files that get created once the job completes.
