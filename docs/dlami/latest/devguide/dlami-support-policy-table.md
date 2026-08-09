# DLAMI Support Policy Table

For more details see the [Support
Policy](support-policy.md "support-policy.md").

###### Security patches not available for PyTorch 2.8 and 2.9 DLAMIs

PyTorch DLAMIs for versions earlier than 2.10 (that is, PyTorch 2.8 and 2.9)
contain known common vulnerabilities and exposures (CVEs) that cannot be patched.
Because we maintain a separate DLAMI currency release for each PyTorch version, we
do not backport security fixes to these images.

We recommend that you migrate to PyTorch 2.10 or later DLAMIs, which
continue to receive security patches.

## Supported Framework Versions

| Framework | Current version | CUDA version | GitHub GA  | End of patch |
| --------- | --------------- | ------------ | ---------- | ------------ |
| PyTorch   | 2.12.0          | 13.0         | 2026-05-13 | 2027-05-13   |
| PyTorch   | 2.11.0          | 13.0         | 2026-03-23 | 2027-03-23   |
| PyTorch   | 2.10.0          | 13.0         | 2026-01-21 | 2027-01-21   |
| PyTorch   | 2.9.0           | 13.0         | 2025-10-15 | 2026-10-15   |
| PyTorch   | 2.8.0           | 12.9         | 2025-08-06 | 2026-08-06   |

## Supported Operating System Versions

| Operating System  | End of patch |
| ----------------- | ------------ |
| Amazon Linux 2023 | 2029-06-30   |
| Ubuntu 26.04      | 2031-04-30   |
| Ubuntu 24.04      | 2029-04-30   |
| Ubuntu 22.04      | 2027-04-30   |

## Unsupported Framework Versions

Versions listed in this table will appear for 2 years past their support date.

| Framework  | Current version | CUDA version | GitHub GA  | End of patch |
| ---------- | --------------- | ------------ | ---------- | ------------ |
| PyTorch    | 2.7.0           | 12.8         | 2025-04-23 | 2026-04-23   |
| PyTorch    | 2.6.0           | 12.6         | 2025-01-29 | 2026-01-29   |
| PyTorch    | 2.5.1           | 12.4         | 2024-11-24 | 2025-11-24   |
| PyTorch    | 2.4.1           | 12.4         | 2024-07-24 | 2025-07-24   |
| PyTorch    | 2.3.0           | 12.1         | 2024-04-24 | 2025-04-24   |
| PyTorch    | 2.2.0           | 12.1         | 2024-01-30 | 2025-01-30   |
| PyTorch    | 1.13.1          | 11.7         | 2022-10-28 | 2024-10-28   |
| PyTorch    | 2.1.0           | 12.1         | 2023-10-04 | 2024-10-04   |
| PyTorch    | 2.0.0           | 12.1         | 2023-03-15 | 2024-03-15   |
| PyTorch    | 1.12.1          | 11.6         | 2022-07-01 | 2023-07-01   |
| PyTorch    | 1.11.0          | 11.5         | 2022-03-10 | 2023-03-10   |
| TensorFlow | 2.18.0          | 12.5         | 2024-10-24 | 2026-01-31   |
| TensorFlow | 2.17.0          | 12.3         | 2024-11-07 | 2025-11-07   |
| TensorFlow | 2.16.0          | 12.3         | 2024-03-07 | 2025-03-07   |
| TensorFlow | 2.15.0          | 12.2         | 2023-11-14 | 2024-11-14   |
| TensorFlow | 2.13.0          | 11.8         | 2023-07-19 | 2024-07-19   |
| TensorFlow | 2.12.0          | 11.8         | 2023-03-23 | 2024-03-23   |
| TensorFlow | 2.11.0          | 11.2         | 2022-11-18 | 2023-11-18   |
| TensorFlow | 2.10.1          | 11.2         | 2022-09-06 | 2023-09-06   |
| TensorFlow | 2.9.3           | 11.2         | 2022-05-17 | 2023-05-17   |

## Unsupported Operating System Versions

| Operating System | End of patch |
| ---------------- | ------------ |
| Amazon Linux 2   | 2026-06-30   |
| Ubuntu 20.04     | 2025-05-31   |
| Ubuntu 18.04     | 2023-05-31   |

## Release Notes Archive

Release notes for DLAMI versions that are no longer supported. These archives provide
historical information for reference purposes.

### Base DLAMIs

###### Release Notes

- [Base GPU AMI (Ubuntu 20.04)](aws-deep-learning-base-gpu-ami-ubuntu-20.04.md "aws-deep-learning-base-gpu-ami-ubuntu-20.04.md")
- [Base Proprietary Nvidia GPU AMI (Amazon Linux 2)](aws-deep-learning-x86-base-gpu-ami-amazon-linux-2-prop.md "aws-deep-learning-x86-base-gpu-ami-amazon-linux-2-prop.md")
- [Base GPU AMI (Amazon Linux 2)](aws-deep-learning-x86-base-gpu-ami-amazon-linux-2.md "aws-deep-learning-x86-base-gpu-ami-amazon-linux-2.md")
- [ARM64 Base GPU AMI (Amazon Linux 2)](aws-deep-learning-arm64-base-gpu-ami-amazon-linux-2.md "aws-deep-learning-arm64-base-gpu-ami-amazon-linux-2.md")

### Multi-Framework DLAMIs (Amazon Linux 2)

###### Release Notes

- [Multi Framework DLAMI (Amazon Linux 2)](aws-deep-learning-multiframework-ami-amazon-linux-2-prop.md "aws-deep-learning-multiframework-ami-amazon-linux-2-prop.md")
- [Multi Framework DLAMI (Amazon Linux 2)](aws-deep-learning-multiframework-ami-amazon-linux-2.md "aws-deep-learning-multiframework-ami-amazon-linux-2.md")

### Qualcomm DLAMIs (Amazon Linux 2)

###### Release Notes

- [Base Qualcomm AMI (Amazon Linux 2)](aws-deep-learning-x86-base-qualcomm-ami-amazon-linux-2.md "aws-deep-learning-x86-base-qualcomm-ami-amazon-linux-2.md")

### PyTorch DLAMIs

###### Release Notes

- [GPU PyTorch 2.7 (Ubuntu 22.04)](aws-deep-learning-x86-gpu-pytorch-2.7-ubuntu-22-04.md "aws-deep-learning-x86-gpu-pytorch-2.7-ubuntu-22-04.md")
- [GPU PyTorch 2.7 (Amazon Linux 2023)](aws-deep-learning-x86-gpu-pytorch-2.7-amazon-linux-2023.md "aws-deep-learning-x86-gpu-pytorch-2.7-amazon-linux-2023.md")
- [ARM64 AMI GPU PyTorch 2.7 (Ubuntu 22.04)](aws-deep-learning-arm64-gpu-pytorch-2.7-ubuntu-22-04.md "aws-deep-learning-arm64-gpu-pytorch-2.7-ubuntu-22-04.md")
- [ARM64 AMI GPU PyTorch 2.7 (Amazon Linux 2023)](aws-deep-learning-arm64-gpu-pytorch-2.7-amazon-linux-2023.md "aws-deep-learning-arm64-gpu-pytorch-2.7-amazon-linux-2023.md")
- [GPU PyTorch 2.6 (Ubuntu 22.04)](aws-deep-learning-x86-gpu-pytorch-2.6-ubuntu-22-04.md "aws-deep-learning-x86-gpu-pytorch-2.6-ubuntu-22-04.md")
- [GPU PyTorch 2.6 (Amazon Linux 2023)](aws-deep-learning-x86-gpu-pytorch-2.6-amazon-linux-2023.md "aws-deep-learning-x86-gpu-pytorch-2.6-amazon-linux-2023.md")
- [ARM64 AMI GPU PyTorch 2.6 (Ubuntu 22.04)](aws-deep-learning-arm64-gpu-pytorch-2.6-ubuntu-22-04.md "aws-deep-learning-arm64-gpu-pytorch-2.6-ubuntu-22-04.md")
- [ARM64 AMI GPU PyTorch 2.6 (Amazon Linux 2023)](aws-deep-learning-arm64-gpu-pytorch-2.6-amazon-linux-2023.md "aws-deep-learning-arm64-gpu-pytorch-2.6-amazon-linux-2023.md")
- [GPU PyTorch 2.5 (Ubuntu 22.04)](aws-deep-learning-x86-gpu-pytorch-2.5-ubuntu-22-04.md "aws-deep-learning-x86-gpu-pytorch-2.5-ubuntu-22-04.md")
- [GPU PyTorch 2.5 (Amazon Linux 2023)](aws-deep-learning-x86-gpu-pytorch-2.5-amazon-linux-2023.md "aws-deep-learning-x86-gpu-pytorch-2.5-amazon-linux-2023.md")
- [ARM64 AMI GPU PyTorch 2.5 (Ubuntu 22.04)](aws-deep-learning-arm64-gpu-pytorch-2.5-ubuntu-22-04.md "aws-deep-learning-arm64-gpu-pytorch-2.5-ubuntu-22-04.md")
- [GPU PyTorch 2.4 (Ubuntu 22.04)](aws-deep-learning-ami-gpu-pytorch-2.4-ubuntu-22-04.md "aws-deep-learning-ami-gpu-pytorch-2.4-ubuntu-22-04.md")
- [ARM64 AMI GPU PyTorch 2.4 (Ubuntu 22.04)](aws-deep-learning-arm64-ami-gpu-pytorch-2.4-ubuntu-22-04.md "aws-deep-learning-arm64-ami-gpu-pytorch-2.4-ubuntu-22-04.md")

### TensorFlow DLAMIs

###### Release Notes

- [GPU TensorFlow 2.18 (Amazon Linux 2023)](aws-deep-learning-x86-gpu-tensorflow-2.18-amazon-linux-2023.md "aws-deep-learning-x86-gpu-tensorflow-2.18-amazon-linux-2023.md")
- [GPU TensorFlow 2.18 (Ubuntu 22.04)](aws-deep-learning-x86-gpu-tensorflow-2.18-ubuntu-22-04.md "aws-deep-learning-x86-gpu-tensorflow-2.18-ubuntu-22-04.md")
- [GPU TensorFlow 2.17 (Ubuntu 22.04)](aws-deep-learning-x86-gpu-tensorflow-2.17-ubuntu-22-04.md "aws-deep-learning-x86-gpu-tensorflow-2.17-ubuntu-22-04.md")
- [GPU TensorFlow 2.16 (Amazon Linux 2)](aws-deep-learning-ami-gpu-tensorflow-2.16-amazon-linux-2.md "aws-deep-learning-ami-gpu-tensorflow-2.16-amazon-linux-2.md")
- [GPU TensorFlow 2.16 (Ubuntu 20.04)](aws-deep-learning-ami-gpu-tensorflow-2.16-ubuntu-20-04.md "aws-deep-learning-ami-gpu-tensorflow-2.16-ubuntu-20-04.md")
