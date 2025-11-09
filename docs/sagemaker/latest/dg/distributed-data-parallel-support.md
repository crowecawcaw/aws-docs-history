# Supported frameworks, AWS Regions, and

instances types

Before using the SageMaker AI distributed data parallelism (SMDDP) library, check what are the
supported ML frameworks and instance types and if there are enough quotas in your AWS account
and AWS Region.

## Supported frameworks

The following tables show the deep learning frameworks and their versions that SageMaker AI and
SMDDP support. The SMDDP library is available in [SageMaker AI Framework Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only"), integrated in [Docker containers distributed
by the SageMaker model parallelism (SMP) library v2](distributed-model-parallel-support-v2.md#distributed-model-parallel-supported-frameworks-v2 "distributed-model-parallel-support-v2.md#distributed-model-parallel-supported-frameworks-v2"), or downloadable as a binary
file.

###### Note

To check the latest updates and release notes of the SMDDP library, see the [SageMaker AI data parallelism library release notes](data-parallel-release-notes.md "data-parallel-release-notes.md").

###### Topics

- [PyTorch](#distributed-data-parallel-supported-frameworks-pytorch "#distributed-data-parallel-supported-frameworks-pytorch")
- [PyTorch Lightning](#distributed-data-parallel-supported-frameworks-lightning "#distributed-data-parallel-supported-frameworks-lightning")
- [Hugging Face Transformers](#distributed-data-parallel-supported-frameworks-transformers "#distributed-data-parallel-supported-frameworks-transformers")
- [TensorFlow
  (deprecated)](#distributed-data-parallel-supported-frameworks-tensorflow "#distributed-data-parallel-supported-frameworks-tensorflow")

### PyTorch

| PyTorch version | SMDDP library version                | SageMaker AI Framework Container images pre-installed with SMDDP                                             | SMP Docker images pre-installed with SMDDP                                                           | URL of the binary file\*\*                                                                                                                    |
| --------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| v2.3.1          | `smdistributed-dataparallel==v2.5.0` | Not available                                                                                                | `658645717510.dkr.ecr.`<us-west-2>`.amazonaws.com/smdistributed-modelparallel:2.4.1-gpu-py311-cu121` | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.4.1/cu121/2024-10-09/smdistributed_dataparallel-2.5.0-cp311-cp311-linux_x86_64.whl` |
| v2.3.0          | `smdistributed-dataparallel==v2.3.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.3.0-gpu-py311-cu121-ubuntu20.04-sagemaker` | Currently not available                                                                              | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.3.0/cu121/2024-05-23/smdistributed_dataparallel-2.3.0-cp311-cp311-linux_x86_64.whl` |
| v2.2.0          | `smdistributed-dataparallel==v2.2.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.2.0-gpu-py310-cu121-ubuntu20.04-sagemaker` | `658645717510.dkr.ecr.`<region>`.amazonaws.com/smdistributed-modelparallel:2.2.0-gpu-py310-cu121`    | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.2.0/cu121/2024-03-04/smdistributed_dataparallel-2.2.0-cp310-cp310-linux_x86_64.whl` |
| v2.1.0          | `smdistributed-dataparallel==v2.1.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.1.0-gpu-py310-cu121-ubuntu20.04-sagemaker` | `658645717510.dkr.ecr.`<region>`.amazonaws.com/smdistributed-modelparallel:2.1.2-gpu-py310-cu121`    | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.1.0/cu121/2024-02-04/smdistributed_dataparallel-2.1.0-cp310-cp310-linux_x86_64.whl` |
| v2.0.1          | `smdistributed-dataparallel==v2.0.1` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.0.1-gpu-py310-cu118-ubuntu20.04-sagemaker` | Not available                                                                                        | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.0.1/cu118/2023-12-07/smdistributed_dataparallel-2.0.2-cp310-cp310-linux_x86_64.whl` |
| v2.0.0          | `smdistributed-dataparallel==v1.8.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.0.0-gpu-py310-cu118-ubuntu20.04-sagemaker` | Not available                                                                                        | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.0.0/cu118/2023-03-20/smdistributed_dataparallel-1.8.0-cp310-cp310-linux_x86_64.whl` |
| v1.13.1         | `smdistributed-dataparallel==v1.7.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.13.1-gpu-py39-cu117-ubuntu20.04-sagemaker` | Not available                                                                                        | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/1.13.1/cu117/2023-01-09/smdistributed_dataparallel-1.7.0-cp39-cp39-linux_x86_64.whl`  |
| v1.12.1         | `smdistributed-dataparallel==v1.6.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.12.1-gpu-py38-cu113-ubuntu20.04-sagemaker` | Not available                                                                                        | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/1.12.1/cu113/2022-12-05/smdistributed_dataparallel-1.6.0-cp38-cp38-linux_x86_64.whl`  |
| v1.12.0         | `smdistributed-dataparallel==v1.5.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.12.0-gpu-py38-cu113-ubuntu20.04-sagemaker` | Not available                                                                                        | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/1.12.0/cu113/2022-07-01/smdistributed_dataparallel-1.5.0-cp38-cp38-linux_x86_64.whl`  |
| v1.11.0         | `smdistributed-dataparallel==v1.4.1` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.11.0-gpu-py38-cu113-ubuntu20.04-sagemaker` | Not available                                                                                        | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/1.11.0/cu113/2022-04-14/smdistributed_dataparallel-1.4.1-cp38-cp38-linux_x86_64.whl`  |

\*\* The URLs of the binary files are for installing the SMDDP library in custom
containers. For more information, see [Create your own Docker container with
the SageMaker AI distributed data parallel library](data-parallel-bring-your-own-container.md "data-parallel-bring-your-own-container.md").

###### Note

The SMDDP library is available in AWS Regions where the [SageMaker AI Framework Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") and the [SMP Docker images](distributed-model-parallel-support-v2.md "distributed-model-parallel-support-v2.md") are in
service.

###### Note

The SMDDP library v1.4.0 and later works as a backend of PyTorch distributed
(torch.distributed) data parallelism (torch.parallel.DistributedDataParallel). In
accordance with the change, the following [smdistributed APIs](https://sagemaker.readthedocs.io/en/stable/api/training/sdp_versions/latest/smd_data_parallel_pytorch.html#pytorch-api "https://sagemaker.readthedocs.io/en/stable/api/training/sdp_versions/latest/smd_data_parallel_pytorch.html#pytorch-api") for the PyTorch distributed package have been
deprecated.

- `smdistributed.dataparallel.torch.distributed` is deprecated. Use the
  [torch.distributed](https://pytorch.org/docs/stable/distributed.html "https://pytorch.org/docs/stable/distributed.html") package instead.
- `smdistributed.dataparallel.torch.parallel.DistributedDataParallel` is
  deprecated. Use the [torch.nn.parallel.DistributedDataParallel](https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html "https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html") API instead.
  If you need to use the previous versions of the library (v1.3.0 or before), see the
  [archived SageMaker AI distributed data parallelism documentation](https://sagemaker.readthedocs.io/en/stable/api/training/sdp_versions/latest.html#documentation-archive "https://sagemaker.readthedocs.io/en/stable/api/training/sdp_versions/latest.html#documentation-archive") in the _SageMaker AI
  Python SDK documentation_.

### PyTorch Lightning

The SMDDP library is available for PyTorch Lightning in the following SageMaker AI Framework
Containers for PyTorch and the SMP Docker containers.

**PyTorch Lightning v2**

| PyTorch Lightning version | PyTorch version | SMDDP library version                | SageMaker AI Framework Container images pre-installed with SMDDP                                             | SMP Docker images pre-installed with SMDDP                                                        | URL of the binary file\*\*                                                                                                                    |
| ------------------------- | --------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.2.5                     | 2.3.0           | `smdistributed-dataparallel==v2.3.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.3.0-gpu-py311-cu121-ubuntu20.04-sagemaker` | Currently not available                                                                           | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.3.0/cu121/2024-05-23/smdistributed_dataparallel-2.3.0-cp311-cp311-linux_x86_64.whl` |
| 2.2.0                     | 2.2.0           | `smdistributed-dataparallel==v2.2.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.2.0-gpu-py310-cu121-ubuntu20.04-sagemaker` | `658645717510.dkr.ecr.`<region>`.amazonaws.com/smdistributed-modelparallel:2.2.0-gpu-py310-cu121` | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.2.0/cu121/2024-03-04/smdistributed_dataparallel-2.2.0-cp310-cp310-linux_x86_64.whl` |
| 2.1.2                     | 2.1.0           | `smdistributed-dataparallel==v2.1.0` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.1.0-gpu-py310-cu121-ubuntu20.04-sagemaker` | `658645717510.dkr.ecr.`<region>`.amazonaws.com/smdistributed-modelparallel:2.1.2-gpu-py310-cu121` | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.1.0/cu121/2024-02-04/smdistributed_dataparallel-2.1.0-cp310-cp310-linux_x86_64.whl` |
| 2.1.0                     | 2.0.1           | `smdistributed-dataparallel==v2.0.1` | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.0.1-gpu-py310-cu118-ubuntu20.04-sagemaker` | Not available                                                                                     | `https://smdataparallel.s3.amazonaws.com/binary/pytorch/2.0.1/cu118/2023-12-07/smdistributed_dataparallel-2.0.2-cp310-cp310-linux_x86_64.whl` |

**PyTorch Lightning v1**

| PyTorch Lightning version                  | PyTorch version | SMDDP library version                | SageMaker AI Framework Container images pre-installed with SMDDP                                           | URL of the binary file\*\*                                                                                                                    |
| ------------------------------------------ | --------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.7.2<br>1.7.0<br>1.6.4<br>1.6.3<br>1.5.10 | 1.12.0          | `smdistributed-dataparallel==v1.5.0` | 763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.12.0-gpu-py38-cu113-ubuntu20.04-sagemaker | https://smdataparallel.s3.amazonaws.com/binary/pytorch/1.12.0/cu113/2022-07-01/smdistributed\_dataparallel-1.5.0-cp38-cp38-linux\_x86\_64.whl |

\*\* The URLs of the binary files are for installing the SMDDP library in custom
containers. For more information, see [Create your own Docker container with
the SageMaker AI distributed data parallel library](data-parallel-bring-your-own-container.md "data-parallel-bring-your-own-container.md").

###### Note

PyTorch Lightning and its utility libraries such as Lightning Bolts are not preinstalled
in the PyTorch DLCs. When you construct a SageMaker AI PyTorch estimator and submit a training
job request in [Step 2](data-parallel-use-api.md#data-parallel-framework-estimator "data-parallel-use-api.md#data-parallel-framework-estimator"), you need to provide `requirements.txt` to install
`pytorch-lightning` and `lightning-bolts` in the SageMaker AI PyTorch
training container.

```
# requirements.txt
pytorch-lightning
lightning-bolts
```

For more information about specifying the source directory to place the
`requirements.txt` file along with your training script and a job submission,
see [Using third-party libraries](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#id12 "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#id12") in the _Amazon SageMaker AI
Python SDK documentation_.

### Hugging Face Transformers

The AWS Deep Learning Containers for Hugging Face use the SageMaker Training Containers for
PyTorch and TensorFlow as their base images. To look up the Hugging Face Transformers library
versions and paired PyTorch and TensorFlow versions, see the latest [Hugging Face Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#huggingface-training-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#huggingface-training-containers") and the [Prior Hugging Face Container Versions](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#prior-hugging-face-container-versions "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#prior-hugging-face-container-versions").

### TensorFlow

(deprecated)

###### Important

The SMDDP library discontinued support for TensorFlow and is no longer available in
DLCs for TensorFlow later than v2.11.0. The following table lists previous DLCs for
TensorFlow with the SMDDP library installed.

| TensorFlow version    | SMDDP library version                |
| --------------------- | ------------------------------------ |
| 2.9.1, 2.10.1, 2.11.0 | `smdistributed-dataparallel==v1.4.1` |
| 2.8.3                 | `smdistributed-dataparallel==v1.3.0` |

## AWS Regions

The SMDDP library is available in all of the AWS Regions where the [AWS Deep Learning Containers for SageMaker AI](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") and the [SMP Docker images](distributed-model-parallel-support-v2.md "distributed-model-parallel-support-v2.md") are in
service.

## Supported instance

types

The SMDDP library requires one of the following instance types.

| Instance type        |
| -------------------- |
| `ml.p3dn.24xlarge`\* |
| `ml.p4d.24xlarge`    |
| `ml.p4de.24xlarge`   |

###### Tip

To properly run distributed training on the EFA-enabled instance types, you should
enable traffic between the instances by setting up the security group of your VPC to allow
all inbound and outbound traffic to and from the security group itself. To learn how to set
up the security group rules, see [Step 1: Prepare an EFA-enabled security group](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security") in the _Amazon EC2 User Guide_.

###### Important

\* The SMDDP library has discontinued support for optimizing its collective communication
operations on P3 instances. While you can still utilize the SMDDP optimized
`AllReduce` collective on `ml.p3dn.24xlarge` instances, there will
be no further development support to enhance performance on this instance type. Note that
the SMDDP optimized `AllGather` collective is only available for P4
instances.

For specs of the instance types, see the **Accelerated
Computing** section in the [Amazon EC2
Instance Types page](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/"). For information about instance pricing, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

If you encountered an error message similar to the following, follow the instructions at
[Request a service quota increase for SageMaker AI resources](regions-quotas.md#service-limit-increase-request-procedure "regions-quotas.md#service-limit-increase-request-procedure").

```
ResourceLimitExceeded: An error occurred (ResourceLimitExceeded) when calling
the CreateTrainingJob operation: The account-level service limit 'ml.p3dn.24xlarge
for training job usage' is 0 Instances, with current utilization of 0 Instances
and a request delta of 1 Instances.
Please contact AWS support to request an increase for this limit.
```
