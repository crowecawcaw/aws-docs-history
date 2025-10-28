# Running distributed training workloads with Slurm on HyperPod

SageMaker HyperPod is specialized for workloads of training large language models (LLMs) and
foundation models (FMs). These workloads often require the use of multiple parallelism
techniques and optimized operations for ML infrastructure and resources. Using
SageMaker HyperPod, you can use the following SageMaker AI distributed training frameworks:

- The [SageMaker AI distributed data parallelism (SMDDP)
  library](data-parallel.md "data-parallel.md") that offers collective communication operations optimized for
  AWS.
- The [SageMaker AI model parallelism (SMP)
  library](model-parallel-v2.md "model-parallel-v2.md") that implements various model parallelism techniques.

###### Topics

- [Using SMDDP on a SageMaker HyperPod](#sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload-smddp "#sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload-smddp")
- [Using SMP on a SageMaker HyperPod cluster](#sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload-smp "#sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload-smp")

## Using SMDDP on a SageMaker HyperPod

The [SMDDP library](data-parallel.md "data-parallel.md") is a collective
communication library that improves compute performance of distributed data parallel
training. The SMDDP library works with the following open source distributed
training frameworks:

- [PyTorch
  distributed data parallel (DDP)](https://pytorch.org/docs/stable/notes/ddp.html "https://pytorch.org/docs/stable/notes/ddp.html")
- [PyTorch fully
  sharded data parallelism (FSDP)](https://pytorch.org/docs/stable/fsdp.html "https://pytorch.org/docs/stable/fsdp.html")
- [DeepSpeed](https://github.com/microsoft/DeepSpeed "https://github.com/microsoft/DeepSpeed")
- [Megatron-DeepSpeed](https://github.com/microsoft/Megatron-DeepSpeed "https://github.com/microsoft/Megatron-DeepSpeed")

The SMDDP library addresses communications overhead of the key collective
communication operations by offering the following for SageMaker HyperPod.

- The library offers `AllGather` optimized for AWS.
  `AllGather` is a key operation used in sharded data parallel
  training, which is a memory-efficient data parallelism technique offered by
  popular libraries. These include the SageMaker AI model parallelism (SMP) library,
  DeepSpeed Zero Redundancy Optimizer (ZeRO), and PyTorch Fully Sharded Data
  Parallelism (FSDP).
- The library performs optimized node-to-node communication by fully
  utilizing the AWS network infrastructure and the SageMaker AI ML instance
  topology.

**To run sample data-parallel training jobs**

Explore the following distributed training samples implementing data parallelism
techniques using the SMDDP library.

- [`awsome-distributed-training/3.test_cases/12.SM-dataparallel-FSDP`](https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/12.SM-dataparallel-FSDP "https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/12.SM-dataparallel-FSDP")
- [`awsome-distributed-training/3.test_cases/13.SM-dataparallel-deepspeed`](https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/13.SM-dataparallel-deepspeed "https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/13.SM-dataparallel-deepspeed")

**To set up an environment for using the SMDDP library on
SageMaker HyperPod**

The following are training environment requirements for using the SMDDP library on
SageMaker HyperPod.

- PyTorch v2.0.1 and later
- CUDA v11.8 and later
- `libstdc++` runtime version greater than 3
- Python v3.10.x and later
- `ml.p4d.24xlarge` and `ml.p4de.24xlarge`, which are
  supported instance types by the SMDDP library
- `imdsv2` enabled on training host

Depending on how you want to run the distributed training job, there are two
options to install the SMDDP library:

- A direct installation using the SMDDP binary file.
- Using the SageMaker AI Deep Learning Containers (DLCs) pre-installed with the
  SMDDP library.

Docker images pre-installed with the SMDDP library or the URLs to the SMDDP binary
files are listed at [Supported Frameworks](distributed-data-parallel-support.md#distributed-data-parallel-supported-frameworks "distributed-data-parallel-support.md#distributed-data-parallel-supported-frameworks") in the SMDDP library documentation.

###### To install the SMDDP library on the SageMaker HyperPod DLAMI

- `pip install --no-cache-dir
https://smdataparallel.s3.amazonaws.com/binary/pytorch/`<pytorch-version>/cuXYZ/YYYY-MM-DD/smdistributed_dataparallel-X.Y.Z-cp310-cp310-linux_x86_64`.whl`

###### Note

If you work in a Conda environment, ensure that you install PyTorch
using `conda install` instead of `pip`.

```
conda install pytorch==`X.Y.Z`  torchvision==`X.Y.Z` torchaudio==`X.Y.Z` pytorch-cuda=`X.Y.Z` -c pytorch -c nvidia
```

###### To use the SMDDP library on a Docker container

- The SMDDP library is pre-installed on the SageMaker AI Deep Learning Containers
  (DLCs). To find the list of SageMaker AI framework DLCs for PyTorch with the SMDDP
  library, see [Supported Frameworks](distributed-data-parallel-support.md#distributed-data-parallel-supported-frameworks "distributed-data-parallel-support.md#distributed-data-parallel-supported-frameworks") in the SMDDP library documentation. You
  can also bring your own Docker container with required dependencies
  installed to use the SMDDP library. To learn more about setting up a custom
  Docker container to use the SMDDP library, see also [Create your own Docker container with
  the SageMaker AI distributed data parallel library](data-parallel-bring-your-own-container.md "data-parallel-bring-your-own-container.md").

###### Important

To use the SMDDP library in a Docker container, mount the
`/var/log` directory from the host machine onto
`/var/log` in the container. This can be done by adding
the following option when running your container.

```
docker run `<OTHER_OPTIONS>` **-v /var/log:/var/log** ...
```

To learn how to run data-parallel training jobs with SMDDP in general, see [Distributed training with the SageMaker AI
distributed data parallelism library](data-parallel-modify-sdp.md "data-parallel-modify-sdp.md").

## Using SMP on a SageMaker HyperPod cluster

The [SageMaker AI model parallelism (SMP) library](model-parallel-v2.md "model-parallel-v2.md")
offers various [state-of-the-art
model parallelism techniques](model-parallel-core-features-v2.md "model-parallel-core-features-v2.md"), including:

- fully sharded data parallelism
- expert parallelism
- mixed precision training with FP16/BF16 and FP8 data types
- tensor parallelism

The SMP library is also
compatible with open source frameworks such as PyTorch FSDP, NVIDIA Megatron, and
NVIDIA Transformer Engine.

**To run a sample model-parallel training
workload**

The SageMaker AI service teams provide sample training jobs implementing model
parallelism with the SMP library at [`awsome-distributed-training/3.test_cases/17.SM-modelparallelv2`](https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/17.SM-modelparallelv2 "https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/17.SM-modelparallelv2").
