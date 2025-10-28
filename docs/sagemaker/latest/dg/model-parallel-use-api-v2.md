# Use the SageMaker model parallelism

library v2

On this page, you'll learn how to use the SageMaker model parallelism library v2 APIs and get
started with running a PyTorch Fully Sharded Data Parallel (FSDP) training job in the SageMaker
Training platform or on a SageMaker HyperPod cluster.

There are various scenarios for running a PyTorch training job with SMP v2.

1. For SageMaker training, use one of the pre-built SageMaker Framework Containers for PyTorch
   v2.0.1 and later, which are pre-packaged with SMP v2.
2. Use the SMP v2 binary file to set up a Conda environment for running a distributed
   training workload on a SageMaker HyperPod cluster.
3. Extend the pre-built SageMaker Framework Containers for PyTorch v2.0.1 and later
   to install any additional functional requirements for your use case. To learn how to
   extend a pre-built container, see [Extend a Pre-built
   Container](prebuilt-containers-extend.md "prebuilt-containers-extend.md").
4. You can also bring your own Docker container and manually set up all SageMaker
   Training environment using the [SageMaker Training
   toolkit](https://github.com/aws/sagemaker-training-toolkit "https://github.com/aws/sagemaker-training-toolkit") and install the SMP v2 binary file. This is the least
   recommended option due to the complexity of dependencies. To learn how to run your
   own Docker container, see [Adapting Your Own
   Training Container](adapt-training-container.md "adapt-training-container.md").
   This getting started guide covers the first two scenarios.

###### Topics

- [Step 1: Adapt your PyTorch FSDP training script](#model-parallel-adapt-pytorch-script-v2 "#model-parallel-adapt-pytorch-script-v2")
- [Step 2: Launch a training
  job](#model-parallel-launch-a-training-job-v2 "#model-parallel-launch-a-training-job-v2")

## Step 1: Adapt your PyTorch FSDP training script

To activate and configure the SMP v2 library, start with importing and adding the
`torch.sagemaker.init()` module at the top of the script. This module
takes in the SMP configuration dictionary of [SMP v2 core
feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config") that you'll prepare
in [Step 2: Launch a training
job](#model-parallel-launch-a-training-job-v2 "#model-parallel-launch-a-training-job-v2"). Also, for using the
various core features offered by SMP v2, you might need to make few more changes to
adapt your training script. More detailed instructions on adapting your training script
for using the SMP v2 core features are provided at [Core features of the SageMaker model
parallelism library v2](model-parallel-core-features-v2.md "model-parallel-core-features-v2.md").

SageMaker Training
In your training script, add the following two lines of code, which is the
minimal requirement to start training with SMP v2. In [Step 2: Launch a training
job](#model-parallel-launch-a-training-job-v2 "#model-parallel-launch-a-training-job-v2"), you’ll set up an
object of the SageMaker `PyTorch` estimator class with an SMP
configuration dictionary through the `distribution` argument of
the estimator class.

```
import torch.sagemaker as tsm
tsm.init()
```

###### Note

You can also directly pass a configuration dictionary of the [SMP v2 core
feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config") to
the `torch.sagemaker.init()` module. However, the parameters
passed to the PyTorch estimator in [Step 2: Launch a training
job](#model-parallel-launch-a-training-job-v2 "#model-parallel-launch-a-training-job-v2") take priority
and override the ones specified to the
`torch.sagemaker.init()` module.

SageMaker HyperPod
In your training script, add the following two lines of code. In [Step 2: Launch a training
job](#model-parallel-launch-a-training-job-v2 "#model-parallel-launch-a-training-job-v2"), you’ll set up a
`smp_config.json` file for setting up SMP configurations in
JSON format, and upload it to a storage or a file system mapped with your
SageMaker HyperPod cluster. We recommend that you keep the configuration file
under the same directory where you upload your training script.

```
import torch.sagemaker as tsm
tsm.init("`/dir_to_training_files/smp_config.json`")
```

###### Note

You can also directly pass a configuration dictionary of
the [SMP v2 core
feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config") into the `torch.sagemaker.init()`
module.

## Step 2: Launch a training

job

Learn how to configure SMP distribution options for launching a PyTorch FSDP training
job with SMP core features.

SageMaker Training
When you set up a training job launcher object of the [PyTorch framework estimator](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html") class in the SageMaker Python SDK,
configure [SMP v2 core
feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config") through
`distribution` argument as follows.

###### Note

The `distribution` configuration for SMP v2 is integrated
in the SageMaker Python SDK starting from v2.200. Make sure that you use
the SageMaker Python SDK v2.200 or later.

###### Note

In SMP v2, you should configure `smdistributed` with
`torch_distributed` for the `distribution`
argument of the SageMaker `PyTorch` estimator. With
`torch_distributed`, SageMaker AI runs
`torchrun`, which is the default multi-node job launcher of
[PyTorch Distributed](https://pytorch.org/tutorials/beginner/dist_overview.html "https://pytorch.org/tutorials/beginner/dist_overview.html").

```
from sagemaker.pytorch import PyTorch

estimator = PyTorch(
    framework_version=`2.2.0`,
    py_version="`310`"
    # image_uri="<smp-docker-image-uri>" # For using prior versions, specify the SMP image URI directly.
    entry_point="`your-training-script.py`", # Pass the training script you adapted with SMP from Step 1.
    ... # Configure other required and optional parameters
    distribution={
        "torch_distributed": { "enabled": True },
        "smdistributed": {
            "modelparallel": {
                "enabled": True,
                "parameters": {
                    "hybrid_shard_degree": `Integer`,
                    "sm_activation_offloading": `Boolean`,
                    "activation_loading_horizon": `Integer`,
                    "fsdp_cache_flush_warnings": `Boolean`,
                    "allow_empty_shards": `Boolean`,
                    "tensor_parallel_degree": `Integer`,
                    "expert_parallel_degree": `Integer`,
                    "random_seed": `Integer`
                }
            }
        }
    }
)
```

###### Important

For using one of the prior versions of PyTorch or SMP instead of the
latest, you need to specify the SMP Docker image directly using the
`image_uri` argument instead of the
`framework_version` and `py_version` pair. The
following is an example of

```
estimator = PyTorch(
    ...,
    image_uri="658645717510.dkr.ecr.us-west-2.amazonaws.com/smdistributed-modelparallel:2.2.0-gpu-py310-cu121"
)
```

To find SMP Docker image URIs, see [Supported
frameworks](distributed-model-parallel-support-v2.md#distributed-model-parallel-supported-frameworks-v2 "distributed-model-parallel-support-v2.md#distributed-model-parallel-supported-frameworks-v2").

SageMaker HyperPod
Before you start, make sure if the following prerequisites are
met.

- An Amazon FSx shared directory mounted (`/fsx`) to your
  HyperPod cluster.
- Conda installed in the FSx shared directory. To learn how to
  install Conda, use the instructions at [Installing on Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html "https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html") in the _Conda User
  Guide_.
- `cuda11.8` or `cuda12.1` installed on the
  head and compute nodes of your HyperPod cluster.

If the prerequisites are all met, proceed to the following
instructions on launching a workload with SMP v2 on a HyperPod
cluster.

1. Prepare an `smp_config.json` file that contains a
   dictionary of [SMP v2 core
   feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config").
   Make sure that you upload this JSON file to where you store your
   training script, or the path you specified to the
   `torch.sagemaker.init()` module in [Step 1](#model-parallel-adapt-pytorch-script-v2 "#model-parallel-adapt-pytorch-script-v2").
   If you’ve already passed the configuration dictionary to the
   `torch.sagemaker.init()` module in the training
   script in [Step 1](#model-parallel-adapt-pytorch-script-v2 "#model-parallel-adapt-pytorch-script-v2"), you can skip this step.

```
// smp_config.json
{
    "hybrid_shard_degree": `Integer`,
    "sm_activation_offloading": `Boolean`,
    "activation_loading_horizon": `Integer`,
    "fsdp_cache_flush_warnings": `Boolean`,
    "allow_empty_shards": `Boolean`,
    "tensor_parallel_degree": `Integer`,
    "expert_parallel_degree": `Integer`,
    "random_seed": `Integer`
}
```

2. Upload the `smp_config.json` file to a directory in
   your file system. The directory path must match with the path you
   specified in [Step 1](#model-parallel-adapt-pytorch-script-v2 "#model-parallel-adapt-pytorch-script-v2"). If you’ve already passed the configuration
   dictionary to the `torch.sagemaker.init()` module in the
   training script, you can skip this step.
3. On the compute nodes of your cluster, start a terminal session
   with the following command.

```
sudo su -l ubuntu
```

4. Create a Conda environment on the compute nodes. The following
   code is an example script of creating a Conda environment and
   installing SMP, [SMDDP](data-parallel.md "data-parallel.md"), CUDA,
   and other dependencies.

```
# Run on compute nodes
SMP_CUDA_VER=`<11.8 or 12.1>`

source /fsx/`<path_to_miniconda>`/miniconda3/bin/activate

export ENV_PATH=/fsx/<path to miniconda>/miniconda3/envs/`<ENV_NAME>`
conda create -p ${ENV_PATH} python=3.10

conda activate ${ENV_PATH}

# Verify aws-cli is installed: Expect something like "aws-cli/2.15.0*"
aws ‐‐version
# Install aws-cli if not already installed
# https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#cliv2-linux-install

# Install the SMP library
conda install pytorch="`2.0.1=sm_py3.10_cuda`${SMP_CUDA_VER}*" packaging ‐‐override-channels \
  -c `https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/smp-2.0.0-pt-2.0.1/2023-12-11/smp-v2/` \
  -c pytorch -c numba/label/dev \
  -c nvidia -c conda-forge

# Install dependencies of the script as below
python -m pip install packaging transformers==4.31.0 accelerate ninja tensorboard h5py datasets \
    && python -m pip install expecttest hypothesis \
    && python -m pip install "flash-attn>=2.0.4" ‐‐no-build-isolation

# Install the SMDDP wheel
SMDDP_WHL="`smdistributed_dataparallel-2.0.2-cp310-cp310-linux_x86_64.whl`" \
  && wget -q `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.0.1/cu118/2023-12-07/`${SMDDP_WHL} \
  && pip install ‐‐force ${SMDDP_WHL} \
  && rm ${SMDDP_WHL}

# cuDNN installation for Transformer Engine installation for CUDA 11.8
# Please download from below link, you need to agree to terms
# https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.5/local_installers/11.x/cudnn-linux-x86_64-8.9.5.30_cuda11-archive.tar.xz

tar xf cudnn-linux-x86_64-8.9.5.30_cuda11-archive.tar.xz \
    && rm -rf /usr/local/cuda-$SMP_CUDA_VER/include/cudnn* /usr/local/cuda-$SMP_CUDA_VER/lib/cudnn* \
    && cp ./cudnn-linux-x86_64-8.9.5.30_cuda11-archive/include/* /usr/local/cuda-$SMP_CUDA_VER/include/ \
    && cp ./cudnn-linux-x86_64-8.9.5.30_cuda11-archive/lib/* /usr/local/cuda-$SMP_CUDA_VER/lib/ \
    && rm -rf cudnn-linux-x86_64-8.9.5.30_cuda11-archive.tar.xz \
    && rm -rf cudnn-linux-x86_64-8.9.5.30_cuda11-archive/

# Please download from below link, you need to agree to terms
# https://developer.download.nvidia.com/compute/cudnn/secure/8.9.7/local_installers/12.x/cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz \
# cuDNN installation for TransformerEngine installation for cuda12.1
tar xf cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz \
    && rm -rf /usr/local/cuda-$SMP_CUDA_VER/include/cudnn* /usr/local/cuda-$SMP_CUDA_VER/lib/cudnn* \
    && cp ./cudnn-linux-x86_64-8.9.7.29_cuda12-archive/include/* /usr/local/cuda-$SMP_CUDA_VER/include/ \
    && cp ./cudnn-linux-x86_64-8.9.7.29_cuda12-archive/lib/* /usr/local/cuda-$SMP_CUDA_VER/lib/ \
    && rm -rf cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz \
    && rm -rf cudnn-linux-x86_64-8.9.7.29_cuda12-archive/

# TransformerEngine installation
export CUDA_HOME=/usr/local/cuda-$SMP_CUDA_VER
export CUDNN_PATH=/usr/local/cuda-$SMP_CUDA_VER/lib
export CUDNN_LIBRARY=/usr/local/cuda-$SMP_CUDA_VER/lib
export CUDNN_INCLUDE_DIR=/usr/local/cuda-$SMP_CUDA_VER/include
export PATH=/usr/local/cuda-$SMP_CUDA_VER/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-$SMP_CUDA_VER/lib

python -m pip install ‐‐no-build-isolation git+https://github.com/NVIDIA/TransformerEngine.git@v1.0
```

5. Run a test training job.
   1. In the shared file system (`/fsx`), clone the
      [Awsome Distributed Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/ "https://github.com/aws-samples/awsome-distributed-training/"),
      and go to the `3.test_cases/11.modelparallel`
      folder.

   ```
   git clone https://github.com/aws-samples/awsome-distributed-training/
   cd awsome-distributed-training/3.test_cases/11.modelparallel
   ```

   2. Submit a job using `sbatch` as follows.

   ```
   conda activate <ENV_PATH>
   sbatch -N 16 conda_launch.sh
   ```

   If the job submission is successful, the output message of
   this `sbatch` command should be similar to
   `Submitted batch job ABCDEF`. 3. Check the log file in the current directory
   under `logs/`.

   ```
   tail -f ./logs/`fsdp_smp_ABCDEF.out`
   ```
