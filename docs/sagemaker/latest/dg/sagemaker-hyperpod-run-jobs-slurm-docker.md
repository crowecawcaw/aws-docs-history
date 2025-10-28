# Running Docker containers on

a Slurm compute node on HyperPod

To run Docker containers with Slurm on SageMaker HyperPod, you need to use [Enroot](https://github.com/NVIDIA/enroot "https://github.com/NVIDIA/enroot") and [Pyxis](https://github.com/NVIDIA/pyxis "https://github.com/NVIDIA/pyxis"). The Enroot package helps
convert Docker images into a runtime that Slurm can understand, while the Pyxis enables
scheduling the runtime as a Slurm job through an `srun` command, `srun
 --container-image=`docker/image:tag``.

###### Tip

The Docker, Enroot, and Pyxis packages should be installed during cluster creation
as part of running the lifecycle scripts as guided in [Base lifecycle scripts provided by HyperPod](sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md "sagemaker-hyperpod-lifecycle-best-practices-slurm-slurm-base-config.md"). Use
the [base lifecycle scripts](https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config "https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config") provided by the HyperPod service team
when creating a HyperPod cluster. Those base scripts are set up to install
the packages by default. In the [`config.py`](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/config.py "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/config.py") script, there's the `Config`
class with the boolean type parameter for installing the packages set to
`True` (`enable_docker_enroot_pyxis=True`). This is called
by and parsed in the [`lifecycle_script.py`](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/lifecycle_script.py "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/lifecycle_script.py") script, which calls
`install_docker.sh` and `install_enroot_pyxis.sh` scripts
from the [`utils`](https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/utils "https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/utils") folder. The installation scripts are where the
actual installations of the packages take place. Additionally, the installation
scripts identify if they can detect NVMe store paths from the instances they are run
on and set up the root paths for Docker and Enroot to `/opt/dlami/nvme`.
The default root volume of any fresh instance is mounted to `/tmp` only
with a 100GB EBS volume, which runs out if the workload you plan to run involves
training of LLMs and thus large size Docker containers. If you use instance families
such as P and G with local NVMe storage, you need to make sure that you use the NVMe
storage attached at `/opt/dlami/nvme`, and the installation scripts take
care of the configuration processes.

**To check if the root paths are set up properly**

On a compute node of your Slurm cluster on SageMaker HyperPod, run the following commands to
make sure that the lifecycle script worked properly and the root volume of each node is
set to `/opt/dlami/nvme/*`. The following commands shows examples of checking
the Enroot runtime path and the data root path for 8 compute nodes of a Slurm
cluster.

```
`$` `srun -N `8` cat /etc/enroot/enroot.conf | grep "ENROOT_RUNTIME_PATH"`
`ENROOT_RUNTIME_PATH /opt/dlami/nvme/tmp/enroot/user-$(id -u)
... // The same or similar lines repeat 7 times`
```

```
`$` `srun -N `8` cat /etc/docker/daemon.json`
`{
 "data-root": "/opt/dlami/nvme/docker/data-root"
}
... // The same or similar lines repeat 7 times`
```

After you confirm that the runtime paths are properly set to
`/opt/dlami/nvme/*`, you're ready to build and run Docker containers with
Enroot and Pyxis.

**To test Docker with Slurm**

1. On your compute node, try the following commands to check if Docker and Enroot
   are properly installed.

```
`$` `docker --help`
`$` `enroot --help`
```

2. Test if Pyxis and Enroot installed correctly by running one of the [NVIDIA CUDA
   Ubuntu](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda "https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda") images.

````
`$` `srun --container-image=nvidia/cuda:`XX.Y.Z`-base-ubuntu`XX.YY` nvidia-smi`
`pyxis: importing docker image: nvidia/cuda:XX.Y.Z-base-ubuntuXX.YY
pyxis: imported docker image: nvidia/cuda:XX.Y.Z-base-ubuntuXX.YY
DAY MMM DD HH:MM:SS YYYY
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.141.03 Driver Version: 470.141.03 CUDA Version: XX.YY |
|-------------------------------+----------------------+----------------------+
| GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC |
| Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. |
| | | MIG M. |
|===============================+======================+======================|
| 0 Tesla T4 Off | 00000000:00:1E.0 Off | 0 |
| N/A 40C P0 27W / 70W | 0MiB / 15109MiB | 0% Default |
| | | N/A | +-------------------------------+----------------------+----------------------+ +-----------------------------------------------------------------------------+
| Processes: | | GPU GI CI PID Type Process name GPU Memory |
| ID ID Usage | |=============================================================================|
| No running processes found | +-----------------------------------------------------------------------------+` ``` You can also test it by creating a script and running an `sbatch` command as follows. ``` `$` `cat <<EOF >> container-test.sh #!/bin/bash #SBATCH --container-image=nvidia/cuda:`XX.Y.Z`-base-ubuntu`XX.YY` nvidia-smi EOF` `$` `sbatch container-test.sh` `pyxis: importing docker image: nvidia/cuda:XX.Y.Z-base-ubuntuXX.YY pyxis: imported docker image: nvidia/cuda:XX.Y.Z-base-ubuntuXX.YY DAY MMM DD HH:MM:SS YYYY +-----------------------------------------------------------------------------+ | NVIDIA-SMI 470.141.03 Driver Version: 470.141.03 CUDA Version: XX.YY |
|-------------------------------+----------------------+----------------------+
| GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC |
| Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. |
| | | MIG M. |
|===============================+======================+======================|
| 0 Tesla T4 Off | 00000000:00:1E.0 Off | 0 |
| N/A 40C P0 27W / 70W | 0MiB / 15109MiB | 0% Default |
| | | N/A | +-------------------------------+----------------------+----------------------+ +-----------------------------------------------------------------------------+
| Processes: | | GPU GI CI PID Type Process name GPU Memory |
| ID ID Usage | |=============================================================================|
| No running processes found | +-----------------------------------------------------------------------------+` ``` **To run a test Slurm job with Docker** After you have completed setting up Slurm with Docker, you can bring any pre-built Docker images and run using Slurm on SageMaker HyperPod. The following is a sample use case that walks you through how to run a training job using Docker and Slurm on SageMaker HyperPod. It shows an example job of model-parallel training of the Llama 2 model with the SageMaker AI model parallelism (SMP) library. 1. If you want to use one of the pre-built ECR images distributed by SageMaker AI or DLC, make sure that you give your HyperPod cluster the permissions to pull ECR images through the [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod"). If you use your own or an open source Docker image, you can skip this step. Add the following permissions to the [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod"). In this tutorial, we use the [SMP Docker image](distributed-model-parallel-support-v2.md#distributed-model-parallel-supported-frameworks-v2 "distributed-model-parallel-support-v2.md#distributed-model-parallel-supported-frameworks-v2") pre-packaged with the SMP library . JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ecr:BatchCheckLayerAvailability", "ecr:BatchGetImage", "ecr-public:*", "ecr:GetDownloadUrlForLayer", "ecr:GetAuthorizationToken", "sts:*" ], "Resource": "*" } ] }` ``` 2. On the compute node, clone the repository and go to the folder that provides the example scripts of training with SMP. ``` `$` `git clone https://github.com/aws-samples/awsome-distributed-training/` `$` `cd awsome-distributed-training/3.test_cases/17.SM-modelparallelv2` ``` 3. In this tutorial, run the sample script [`docker_build.sh`](https://github.com/aws-samples/awsome-distributed-training/blob/main/3.test_cases/17.SM-modelparallelv2/docker_build.sh "https://github.com/aws-samples/awsome-distributed-training/blob/main/3.test_cases/17.SM-modelparallelv2/docker_build.sh") that pulls the SMP Docker image, build the Docker container, and runs it as an Enroot runtime. You can modify this as you want. ``` `$` `cat docker_build.sh` `#!/usr/bin/env bash region=`us-west-2` dlc_account_id=`658645717510` aws ecr get-login-password --region $region | docker login --username AWS --password-stdin $dlc_account_id.dkr.ecr.$region.amazonaws.com docker build -t smpv2 . enroot import -o smpv2.sqsh dockerd://smpv2:latest` ``` ``` `$` `bash docker_build.sh` ``` 4. Create a batch script to launch a training job using `sbatch`. In this tutorial, the provided sample script [`launch_training_enroot.sh`](https://github.com/aws-samples/awsome-distributed-training/blob/main/3.test_cases/17.SM-modelparallelv2/launch_training_enroot.sh "https://github.com/aws-samples/awsome-distributed-training/blob/main/3.test_cases/17.SM-modelparallelv2/launch_training_enroot.sh") launches a model-parallel training job of the 70-billion-parameter Llama 2 model with a synthetic dataset on 8 compute nodes. A set of training scripts are provided at [`3.test_cases/17.SM-modelparallelv2/scripts`](https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/17.SM-modelparallelv2/scripts "https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/17.SM-modelparallelv2/scripts"), and `launch_training_enroot.sh` takes `train_external.py` as the entrypoint script. ###### Important To use the a Docker container on SageMaker HyperPod, you must mount the `/var/log` directory from the host machine, which is the HyperPod compute node in this case, onto the `/var/log` directory in the container. You can set it up by adding the following variable for Enroot. ``` "${HYPERPOD_PATH:="`/var/log/aws/clusters`":"`/var/log/aws/clusters`"}" ``` ``` `$` `cat `launch_training_enroot.sh`` `#!/bin/bash # Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. # SPDX-License-Identifier: MIT-0 #SBATCH --nodes=`8` # number of nodes to use, 2 p4d(e) = 16 A100 GPUs #SBATCH --job-name=`smpv2_llama` # name of your job #SBATCH --exclusive # job has exclusive use of the resource, no sharing #SBATCH --wait-all-nodes=1 set -ex; ########################### ###### User Variables ##### ########################### ######################### model_type=`llama_v2` model_size=`70b` # Toggle this to use synthetic data use_synthetic_data=1 # To run training on your own data set Training/Test Data path -> Change this to the tokenized dataset path in Fsx. Acceptable formats are huggingface (arrow) and Jsonlines. # Also change the use_synthetic_data to 0 export TRAINING_DIR=`/fsx/path_to_data` export TEST_DIR=`/fsx/path_to_data` export CHECKPOINT_DIR=$(pwd)/checkpoints # Variables for Enroot : "${IMAGE:=$(pwd)`/smpv2.sqsh`}" : "${HYPERPOD_PATH:="`/var/log/aws/clusters`":"`/var/log/aws/clusters`"}" `# This is needed for validating its hyperpod cluster` : "${TRAIN_DATA_PATH:=$TRAINING_DIR:$TRAINING_DIR}" : "${TEST_DATA_PATH:=$TEST_DIR:$TEST_DIR}" : "${CHECKPOINT_PATH:=$CHECKPOINT_DIR:$CHECKPOINT_DIR}" ########################### ## Environment Variables ## ########################### #export NCCL_SOCKET_IFNAME=en export NCCL_ASYNC_ERROR_HANDLING=1 export NCCL_PROTO="simple" export NCCL_SOCKET_IFNAME="^lo,docker" export RDMAV_FORK_SAFE=1 export FI_EFA_USE_DEVICE_RDMA=1 export NCCL_DEBUG_SUBSYS=off export NCCL_DEBUG="INFO" export SM_NUM_GPUS=8 export GPU_NUM_DEVICES=8 export FI_EFA_SET_CUDA_SYNC_MEMOPS=0 # async runtime error ... export CUDA_DEVICE_MAX_CONNECTIONS=1 ######################### ## Command and Options ## ######################### if [ "$model_size" == "7b" ]; then HIDDEN_WIDTH=4096 NUM_LAYERS=32 NUM_HEADS=32 LLAMA_INTERMEDIATE_SIZE=11008 DEFAULT_SHARD_DEGREE=8 # More Llama model size options elif [ "$model_size" == "70b" ]; then HIDDEN_WIDTH=8192 NUM_LAYERS=80 NUM_HEADS=64 LLAMA_INTERMEDIATE_SIZE=28672 # Reduce for better perf on p4de DEFAULT_SHARD_DEGREE=64 fi if [ -z "$shard_degree" ]; then SHARD_DEGREE=$DEFAULT_SHARD_DEGREE else SHARD_DEGREE=$shard_degree fi if [ -z "$LLAMA_INTERMEDIATE_SIZE" ]; then LLAMA_ARGS="" else LLAMA_ARGS="--llama_intermediate_size $LLAMA_INTERMEDIATE_SIZE " fi if [ $use_synthetic_data == 1 ]; then echo "using synthetic data" declare -a ARGS=( --container-image $IMAGE --container-mounts $HYPERPOD_PATH,$CHECKPOINT_PATH ) else echo "using real data...." declare -a ARGS=( --container-image $IMAGE --container-mounts $HYPERPOD_PATH,$TRAIN_DATA_PATH,$TEST_DATA_PATH,$CHECKPOINT_PATH ) fi declare -a TORCHRUN_ARGS=( # change this to match the number of gpus per node: --nproc_per_node=`8` \ --nnodes=$SLURM_JOB_NUM_NODES \ --rdzv_id=$SLURM_JOB_ID \ --rdzv_backend=`c10d` \ --rdzv_endpoint=$(hostname) \ ) srun -l "${ARGS[@]}" torchrun "${TORCHRUN_ARGS[@]}" `/path_to/train_external.py` \ --train_batch_size `4` \ --max_steps `100` \ --hidden_width $HIDDEN_WIDTH \ --num_layers $NUM_LAYERS \ --num_heads $NUM_HEADS \ ${LLAMA_ARGS} \ --shard_degree $SHARD_DEGREE \ --model_type $model_type \ --profile_nsys `1` \ --use_smp_implementation `1` \ --max_context_width `4096` \ --tensor_parallel_degree `1` \ --use_synthetic_data $use_synthetic_data \ --training_dir $TRAINING_DIR \ --test_dir $TEST_DIR \ --dataset_type `hf` \ --checkpoint_dir $CHECKPOINT_DIR \ --checkpoint_freq `100` \` `$` `sbatch `launch_training_enroot.sh`` ``` To find the downloadable code examples, see [Run a model-parallel training job using the SageMaker AI model parallelism library, Docker and Enroot with Slurm](https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/17.SM-modelparallelv2#option-2----run-training-using-docker-and-enroot "https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/17.SM-modelparallelv2#option-2----run-training-using-docker-and-enroot") in the *Awsome Distributed Training GitHub repository*. For more information about distributed training with a Slurm cluster on SageMaker HyperPod, proceed to the next topic at [Running distributed training workloads with Slurm on HyperPod](sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload.md "sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload.md").
````
