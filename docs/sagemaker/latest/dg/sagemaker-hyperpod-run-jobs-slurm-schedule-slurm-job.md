# Scheduling a Slurm job on

a SageMaker HyperPod cluster

You can launch training jobs using the standard Slurm `sbatch` or
`srun` commands. For example, to launch an 8-node training job, you can
run `srun -N 8 --exclusive train.sh` SageMaker HyperPod supports training in a
range of environments, including `conda`, `venv`,
`docker`, and `enroot`. You can configure an ML environment by
running lifecycle scripts on your SageMaker HyperPod clusters. You also have an option to
attach a shared file system such as Amazon FSx, which can also be used as a virtual
environment.

The following example shows how to run a job for training Llama-2 with the Fully
Sharded Data Parallelism (FSDP) technique on a SageMaker HyperPod cluster with an Amazon FSx shared
file system. You can also find more examples from the [Awsome Distributed
Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/ "https://github.com/aws-samples/awsome-distributed-training/").

###### Tip

All SageMaker HyperPod examples are available in the `3.test_cases` folder of
the [Awsome
Distributed Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/ "https://github.com/aws-samples/awsome-distributed-training/").

1. Clone the [Awsome
   Distributed Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/ "https://github.com/aws-samples/awsome-distributed-training/"), and copy the training job
   examples to your Amazon FSx file system.

```
`$` `TRAINING_DIR=`/fsx/users/my-user/fsdp``
`$` `git clone https://github.com/aws-samples/awsome-distributed-training/`
```

2. Run the [`create_conda_env.sh`](https://github.com/aws-samples/awsome-distributed-training/blob/main/3.test_cases/10.FSDP/0.create_conda_env.sh "https://github.com/aws-samples/awsome-distributed-training/blob/main/3.test_cases/10.FSDP/0.create_conda_env.sh") script. This creates a
   `conda` environment on your Amazon FSx file system. Make sure that the
   file system is accessible to all nodes in the cluster.
3. Build the virtual Conda environment by launching a single node slurm job as
   follows.

```
`$` `srun -N 1 `/path_to/create_conda_env.sh``
```

4. After the environment is built, you can launch a training job by pointing to
   the environment path on the shared volume. You can launch both single-node and
   multi-node training jobs with the same setup. To launch a job, create a job
   launcher script (also called an entry point script) as follows.

```
#!/usr/bin/env bash
set -ex

ENV_PATH=`/fsx/users/my_user/pytorch_env`
TORCHRUN=$ENV_PATH/bin/torchrun
TRAINING_SCRIPT=`/fsx/users/my_user/pt_train.py`

WORLD_SIZE_JOB=$SLURM_NTASKS
RANK_NODE=$SLURM_NODEID
PROC_PER_NODE=8
MASTER_ADDR=(`scontrol show hostnames \$SLURM_JOB_NODELIST | head -n 1`)
MASTER_PORT=$(expr 10000 + $(echo -n $SLURM_JOBID | tail -c 4))

DIST_ARGS="--nproc_per_node=$PROC_PER_NODE \
           --nnodes=$WORLD_SIZE_JOB \
           --node_rank=$RANK_NODE \
           --master_addr=$MASTER_ADDR \
           --master_port=$MASTER_PORT \
          "

$TORCHRUN $DIST_ARGS $TRAINING_SCRIPT
```

###### Tip

If you want to make your training job more resilient against hardware
failures by using the auto-resume capability of SageMaker HyperPod, you need to
properly set up the environment variable `MASTER_ADDR` in the
entrypoint script. To learn more, see [Automatic node
recovery and auto-resume](sagemaker-hyperpod-resiliency-slurm-auto-resume.md "sagemaker-hyperpod-resiliency-slurm-auto-resume.md").

This tutorial assumes that this script is saved as
`/fsx/users/my_user/train.sh`. 5. With this script in the shared volume at
`/fsx/users/my_user/train.sh`, run the following
`srun` command to schedule the Slurm job.

```
`$` `cd /fsx/users/my_user/`
`$` `srun -N 8 train.sh`
```
