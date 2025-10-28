# Compatibility with the

SMDDP library optimized for AWS infrastructure

You can use the SageMaker model parallelism library v2 (SMP v2) in conjunction with the
[SageMaker distributed data parallelism (SMDDP)
library](data-parallel.md "data-parallel.md") that offers the `AllGather` collective communication
operation optimized for AWS infrastructure. In distributed training, collective
communication operations are designed for synchronizing multiple GPU workers and
exchange information between them. `AllGather` is one of the core collective
communication operations typically used in sharded data parallelism. To learn more about
the SMDDP `AllGather` operation, see [SMDDP AllGather collective
operation](data-parallel-intro.md#data-parallel-allgather "data-parallel-intro.md#data-parallel-allgather") Optimizing such collective communication operations would directly contribute to a
faster end-to-end training without side effects on convergence.

###### Note

The SMDDP library supports P4 and P4de instances (see also [Supported frameworks, AWS Regions, and
instances types](distributed-data-parallel-support.md "distributed-data-parallel-support.md") by the SMDDP library).

The SMDDP library integrates natively with PyTorch through the [process group](https://pytorch.org/docs/stable/distributed.html "https://pytorch.org/docs/stable/distributed.html") layer.
To use the SMDDP library, you only need to add two lines of code to your training
script. It supports any training frameworks such as SageMaker Model Parallelism Library,
PyTorch FSDP, and DeepSpeed.

To activate SMDDP and use its `AllGather` operation, you need to add two
lines of code to your training script as part of [Step 1: Adapt your PyTorch FSDP training script](model-parallel-use-api-v2.md#model-parallel-adapt-pytorch-script-v2 "model-parallel-use-api-v2.md#model-parallel-adapt-pytorch-script-v2"). Note that you need to initialize
PyTorch Distributed with the SMDDP backend first, and then run the SMP
initialization.

```
import torch.distributed as dist

# Initialize with SMDDP
import smdistributed.dataparallel.torch.torch_smddp
dist.init_process_group(backend="smddp") # Replacing "nccl"

 # Initialize with SMP
import torch.sagemaker as tsm
tsm.init()
```

[SageMaker Framework Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") for PyTorch (see also [Supported frameworks and
AWS Regions](distributed-model-parallel-support-v2.md "distributed-model-parallel-support-v2.md") by SMP v2 and [Supported frameworks, AWS Regions, and
instances types](distributed-data-parallel-support.md "distributed-data-parallel-support.md") by the SMDDP library) are pre-packaged
with the SMP binary and the SMDDP binary. To learn more about the SMDDP library, see
[Run distributed training with the SageMaker AI distributed data
parallelism library](data-parallel.md "data-parallel.md").
