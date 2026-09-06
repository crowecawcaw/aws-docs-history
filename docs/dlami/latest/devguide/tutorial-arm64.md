

# The ARM64 DLAMI
<a name="tutorial-arm64"></a>

AWS ARM64 GPU DLAMIs are designed to provide high performance and cost efficiency for deep learning workloads. Specifically, the G5g instance type features the Arm64-based [AWS Graviton2 processor](https://aws.amazon.com/ec2/graviton/), which was built from the ground up by AWS and optimized for how customers run their workloads in the cloud. AWS ARM64 GPU DLAMIs are pre-configured with Docker, NVIDIA Docker, NVIDIA Driver, CUDA, CuDNN, NCCL, as well as popular machine learning frameworks such as TensorFlow and PyTorch.

With the G5g instance type, you can take advantage of the price and performance benefits of Graviton2 to deploy GPU-accelerated deep learning models at a significantly lower cost when compared with x86-based instances with GPU acceleration.

## Select a ARM64 DLAMI
<a name="tutorial-arm64-select-dlami"></a>

Launch a [G5g instance](https://aws.amazon.com/ec2/instance-types/g5g/) with the ARM64 DLAMI of your choice. 

For step-by-step instructions on launching a DLAMI, see [Launching and Configuring a DLAMI.](https://docs.aws.amazon.com/dlami/latest/devguide/launch-config.html) 

For a list of the most recent ARM64 DLAMIs, see the [Release Notes for DLAMI](https://docs.aws.amazon.com/dlami/latest/devguide/appendix-ami-release-notes.html).

## Get Started
<a name="tutorial-arm64-get-started"></a>

The following topics show you how to get started using the ARM64 DLAMI. 

**Topics**
+ [Select a ARM64 DLAMI](#tutorial-arm64-select-dlami)
+ [Get Started](#tutorial-arm64-get-started)
+ [Using the ARM64 GPU PyTorch DLAMI](tutorial-arm64-pytorch.md)