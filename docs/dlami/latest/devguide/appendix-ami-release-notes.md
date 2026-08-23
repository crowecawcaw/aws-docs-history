# Deep Learning AMIs Release Notes

Here you can find detailed release notes for all currently supported AWS Deep Learning AMIs (DLAMI)
options.

For release notes for DLAMI frameworks that we no longer support, see the **Unsupported Framework Release Notes Archive** section of the [DLAMI Framework Support
Policy](dlami-support-policy-table.md "dlami-support-policy-table.md") page.

###### Security patches not available for PyTorch 2.9 DLAMIs

PyTorch DLAMIs for versions earlier than 2.10 (that is, PyTorch 2.9)
contain known common vulnerabilities and exposures (CVEs) that cannot be patched.
Because we maintain a separate DLAMI currency release for each PyTorch version, we
do not backport security fixes to these images.

We recommend that you migrate to PyTorch 2.10 or later DLAMIs, which
continue to receive security patches.

###### Release Notes

- [Release Notes for Base DLAMIs](#appendix-ami-release-notes-base "#appendix-ami-release-notes-base")
- [Release Notes for Single Framework DLAMIs](#appendix-ami-release-notes-single "#appendix-ami-release-notes-single")
- [Release Notes for Multi-Framework DLAMIs](#appendix-ami-release-notes-multi "#appendix-ami-release-notes-multi")

## Release Notes for Base DLAMIs

### X86 Base DLAMI Release Notes

Below are the release notes for X86 Base DLAMI:

######

GPU

- [Base AMI with Single CUDA (Amazon Linux 2023)](aws-deep-learning-x86-base-with-single-cuda-ami-amazon-linux-2023.md "aws-deep-learning-x86-base-with-single-cuda-ami-amazon-linux-2023.md")
- [Base AMI with Single CUDA (Ubuntu 24.04)](aws-deep-learning-x86-base-with-single-cuda-ami-ubuntu-24-04.md "aws-deep-learning-x86-base-with-single-cuda-ami-ubuntu-24-04.md")
- [Base AMI with Single CUDA (Ubuntu 22.04)](aws-deep-learning-x86-base-with-single-cuda-ami-ubuntu-22-04.md "aws-deep-learning-x86-base-with-single-cuda-ami-ubuntu-22-04.md")
- [Base GPU AMI (Amazon Linux 2023)](aws-deep-learning-x86-base-gpu-ami-amazon-linux-2023.md "aws-deep-learning-x86-base-gpu-ami-amazon-linux-2023.md")
- [Base GPU AMI (Ubuntu 26.04)](aws-deep-learning-x86-base-gpu-ami-ubuntu-26-04.md "aws-deep-learning-x86-base-gpu-ami-ubuntu-26-04.md")
- [Base GPU AMI (Ubuntu 24.04)](aws-deep-learning-x86-base-gpu-ami-ubuntu-24-04.md "aws-deep-learning-x86-base-gpu-ami-ubuntu-24-04.md")
- [Base GPU AMI (Ubuntu 22.04)](aws-deep-learning-x86-base-gpu-ami-ubuntu-22-04.md "aws-deep-learning-x86-base-gpu-ami-ubuntu-22-04.md")

### ARM64 Base DLAMI Release Notes

Below are the release notes for ARM64 Base DLAMI:

######

GPU

- [ARM64 Base AMI with Single CUDA (Amazon Linux 2023)](aws-deep-learning-arm64-base-with-single-cuda-ami-amazon-linux-2023.md "aws-deep-learning-arm64-base-with-single-cuda-ami-amazon-linux-2023.md")
- [ARM64 Base AMI with Single CUDA (Ubuntu 24.04)](aws-deep-learning-arm64-base-with-single-cuda-ami-ubuntu-24-04.md "aws-deep-learning-arm64-base-with-single-cuda-ami-ubuntu-24-04.md")
- [ARM64 Base AMI with Single CUDA (Ubuntu 22.04)](aws-deep-learning-arm64-base-with-single-cuda-ami-ubuntu-22-04.md "aws-deep-learning-arm64-base-with-single-cuda-ami-ubuntu-22-04.md")
- [ARM64 Base GPU AMI (Amazon Linux 2023)](aws-deep-learning-arm64-base-gpu-ami-amazon-linux-2023.md "aws-deep-learning-arm64-base-gpu-ami-amazon-linux-2023.md")
- [ARM64 Base GPU AMI (Ubuntu 26.04)](aws-deep-learning-arm64-base-gpu-ami-ubuntu-26-04.md "aws-deep-learning-arm64-base-gpu-ami-ubuntu-26-04.md")
- [ARM64 Base GPU AMI (Ubuntu 24.04)](aws-deep-learning-arm64-base-gpu-ami-ubuntu-24-04.md "aws-deep-learning-arm64-base-gpu-ami-ubuntu-24-04.md")
- [ARM64 Base GPU AMI (Ubuntu 22.04)](aws-deep-learning-arm64-base-gpu-ami-ubuntu-22-04.md "aws-deep-learning-arm64-base-gpu-ami-ubuntu-22-04.md")

**AWS Neuron**

- Refer to the [Neuron DLAMI User Guide](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/deploy/environments/dlami.html#neuron-base-dlami "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/deploy/environments/dlami.html#neuron-base-dlami").

## Release Notes for Single Framework DLAMIs

### PyTorch DLAMIs

#### X86 PyTorch DLAMI Release Notes

Below are the Release notes for X86 PyTorch DLAMIs:

######

GPU

- [GPU PyTorch 2.13 (Amazon Linux 2023)](aws-deep-learning-x86-gpu-pytorch-2.13-amazon-linux-2023.md "aws-deep-learning-x86-gpu-pytorch-2.13-amazon-linux-2023.md")
- [GPU PyTorch 2.13 (Ubuntu 26.04)](aws-deep-learning-x86-gpu-pytorch-2.13-ubuntu-26-04.md "aws-deep-learning-x86-gpu-pytorch-2.13-ubuntu-26-04.md")
- [GPU PyTorch 2.12 (Amazon Linux 2023)](aws-deep-learning-x86-gpu-pytorch-2.12-amazon-linux-2023.md "aws-deep-learning-x86-gpu-pytorch-2.12-amazon-linux-2023.md")
- [GPU PyTorch 2.12 (Ubuntu 24.04)](aws-deep-learning-x86-gpu-pytorch-2.12-ubuntu-24-04.md "aws-deep-learning-x86-gpu-pytorch-2.12-ubuntu-24-04.md")
- [GPU PyTorch 2.11 (Amazon Linux 2023)](aws-deep-learning-x86-gpu-pytorch-2.11-amazon-linux-2023.md "aws-deep-learning-x86-gpu-pytorch-2.11-amazon-linux-2023.md")
- [GPU PyTorch 2.11 (Ubuntu 24.04)](aws-deep-learning-x86-gpu-pytorch-2.11-ubuntu-24-04.md "aws-deep-learning-x86-gpu-pytorch-2.11-ubuntu-24-04.md")
- [GPU PyTorch 2.10 (Amazon Linux 2023)](aws-deep-learning-x86-gpu-pytorch-2.10-amazon-linux-2023.md "aws-deep-learning-x86-gpu-pytorch-2.10-amazon-linux-2023.md")
- [GPU PyTorch 2.10 (Ubuntu 24.04)](aws-deep-learning-x86-gpu-pytorch-2.10-ubuntu-24-04.md "aws-deep-learning-x86-gpu-pytorch-2.10-ubuntu-24-04.md")
- [GPU PyTorch 2.9 (Amazon Linux 2023)](aws-deep-learning-x86-gpu-pytorch-2.9-amazon-linux-2023.md "aws-deep-learning-x86-gpu-pytorch-2.9-amazon-linux-2023.md")
- [GPU PyTorch 2.9 (Ubuntu 24.04)](aws-deep-learning-x86-gpu-pytorch-2.9-ubuntu-24-04.md "aws-deep-learning-x86-gpu-pytorch-2.9-ubuntu-24-04.md")

######

AWS Neuron

- Refer to the [Neuron DLAMI User Guide](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/deploy/environments/dlami.html#neuron-multi-framework-dlami "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/deploy/environments/dlami.html#neuron-multi-framework-dlami")

#### ARM64 PyTorch DLAMI Release Notes

Below are the Release notes for ARM64 PyTorch DLAMIs:

######

GPU

- [ARM64 AMI GPU PyTorch 2.12 (Amazon Linux 2023)](aws-deep-learning-arm64-gpu-pytorch-2.12-amazon-linux-2023.md "aws-deep-learning-arm64-gpu-pytorch-2.12-amazon-linux-2023.md")
- [ARM64 AMI GPU PyTorch 2.12 (Ubuntu 24.04)](aws-deep-learning-arm64-gpu-pytorch-2.12-ubuntu-24-04.md "aws-deep-learning-arm64-gpu-pytorch-2.12-ubuntu-24-04.md")
- [ARM64 AMI GPU PyTorch 2.11 (Amazon Linux 2023)](aws-deep-learning-arm64-gpu-pytorch-2.11-amazon-linux-2023.md "aws-deep-learning-arm64-gpu-pytorch-2.11-amazon-linux-2023.md")
- [ARM64 AMI GPU PyTorch 2.11 (Ubuntu 24.04)](aws-deep-learning-arm64-gpu-pytorch-2.11-ubuntu-24-04.md "aws-deep-learning-arm64-gpu-pytorch-2.11-ubuntu-24-04.md")
- [ARM64 AMI GPU PyTorch 2.10 (Amazon Linux 2023)](aws-deep-learning-arm64-gpu-pytorch-2.10-amazon-linux-2023.md "aws-deep-learning-arm64-gpu-pytorch-2.10-amazon-linux-2023.md")
- [ARM64 AMI GPU PyTorch 2.10 (Ubuntu 24.04)](aws-deep-learning-arm64-gpu-pytorch-2.10-ubuntu-24-04.md "aws-deep-learning-arm64-gpu-pytorch-2.10-ubuntu-24-04.md")
- [ARM64 AMI GPU PyTorch 2.9 (Amazon Linux 2023)](aws-deep-learning-arm64-gpu-pytorch-2.9-amazon-linux-2023.md "aws-deep-learning-arm64-gpu-pytorch-2.9-amazon-linux-2023.md")
- [ARM64 AMI GPU PyTorch 2.9 (Ubuntu 24.04)](aws-deep-learning-arm64-gpu-pytorch-2.9-ubuntu-24-04.md "aws-deep-learning-arm64-gpu-pytorch-2.9-ubuntu-24-04.md")

**AWS Neuron**

- Refer to the [Neuron DLAMI User Guide](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/deploy/environments/dlami.html#neuron-multi-framework-dlami "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/deploy/environments/dlami.html#neuron-multi-framework-dlami")

## Release Notes for Multi-Framework DLAMIs

###### Tip

If you use only one machine learning framework, then we recommend a [single-framework DLAMI](#appendix-ami-release-notes-single "#appendix-ami-release-notes-single").

### Multi-Framework DLAMI Release Notes

Below are the release notes for Multi-Framework X86 DLAMI:

**AWS Neuron**

- Refer to the [Neuron DLAMI User Guide](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/deploy/environments/dlami.html#neuron-multi-framework-dlami "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/deploy/environments/dlami.html#neuron-multi-framework-dlami")
