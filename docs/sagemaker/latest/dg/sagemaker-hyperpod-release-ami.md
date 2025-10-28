# Amazon SageMaker HyperPod AMI

Amazon SageMaker HyperPod Amazon Machine Images (AMIs) are specialized machine images for
distributed machine learning workloads and high-performance computing. These AMIs enhance
base images with essential components including GPU drivers and AWS Neuron accelerator
support.

Key components added to HyperPod AMIs include:

- [Public AMIs](sagemaker-hyperpod-release-public-ami.md "sagemaker-hyperpod-release-public-ami.md") with
  support for [building custom
  AMIs](hyperpod-custom-ami-support.md "hyperpod-custom-ami-support.md")
- Advanced orchestration tools:
  - [Orchestrating SageMaker HyperPod clusters with
    Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md")
  - [Orchestrating SageMaker HyperPod clusters with
    Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md")

- Cluster management dependencies
- Built-in resiliency features:
  - cluster health check
  - auto-resume capabilities

- Support for HyperPod cluster management and configuration
  These enhancements are built upon the following base Deep Learning AMIs (DLAMIs):

- [AWS Deep
  Learning Base GPU AMI (Ubuntu 20.04)](https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-20-04/ "https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-20-04/") for orchestration with
  Slurm.
- Amazon Linux 2 or Amazon Linux 2023 based AMI for orchestration with Amazon EKS.
  Choose your HyperPod AMIs based on your orchestration preference:

- For Slurm orchestration, see [SageMaker HyperPod AMI releases for
  Slurm](sagemaker-hyperpod-release-ami-slurm.md "sagemaker-hyperpod-release-ami-slurm.md").
- For Amazon EKS orchestration, see [SageMaker HyperPod AMI releases for
  Amazon EKS](sagemaker-hyperpod-release-ami-eks.md "sagemaker-hyperpod-release-ami-eks.md").
  For information about Amazon SageMaker HyperPod feature releases, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md "sagemaker-hyperpod-release-notes.md").
