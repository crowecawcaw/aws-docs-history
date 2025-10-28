# Validating runtime before running production workloads on a HyperPod Slurm

cluster

To check the runtime before running any production workloads on a Slurm cluster on
HyperPod, use the runtime validation script [`hyperpod-precheck.py`](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/hyperpod-precheck.py "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/hyperpod-precheck.py"). This script checks if the Slurm
cluster has all packages installed for running Docker, if the cluster has a properly
mounted FSx for Lustre file system and a user directory sharing the file system, and if the
Slurm deamon is running on all compute nodes.

To run the script on multiple nodes at once, use `srun` as shown in the
following example command of running the script on a Slurm cluster of 8 nodes.

```
# The following command runs on 8 nodes
srun -N `8` python3 hyperpod-precheck.py
```

###### Note

To learn more about the validation script such as what runtime validation
functions the script provides and guidelines to resolve issues that don't pass the
validations, see [Runtime validation before running workloads](https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod#35-runtime-validation-before-running-workloads "https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod#35-runtime-validation-before-running-workloads") in the _Awsome
Distributed Training GitHub repository_.
