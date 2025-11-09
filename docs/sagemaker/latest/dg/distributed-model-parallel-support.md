# Supported Frameworks and

AWS Regions

Before using the SageMaker model parallelism library, check the supported frameworks and instance
types, and determine if there are enough quotas in your AWS account and
AWS Region.

###### Note

To check the latest updates and release notes of the library, see the [SageMaker Model Parallel Release Notes](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel_release_notes/smd_model_parallel_change_log.html "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel_release_notes/smd_model_parallel_change_log.html") in the _SageMaker Python SDK
documentation_.

## Supported Frameworks

The SageMaker model parallelism library supports the following deep learning frameworks and is
available in AWS Deep Learning Containers (DLC) or downloadable as a binary
file.

PyTorch versions supported by SageMaker AI and the SageMaker model parallelism library

| PyTorch version | SageMaker model parallelism library version | `smdistributed-modelparallel` integrated DLC image<br>URI                                                    | URL of the binary file\*\*                                                                                                                                                                |
| --------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v2.0.0          | `smdistributed-modelparallel==v1.15.0`      | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:2.0.0-gpu-py310-cu118-ubuntu20.04-sagemaker` | https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/pytorch-2.0.0/build-artifacts/2023-04-14-20-14/smdistributed\_modelparallel-1.15.0-cp310-cp310-linux\_x86\_64.whl |
| v1.13.1         | `smdistributed-modelparallel==v1.15.0`      | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.13.1-gpu-py39-cu117-ubuntu20.04-sagemaker` | https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/pytorch-1.13.1/build-artifacts/2023-04-17-15-49/smdistributed\_modelparallel-1.15.0-cp39-cp39-linux\_x86\_64.whl  |
| v1.12.1         | `smdistributed-modelparallel==v1.13.0`      | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.12.1-gpu-py38-cu113-ubuntu20.04-sagemaker` | https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/pytorch-1.12.1/build-artifacts/2022-12-08-21-34/smdistributed\_modelparallel-1.13.0-cp38-cp38-linux\_x86\_64.whl  |
| v1.12.0         | `smdistributed-modelparallel==v1.11.0`      | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.12.0-gpu-py38-cu113-ubuntu20.04-sagemaker` | https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/pytorch-1.12.0/build-artifacts/2022-08-12-16-58/smdistributed\_modelparallel-1.11.0-cp38-cp38-linux\_x86\_64.whl  |
| v1.11.0         | `smdistributed-modelparallel==v1.10.0`      | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.11.0-gpu-py38-cu113-ubuntu20.04-sagemaker` | https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/pytorch-1.11.0/build-artifacts/2022-07-11-19-23/smdistributed\_modelparallel-1.10.0-cp38-cp38-linux\_x86\_64.whl  |
| v1.10.2         | `smdistributed-modelparallel==v1.7.0`       | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.10.2-gpu-py38-cu113-ubuntu20.04-sagemaker` | -                                                                                                                                                                                         |
| v1.10.0         | `smdistributed-modelparallel==v1.5.0`       | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.10.0-gpu-py38-cu113-ubuntu20.04-sagemaker` | -                                                                                                                                                                                         |
| v1.9.1          | `smdistributed-modelparallel==v1.4.0`       | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.9.1-gpu-py38-cu111-ubuntu20.04`            | -                                                                                                                                                                                         |
| v1.8.1\*        | `smdistributed-modelparallel==v1.6.0`       | `763104351884.dkr.ecr.`<region>`.amazonaws.com/pytorch-training:1.8.1-gpu-py36-cu111-ubuntu18.04`            | -                                                                                                                                                                                         |

###### Note

The SageMaker model parallelism library v1.6.0 and later provides extended features for
PyTorch. For more information, see [Core Features of the SageMaker Model Parallelism
Library](model-parallel-core-features.md "model-parallel-core-features.md").

\*\* The URLs of the binary files are for installing the SageMaker model parallelism library in
custom containers. For more information, see [Create Your Own Docker
Container with the SageMaker Distributed Model Parallel Library](model-parallel-sm-sdk.md#model-parallel-bring-your-own-container "model-parallel-sm-sdk.md#model-parallel-bring-your-own-container").

TensorFlow versions supported by SageMaker AI and the SageMaker model parallelism library

| TensorFlow version | SageMaker model parallelism library version | `smdistributed-modelparallel` integrated DLC image<br>URI                                            |
| ------------------ | ------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| v2.6.0             | `smdistributed-modelparallel==v1.4.0`       | `763104351884.dkr.ecr.`<region>`.amazonaws.com/tensorflow-training:2.6.0-gpu-py38-cu112-ubuntu20.04` |
| v2.5.1             | `smdistributed-modelparallel==v1.4.0`       | `763104351884.dkr.ecr.`<region>`.amazonaws.com/tensorflow-training:2.5.1-gpu-py37-cu112-ubuntu18.04` |

**Hugging Face Transformers versions supported by SageMaker AI and the SageMaker
distributed data parallel library**

The AWS Deep Learning Containers for Hugging Face use the SageMaker Training Containers for
PyTorch and TensorFlow as their base images. To look up the Hugging Face Transformers library
versions and paired PyTorch and TensorFlow versions, see the latest [Hugging Face Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#huggingface-training-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#huggingface-training-containers") and the [Prior Hugging Face Container Versions](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#prior-hugging-face-container-versions "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#prior-hugging-face-container-versions").

## AWS Regions

The SageMaker data parallel library is available in all of the AWS Regions where the [AWS Deep Learning Containers for SageMaker](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") are in service. For more information,
see [Available Deep Learning Containers Images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#available-deep-learning-containers-images "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#available-deep-learning-containers-images").

## Supported Instance Types

The SageMaker model parallelism library requires one of the following ML instance types.

| Instance type      |
| ------------------ |
| `ml.g4dn.12xlarge` |
| `ml.p3.16xlarge`   |
| `ml.p3dn.24xlarge` |
| `ml.p4d.24xlarge`  |
| `ml.p4de.24xlarge` |

For specs of the instance types, see the **Accelerated
Computing** section in the [Amazon EC2 Instance Types page](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/"). For information about
instance pricing, see [Amazon SageMaker AI
Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

If you encountered an error message similar to the following, follow the instructions
at [Request a service quota increase for SageMaker AI resources](regions-quotas.md#service-limit-increase-request-procedure "regions-quotas.md#service-limit-increase-request-procedure").

```
ResourceLimitExceeded: An error occurred (ResourceLimitExceeded) when calling
    the CreateTrainingJob operation: The account-level service limit 'ml.p3dn.24xlarge
    for training job usage' is 0 Instances, with current utilization of 0 Instances
    and a request delta of 1 Instances.
    Please contact AWS support to request an increase for this limit.
```
