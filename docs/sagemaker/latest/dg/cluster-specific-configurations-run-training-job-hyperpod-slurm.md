# Running a training job on HyperPod Slurm

SageMaker HyperPod Recipes supports submitting a training job to a GPU/Trainium slurm
cluster. Before you submit the training job, update the cluster configuration. Use
one of the following methods to update the cluster configuration:

- Modify `slurm.yaml`
- Override it through the command line
  After you've updated the cluster configuration, install the environment.

## Configure the cluster

To submit a training job to a Slurm cluster, specify the Slurm-specific
configuration. Modify `slurm.yaml` to configure the Slurm cluster.
The following is an example of a Slurm cluster configuration. You can modify
this file for your own training needs:

```
job_name_prefix: 'sagemaker-'
slurm_create_submission_file_only: False
stderr_to_stdout: True
srun_args:
  # - "--no-container-mount-home"
slurm_docker_cfg:
  docker_args:
    # - "--runtime=nvidia"
  post_launch_commands:
container_mounts:
  - "/fsx:/fsx"
```

1. `job_name_prefix`: Specify a job name prefix to easily
   identify your submissions to the Slurm cluster.
2. `slurm_create_submission_file_only`: Set this configuration
   to True for a dry run to help you debug.
3. `stderr_to_stdout`: Specify whether you're redirecting your
   standard error (stderr) to standard output (stdout).
4. `srun_args`: Customize additional srun configurations, such
   as excluding specific compute nodes. For more information, see the srun
   documentation.
5. `slurm_docker_cfg`: The SageMaker HyperPod recipe launcher
   launches a Docker container to run your training job. You can specify
   additional Docker arguments within this parameter.
6. `container_mounts`: Specify the volumes you're mounting
   into the container for the recipe launcher, for your training jobs to
   access the files in those volumes.
