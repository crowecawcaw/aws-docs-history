# SageMaker AI data parallelism library release notes

See the following release notes to track the latest updates for the SageMaker AI distributed data
parallelism (SMDDP) library.

## The SageMaker AI distributed data parallelism library v2.5.0

_Date: October 17, 2024_

**New features**

- Added support for PyTorch v2.4.1 with CUDA v12.1.

**Integration into Docker containers distributed by the SageMaker AI model
parallelism (SMP) library**

This version of the SMDDP library is migrated to [The SageMaker model parallelism
library v2.6.0](model-parallel-release-notes.md#model-parallel-release-notes-20241017 "model-parallel-release-notes.md#model-parallel-release-notes-20241017").

```
658645717510.dkr.ecr.`<us-west-2>`.amazonaws.com/smdistributed-modelparallel:2.4.1-gpu-py311-cu121
```

For Regions where the SMP Docker images are available, see [AWS Regions](distributed-model-parallel-support-v2.md#distributed-model-parallel-availablity-zone-v2 "distributed-model-parallel-support-v2.md#distributed-model-parallel-availablity-zone-v2").

**Binary file of this release**

You can download or install the library using the following URL.

```
https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.4.1/cu121/2024-10-09/smdistributed_dataparallel-2.5.0-cp311-cp311-linux_x86_64.whl
```

## The SageMaker AI distributed data parallelism library v2.3.0

_Date: June 11, 2024_

**New features**

- Added support for PyTorch v2.3.0 with CUDA v12.1 and Python v3.11.
- Added support for PyTorch Lightning v2.2.5. This is integrated into the
  SageMaker AI framework container for PyTorch v2.3.0.
- Added instance type validation during import to prevent loading the SMDDP
  library on unsupported instance types. For a list of instance types compatible
  with the SMDDP library, see [Supported frameworks, AWS Regions, and
  instances types](distributed-data-parallel-support.md "distributed-data-parallel-support.md").

**Integration into SageMaker AI Framework Containers**

This version of the SMDDP library is migrated to the following [SageMaker AI Framework Container](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only").

- PyTorch v2.3.0

```
`763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.3.0-gpu-py311-cu121-ubuntu20.04-sagemaker`
```

For a complete list of versions of the SMDDP library and the pre-built containers, see
[Supported frameworks, AWS Regions, and
instances types](distributed-data-parallel-support.md "distributed-data-parallel-support.md").

**Binary file of this release**

You can download or install the library using the following URL.

```
https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.3.0/cu121/2024-05-23/smdistributed_dataparallel-2.3.0-cp311-cp311-linux_x86_64.whl
```

**Other changes**

- The SMDDP library v2.2.0 is integrated into the SageMaker AI framework container for
  PyTorch v2.2.0.

## The SageMaker AI distributed data parallelism library v2.2.0

_Date: March 4, 2024_

**New features**

- Added support for PyTorch v2.2.0 with CUDA v12.1.

**Integration into Docker containers distributed by the SageMaker AI model
parallelism (SMP) library**

This version of the SMDDP library is migrated to [The SageMaker model parallelism
library v2.2.0](model-parallel-release-notes.md#model-parallel-release-notes-20240307 "model-parallel-release-notes.md#model-parallel-release-notes-20240307").

```
658645717510.dkr.ecr.`<region>`.amazonaws.com/smdistributed-modelparallel:2.2.0-gpu-py310-cu121
```

For Regions where the SMP Docker images are available, see [AWS Regions](distributed-model-parallel-support-v2.md#distributed-model-parallel-availablity-zone-v2 "distributed-model-parallel-support-v2.md#distributed-model-parallel-availablity-zone-v2").

**Binary file of this release**

You can download or install the library using the following URL.

```
https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.2.0/cu121/2024-03-04/smdistributed_dataparallel-2.2.0-cp310-cp310-linux_x86_64.whl
```

## The SageMaker AI distributed data parallelism library v2.1.0

_Date: March 1, 2024_

**New features**

- Added support for PyTorch v2.1.0 with CUDA v12.1.

**Bug fixes**

- Fixed the CPU memory leak issue in [SMDDP
  v2.0.1](#data-parallel-release-notes-20231207 "#data-parallel-release-notes-20231207").

**Integration into SageMaker AI Framework Containers**

This version of the SMDDP library passed benchmark testing and is migrated to the
following [SageMaker AI Framework Container](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only").

- PyTorch v2.1.0

```
763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.1.0-gpu-py310-cu121-ubuntu20.04-sagemaker
```

**Integration into Docker containers distributed by the SageMaker AI model
parallelism (SMP) library**

This version of the SMDDP library is migrated to [The SageMaker model parallelism
library v2.1.0](model-parallel-release-notes.md#model-parallel-release-notes-20240206 "model-parallel-release-notes.md#model-parallel-release-notes-20240206").

```
658645717510.dkr.ecr.`<region>`.amazonaws.com/smdistributed-modelparallel:2.1.2-gpu-py310-cu121
```

For Regions where the SMP Docker images are available, see [AWS Regions](distributed-model-parallel-support-v2.md#distributed-model-parallel-availablity-zone-v2 "distributed-model-parallel-support-v2.md#distributed-model-parallel-availablity-zone-v2").

**Binary file of this release**

You can download or install the library using the following URL.

```
https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.1.0/cu121/2024-02-04/smdistributed_dataparallel-2.1.0-cp310-cp310-linux_x86_64.whl
```

## The SageMaker AI distributed data

parallelism library v2.0.1

_Date: December 7, 2023_

**New features**

- Added a new SMDDP-implementation of `AllGather` collective
  operation optimized for AWS compute resources and network infrastructure. To
  learn more, see [SMDDP AllGather collective
  operation](data-parallel-intro.md#data-parallel-allgather "data-parallel-intro.md#data-parallel-allgather").
- The SMDDP `AllGather` collective operation is compatible with
  PyTorch FSDP and DeepSpeed. To learn more, see [Use the SMDDP library in your PyTorch training
  script](data-parallel-modify-sdp-pt.md "data-parallel-modify-sdp-pt.md").
- Added support for PyTorch v2.0.1

**Known issues**

- There's a CPU memory leak issue from a gradual CPU memory increase while
  training with SMDDP `AllReduce` in DDP mode.

**Integration into SageMaker AI Framework Containers**

This version of the SMDDP library passed benchmark testing and is migrated to the
following [SageMaker AI Framework Container](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only").

- PyTorch v2.0.1

```
763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.0.1-gpu-py310-cu118-ubuntu20.04-sagemaker
```

**Binary file of this release**

You can download or install the library using the following URL.

```
https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.0.1/cu118/2023-12-07/smdistributed_dataparallel-2.0.2-cp310-cp310-linux_x86_64.whl
```

**Other changes**

- Starting from this release, documentation for the SMDDP library is fully
  available in this _Amazon SageMaker AI Developer Guide_. In favor of the
  complete developer guide for SMDDP v2 housed in the _Amazon SageMaker AI Developer
  Guide_, documentation for the [additional reference for SMDDP v1.x](https://sagemaker.readthedocs.io/en/stable/api/training/smd_data_parallel.html "https://sagemaker.readthedocs.io/en/stable/api/training/smd_data_parallel.html") in the _SageMaker AI Python
  SDK documentation_ is no longer supported. If you still need SMP
  v1.x documentation, see the following snapshot of the documentation at [SageMaker Python SDK v2.212.0 documentation](https://sagemaker.readthedocs.io/en/v2.212.0/api/training/distributed.html#the-sagemaker-distributed-data-parallel-library "https://sagemaker.readthedocs.io/en/v2.212.0/api/training/distributed.html#the-sagemaker-distributed-data-parallel-library").
