# SageMaker HyperPod AMI releases for

Amazon EKS

The following release notes track the latest updates for Amazon SageMaker HyperPod AMI releases
for Amazon EKS orchestration. Each release note includes a summarized list of packages
pre-installed or pre-configured in the SageMaker HyperPod DLAMIs for Amazon EKS support. Each DLAMI
is built on AL2023 and supports a specific Kubernetes version. For
HyperPod DLAMI releases for Slurm orchestration, see [SageMaker HyperPod AMI releases for
Slurm](sagemaker-hyperpod-release-ami-slurm.md "sagemaker-hyperpod-release-ami-slurm.md"). For information about
Amazon SageMaker HyperPod feature releases, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md "sagemaker-hyperpod-release-notes.md").

## SageMaker HyperPod AMI

releases for Amazon EKS: November 07, 2025

**AMI general updates**

- Released updates for SageMaker HyperPod AMI for Amazon EKS versions 1.28, 1.29, 1.30,
  1.31, 1.32, and 1.33.
- Base DLAMI release note is available [here](../../../dlami/latest/devguide/appendix-ami-release-notes.md#appendix-ami-release-notes-base "../../../dlami/latest/devguide/appendix-ami-release-notes.md#appendix-ami-release-notes-base").

**SageMaker HyperPod DLAMI for Amazon EKS support**

This release includes the following updates:

Kubernetes v1.28

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.28.15

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.28.15

- Package updates include boto3, botocore, pip, regex, psutil, and nvidia container toolkit components.
- Added package: annotated-doc 0.0.3

Kubernetes v1.29

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.29.15

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.29.15

- Package updates include kernel updates, glibc updates, and various system libraries.
- Added package: annotated-doc 0.0.3

Kubernetes v1.30

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.30.11

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.30.11

- Package updates include kernel livepatch updates and system library updates.
- Added package: annotated-doc 0.0.3

Kubernetes v1.31

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.31.7

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.31.13

- AL2023 (arm):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.31.13
  - Kernel version: 6.12.46-66.121.amzn2023.aarch64

- Package updates include extensive system library updates, kernel updates, and boost library updates.
- Added packages: apr-util-lmdb, kernel-livepatch-6.1.156-177.286

Kubernetes v1.32

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.32.3
  - AWS IAM Authenticator version: v0.6.29

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.32.9

- AL2023 (arm):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.32.9
  - Kernel version: 6.12.46-66.121.amzn2023.aarch64

- Package updates include kernel livepatch updates and system library updates.
- Added package: annotated-doc 0.0.3

Kubernetes v1.33

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.33.5
  - Kernel version: 6.1.155-176.282.amzn2023.x86_64

- AL2023 (arm):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.33.5
  - Kernel version: 6.12.46-66.121.amzn2023.aarch64

- Package updates include extensive system library updates, kernel updates, and boost library updates.
- Added packages: apr-util-lmdb, kernel-livepatch updates

###### Note

runc version has been upgraded to 1.3.2 [Security bulletin](https://aws.amazon.com/security/security-bulletins/rss/aws-2025-024/ "https://aws.amazon.com/security/security-bulletins/rss/aws-2025-024/")

## SageMaker HyperPod AMI

releases for Amazon EKS: October 29, 2025

**AMI general updates**

- Released updates for SageMaker HyperPod AMI for Amazon EKS versions 1.28, 1.29, 1.30,
  1.31, 1.32, and 1.33.
- Base DLAMI release note is available [here](../../../dlami/latest/devguide/aws-deep-learning-ami-baseoss-aml2-2025-10-14.md "../../../dlami/latest/devguide/aws-deep-learning-ami-baseoss-aml2-2025-10-14.md").

**SageMaker HyperPod DLAMI for Amazon EKS support**

This release includes the following updates:

Kubernetes v1.28

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.28.15

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.28.15

- Package updates include boto3, botocore, pip, regex, psutil, and nvidia container toolkit components.
- Added package: annotated-doc 0.0.3

Kubernetes v1.29

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.29.15

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.29.15

- Package updates include kernel updates, glibc updates, and various system libraries.
- Added package: annotated-doc 0.0.3

Kubernetes v1.30

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.30.11

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.30.11

- Package updates include kernel livepatch updates and system library updates.
- Added package: annotated-doc 0.0.3

Kubernetes v1.31

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.31.7

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.31.13

- AL2023 (arm):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.31.13
  - Kernel version: 6.12.46-66.121.amzn2023.aarch64

- Package updates include extensive system library updates, kernel updates, and boost library updates.
- Added packages: apr-util-lmdb, kernel-livepatch-6.1.156-177.286

Kubernetes v1.32

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- AL2 (x86_64):
  - NVIDIA driver version: 570.195.03
  - CUDA version: 12.8
  - Kubernetes version: 1.32.3

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.32.9

- AL2023 (arm):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.32.9
  - Kernel version: 6.12.46-66.121.amzn2023.aarch64

- Package updates include kernel livepatch updates and system library updates.
- Added package: annotated-doc 0.0.3

Kubernetes v1.33

- AL2023 (x86_64):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.33.5
  - Kernel version: 6.1.155-176.282.amzn2023.x86_64

- AL2023 (arm):
  - NVIDIA driver version: 580.95.05
  - CUDA version: 13.0
  - Kubernetes version: 1.33.5
  - Kernel version: 6.12.46-66.121.amzn2023.aarch64

- Package updates include extensive system library updates, kernel updates, and boost library updates.
- Added packages: apr-util-lmdb, kernel-livepatch updates

## SageMaker HyperPod AMI

releases for Amazon EKS: October 22, 2025

**AL2x86**

###### Note

Amazon Linux 2 is now deprecated. The Kubernetes AMI is based on AL2023.

Base DLAMI release note is available [here](../../../dlami/latest/devguide/aws-deep-learning-ami-baseoss-aml2-2025-10-14.md "../../../dlami/latest/devguide/aws-deep-learning-ami-baseoss-aml2-2025-10-14.md").

- EKS versions 1.28 - 1.32
- This release contains CVE patches for affected NVIDIA Driver packages
  found in the [Nvidia
  October Security Bulletin](https://nvidia.custhelp.com/app/answers/detail/a_id/5703 "https://nvidia.custhelp.com/app/answers/detail/a_id/5703").
- NVIDIA SMI

```
NVIDIA-SMI 570.195.03
Driver Version: 570.195.03
CUDA Version: 12.8
```

- Major versions

| package name                     | version                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| framework_version                | 70                                                                                  |
| gdr_copy                         | 2.4.1                                                                               |
| supported_ec2_instances          | G4dn, G5, G6, Gr6, G6e, P4d, P4de, P5, P5e, P5en                                    |
| efa_version                      | 1.43.3                                                                              |
| ebs_volume_type                  | gp3                                                                                 |
| nvidia_driver                    | 570.195.03                                                                          |
| python_location                  | /usr/bin/python3.10                                                                 |
| nvidia_cuda_stack                | /usr/local/cuda-12.1,/usr/local/cuda-12.2,/usr/local/cuda-12.3,/usr/local/cuda-12.4 |
| ssm_agent_version                | 3.3.3050.0                                                                          |
| kernel_version                   | 5.10.244-240.965.amzn2.x86_64                                                       |
| nvidia_container_toolkit_version | 1.17.8                                                                              |
| ofi_nccl_version                 | 1.16.3                                                                              |
| operating_system                 | Amazon Linux 2                                                                      |
| default_cuda                     | /usr/local/cuda-12.1/                                                               |
| compute_architecture             | x86_64                                                                              |

- Added packages: No packages were added in this release.
- Updated packages

| package name          | previous version | new version    |
| --------------------- | ---------------- | -------------- |
| boto3                 | 1.40.46          | 1.40.49        |
| botocore              | 1.40.46          | 1.40.49        |
| fastapi               | 0.118.0          | 0.118.2        |
| filelock              | 3.19.1           | 3.20.0         |
| importlib_metadata    | 8.7.0            | 8.0.0          |
| jaraco.context        | 6.0.1            | 5.3.0          |
| jaraco.functools      | 4.3.0            | 4.0.1          |
| matplotlib            | 3.10.6           | 3.10.7         |
| packaging             | 25               | 24.2           |
| platformdirs          | 4.4.0            | 4.5.0          |
| propcache             | 0.4.0            | 0.4.1          |
| rich                  | 14.1.0           | 14.2.0         |
| tomli                 | 2.2.1            | 2.3.0          |
| types-python-dateutil | 2.9.0.20250822   | 2.9.0.20251008 |
| virtualenv            | 20.34.0          | 20.35.1        |
| websocket-client      | 1.8.0            | 1.9.0          |

- Removed packages: No packages were removed in this release.

**AL2023x86**

Base DLAMI release note is available [here](../../../dlami/latest/devguide/aws-deep-learning-ami-gpubaseoss-al2023-2025-10-14.md "../../../dlami/latest/devguide/aws-deep-learning-ami-gpubaseoss-al2023-2025-10-14.md").

- EKS versions 1.28 - 1.32. No release for EKS version 1.33.
- This release contains CVE patches for affected NVIDIA Driver packages
  found in the [Nvidia
  October Security Bulletin](https://nvidia.custhelp.com/app/answers/detail/a_id/5703 "https://nvidia.custhelp.com/app/answers/detail/a_id/5703").
- NVIDIA SMI

```
NVIDIA-SMI 580.95.05
Driver Version: 580.95.05
CUDA Version: 13.0
```

- Major versions

| package name                     | version                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| gdr_copy                         | 2.5.1                                                                               |
| supported_ec2_instances          | G4dn, G5, G6, Gr6, G6e, P4d, P4de, P5, P5e, P5en, P6-B200                           |
| efa_version                      | 1.43.3                                                                              |
| ebs_volume_type                  | gp3                                                                                 |
| nvidia_gds_version               | 1.15.0.42                                                                           |
| nvidia_driver                    | 580.95.05                                                                           |
| python_location                  | /usr/bin/python3.9                                                                  |
| nvidia_cuda_stack                | /usr/local/cuda-12.6,/usr/local/cuda-12.8,/usr/local/cuda-12.9,/usr/local/cuda-13.0 |
| ssm_agent_version                | 3.3.3050.0                                                                          |
| kernel_version                   | 6.1.153-175.280.amzn2023.x86_64                                                     |
| nvidia_container_toolkit_version | 1.17.8                                                                              |
| dcgm_version                     | 4.4.1                                                                               |
| ofi_nccl_version                 | 1.16.3                                                                              |
| operating_system                 | Amazon Linux 2023.9.20250929                                                        |
| default_cuda                     | /usr/local/cuda-12.9/                                                               |
| compute_architecture             | x86_64                                                                              |

- Added packages: No packages were added in this release.
- Updated packages

| package name          | previous version | new version    |
| --------------------- | ---------------- | -------------- |
| boto3                 | 1.40.46          | 1.40.49        |
| botocore              | 1.40.46          | 1.40.49        |
| fastapi               | 0.118.0          | 0.118.2        |
| gdrcopy               | 2.5-1            | 2.5.1-1        |
| gdrcopy-devel         | 2.5-1            | 2.5.1-1        |
| gdrcopy-kmod          | 2.5-1dkms        | 2.5.1-1dkms    |
| jaraco.context        | 6.0.1            | 5.3.0          |
| jaraco.functools      | 4.3.0            | 4.0.1          |
| more-itertools        | 10.8.0           | 10.3.0         |
| packaging             | 25               | 24.2           |
| propcache             | 0.4.0            | 0.4.1          |
| pydantic              | 2.11.10          | 2.12.0         |
| pydantic_core         | 2.33.2           | 2.41.1         |
| rich                  | 14.1.0           | 14.2.0         |
| types-python-dateutil | 2.9.0.20250822   | 2.9.0.20251008 |
| typing_extensions     | 4.12.2           | 4.15.0         |
| virtualenv            | 20.34.0          | 20.35.1        |
| websocket-client      | 1.8.0            | 1.9.0          |

- Removed packages: No packages were removed in this release.

**AL2023 ARM64**

Base DLAMI release note is available [here](../../../dlami/latest/devguide/aws-deep-learning-ami-gpubaseossarm64-al2023-2025-10-14.md "../../../dlami/latest/devguide/aws-deep-learning-ami-gpubaseossarm64-al2023-2025-10-14.md").

- EKS versions 1.31 - 1.33.
- This release contains CVE patches for affected NVIDIA Driver packages
  found in the [Nvidia
  October Security Bulletin](https://nvidia.custhelp.com/app/answers/detail/a_id/5703 "https://nvidia.custhelp.com/app/answers/detail/a_id/5703").
- NVIDIA SMI

```
NVIDIA-SMI 580.95.05
Driver Version: 580.95.05
CUDA Version: 13.0
```

- Major versions

| package name                     | version                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| gdr_copy                         | 2.5                                                                                 |
| supported_ec2_instances          | G5g, P6e-GB200                                                                      |
| efa_version                      | 1.43.3                                                                              |
| ebs_volume_type                  | gp3                                                                                 |
| nvidia_driver                    | 580.95.05                                                                           |
| python_location                  | /usr/bin/python3.9                                                                  |
| nvidia_cuda_stack                | /usr/local/cuda-12.6,/usr/local/cuda-12.8,/usr/local/cuda-12.9,/usr/local/cuda-13.0 |
| ssm_agent_version                | 3.3.3050.0                                                                          |
| kernel_version                   | 6.12.46-66.121.amzn2023.aarch64                                                     |
| nvidia_container_toolkit_version | 1.17.8                                                                              |
| dcgm_version                     | 4.4.1                                                                               |
| ofi_nccl_version                 | 1.16.3                                                                              |
| operating_system                 | Amazon Linux 2023.9.20250929                                                        |
| default_cuda                     | /usr/local/cuda-12.9/                                                               |
| compute_architecture             | aarch64                                                                             |

- Added packages: No packages were added in this release.
- Updated packages

| package name          | previous version  | new version       |
| --------------------- | ----------------- | ----------------- |
| aiohttp               | 3.12.15           | 3.13.0            |
| attrs                 | 25.3.0            | 25.4.0            |
| boto3                 | 1.40.45           | 1.40.49           |
| botocore              | 1.40.45           | 1.40.49           |
| cattrs                | 25.2.0            | 25.3.0            |
| certifi               | 2025.8.3          | 2025.10.5         |
| efa                   | 2.17.2-1.amzn2023 | 2.17.3-1.amzn2023 |
| fastapi               | 0.118.0           | 0.118.2           |
| frozenlist            | 1.7.0             | 1.8.0             |
| importlib_metadata    | 8.7.0             | 8.0.0             |
| jaraco.context        | 5.3.0             | 6.0.1             |
| multidict             | 6.6.4             | 6.7.0             |
| narwhals              | 2.6.0             | 2.7.0             |
| nh3                   | 0.3.0             | 0.3.1             |
| propcache             | 0.3.2             | 0.4.1             |
| pydantic              | 2.11.9            | 2.12.0            |
| pydantic_core         | 2.33.2            | 2.41.1            |
| pylint                | 3.3.8             | 3.3.9             |
| python-json-logger    | 3.3.0             | 4.0.0             |
| rich                  | 14.1.0            | 14.2.0            |
| tomli                 | 2.2.1             | 2.0.1             |
| types-python-dateutil | 2.9.0.20250822    | 2.9.0.20251008    |
| virtualenv            | 20.34.0           | 20.35.1           |
| websocket-client      | 1.8.0             | 1.9.0             |
| yarl                  | 1.20.1            | 1.22.0            |
| zipp                  | 3.19.2            | 3.23.0            |

- Removed packages: No packages were removed in this release.

## SageMaker HyperPod AMI

releases for Amazon EKS: September 29, 2025

**AMI general updates**

- Released the new SageMaker HyperPod AMI for Amazon EKS 1.33. For more information, see
  SageMaker HyperPod AMI releases for Amazon EKS: September 29, 2025.

###### Important

    + The Dynamic Resource Allocation beta Kubernetes API is enabled by default in this release.




    	- This API improves scheduling and monitoring workloads that require resources such as GPUs.
    	- This API was developed by the open source Kubernetes community and might change in future versions of Kubernetes. Before you use the API,
    	 review the [Kubernetes documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/ "https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/") and understand how it affects your workloads.
    + HyperPod is not releasing a HyperPod Amazon Linux 2 AMI for Kubernetes 1.33. AWS recommends that you
     migrate to AL2023. For more information, see [Upgrade from Amazon Linux 2 to AL2023](../../../eks/latest/userguide/al2023.md "../../../eks/latest/userguide/al2023.md").

For more information, see [Kubernetes v1.33](https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/ "https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/").

**SageMaker HyperPod DLAMI for Amazon EKS support**

This release includes the following updates:

Kubernetes v1.28

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- NVIDIA SMI:
  - NVIDIA driver version: 570.172.08
  - CUDA version: 12.8

- Packages:
  - Languages and core libraries:
    - GCC: 11.5.0-5.amzn2023.0.5
    - GCC 14: 14.2.1-7.amzn2023.0.1
    - Java: 17.0.16+8-1.amzn2023.1
    - Perl: 5.32.1-477.amzn2023.0.7
    - Python: 3.9.23-1.amzn2023.0.3
    - Go: 3.2.0-37.amzn2023
    - Rust: 1.89.0-1.amzn2023.0.2

  - Core Libraries:
    - GlibC: 2.34-196.amzn2023.0.1
    - OpenSSL: 3.2.2-1.amzn2023.0.1
    - Zlib: 1.2.11-33.amzn2023.0.5
    - XZ Utils: 5.2.5-9.amzn2023.0.2
    - Util-linux: 2.37.4-1.amzn2023.0.4

  - Neuron:
    - aws-neuronx-dkms: 2.23.9.0-dkms
    - aws-neuronx-tools: 2.25.145.0-1

  - EFA:
    - efa driver: 2.17.2-1.amzn2023
    - efa config: 1.18-1.amzn2023
    - efa nv peermem: 1.2.2-1.amzn2023
    - efa profile: 1.7-1.amzn2023

  - kernel:
    - kernel: 6.1.148-173.267.amzn2023
    - kernel development: 6.1.148-173.267.amzn2023
    - kernel headers: 6.1.148-173.267.amzn2023
    - kernel tools: 6.1.148-173.267.amzn2023
    - kernel modules extra: 6.1.148-173.267.amzn2023
    - kernel livepatch: 1.0-0.amzn2023

  - Nvidia:
    - nvidia container toolkit: 1.17.8-1
    - nvidia container toolkit base: 1.17.8-1
    - libnvidia-container: 1.17.8-1 (with tools)
    - nvidia fabric manager: 570.172.08-1
    - libnvidia-nscq: 570.172.08-1

Kubernetes v1.29

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- NVIDIA SMI:
  - NVIDIA driver version: 570.172.08
  - CUDA version: 12.8

- Packages:
  - Languages and core libraries:
    - GCC: 11.5.0-5.amzn2023.0.5
    - GCC 14: 14.2.1-7.amzn2023.0.1
    - Java: 17.0.16+8-1.amzn2023.1
    - Perl: 5.32.1-477.amzn2023.0.7
    - Python: 3.9.23-1.amzn2023.0.3
    - Go: 3.2.0-37.amzn2023
    - Rust: 1.89.0-1.amzn2023.0.2

  - Core Libraries:
    - GlibC: 2.34-196.amzn2023.0.1
    - OpenSSL: 3.2.2-1.amzn2023.0.1
    - Zlib: 1.2.11-33.amzn2023.0.5
    - XZ Utils: 5.2.5-9.amzn2023.0.2
    - Util-linux: 2.37.4-1.amzn2023.0.4

  - Neuron:
    - aws-neuronx-dkms: 2.23.9.0-dkms
    - aws-neuronx-tools: 2.25.145.0-1

  - EFA:
    - efa driver: 2.17.2-1.amzn2023
    - efa config: 1.18-1.amzn2023
    - efa nv peermem: 1.2.2-1.amzn2023
    - efa profile: 1.7-1.amzn2023

  - kernel:
    - kernel: 6.1.148-173.267.amzn2023
    - kernel development: 6.1.148-173.267.amzn2023
    - kernel headers: 6.1.148-173.267.amzn2023
    - kernel tools: 6.1.148-173.267.amzn2023
    - kernel modules extra: 6.1.148-173.267.amzn2023
    - kernel livepatch: 1.0-0.amzn2023

  - Nvidia:
    - nvidia container toolkit: 1.17.8-1
    - nvidia container toolkit base: 1.17.8-1
    - libnvidia-container: 1.17.8-1 (with tools)
    - nvidia fabric manager: 570.172.08-1
    - libnvidia-nscq: 570.172.08-1

Kubernetes v1.30

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- NVIDIA SMI:
  - NVIDIA driver version: 570.172.08
  - CUDA version: 12.8

- Packages:
  - Languages and core libraries:
    - GCC: 11.5.0-5.amzn2023.0.5
    - GCC 14: 14.2.1-7.amzn2023.0.1
    - Java: 17.0.16+8-1.amzn2023.1
    - Perl: 5.32.1-477.amzn2023.0.7
    - Python: 3.9.23-1.amzn2023.0.3
    - Go: 3.2.0-37.amzn2023
    - Rust: 1.89.0-1.amzn2023.0.2

  - Core Libraries:
    - GlibC: 2.34-196.amzn2023.0.1
    - OpenSSL: 3.2.2-1.amzn2023.0.1
    - Zlib: 1.2.11-33.amzn2023.0.5
    - XZ Utils: 5.2.5-9.amzn2023.0.2
    - Util-linux: 2.37.4-1.amzn2023.0.4

  - Neuron:
    - aws-neuronx-dkms: 2.23.9.0-dkms
    - aws-neuronx-tools: 2.25.145.0-1

  - EFA:
    - efa driver: 2.17.2-1.amzn2023
    - efa config: 1.18-1.amzn2023
    - efa nv peermem: 1.2.2-1.amzn2023
    - efa profile: 1.7-1.amzn2023

  - kernel:
    - kernel: 6.1.148-173.267.amzn2023
    - kernel development: 6.1.148-173.267.amzn2023
    - kernel headers: 6.1.148-173.267.amzn2023
    - kernel tools: 6.1.148-173.267.amzn2023
    - kernel modules extra: 6.1.148-173.267.amzn2023
    - kernel livepatch: 1.0-0.amzn2023

  - Nvidia:
    - nvidia container toolkit: 1.17.8-1
    - nvidia container toolkit base: 1.17.8-1
    - libnvidia-container: 1.17.8-1 (with tools)
    - nvidia fabric manager: 570.172.08-1
    - libnvidia-nscq: 570.172.08-1

Kubernetes v1.31

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- NVIDIA SMI:
  - NVIDIA driver version: 570.172.08
  - CUDA version: 12.8

- Packages:
  - Languages and core libraries:
    - GCC: 11.5.0-5.amzn2023.0.5
    - GCC 14: 14.2.1-7.amzn2023.0.1
    - Java: 17.0.16+8-1.amzn2023.1
    - Perl: 5.32.1-477.amzn2023.0.7
    - Python: 3.9.23-1.amzn2023.0.3
    - Go: 3.2.0-37.amzn2023
    - Rust: 1.89.0-1.amzn2023.0.2

  - Core Libraries:
    - GlibC: 2.34-196.amzn2023.0.1
    - OpenSSL: 3.2.2-1.amzn2023.0.1
    - Zlib: 1.2.11-33.amzn2023.0.5
    - XZ Utils: 5.2.5-9.amzn2023.0.2
    - Util-linux: 2.37.4-1.amzn2023.0.4

  - Neuron:
    - aws-neuronx-dkms: 2.23.9.0-dkms
    - aws-neuronx-tools: 2.25.145.0-1

  - EFA:
    - efa driver: 2.17.2-1.amzn2023
    - efa config: 1.18-1.amzn2023
    - efa nv peermem: 1.2.2-1.amzn2023
    - efa profile: 1.7-1.amzn2023

  - kernel:
    - kernel: 6.1.148-173.267.amzn2023
    - kernel development: 6.1.148-173.267.amzn2023
    - kernel headers: 6.1.148-173.267.amzn2023
    - kernel tools: 6.1.148-173.267.amzn2023
    - kernel modules extra: 6.1.148-173.267.amzn2023
    - kernel livepatch: 1.0-0.amzn2023

  - Nvidia:
    - nvidia container toolkit: 1.17.8-1
    - nvidia container toolkit base: 1.17.8-1
    - libnvidia-container: 1.17.8-1 (with tools)
    - nvidia fabric manager: 570.172.08-1
    - libnvidia-nscq: 570.172.08-1

Kubernetes v1.32

- **Amazon Linux 2 is now deprecated. Kubernetes AMI is based on AL2023.**
- NVIDIA SMI:
  - NVIDIA driver version: 570.172.08
  - CUDA version: 12.8

- Packages:
  - Languages and core libraries:
    - GCC: 11.5.0-5.amzn2023.0.5
    - GCC 14: 14.2.1-7.amzn2023.0.1
    - Java: 17.0.16+8-1.amzn2023.1
    - Perl: 5.32.1-477.amzn2023.0.7
    - Python: 3.9.23-1.amzn2023.0.3
    - Go: 3.2.0-37.amzn2023
    - Rust: 1.89.0-1.amzn2023.0.2

  - Core Libraries:
    - GlibC: 2.34-196.amzn2023.0.1
    - OpenSSL: 3.2.2-1.amzn2023.0.1
    - Zlib: 1.2.11-33.amzn2023.0.5
    - XZ Utils: 5.2.5-9.amzn2023.0.2
    - Util-linux: 2.37.4-1.amzn2023.0.4

  - Neuron:
    - aws-neuronx-dkms: 2.23.9.0-dkms
    - aws-neuronx-tools: 2.25.145.0-1

  - EFA:
    - efa driver: 2.17.2-1.amzn2023
    - efa config: 1.18-1.amzn2023
    - efa nv peermem: 1.2.2-1.amzn2023
    - efa profile: 1.7-1.amzn2023

  - kernel:
    - kernel: 6.1.148-173.267.amzn2023
    - kernel development: 6.1.148-173.267.amzn2023
    - kernel headers: 6.1.148-173.267.amzn2023
    - kernel tools: 6.1.148-173.267.amzn2023
    - kernel modules extra: 6.1.148-173.267.amzn2023
    - kernel livepatch: 1.0-0.amzn2023

  - Nvidia:
    - nvidia container toolkit: 1.17.8-1
    - nvidia container toolkit base: 1.17.8-1
    - libnvidia-container: 1.17.8-1 (with tools)
    - nvidia fabric manager: 570.172.08-1
    - libnvidia-nscq: 570.172.08-1

Kubernetes v1.33
The following table contains information about components within this AMI release
and the corresponding versions.

| component                | AL2023_x86                | AL2023_arm64              |
| ------------------------ | ------------------------- | ------------------------- |
| EKS                      | v1.33.4                   | v1.33.4                   |
| amazon-ssm-agent         | 3.3.2299.0-1.amzn2023     | 3.3.2299.0-1.amzn2023     |
| aws-neuronx-dkms         | 2.23.9.0-dkms             | N/A                       |
| containerd               | 1.7.27-1.eks.amzn2023.0.4 | 1.7.27-1.eks.amzn2023.0.4 |
| efa                      | 2.17.2-1.amzn2023         | 2.17.2-1.amzn2023         |
| ena                      | 2.14.1g                   | 2.14.1g                   |
| kernel                   | 6.12.40-64.114.amzn2023   | N/A                       |
| kernel6.12               | N/A                       | 6.12.40-64.114.amzn2023   |
| kmod-nvidia-latest-dkms  | 570.172.08-1.amzn2023     | 570.172.08-1.el9          |
| nvidia-container-toolkit | 1.17.8-1                  | 1.17.8-1                  |
| runc                     | 1.2.6-1.amzn2023.0.1      | 1.2.6-1.amzn2023.0.1      |

## SageMaker HyperPod AMI

releases for Amazon EKS: August 25, 2025

**SageMaker HyperPod DLAMI for Amazon EKS support**

This release includes the following updates:

Kubernetes v1.28
**NVIDIA SMI:**

- Nvidia Driver Version: 570.172.08
- CUDA Version: 12.8

**Added Packages:**

- kernel-livepatch-5.10.240-238.955.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Updated Packages:**

- gdk-pixbuf2.x86_64: 2.36.12-3.amzn2 →
  2.36.12-3.amzn2.0.2
- kernel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-devel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-headers.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-tools.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- libgs.x86_64: 9.54.0-9.amzn2.0.11 → 9.54.0-9.amzn2.0.12
- microcode_ctl.x86_64: 2:2.1-47.amzn2.4.24 →
  2:2.1-47.amzn2.4.25
- pam.x86_64: 1.1.8-23.amzn2.0.2 → 1.1.8-23.amzn2.0.4

**Removed Packages:**

- kernel-livepatch-5.10.239-236.958.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Repository Changed:**

- libnvidia-container-tools.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- libnvidia-container1.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit-base.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit

Kubernetes v1.29
**NVIDIA SMI:**

- Nvidia Driver Version: 570.172.08
- CUDA Version: 12.8

**Added Packages:**

- kernel-livepatch-5.10.240-238.955.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Updated Packages:**

- gdk-pixbuf2.x86_64: 2.36.12-3.amzn2 →
  2.36.12-3.amzn2.0.2
- kernel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-devel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-headers.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-tools.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- libgs.x86_64: 9.54.0-9.amzn2.0.11 → 9.54.0-9.amzn2.0.12
- microcode_ctl.x86_64: 2:2.1-47.amzn2.4.24 →
  2:2.1-47.amzn2.4.25
- pam.x86_64: 1.1.8-23.amzn2.0.2 → 1.1.8-23.amzn2.0.4

**Removed Packages:**

- kernel-livepatch-5.10.239-236.958.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Repository Changed:**

- libnvidia-container-tools.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- libnvidia-container1.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit-base.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit

Kubernetes v1.30
**NVIDIA SMI:**

- Nvidia Driver Version: 570.172.08
- CUDA Version: 12.8

**Added Packages:**

- kernel-livepatch-5.10.240-238.955.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Updated Packages:**

- aws-neuronx-dkms.noarch: 2.22.2.0-dkms → 2.23.9.0-dkms
- efa.x86_64: 2.15.3-1.amzn2 → 2.17.2-1.amzn2
- efa-nv-peermem.x86_64: 1.2.1-1.amzn2 → 1.2.2-1.amzn2
- gdk-pixbuf2.x86_64: 2.36.12-3.amzn2 →
  2.36.12-3.amzn2.0.2
- ibacm.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- infiniband-diags.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- kernel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-devel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-headers.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-tools.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- libfabric-aws.x86_64: 2.1.0amzn3.0-1.amzn2 →
  2.1.0amzn5.0-1.amzn2
- libfabric-aws-devel.x86_64: 2.1.0amzn3.0-1.amzn2 →
  2.1.0amzn5.0-1.amzn2
- libgs.x86_64: 9.54.0-9.amzn2.0.11 → 9.54.0-9.amzn2.0.12
- libibumad.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- libibverbs.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- libibverbs-core.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- libibverbs-utils.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- libnccl-ofi.x86_64: 1.15.0-1.amzn2 → 1.16.2-1.amzn2
- librdmacm.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- librdmacm-utils.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- microcode_ctl.x86_64: 2:2.1-47.amzn2.4.24 →
  2:2.1-47.amzn2.4.25
- pam.x86_64: 1.1.8-23.amzn2.0.2 → 1.1.8-23.amzn2.0.4
- rdma-core.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- rdma-core-devel.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2

**Removed Packages:**

- kernel-livepatch-5.10.239-236.958.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Repository Changed:**

- libnvidia-container-tools.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- libnvidia-container1.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit-base.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit

Kubernetes v1.31
**NVIDIA SMI:**

- Nvidia Driver Version: 570.172.08
- CUDA Version: 12.8

**Added Packages:**

- kernel-livepatch-5.10.240-238.955.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Updated Packages:**

- gdk-pixbuf2.x86_64: 2.36.12-3.amzn2 →
  2.36.12-3.amzn2.0.2
- kernel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-devel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-headers.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-tools.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- libgs.x86_64: 9.54.0-9.amzn2.0.11 → 9.54.0-9.amzn2.0.12
- microcode_ctl.x86_64: 2:2.1-47.amzn2.4.24 →
  2:2.1-47.amzn2.4.25
- pam.x86_64: 1.1.8-23.amzn2.0.2 → 1.1.8-23.amzn2.0.4

**Removed Packages:**

- kernel-livepatch-5.10.239-236.958.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Repository Changed:**

- libnvidia-container-tools.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- libnvidia-container1.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit-base.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit

Kubernetes v1.32
**NVIDIA SMI:**

- Nvidia Driver Version: 570.172.08
- CUDA Version: 12.8

**Added Packages:**

- kernel-livepatch-5.10.240-238.955.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Updated Packages:**

- aws-neuronx-dkms.noarch: 2.22.2.0-dkms → 2.23.9.0-dkms
- efa.x86_64: 2.15.3-1.amzn2 → 2.17.2-1.amzn2
- efa-nv-peermem.x86_64: 1.2.1-1.amzn2 → 1.2.2-1.amzn2
- gdk-pixbuf2.x86_64: 2.36.12-3.amzn2 →
  2.36.12-3.amzn2.0.2
- ibacm.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- infiniband-diags.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- kernel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-devel.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-headers.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- kernel-tools.x86_64: 5.10.239-236.958.amzn2 →
  5.10.240-238.955.amzn2
- libfabric-aws.x86_64: 2.1.0amzn3.0-1.amzn2 →
  2.1.0amzn5.0-1.amzn2
- libfabric-aws-devel.x86_64: 2.1.0amzn3.0-1.amzn2 →
  2.1.0amzn5.0-1.amzn2
- libgs.x86_64: 9.54.0-9.amzn2.0.11 → 9.54.0-9.amzn2.0.12
- libibumad.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- libibverbs.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- libibverbs-core.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- libibverbs-utils.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- libnccl-ofi.x86_64: 1.15.0-1.amzn2 → 1.16.2-1.amzn2
- librdmacm.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- librdmacm-utils.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- microcode_ctl.x86_64: 2:2.1-47.amzn2.4.24 →
  2:2.1-47.amzn2.4.25
- pam.x86_64: 1.1.8-23.amzn2.0.2 → 1.1.8-23.amzn2.0.4
- rdma-core.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2
- rdma-core-devel.x86_64: 57.amzn1-1.amzn2.0.2 →
  58.amzn0-1.amzn2.0.2

**Removed Packages:**

- kernel-livepatch-5.10.239-236.958.x86_64 1.0-0.amzn2
  amzn2extra-kernel-5.10

**Repository Changed:**

- libnvidia-container-tools.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- libnvidia-container1.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit
- nvidia-container-toolkit-base.x86_64: cuda-rhel8-x86_64 →
  nvidia-container-toolkit

## SageMaker HyperPod AMI

releases for Amazon EKS: August 12, 2025

**The AMI includes the following:**

- Supported AWS Service: Amazon EC2
- Operating System: Amazon Linux 2023
- Compute Architecture: ARM64
- Latest available version is installed for the following packages:
  - Linux Kernel: 6.12
  - FSx Lustre
  - Docker
  - AWS CLI v2 at `/usr/bin/aws`
  - NVIDIA DCGM
  - Nvidia container toolkit:
    - Version command: `nvidia-container-cli -V`

  - Nvidia-docker2:
    - Version command: `nvidia-docker version`

  - Nvidia-IMEX: v570.172.08-1

- NVIDIA Driver: 570.158.01
- NVIDIA CUDA 12.4, 12.5, 12.6, 12.8 stack:
  - CUDA, NCCL and cuDDN installation directories: `/usr/local/cuda-xx.x/`
    - Example: `/usr/local/cuda-12.8/`, `/usr/local/cuda-12.8/`

  - Compiled NCCL Version:
    - For CUDA directory of 12.4, compiled NCCL Version 2.22.3+CUDA12.4
    - For CUDA directory of 12.5, compiled NCCL Version 2.22.3+CUDA12.5
    - For CUDA directory of 12.6, compiled NCCL Version 2.24.3+CUDA12.6
    - For CUDA directory of 12.8, compiled NCCL Version 2.27.5+CUDA12.8

  - Default CUDA: 12.8
    - PATH `/usr/local/cuda` points to CUDA 12.8
    - Updated below env vars:
      - `LD_LIBRARY_PATH` to have `/usr/local/cuda-12.8/lib:/usr/local/cuda-12.8/lib64:/usr/local/cuda-12.8:/usr/local/cuda-12.8/targets/sbsa-linux/lib:/usr/local/cuda-12.8/nvvm/lib64:/usr/local/cuda-12.8/extras/CUPTI/lib64`
      - `PATH` to have `/usr/local/cuda-12.8/bin/:/usr/local/cuda-12.8/include/`
      - For any different CUDA version, please update `LD_LIBRARY_PATH` accordingly.

- EFA installer: 1.42.0
- Nvidia GDRCopy: 2.5.1
- AWS OFI NCCL plugin comes with EFA installer
  - Paths `/opt/amazon/ofi-nccl/lib` and `/opt/amazon/ofi-nccl/efa` are added to `LD_LIBRARY_PATH`.

- AWS CLI v2 at `/usr/local/bin/aws`
- EBS volume type: gp3
- Python: `/usr/bin/python3.9`

## SageMaker HyperPod AMI

releases for Amazon EKS: August 6, 2025

**SageMaker HyperPod DLAMI for Amazon EKS support**

The AMIs include the following updates:

K8s v1.28

- **Neuron packages:**
  - **aws-neuronx-collectives:**
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-dkms:**
    2.23.9.0-dkms
  - **aws-neuronx-runtime-lib:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-k8-plugin:** 2.27.7.0-1
  - **aws-neuronx-k8-scheduler:**
    2.27.7.0-1
  - **aws-neuronx-tools:**
    2.25.145.0-1

K8s v1.29

- **Neuron packages:**
  - **aws-neuronx-collectives:**
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-dkms:**
    2.23.9.0-dkms
  - **aws-neuronx-runtime-lib:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-k8-plugin:** 2.27.7.0-1
  - **aws-neuronx-k8-scheduler:**
    2.27.7.0-1
  - **aws-neuronx-tools:**
    2.25.145.0-1

K8s v1.30

- **Neuron packages:**
  - **aws-neuronx-collectives:**
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-dkms:**
    2.23.9.0-dkms
  - **aws-neuronx-runtime-lib:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-k8-plugin:** 2.27.7.0-1
  - **aws-neuronx-k8-scheduler:**
    2.27.7.0-1
  - **aws-neuronx-tools:**
    2.25.145.0-1

K8s v1.31

- **Neuron packages:**
  - **aws-neuronx-collectives:**
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-dkms:**
    2.23.9.0-dkms
  - **aws-neuronx-runtime-lib:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-k8-plugin:** 2.27.7.0-1
  - **aws-neuronx-k8-scheduler:**
    2.27.7.0-1
  - **aws-neuronx-tools:**
    2.25.145.0-1

K8s v1.32

- **Neuron packages:**
  - **aws-neuronx-collectives:**
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-dkms:**
    2.23.9.0-dkms
  - **aws-neuronx-runtime-lib:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-k8-plugin:** 2.27.7.0-1
  - **aws-neuronx-k8-scheduler:**
    2.27.7.0-1
  - **aws-neuronx-tools:**
    2.25.145.0-1

###### Important

- Deep Learning Base OSS Nvidia Driver AMI (Amazon Linux 2) Version 70.3
- Deep Learning Base Proprietary Nvidia Driver AMI (Amazon Linux 2) Version
  68.4
- Latest CUDA 12.8 support
- Upgraded Nvidia Driver to from 570.158.01 to 570.172.08 to fix CVE's
  present in the Nvidia Security Bulletin for July

## SageMaker HyperPod AMI

releases for Amazon EKS: July 31, 2025

Amazon SageMaker HyperPod now supports a new AMI for Amazon EKS clusters that updates the base
operating system to Amazon Linux 2023. This release provides several improvements from
Amazon Linux 2 (AL2). HyperPod releases new AMIs regularly, and we recommend that
you run all of your HyperPod clusters on the latest and most secure
versions of AMIs to address vulnerabilities and phase out outdated software and
libraries.

### Key

upgrades

- **Operating System**: Amazon Linux 2023
  (updated from Amazon Linux 2, or AL2)
- **Package Manager**: DNF is the default
  package management tool, replacing YUM used in AL2
- **Networking Service**:
  `systemd-networkd` manages network interfaces, replacing
  ISC `dhclient` used in AL2
- **Linux Kernel**: Version 6.1, updated
  from the kernel used in AL2
- **Glibc**: Version 2.34, updated from the
  version in AL2
- **GCC**: Version 11.5.0, updated from the
  version in AL2
- **NFS**: Version 1:2.6.1, updated from
  version 1:1.3.4 in AL2
- **NVIDIA Driver**: Version 570.172.08, a
  newer driver version
- **Python**: Version 3.9, replacing Python
  2.7 used in AL2
- **NVME**: Version 1.11.1, a newer version
  of the NVMe driver

### Before you

upgrade

There are a few important things to know before upgrading. With AL2023,
several packages have been added, upgraded or removed compared to AL2. We
strongly recommend that you test your applications with AL2023 before
upgrading your clusters. For a comprehensive list of all package changes in
AL2023, see [Package changes in
Amazon Linux 2023](../../../linux/al2023/release-notes/compare-packages.md "../../../linux/al2023/release-notes/compare-packages.md").

The following are some of the significant changes between AL2 and
AL2023:

- **Python 3.10**: The most significant
  update, apart from the operating system, is the Python version upgrade.
  After upgrading, clusters have Python 3.10 as default. While some Python
  3.8 distributed training workloads might be compatible with Python 3.10,
  we strongly recommend that you test your specific workloads separately.
  If migration to Python 3.10 proves challenging but you still want to
  upgrade your cluster for other new features, you can install an older
  Python version by using the command `yum install python-xx.x`
  with [lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md") before running any workloads. Ensure you
  test both your existing lifecycle scripts and application code for
  compatibility.
- **NVIDIA runtime enforcement**: AL2023
  strictly enforces the NVIDIA container runtime requirements, causing
  containers with hard-coded NVIDIA environment variables (such as
  `NVIDIA_VISIBLE_DEVICES: "all"`) to fail on CPU-only
  nodes (whereas AL2 ignored these settings when no GPU drivers are
  present). You can override the enforcement by setting
  `NVIDIA_VISIBLE_DEVICES: "void"` in your pod
  specification or by using CPU-only images.
- **cgroup v2**: AL2023 features the next
  generation of unified control group hierarchy (cgroup v2). cgroup v2 is
  used for container runtimes and is also used by `systemd`.
  While AL2023 still includes code that can make the system run using
  cgroup v1, this isn't a recommended configuration.
- **Amazon VPC CNI and `eksctl`
  versions**: AL2023 also requires your Amazon VPC CNI version
  to be 1.16.2 or greater and your `eksctl` version to be
  0.176.0 or greater.
- **EFA on FSx for Lustre**: You can now use
  EFA on FSx for Lustre, which enables you to achieve application performance
  comparable to on-premises AI/ML or HPC (high performance computing)
  clusters, while benefiting from the scalability, flexibility and
  elasticity of cloud computing.

Additionally, upgrading to AL2023 requires at minimum version
`1.0.643.0_1.0.192.0` of Health Monitoring Agent. Complete the
following procedure to update the Health Monitoring Agent:

1. If you use HyperPod lifecycle scripts from the GitHub
   repository [awsome-distributed-training](https://github.com/aws-samples/awsome-distributed-training) "https://github.com/aws-samples/awsome-distributed-training)"), make sure to pull the latest
   version. Earlier versions are not compatible with AL2023. The new
   lifecycle script ensures that `containerd` uses the
   additional mounted storage for pulling in container images in
   AL2023.
2. Pull in the latest version of the [HyperPod CLI git repository](https://github.com/aws/sagemaker-hyperpod-cli/tree/main "https://github.com/aws/sagemaker-hyperpod-cli/tree/main").
3. Update dependencies with the following command: `helm
dependencies update helm_chart/HyperPodHelmChart`
4. As mentioned on the step 4 in the [README of HyperPodHelmChart](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart#step-four-whenever-you-want-to-upgrade-the-installation-of-helm-charts "https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart#step-four-whenever-you-want-to-upgrade-the-installation-of-helm-charts"), run the following command to
   upgrade the version of dependencies running on the cluster: `helm
upgrade dependencies helm_chart/HyperPodHelmChart -namespace
kube-system`

### Workloads

that have been tested on upgraded EKS clusters

The following are some use cases where the upgrade has been tested:

- **Backwards compatibility**: Popular
  distributed training jobs involving PyTorch should be backwards
  compatible on the new AMI. However, since your workloads may depend on
  specific Python or Linux libraries, we recommend first testing on a
  smaller scale or subset of nodes before upgrading your larger
  clusters.
- **Accelerator testing**: Jobs across
  various instance types, utilizing both NVIDIA accelerators (for the P
  and G instance families) and AWS Neuron accelerators (for Trn
  instances) have been tested.

### How to

upgrade your AMI and associated workloads

You can upgrade to the new AMI using one of the following methods:

- Use the [create-cluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") API to create a new cluster with the latest
  AMI.
- Use the [update-cluster-software](../APIReference/API_UpdateClusterSoftware.md "../APIReference/API_UpdateClusterSoftware.md") API to upgrade your existing
  cluster. Note that this option re-runs any lifecycle scripts.

The cluster is unavailable during the update process. We recommend planning
for this downtime and restarting the training workload from an existing
checkpoint after the upgrade completes. As a best practice, we recommend that
you perform testing on a smaller cluster before upgrading your larger
clusters.

If the update command fails, first identify the cause of the failure. For
lifecycle script failures, make the necessary corrections to your scripts and
retry. For any other issues that cannot be resolved, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

### Troubleshooting

Use the following section to help with troubleshooting any issues you
encounter when upgrading to AL2023.

**How do I fix errors such as `"nvml error: driver
 not loaded: unknown"` on CPU-only cluster nodes?**

If containers that worked on CPU AL2 Amazon EKS nodes now fail on AL2023, your
container image may have hard-coded NVIDIA environment variables. You can check
for hard-coded environment variables with the following command:

```
docker inspect image:tag | grep -i nvidia
```

AL2023 strictly enforces these requirements whereas AL2 was more lenient on
CPU-only nodes. One solution is to override the AL2023 enforcement by setting
certain NVIDIA environment variables in your Amazon EKS pod specification, as shown
in the following example:

```
yaml
containers:
- name: your-container
image: your-image:tag
env:
- name: NVIDIA_VISIBLE_DEVICES
value: "void"
- name: NVIDIA_DRIVER_CAPABILITIES
value: ""
```

Another alternative is to use CPU-only container images (such as
`pytorch/pytorch:latest-cpu`) or build custom images without
NVIDIA dependencies.

## SageMaker HyperPod AMI

releases for Amazon EKS: July 15, 2025

**SageMaker HyperPod DLAMI for Amazon EKS support**

The AMIs include the following updates:

K8s v1.28

- **Latest NVIDIA Driver:**
  550.163.01
- **Default CUDA:** 12.4
- **EFA Installer:** 1.38.0
- **Neuron packages:**
  - **aws-neuronx-dkms.noarch:**
    2.22.2.0-dkms
  - **aws-neuronx-oci-hook.x86_64:**
    2.4.4.0-1
  - **aws-neuronx-tools.x86_64:**
    2.18.3.0-1
  - **aws-neuron-dkms.noarch:**
    2.3.26.0-dkms
  - **aws-neuron-k8-plugin.x86_64:**
    1.9.3.0-1
  - **aws-neuron-k8-scheduler.x86_64:**
    1.9.3.0-1
  - **aws-neuron-runtime.x86_64:**
    1.6.24.0-1
  - **aws-neuron-runtime-base.x86_64:**
    1.6.21.0-1
  - **aws-neuron-tools.x86_64:**
    2.1.4.0-1
  - **aws-neuronx-collectives.x86_64:**
    2.26.43.0_47cc904ea-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.16.2.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.16.1.0_0a6506a47-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.26.42.0_2ff3b5c7d-1
  - **aws-neuronx-tools.x86_64:**
    2.24.54.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0

K8s v1.29

- **Nvidia Driver Version:**
  550.163.01
- **CUDA Version:** 12.4
- **EFA Installer:** 1.38.0
- **Neuron packages:**
  - **aws-neuronx-dkms.noarch:**
    2.22.2.0-dkms
  - **aws-neuronx-oci-hook.x86_64:**
    2.4.4.0-1
  - **aws-neuronx-tools.x86_64:**
    2.18.3.0-1
  - **aws-neuron-dkms.noarch:**
    2.3.26.0-dkms
  - **aws-neuron-k8-plugin.x86_64:**
    1.9.3.0-1
  - **aws-neuron-k8-scheduler.x86_64:**
    1.9.3.0-1
  - **aws-neuron-runtime.x86_64:**
    1.6.24.0-1
  - **aws-neuron-runtime-base.x86_64:**
    1.6.21.0-1
  - **aws-neuron-tools.x86_64:**
    2.1.4.0-1
  - **aws-neuronx-collectives.x86_64:**
    2.26.43.0_47cc904ea-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.16.2.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.16.1.0_0a6506a47-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.26.42.0_2ff3b5c7d-1
  - **aws-neuronx-tools.x86_64:**
    2.24.54.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0

K8s v1.30

- **Nvidia Driver Version:**
  550.163.01
- **CUDA Version:** 12.4
- **EFA installer version:**
  1.38.0
- **Neuron packages:**
  - **aws-neuronx-dkms.noarch:**
    2.22.2.0-dkms
  - **aws-neuronx-oci-hook.x86_64:**
    2.4.4.0-1
  - **aws-neuronx-tools.x86_64:**
    2.18.3.0-1
  - **aws-neuron-dkms.noarch:**
    2.3.26.0-dkms
  - **aws-neuron-k8-plugin.x86_64:**
    1.9.3.0-1
  - **aws-neuron-k8-scheduler.x86_64:**
    1.9.3.0-1
  - **aws-neuron-runtime.x86_64:**
    1.6.24.0-1
  - **aws-neuron-runtime-base.x86_64:**
    1.6.21.0-1
  - **aws-neuron-tools.x86_64:**
    2.1.4.0-1
  - **aws-neuronx-collectives.x86_64:**
    2.26.43.0_47cc904ea-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.16.2.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.16.1.0_0a6506a47-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.26.42.0_2ff3b5c7d-1
  - **aws-neuronx-tools.x86_64:**
    2.24.54.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0

K8s v1.31

- **Nvidia Driver Version:**
  550.163.01
- **CUDA Version:** 12.4
- **EFA installer version:**
  1.38.0
- **Neuron packages:**
  - **aws-neuronx-dkms.noarch:**
    2.22.2.0-dkms
  - **aws-neuronx-oci-hook.x86_64:**
    2.4.4.0-1
  - **aws-neuronx-tools.x86_64:**
    2.18.3.0-1
  - **aws-neuron-dkms.noarch:**
    2.3.26.0-dkms
  - **aws-neuron-k8-plugin.x86_64:**
    1.9.3.0-1
  - **aws-neuron-k8-scheduler.x86_64:**
    1.9.3.0-1
  - **aws-neuron-runtime.x86_64:**
    1.6.24.0-1
  - **aws-neuron-runtime-base.x86_64:**
    1.6.21.0-1
  - **aws-neuron-tools.x86_64:**
    2.1.4.0-1
  - **aws-neuronx-collectives.x86_64:**
    2.26.43.0_47cc904ea-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.16.2.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.16.1.0_0a6506a47-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.26.42.0_2ff3b5c7d-1
  - **aws-neuronx-tools.x86_64:**
    2.24.54.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0

K8s v1.32

- **Nvidia Driver Version:**
  550.163.01
- **CUDA Version:** 12.4
- **EFA installer version:**
  1.38.0
- **Neuron packages:**
  - **aws-neuronx-dkms.noarch:**
    2.22.2.0-dkms
  - **aws-neuronx-oci-hook.x86_64:**
    2.4.4.0-1
  - **aws-neuronx-tools.x86_64:**
    2.18.3.0-1
  - **aws-neuron-dkms.noarch:**
    2.3.26.0-dkms
  - **aws-neuron-k8-plugin.x86_64:**
    1.9.3.0-1
  - **aws-neuron-k8-scheduler.x86_64:**
    1.9.3.0-1
  - **aws-neuron-runtime.x86_64:**
    1.6.24.0-1
  - **aws-neuron-runtime-base.x86_64:**
    1.6.21.0-1
  - **aws-neuron-tools.x86_64:**
    2.1.4.0-1
  - **aws-neuronx-collectives.x86_64:**
    2.26.43.0_47cc904ea-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.16.2.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.16.1.0_0a6506a47-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.26.26.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.26.42.0_2ff3b5c7d-1
  - **aws-neuronx-tools.x86_64:**
    2.24.54.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0

## SageMaker HyperPod AMI

releases for Amazon EKS: June 09, 2025

**SageMaker HyperPod DLAMI for Amazon EKS support**

Neuron SDK Updates

- **aws-neuronx-dkms.noarch:**
  2.21.37.0 (from 2.20.74.0)

## SageMaker HyperPod AMI

releases for Amazon EKS: May 22, 2025

**AMI general updates**

**SageMaker HyperPod DLAMI for Amazon EKS support**

Deep Learning Base AMI AL2

- **Latest NVIDIA Driver:**
  550.163.01
- **CUDA Stack updates:**
  - **Default CUDA:**
    12.1
  - **NCCL Version:**
    2.22.3

- **EFA Installer:** 1.38.0
- **AWS OFI NCCL:** 1.13.2
- **Linux Kernel:** 5.10
- **GDRCopy:** 2.4

###### Important

- **NVIDIA Container Toolkit 1.17.4
  update:** CUDA compat libraries mounting is now
  disabled
- **EFA Updates from 1.37 to
  1.38:**
  - AWS OFI NCCL plugin now located in
    /opt/amazon/ofi-nccl
  - Previous location /opt/aws-ofi-nccl/ is
    deprecated

Neuron SDK Updates

- **aws-neuronx-dkms.noarch:**
  2.20.74.0 (from 2.20.28.0)
- **aws-neuronx-collectives.x86_64:**
  2.25.65.0_9858ac9a1-1 (from 2.24.59.0_838c7fc8b-1)
- **aws-neuronx-runtime-lib.x86_64:**
  2.25.57.0_166c7a468-1 (from 2.24.53.0_f239092cc-1)
- **aws-neuronx-tools.x86_64:**
  2.23.9.0 (from 2.22.61.0)
- **aws-neuronx-gpsimd-customop-lib.x86_64:**
  0.15.12.0 (from 0.14.12.0)
- **aws-neuronx-gpsimd-tools.x86_64:**
  0.15.1.0_5d31b6a3f (from 0.14.6.0_241eb69f4)
- **aws-neuronx-k8-plugin.x86_64:** 2.25.24.0 (from 2.24.23.0)
- **aws-neuronx-k8-scheduler.x86_64:** 2.25.24.0 (from
  2.24.23.0)

**Support notes:**

- AMI components including CUDA versions may be removed or
  changed based on framework support policy
- Kernel version is pinned for compatibility. Users should avoid
  updates unless required for security patches
- For EC2 instances with multiple network cards, please refer to
  EFA configuration guide for proper setup

## SageMaker HyperPod AMI

releases for Amazon EKS: May 07, 2025

Installed the latest version of AWS Neuron SDK

- **tensorflow-model-server-neuron.x86_64**
  2.8.0.2.3.0.0-0 neuron

## SageMaker HyperPod AMI

releases for Amazon EKS: April 28, 2025

**Improvements for K8s**

- Upgraded NVIDIA driver from version 550.144.03 to 550.163.01. This upgrade
  is to address Common Vulnerabilities and Exposures (CVEs) present in the
  [NVIDIA GPU Display Security Bulletin for April 2025](https://nvidia.custhelp.com/app/answers/detail/a_id/5630 "https://nvidia.custhelp.com/app/answers/detail/a_id/5630").

**SageMaker HyperPod DLAMI for Amazon EKS support**

Installed the latest version of AWS Neuron SDK

- **aws-neuronx-dkms.noarch:**
  2.20.28.0-dkms
- **aws-neuronx-oci-hook.x86_64:**
  2.4.4.0-1
- **aws-neuronx-tools.x86_64:**
  2.18.3.0-1
- **aws-neuron-dkms.noarch:**
  2.3.26.0-dkms
- **aws-neuron-k8-plugin.x86_64:**
  1.9.3.0-1
- **aws-neuron-k8-scheduler.x86_64:** 1.9.3.0-1
- **aws-neuron-runtime.x86_64:**
  1.6.24.0-1
- **aws-neuron-runtime-base.x86_64:**
  1.6.21.0-1
- **aws-neuron-tools.x86_64:**
  2.1.4.0-1
- **aws-neuronx-collectives.x86_64:**
  2.24.59.0_838c7fc8b-1
- **aws-neuronx-gpsimd-customop.x86_64:**
  0.2.3.0-1
- **aws-neuronx-gpsimd-customop-lib.x86_64:**
  0.14.12.0-1
- **aws-neuronx-gpsimd-tools.x86_64:**
  0.14.6.0_241eb69f4-1
- **aws-neuronx-k8-plugin.x86_64:**
  2.24.23.0-1
- **aws-neuronx-k8-scheduler.x86_64:**
  2.24.23.0-1
- **aws-neuronx-runtime-lib.x86_64:**
  2.24.53.0_f239092cc-1
- **aws-neuronx-tools.x86_64:**
  2.22.61.0-1
- **tensorflow-model-server-neuronx.x86_64:**
  2.10.1.2.12.2.0-0

## SageMaker HyperPod AMI

releases for Amazon EKS: April 18, 2025

**AMI general updates**

- New SageMaker HyperPod AMI for Amazon EKS 1.32.1.

**SageMaker HyperPod DLAMI for Amazon EKS support**

The AMIs include the following:

Deep Learning EKS AMI 1.32.1

- **Amazon EKS Components**
  - Kubernetes Version: 1.32.1
  - Containerd Version: 1.7.27
  - Runc Version: 1.1.14
  - AWS IAM Authenticator: 0.6.29

- **Amazon SSM Agent:** 3.3.1611.0
- **Linux Kernel:** 5.10.235
- **OSS Nvidia driver:**
  550.163.01
- **NVIDIA CUDA:** 12.4
- **EFA Installer:** 1.38.0
- **GDRCopy:** 2.4.1-1
- **Nvidia container toolkit:**
  1.17.6
- **AWS OFI NCCL:** 1.13.2
- **aws-neuronx-tools:**
  2.18.3.0
- **aws-neuronx-runtime-lib:**
  2.24.53.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.20.28.0
- **aws-neuronx-collectives:**
  2.24.59.0

## SageMaker HyperPod AMI

releases for Amazon EKS: February 18, 2025

**Improvements for K8s**

- Upgraded Nvidia container toolkit from version 1.17.3 to version
  1.17.4.
- Fixed the issue where customers were unable to connect to nodes after a
  reboot.
- Upgraded Elastic Fabric Adapter (EFA) version from 1.37.0 to
  1.38.0.
- The EFA now includes the AWS OFI NCCL plugin, which is located in the
  `/opt/amazon/ofi-nccl` directory instead of the original
  `/opt/aws-ofi-nccl/` path. If you need to update your
  `LD_LIBRARY_PATH` environment variable, make sure to modify
  the path to point to the new `/opt/amazon/ofi-nccl` location for
  the OFI NCCL plugin.
- Removed the emacs package from these DLAMIs. You can install emacs from
  GNU emac.

**SageMaker HyperPod DLAMI for Amazon EKS support**

Installed the latest version of neuron SDK

- **aws-neuronx-dkms.noarch:**
  2.19.64.0-dkms @neuron
- **aws-neuronx-oci-hook.x86_64:**
  2.4.4.0-1 @neuron
- **aws-neuronx-tools.x86_64:**
  2.18.3.0-1 @neuron
- **aws-neuronx-collectives.x86_64:**
  2.23.135.0_3e70920f2-1 neuron
- **aws-neuronx-gpsimd-customop.x86_64:** 0.2.3.0-1
  neuron
- **aws-neuronx-gpsimd-customop-lib.x86_64**
- **aws-neuronx-gpsimd-tools.x86_64:**
  0.13.2.0_94ba34927-1 neuron
- **aws-neuronx-k8-plugin.x86_64:**
  2.23.45.0-1 neuron
- **aws-neuronx-k8-scheduler.x86_64:** 2.23.45.0-1
  neuron
- **aws-neuronx-runtime-lib.x86_64:**
  2.23.112.0_9b5179492-1 neuron
- **aws-neuronx-tools.x86_64:**
  2.20.204.0-1 neuron
- **tensorflow-model-server-neuronx.x86_64**

## SageMaker HyperPod AMI

releases for Amazon EKS: January 22, 2025

**AMI general updates**

- New SageMaker HyperPod AMI for Amazon EKS 1.31.2.

**SageMaker HyperPod DLAMI for Amazon EKS support**

The AMIs include the following:

Deep Learning EKS AMI 1.31

- **Amazon EKS Components**
  - Kubernetes Version: 1.31.2
  - Containerd Version: 1.7.23
  - Runc Version: 1.1.14
  - AWS IAM Authenticator: 0.6.26

- **Amazon SSM Agent:**
  3.3.987
- **Linux Kernel:** 5.10.230
- **OSS Nvidia driver:**
  550.127.05
- **NVIDIA CUDA:** 12.4
- **EFA Installer:** 1.37.0
- **GDRCopy:** 2.4.1-1
- **Nvidia container toolkit:**
  1.17.3
- **AWS OFI NCCL:** 1.13.0
- **aws-neuronx-tools:**
  2.18.3
- **aws-neuronx-runtime-lib:**
  2.23.112.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.18.20.0
- **aws-neuronx-collectives:**
  2.23.133.0

## SageMaker HyperPod AMI

releases for Amazon EKS: December 21, 2024

**SageMaker HyperPod DLAMI for Amazon EKS support**

The AMIs include the following:

K8s v1.28

- **Amazon EKS Components**
  - Kubernetes Version: 1.28.15
  - Containerd Version: 1.7.23
  - Runc Version: 1.1.14
  - AWS IAM Authenticator: 0.6.26

- **Amazon SSM Agent:**
  3.3.987
- **Linux Kernel:** 5.10.228
- **OSS NVIDIA driver:**
  550.127.05
- **NVIDIA CUDA:** 12.4
- **EFA Installer:** 1.37.0
- **GDRCopy:** 2.4
- **NVIDIA container toolkit:**
  1.17.3
- **AWS OFI NCCL:** 1.13.0
- **aws-neuronx-tools:**
  2.18.3.0-1
- **aws-neuronx-runtime-lib:**
  2.23.112.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.18.20.0
- **aws-neuronx-collectives:**
  2.23.135.0

K8s v1.29

- **Amazon EKS Components**
  - Kubernetes Version: 1.29.10
  - Containerd Version: 1.7.23
  - Runc Version: 1.1.14
  - AWS IAM Authenticator: 0.6.26

- **Amazon SSM Agent:**
  3.3.987
- **Linux Kernel:** 5.15.0
- **OSS Nvidia driver:**
  550.127.05
- **NVIDIA CUDA:** 12.4
- **EFA Installer:** 1.37.0
- **GDRCopy:** 2.4
- **Nvidia container toolkit:**
  1.17.3
- **AWS OFI NCCL:** 1.13.0
- **aws-neuronx-tools:**
  2.18.3.0-1
- **aws-neuronx-runtime-lib:**
  2.23.112.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.18.20.0
- **aws-neuronx-collectives:**
  2.23.135.0

K8s v1.30

- **Amazon EKS Components**
  - Kubernetes Version: 1.30.6
  - Containerd Version: 1.7.23
  - Runc Version: 1.1.14
  - AWS IAM Authenticator: 0.6.26

- **Amazon SSM Agent:**
  3.3.987.0
- **Linux Kernel:** 5.10.228
- **OSS Nvidia driver:**
  550.127.05
- **NVIDIA CUDA:** 12.4
- **EFA Installer:** 1.37.0
- **GDRCopy:** 2.4
- **Nvidia container toolkit:**
  1.17.3
- **AWS OFI NCCL:** 1.13.0
- **aws-neuronx-tools:**
  2.18.3.0-1
- **aws-neuronx-runtime-lib:**
  2.23.112.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.18.20.0
- **aws-neuronx-collectives:**
  2.23.135.0

## SageMaker HyperPod AMI

releases for Amazon EKS: December 13, 2024

**SageMaker HyperPod DLAMI for Amazon EKS upgrade**

- Updated SSM Agent to version `3.3.1311.0`.

## SageMaker HyperPod AMI

releases for Amazon EKS: November 24, 2024

**AMI general updates**

- Released in `MEL` (Melbourne) Region.
- Updated SageMaker HyperPod base DLAMI to the following versions:
  - Kubernetes: 2024-11-01.

## SageMaker HyperPod AMI

releases for Amazon EKS: November 15, 2024

**SageMaker HyperPod DLAMI for Amazon EKS support**

The AMIs include the following:

Deep Learning EKS AMI 1.28

- **Amazon EKS Components**
  - Kubernetes Version: 1.28.15
  - Containerd Version: 1.7.23
  - Runc Version: 1.1.14
  - AWS IAM Authenticator: 0.6.26

- **Amazon SSM Agent:**
  3.3.987
- **Linux Kernel:** 5.10.228
- **OSS NVIDIA driver:**
  550.127.05
- **NVIDIA CUDA:** 12.4
- **EFA Installer:** 1.34.0
- **GDRCopy:** 2.4
- **NVIDIA container toolkit:**
  1.17.3
- **AWS OFI NCCL:** 1.11.0
- **aws-neuronx-tools:**
  2.18.3.0-1
- **aws-neuronx-runtime-lib:**
  2.22.19.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.18.20.0
- **aws-neuronx-collectives:**
  2.22.33.0

Deep Learning EKS AMI 1.29

- **Amazon EKS Components**
  - Kubernetes Version: 1.29.10
  - Containerd Version: 1.7.23
  - Runc Version: 1.1.14
  - AWS IAM Authenticator: 0.6.26

- **Amazon SSM Agent:**
  3.3.987
- **Linux Kernel:** 5.10.228
- **OSS Nvidia driver:**
  550.127.05
- **NVIDIA CUDA:** 12.4
- **EFA Installer:** 1.34.0
- **GDRCopy:** 2.4
- **Nvidia container toolkit:**
  1.17.3
- **AWS OFI NCCL:** 1.11.0
- **aws-neuronx-tools:**
  2.18.3.0-1
- **aws-neuronx-runtime-lib:**
  2.22.19.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.18.20.0
- **aws-neuronx-collectives:**
  2.22.33.0

Deep Learning EKS AMI 1.30

- **Amazon EKS Components**
  - Kubernetes Version: 1.30.6
  - Containerd Version: 1.7.23
  - Runc Version: 1.1.14
  - AWS IAM Authenticator: 0.6.26

- **Amazon SSM Agent:**
  3.3.987
- **Linux Kernel:** 5.10.228
- **OSS Nvidia driver:**
  550.127.05
- **NVIDIA CUDA:** 12.4
- **EFA Installer:** 1.34.0
- **GDRCopy:** 2.4
- **Nvidia container toolkit:**
  1.17.3
- **AWS OFI NCCL:** 1.11.0
- **aws-neuronx-tools:**
  2.18.3.0-1
- **aws-neuronx-runtime-lib:**
  2.22.19.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.18.20.0
- **aws-neuronx-collectives:**
  2.22.33.0

## SageMaker HyperPod AMI

releases for Amazon EKS: November 11, 2024

**AMI general updates**

- Updated SageMaker HyperPod DLAMI with Amazon EKS versions 1.28.13, 1.29.8,
  1.30.4.

## SageMaker HyperPod AMI

releases for Amazon EKS: October 21, 2024

**AMI general updates**

- Updated SageMaker HyperPod base DLAMI to the following versions:
  - Amazon EKS: 1.28.11, 1.29.6, 1.30.2.

## SageMaker HyperPod AMI

releases for Amazon EKS: September 10, 2024

**SageMaker HyperPod DLAMI for Amazon EKS support**

The AMIs include the following:

Deep Learning EKS AMI 1.28

- **Amazon EKS Components**
  - Kubernetes Version: 1.28.11
  - Containerd Version: 1.7.20
  - Runc Version: 1.1.11
  - AWS IAM Authenticator: 0.6.21

- **Amazon SSM Agent:**
  3.3.380
- **Linux Kernel:** 5.10.223
- **OSS NVIDIA driver:**
  535.183.01
- **NVIDIA CUDA:** 12.2
- **EFA Installer:** 1.32.0
- **GDRCopy:** 2.4
- **NVIDIA container toolkit:**
  1.16.1
- **AWS OFI NCCL:** 1.9.1
- **aws-neuronx-tools:**
  2.18.3.0-1
- **aws-neuronx-runtime-lib:**
  2.21.41.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.17.17.0
- **aws-neuronx-collectives:**
  2.21.46.0

Deep Learning EKS AMI 1.29

- **Amazon EKS Components**
  - Kubernetes Version: 1.29.6
  - Containerd Version: 1.7.20
  - Runc Version: 1.1.11
  - AWS IAM Authenticator: 0.6.21

- **Amazon SSM Agent:**
  3.3.380
- **Linux Kernel:** 5.10.223
- **OSS Nvidia driver:**
  535.183.01
- **NVIDIA CUDA:** 12.2
- **EFA Installer:** 1.32.0
- **GDRCopy:** 2.4
- **Nvidia container toolkit:**
  1.16.1
- **AWS OFI NCCL:** 1.9.1
- **aws-neuronx-tools:**
  2.18.3.0-1
- **aws-neuronx-runtime-lib:**
  2.21.41.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.17.17.0
- **aws-neuronx-collectives:**
  2.21.46.0

Deep Learning EKS AMI 1.30

- **Amazon EKS Components**
  - Kubernetes Version: 1.30.2
  - Containerd Version: 1.7.20
  - Runc Version: 1.1.11
  - AWS IAM Authenticator: 0.6.21

- **Amazon SSM Agent:**
  3.3.380
- **Linux Kernel:** 5.10.223
- **OSS Nvidia driver:**
  535.183.01
- **NVIDIA CUDA:** 12.2
- **EFA Installer:** 1.32.0
- **GDRCopy:** 2.4
- **Nvidia container toolkit:**
  1.16.1
- **AWS OFI NCCL:** 1.9.1
- **aws-neuronx-tools:**
  2.18.3.0-1
- **aws-neuronx-runtime-lib:**
  2.21.41.0
- **aws-neuronx-oci-hook:**
  2.4.4.0-1
- **aws-neuronx-dkms:**
  2.17.17.0
- **aws-neuronx-collectives:**
  2.21.46.0
