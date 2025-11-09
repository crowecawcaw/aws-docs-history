# Supported frameworks and AWS

Regions

Before using SageMaker smart sifting data loader, check if your framework of choice is supported,
that the instance types are available in your AWS account, and that your AWS account
is in one of the supported AWS Regions.

###### Note

SageMaker smart sifting supports PyTorch model training with traditional data parallelism and
distributed data parallelism, which makes model replicas in all GPU workers and uses
the `AllReduce` operation. It doesn’t work with model parallelism
techniques, including sharded data parallelism. Because SageMaker smart sifting works for data
parallelism jobs, make sure that the model you train fits in each GPU memory.

## Supported

Frameworks

SageMaker smart sifting supports the following deep learning frameworks and is available
through AWS Deep Learning Containers.

###### Topics

- [PyTorch](#train-smart-sifting-supported-frameworks-pytorch "#train-smart-sifting-supported-frameworks-pytorch")

### PyTorch

| Framework | Framework version | Deep Learning Container URI                                                                                |
| --------- | ----------------- | ---------------------------------------------------------------------------------------------------------- |
| PyTorch   | 2.1.0             | `763104351884`.dkr.ecr.`region`.amazonaws.com/pytorch-training:2.1.0-gpu-py310-cu121-ubuntu20.04-sagemaker |

For more information about the pre-built containers, see [SageMaker AI Framework Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md") in the _AWS Deep
Learning Containers GitHub repository_.

## AWS Regions

The [containers packaged with the SageMaker smart sifting library](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-training-compiler-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-training-compiler-containers") are available in the
AWS Regions where [AWS Deep Learning Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md") are in service.

## Instance types

You can use SageMaker smart sifting for any PyTorch training jobs on any instance types. We
recommend that you use P4d, P4de, or P5 instances.
