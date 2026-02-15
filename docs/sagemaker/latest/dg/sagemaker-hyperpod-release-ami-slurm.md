# SageMaker HyperPod AMI releases for

Slurm

The following release notes track the latest updates for Amazon SageMaker HyperPod AMI releases
for Slurm orchestration. These HyperPod AMIs are built upon [AWS Deep Learning Base GPU AMI (Ubuntu 22.04)](https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-22-04/ "https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-22-04/"). The HyperPod
service team distributes software patches through [SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami"). For HyperPod AMI releases
for Amazon EKS orchestration, see [SageMaker HyperPod AMI releases for
Amazon EKS](sagemaker-hyperpod-release-ami-eks.md "sagemaker-hyperpod-release-ami-eks.md"). For
information about Amazon SageMaker HyperPod feature releases, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md "sagemaker-hyperpod-release-notes.md").

###### Note

To update existing HyperPod clusters with the latest DLAMI, see [Update the SageMaker HyperPod platform software of a cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software").

## SageMaker HyperPod AMI releases for Slurm: January 25, 2026

**AMI general updates**

- Released updates for SageMaker HyperPod AMI for Slurm versions 24.11.
- Base DLAMI release note is available [here](../../../dlami/latest/devguide/appendix-ami-release-notes.md#appendix-ami-release-notes-base "../../../dlami/latest/devguide/appendix-ami-release-notes.md#appendix-ami-release-notes-base").

**SageMaker HyperPod DLAMI for Slurm support**

This release includes the following updates:

Slurm v24.11

- Slurm 24.11 (ARM64):
  - Linux Kernel version: 6.8
  - Glibc version: 2.35
  - OpenSSL version: 3.0.2
  - FSx Lustre Client version: 2.15.6-1fsx25
  - Runc version: 1.3.4
  - Containerd version: containerd containerd.io v2.2.1
  - NVIDIA Driver version: 580.126.09
  - CUDA version: 12.6, 12.8, 12.9, 13.0
  - EFA Installer version: 2.3.1amzn3.0
  - Python version: 3.10.12
  - Slurm version: 24.11.0
  - nvme-cli version: 1.16
  - collectd version: 5.12.0.
  - lustre-client version: 2.15.6-1fsx25
  - nvidia-imex version: 580.126.09-1
  - systemd version: 249
  - openssh version: 8.9
  - sudo version: 1.9.9
  - ufw version: 0.36.1
  - gcc version: 11.4.0
  - cmake version: 3.22.1
  - git version: 2.34.1
  - make version: 4.3
  - cloudwatch-agent version: 1.300063.0b1323-1
  - nfs-utils version: 1:2.6.1-1ubuntu1.2
  - iscsi-initiator-utils version: 2.1.5-1ubuntu1.1
  - lvm2 version: 2.03.11
  - ec2-instance-connect version: 1.1.14-0ubuntu1.1
  - rdma-core version: 60.0-1

- Slurm 24.11 (x86_64):
  - Linux Kernel version: 6.8
  - Glibc version: 2.35
  - OpenSSL version: 3.0.2
  - FSx Lustre Client version: 2.15.6-1fsx25
  - Runc version: 1.3.4
  - Containerd version: containerd containerd.io v2.2.1
  - aws Neuronx DKMS version: 2.25.4.0
  - NVIDIA Driver version: 580.126.09
  - CUDA version: 12.6, 12.8, 12.9, 13.0
  - EFA Installer version: 2.3.1amzn2.0
  - Python version: 3.10.12
  - Slurm version: 24.11.0
  - nvme-cli version: 1.16
  - stress version: 1.0.5
  - collectd version: 5.12.0.
  - lustre-client version: 2.15.6-1fsx25
  - systemd version: 249
  - openssh version: 8.9
  - sudo version: 1.9.9
  - ufw version: 0.36.1
  - gcc version: 11.4.0
  - cmake version: 3.22.1
  - make version: 4.3
  - cloudwatch-agent version: 1.300063.0b1323-1
  - nfs-utils version: 1:2.6.1-1ubuntu1.2
  - iscsi-initiator-utils version: 2.1.5-1ubuntu1.1
  - lvm2 version: 2.03.11
  - ec2-instance-connect version: 1.1.14-0ubuntu1.1
  - rdma-core version: 60.0-1

## SageMaker HyperPod AMI releases for Slurm: December 29, 2025

**AMI general updates**

- Released updates for SageMaker HyperPod AMI for Slurm versions 24.11.
- Base DLAMI release note is available [here](../../../dlami/latest/devguide/appendix-ami-release-notes.md#appendix-ami-release-notes-base "../../../dlami/latest/devguide/appendix-ami-release-notes.md#appendix-ami-release-notes-base").

**SageMaker HyperPod DLAMI for Slurm support**

This release includes the following updates:

Slurm v24.11

- Slurm 24.11 (ARM64):
  - Linux Kernel version: 6.8
  - Glibc version: 2.35
  - OpenSSL version: 3.0.2
  - FSx Lustre Client version: 2.15.6-1fsx25
  - Runc version: 1.3.4
  - Containerd version: containerd containerd.io v2.2.1
  - NVIDIA Driver version: 580.105.08
  - CUDA version: 12.6, 12.8, 12.9, 13.0
  - EFA Installer version: 2.3.1amzn3.0
  - Python version: 3.10.12
  - Slurm version: 24.11.0
  - nvme-cli version: 1.16
  - collectd version: 5.12.0.
  - lustre-client version: 2.15.6-1fsx25
  - nvidia-imex version: 580.105.08-1
  - systemd version: 249
  - openssh version: 8.9
  - sudo version: 1.9.9
  - ufw version: 0.36.1
  - gcc version: 11.4.0
  - cmake version: 3.22.1
  - git version: 2.34.1
  - make version: 4.3
  - cloudwatch-agent version: 1.300062.0b1304-1
  - nfs-utils version: 1:2.6.1-1ubuntu1.2
  - iscsi-initiator-utils version: 2.1.5-1ubuntu1.1
  - lvm2 version: 2.03.11
  - ec2-instance-connect version: 1.1.14-0ubuntu1.1
  - rdma-core version: 60.0-1

- Slurm 24.11 (x86_64):
  - Linux Kernel version: 6.8
  - Glibc version: 2.35
  - OpenSSL version: 3.0.2
  - FSx Lustre Client version: 2.15.6-1fsx25
  - Runc version: 1.3.4
  - Containerd version: containerd containerd.io v2.2.1
  - aws Neuronx DKMS version: 2.25.4.0
  - NVIDIA Driver version: 580.105.08
  - CUDA version: 12.6, 12.8, 12.9, 13.0
  - EFA Installer version: 2.3.1amzn2.0
  - Python version: 3.10.12
  - Slurm version: 24.11.0
  - nvme-cli version: 1.16
  - stress version: 1.0.5
  - collectd version: 5.12.0.
  - lustre-client version: 2.15.6-1fsx25
  - systemd version: 249
  - openssh version: 8.9
  - sudo version: 1.9.9
  - ufw version: 0.36.1
  - gcc version: 11.4.0
  - cmake version: 3.22.1
  - make version: 4.3
  - cloudwatch-agent version: 1.300062.0b1304-1
  - nfs-utils version: 1:2.6.1-1ubuntu1.2
  - iscsi-initiator-utils version: 2.1.5-1ubuntu1.1
  - lvm2 version: 2.03.11
  - ec2-instance-connect version: 1.1.14-0ubuntu1.1
  - rdma-core version: 60.0-1

## SageMaker HyperPod AMI releases for Slurm: November 22, 2025

**AMI general updates**

- Released updates for SageMaker HyperPod AMI for Slurm versions 24.11.
- Base DLAMI release note is available [here](../../../dlami/latest/devguide/appendix-ami-release-notes.md#appendix-ami-release-notes-base "../../../dlami/latest/devguide/appendix-ami-release-notes.md#appendix-ami-release-notes-base").

**SageMaker HyperPod DLAMI for Slurm support**

This release includes the following updates:

Slurm (arm64)

- Linux Kernel version: 6.8
- Glibc version: 2.35
- OpenSSL version: 3.0.2
- FSx Lustre Client version: 2.15.6-1fsx21
- Runc version: 1.3.3
- Containerd version: containerd containerd.io v2.1.5
- NVIDIA Driver version: 580.95.05
- CUDA version: 12.6, 12.8, 12.9, 13.0
- EFA Installer version: 2.1.0amzn5.0
- Python version: 3.10.12
- Slurm version: 24.11.0
- nvme-cli version: 1.16
- collectd version: 5.12.0.
- lustre-client version: 2.15.6-1fsx21
- nvidia-imex version: 580.95.05-1
- systemd version: 249
- openssh version: 8.9
- sudo version: 1.9.9
- ufw version: 0.36.1
- gcc version: 11.4.0
- cmake version: 3.22.1
- git version: 2.34.1
- make version: 4.3
- cloudwatch-agent version: 1.300062.0b1304-1
- nfs-utils version: 1:2.6.1-1ubuntu1.2
- iscsi-initiator-utils version: 2.1.5-1ubuntu1.1
- lvm2 version: 2.03.11
- ec2-instance-connect version: 1.1.14-0ubuntu1.1
- rdma-core version: 58.amzn0-1

Slurm (x86_64)

- Linux Kernel version: 6.8
- Glibc version: 2.35
- OpenSSL version: 3.0.2
- FSx Lustre Client version: 2.15.6-1fsx21
- Runc version: 1.3.3
- Containerd version: containerd containerd.io v2.1.5
- aws Neuronx DKMS version: 2.24.7.0
- NVIDIA Driver version: 580.95.05
- CUDA version: 12.6, 12.8, 12.9, 13.0
- EFA Installer version: 2.3.1amzn1.0
- Python version: 3.10.12
- Slurm version: 24.11.0
- nvme-cli version: 1.16
- stress version: 1.0.5
- collectd version: 5.12.0.
- lustre-client version: 2.15.6-1fsx21
- systemd version: 249
- openssh version: 8.9
- sudo version: 1.9.9
- ufw version: 0.36.1
- gcc version: 11.4.0
- cmake version: 3.22.1
- make version: 4.3
- cloudwatch-agent version: 1.300062.0b1304-1
- nfs-utils version: 1:2.6.1-1ubuntu1.2
- iscsi-initiator-utils version: 2.1.5-1ubuntu1.1
- lvm2 version: 2.03.11
- ec2-instance-connect version: 1.1.14-0ubuntu1.1
- rdma-core version: 59.amzn0-1

## SageMaker HyperPod release

notes: November 07, 2025

**The AMI includes the following:**

- Supported AWS service: Amazon EC2
- Operating System: Ubuntu 22.04
- Compute Architecture: ARM64
- Updated packages: NVIDIA Driver: 580.95.05
- CUDA Versions: cuda-12.6, cuda-12.8, cuda-12.9, cuda-13.0
- Security fixes: [Runc Security patch](https://aws.amazon.com/security/security-bulletins/rss/aws-2025-024/ "https://aws.amazon.com/security/security-bulletins/rss/aws-2025-024/")

## SageMaker HyperPod release

notes: September 29, 2025

**The AMI includes the following:**

- Supported AWS service: Amazon EC2
- Operating System: Ubuntu 22.04
- Compute Architecture: ARM64
- Updated packages: NVIDIA Driver: 570.172.08
- Security fixes

## SageMaker HyperPod release

notes: August 12, 2025

**The AMI includes the following:**

- Supported AWS service: Amazon EC2
- Operating System: Ubuntu 22.04
- Compute Architecture: ARM64
- Latest available version is installed for the following packages:
  - Linux Kernel: 6.8
  - FSx Lustre
  - Docker
  - AWS CLI v2 at `/usr/bin/aws`
  - NVIDIA DCGM
  - Nvidia container toolkit:
    - Version command: `nvidia-container-cli
-V`

  - Nvidia-docker2:
    - Version command: `nvidia-docker version`

  - Nvidia-IMEX: v570.172.08-1

- NVIDIA Driver: 570.158.01
- NVIDIA CUDA 12.4, 12.5, 12.6, 12.8 stack:
  - CUDA, NCCL and cuDDN installation directories:
    `/usr/local/cuda-xx.x/`
    - Example: `/usr/local/cuda-12.8/`,
      `/usr/local/cuda-12.8/`

  - Compiled NCCL Version:
    - For CUDA directory of 12.4, compiled NCCL Version
      2.22.3+CUDA12.4
    - For CUDA directory of 12.5, compiled NCCL Version
      2.22.3+CUDA12.5
    - For CUDA directory of 12.6, compiled NCCL Version
      2.24.3+CUDA12.6
    - For CUDA directory of 12.8, compiled NCCL Version
      2.27.5+CUDA12.8

  - Default CUDA: 12.8
    - PATH `/usr/local/cuda` points to CUDA
      12.8
    - Updated below env vars:
      - `LD_LIBRARY_PATH` to have
        `/usr/local/cuda-12.8/lib:/usr/local/cuda-12.8/lib64:/usr/local/cuda-12.8:/usr/local/cuda-12.8/targets/sbsa-linux/lib:/usr/local/cuda-12.8/nvvm/lib64:/usr/local/cuda-12.8/extras/CUPTI/lib64`
      - `PATH` to have
        `/usr/local/cuda-12.8/bin/:/usr/local/cuda-12.8/include/`
      - For any different CUDA version, please update
        `LD_LIBRARY_PATH` accordingly.

- EFA installer: 1.42.0
- Nvidia GDRCopy: 2.5.1
- AWS OFI NCCL plugin comes with EFA installer
  - Paths
    `/opt/amazon/ofi-nccl/lib/aarch64-linux-gnu`
    and `/opt/amazon/ofi-nccl/efa` are added to
    `LD_LIBRARY_PATH`.

- AWS CLI v2 at `/usr/local/bin/aws2` and AWS CLI v1 at
  `/usr/bin/aws`
- EBS volume type: gp3
- Python: `/usr/bin/python3.10`

## SageMaker HyperPod release

notes: May 27, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features and improvements**

- Updated base AMI to `Deep Learning Base OSS Nvidia Driver GPU AMI
(Ubuntu 22.04) 20250523` with the following key components:
  - NVIDIA Driver: 570.133.20
  - CUDA: 12.8 (default), with support for CUDA 12.4-12.6
  - NCCL Version: 2.26.5
  - EFA Installer: 1.40.0
  - AWS OFI NCCL: 1.14.2-aws

- Updated Neuron SDK packages:
  - aws-neuronx-collectives: 2.25.65.0-9858ac9a1 (from
    2.24.59.0-838c7fc8b)
  - aws-neuronx-dkms: 2.21.37.0 (from 2.20.28.0)
  - aws-neuronx-runtime-lib: 2.25.57.0-166c7a468 (from
    2.24.53.0-f239092cc)
  - aws-neuronx-tools: 2.23.9.0 (from 2.22.61.0)

**Important notes**

- NVIDIA Container Toolkit 1.17.4 now has disabled mounting of CUDA
  compatible libraries.
- Updated EFA configuration from 1.37 to 1.38, and EFA now includes the
  AWS OFI NCCL plugin, which is located in the
  `/opt/amazon/ofi-nccl` directory instead of the original
  `/opt/aws-ofi-nccl/` path. (Released on February 18,

2025.

- Kernel version is pinned for stability and driver compatibility.

## SageMaker HyperPod AMI

releases for Slurm: May 13, 2025

Amazon SageMaker HyperPod released an updated AMI that supports Ubuntu 22.04 LTS for Slurm
clusters. AWS regularly updates AMIs to ensure you have access to the most current
software stack. Upgrading to the latest AMI provides enhanced security through
comprehensive package updates, improved performance and stability for your
workloads, and compatibility with new instance types and latest kernel
features.

###### Important

The update from Ubuntu 20.04 LTS to Ubuntu 22.04 LTS introduces changes that
might affect compatibility with software and configurations designed for Ubuntu
20.04.

###### In this release note, you will see:

- [Key updates in
  the Ubuntu 22.04 AMI](#sagemaker-hyperpod-ami-slurm-ubuntu22-updates "#sagemaker-hyperpod-ami-slurm-ubuntu22-updates")
- [Upgrading to the
  Ubuntu 22.04 AMI](#sagemaker-hyperpod-ami-slurm-ubuntu22-upgrade "#sagemaker-hyperpod-ami-slurm-ubuntu22-upgrade")
- [Troubleshooting upgrade failures](#sagemaker-hyperpod-ami-slurm-ubuntu22-troubleshoot "#sagemaker-hyperpod-ami-slurm-ubuntu22-troubleshoot")

### Key updates in

the Ubuntu 22.04 AMI

The following table lists the component versions of the Ubuntu 22.04 AMI
compared to the previous AMI.

Component versions of the Ubuntu 22.04 AMI compared to the previous
AMI| Component | Previous version | Updated version |
| --- | --- | --- |
| **Ubuntu OS** | 20.04 LTS | 22.04 LTS |
| **Slurm** | 24.11 | 24.11 (unchanged) |
| **Python** | 3.8 (default) | 3.10 (default) |
| **Elastic Fabric Adapter (EFA) on<br>Amazon FSx** | Not supported | Supported |
| **Linux kernel** | 5.15 | 6.8 |
| **GNU C Library<br>(glibc)** | 2.31 | 2.35 |
| **GNU Compiler Collection<br>(GCC)** | 9.4.0 | 11.4.0 |
| **libc6** | ≤ 2.31 | ≥ 2.35 supported |
| **Network File System<br>(NFS)** | 1:1.3.4 | 1:2.6.1 |

###### Note

Although the Slurm version (24.11) remains unchanged, the underlying OS
and library updates in this AMI may affect your system behavior and workload
compatibility. You must test your workloads before upgrading production
clusters.

### Upgrading to the

Ubuntu 22.04 AMI

Before upgrading your cluster to the Ubuntu 22.04 AMI, complete these
preparation steps and review the upgrade requirements. To troubleshoot upgrade
failures, see [Troubleshooting upgrade failures](#sagemaker-hyperpod-ami-slurm-ubuntu22-troubleshoot "#sagemaker-hyperpod-ami-slurm-ubuntu22-troubleshoot").

#### Review Python compatibility

The Ubuntu 22.04 AMI uses Python 3.10 as the default version, upgraded
from Python 3.8. Although Python 3.10 maintains compatibility with most
Python 3.8 code, you should test your existing workloads before upgrading.
If your workloads require Python 3.8, you can install it using the following
command in your lifecycle script:

```
yum install python-3.8
```

Before upgrading your cluster, make sure to do the following:

1. Test your code compatibility with Python 3.10.
2. Verify your lifecycle scripts work in the new environment.
3. Check that all dependencies are compatible with the new Python
   version.
4. If you created your HyperPod cluster by copying the
   default lifecycle script from GitHub, add the following command to
   your `setup_mariadb_accounting.sh` file before upgrading
   to Ubuntu 22. For the complete script, see [setup_mariadb_accounting.sh on GitHub](https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/setup_mariadb_accounting.sh "https://github.com/aws-samples/awsome-distributed-training/blob/main/1.architectures/5.sagemaker-hyperpod/LifecycleScripts/base-config/setup_mariadb_accounting.sh").

```
apt-get -y -o DPkg::Lock::Timeout=120 update && apt-get -y -o DPkg::Lock::Timeout=120 install apg
```

#### Upgrade your Slurm cluster

You can upgrade your Slurm cluster to use the new AMI in two ways:

1. Create a new cluster using the [`CreateCluster`](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") API.
2. Update an existing cluster's software using the [`UpdateClusterSoftware`](../APIReference/API_UpdateClusterSoftware.md "../APIReference/API_UpdateClusterSoftware.md") API.

#### Validated

configurations

AWS has tested a wide range of distributed training workloads and
infrastructure features on G5, G6, G6e, P4d, P5, and Trn1 instances,
including:

- Distributed training with PyTorch (e.g., FSDP, NeMo, LLaMA,
  MNIST).
- Accelerator testing across instance types with Nvidia (P/G series)
  and AWS Neuron (Trn1).
- Resiliency features that include [auto-resume](sagemaker-hyperpod-resiliency-slurm.md#sagemaker-hyperpod-resiliency-slurm-auto-resume "sagemaker-hyperpod-resiliency-slurm.md#sagemaker-hyperpod-resiliency-slurm-auto-resume") and [deep health checks](sagemaker-hyperpod-eks-resiliency-deep-health-checks.md "sagemaker-hyperpod-eks-resiliency-deep-health-checks.md").

#### Cluster downtime and availability

During the upgrade process, the cluster will be unavailable. To minimize
disruption, do the following:

- Test the upgrade process on smaller clusters.
- Create checkpoints before the upgrade, then restart training
  workloads from existing checkpoints after the upgrade
  completes.

### Troubleshooting upgrade failures

When an upgrade fails, first determine if the failure is related to lifecycle
scripts. These scripts commonly fail due to syntax errors, missing dependencies,
or incorrect configurations.

To investigate failures related to lifecycle scripts, check CloudWatch logs. All
SageMaker HyperPod events and logs are stored under the log group:
`/aws/sagemaker/Clusters/[ClusterName]/[ClusterID]`. Look
specifically at the log stream
`LifecycleConfig/[instance-group-name]/[instance-id]`, which
provides detailed information about any errors during script execution.

If the upgrade failure is unrelated to lifecycle scripts, collect relevant
information including the cluster ARN, error logs, and timestamps, then contact
[AWS support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")
for further assistance.

## SageMaker HyperPod AMI

releases for Slurm: May 07, 2025

Amazon SageMaker HyperPod for Slurm released a major OS version upgrade to Ubuntu 22.04
(from the earlier Ubuntu 20.04). Check DLAMI Ubuntu 22.04 ([release notes](https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-22-04/ "https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-22-04/") ) for more information: `Deep Learning Base OSS
 Nvidia Driver GPU AMI (Ubuntu 22.04) 20250503`.

Key package upgrades:

- Ubuntu 22.04 LTS (from 20.04)
- Python Version:
  - Python 3.10 is now the default Python version in the Slurm AMI
    Ubuntu 22.04
  - This upgrade provide access to the latest features, performance
    improvements and bug fixes introduced in Python 3.10

- Support for EFA on FSx
- New Linux Kernel version 6.8 (updated from 5.15)
- Glibc version: 2.35 (updated from 2.31)
- GCC version: 11.4.0 (updated from 9.4.0)
- Newer libc6 version support (from libc6 version <= 2.31)
- NFS version: 1:2.6.1 (updated from 1:1.3.4)

## SageMaker HyperPod AMI

releases for Slurm: April 28, 2025

**Improvements for Slurm**

- Upgraded NVIDIA driver from version 550.144.03 to 550.163.01. This upgrade
  is to address Common Vulnerabilities and Exposures (CVEs) present in the
  [NVIDIA GPU Display Security Bulletin for April 2025](https://nvidia.custhelp.com/app/answers/detail/a_id/5630 "https://nvidia.custhelp.com/app/answers/detail/a_id/5630").

**Amazon SageMaker HyperPod DLAMI for Slurm support**

Installed the latest version of AWS Neuron SDK

- **aws-neuronx-collectives:**
  2.24.59.0-838c7fc8b
- **aws-neuronx-dkms:**
  2.20.28.0
- **aws-neuronx-runtime-lib:**
  2.24.53.0-f239092cc
- **aws-neuronx-tools/unknown:**
  2.22.61.0

## SageMaker HyperPod AMI

releases for Slurm: February 18, 2025

**Improvements for Slurm**

- Upgraded Slurm version to 24.11.
- Upgraded Elastic Fabric Adapter (EFA) version from 1.37.0 to
  1.38.0.
- The EFA now includes the AWS OFI NCCL plugin. You can find this plugin
  in the `/opt/amazon/ofi-nccl` directory, rather than the original
  `/opt/aws-ofi-nccl/` location. If you need to update your
  `LD_LIBRARY_PATH` environment variable, make sure to modify
  the path to point to the new `/opt/amazon/ofi-nccl` location for
  the OFI NCCL plugin.
- Removed the emacs package from these DLAMIs. You can install emacs from
  GNU emac.

**Amazon SageMaker HyperPod DLAMI for Slurm support**

Installed the latest version of AWS Neuron SDK 2.19

- **aws-neuronx-collectives/unknown:**
  2.23.135.0-3e70920f2 amd64
- **aws-neuronx-dkms/unknown:**
  2.19.64.0 amd64
- **aws-neuronx-runtime-lib/unknown:**
  2.23.112.0-9b5179492 amd64
- **aws-neuronx-tools/unknown:**
  2.20.204.0 amd64

## SageMaker HyperPod AMI

releases for Slurm: December 21, 2024

**SageMaker HyperPod DLAMI for Slurm support**

Deep Learning Slurm AMI

- **NVIDIA driver:**
  550.127.05
- **EFA driver:** 2.13.0-1
- Installed the latest version of AWS Neuron SDK
  - **aws-neuronx-collectives:**
    2.22.33.0
  - **aws-neuronx-dkms:**
    2.18.20.0
  - **aws-neuronx-oci-hook:**
    2.5.8.0
  - **aws-neuronx-runtime-lib:**
    2.22.19.0
  - **aws-neuronx-tools:**
    2.19.0.0

## SageMaker HyperPod AMI

releases for Slurm: November 24, 2024

**AMI general updates**

- Released in `MEL` (Melbourne) Region.
- Updated SageMaker HyperPod base DLAMI to the following versions:
  - Slurm: 2024-11-22.

## SageMaker HyperPod AMI

releases for Slurm: November 15, 2024

**AMI general updates**

- Installed latest `libnvidia-nscq-xxx` package.

**SageMaker HyperPod DLAMI for Slurm support**

Deep Learning Slurm AMI

- **NVIDIA driver:**
  550.127.05
- **EFA driver:** 2.13.0-1
- Installed the latest version of AWS Neuron SDK
  - **aws-neuronx-collectives:**
    v2.22.33.0-d2128d1aa
  - **aws-neuronx-dkms:**
    v2.17.17.0
  - **aws-neuronx-oci-hook:**
    v2.4.4.0
  - **aws-neuronx-runtime-lib:**
    v2.21.41.0
  - **aws-neuronx-tools:**
    v2.18.3.0

## SageMaker HyperPod AMI

releases for Slurm: November 11, 2024

**AMI general updates**

- Updated SageMaker HyperPod base DLAMI to the following version:
  - Slurm: 2024-10-23.

## SageMaker HyperPod AMI

releases for Slurm: October 21, 2024

**AMI general updates**

- Updated SageMaker HyperPod base DLAMI to the following versions:
  - Slurm: 2024-09-27.

## SageMaker HyperPod AMI

releases for Slurm: September 10, 2024

**SageMaker HyperPod DLAMI for Slurm support**

Deep Learning Slurm AMI

- Installed the NVIDIA driver v550.90.07
- Installed the EFA driver v2.10
- Installed the latest version of AWS Neuron SDK
  - **aws-neuronx-collectives:**
    v2.21.46.0
  - **aws-neuronx-dkms:**
    v2.17.17.0
  - **aws-neuronx-oci-hook:**
    v2.4.4.0
  - **aws-neuronx-runtime-lib:**
    v2.21.41.0
  - **aws-neuronx-tools:**
    v2.18.3.0

## SageMaker HyperPod AMI

releases for Slurm: March 14, 2024

**HyperPod DLAMI for Slurm software
patch**

- Upgraded [Slurm](https://slurm.schedmd.com/documentation.html "https://slurm.schedmd.com/documentation.html") to v23.11.1
- Added [OpenPMIx](https://openpmix.github.io/code/getting-the-reference-implementation "https://openpmix.github.io/code/getting-the-reference-implementation") v4.2.6 for enabling [Slurm with
  PMIx](https://slurm.schedmd.com/mpi_guide.html#pmix "https://slurm.schedmd.com/mpi_guide.html#pmix").
- Built upon the [AWS
  Deep Learning Base GPU AMI (Ubuntu 20.04)](https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-20-04/ "https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-20-04/") released on
  2023-10-26
- A complete list of pre-installed packages in this HyperPod DLAMI
  in addition to the base AMI
  - [Slurm](https://slurm.schedmd.com/documentation.html "https://slurm.schedmd.com/documentation.html"): v23.11.1
  - [OpenPMIx](https://openpmix.github.io/code/getting-the-reference-implementation "https://openpmix.github.io/code/getting-the-reference-implementation") : v4.2.6
  - Munge: v0.5.15
  - `aws-neuronx-dkms`: v2.\*
  - `aws-neuronx-collectives`: v2.\*
  - `aws-neuronx-runtime-lib`: v2.\*
  - `aws-neuronx-tools`: v2.\*
  - SageMaker HyperPod software packages to support features such as cluster
    health check and auto-resume

**Upgrade steps**

- Run the following command to call the [UpdateClusterSoftware](../APIReference/API_UpdateClusterSoftware.md "../APIReference/API_UpdateClusterSoftware.md") API to update your existing
  HyperPod clusters with the latest HyperPod DLAMI. To find
  more instructions, see [Update the SageMaker HyperPod platform software of a cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software").

###### Important

Back up your work before running this API. The patching process
replaces the root volume with the updated AMI, which means that your
previous data stored in the instance root volume will be lost. Make sure
that you back up your data from the instance root volume to Amazon S3 or
Amazon FSx for Lustre. For more information, see [Use the backup script provided by SageMaker HyperPod](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software-backup "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software-backup").

```
 `aws sagemaker update-cluster-software --cluster-name `your-cluster-name``
```

###### Note

Note that you should run the AWS CLI command to update your
HyperPod cluster. Updating the HyperPod software
through SageMaker HyperPod console UI is currently not available.

## SageMaker HyperPod AMI

release for Slurm: November 29, 2023

**HyperPod DLAMI for Slurm software
patch**

The HyperPod service team distributes software patches through [SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami"). See the following details about
the latest HyperPod DLAMI.

- Built upon the [AWS Deep Learning Base GPU AMI (Ubuntu 20.04)](https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-20-04/ "https://aws.amazon.com/releasenotes/aws-deep-learning-base-gpu-ami-ubuntu-20-04/") released on
  2023-10-18
- A complete list of pre-installed packages in this HyperPod DLAMI
  in addition to the base AMI
  - [Slurm](https://slurm.schedmd.com/documentation.html "https://slurm.schedmd.com/documentation.html"): v23.02.3
  - Munge: v0.5.15
  - `aws-neuronx-dkms`: v2.\*
  - `aws-neuronx-collectives`: v2.\*
  - `aws-neuronx-runtime-lib`: v2.\*
  - `aws-neuronx-tools`: v2.\*
  - SageMaker HyperPod software packages to support features such as cluster
    health check and auto-resume
