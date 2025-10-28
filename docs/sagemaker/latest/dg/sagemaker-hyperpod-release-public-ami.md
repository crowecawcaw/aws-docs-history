# Public AMI releases

The following release notes track the latest updates for Amazon SageMaker HyperPod public AMI
releases for Amazon EKS orchestration. Each release note includes a summarized list of
packages pre-installed or pre-configured in the SageMaker HyperPod DLAMIs for Amazon EKS support.
Each DLAMI is built on AL2023 and supports a specific Kubernetes version. For
information about Amazon SageMaker HyperPod feature releases, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md "sagemaker-hyperpod-release-notes.md").

This page is regularly updated to provide comprehensive AMI lifecycle management
information including security vulnerabilities, deprecation announcements, and patching
recommendations. As part of a commitment to maintaining secure and up-to-date
infrastructure, SageMaker AI continuously monitors all HyperPod public AMIs for
critical vulnerabilities using automated scanning workflows. When critical security
issues are identified, AMIs are systematically deprecated with appropriate migration
guidance. Regular updates include Common Vulnerabilites and Exposures (CVE) remediation
status, compliance findings, and recommended actions to ensure that you can maintain
secure HyperPod environments while minimizing operational disruption during AMI
transitions.

## SageMaker HyperPod

public AMI releases: August 04, 2025

Amazon SageMaker HyperPod now supports new public AMIs for Amazon EKS clusters. The AMIs include
the following:

K8s v1.32
AMI Name: HyperPod EKS 1.32 x86_64 AMI Amazon Linux 2
2025080407

- **Amazon EKS Components**
  - Kubernetes Version: 1.32.3
  - Containerd Version: 1.7.23
  - Runc Version: 1.2.6
  - AWS IAM Authenticator: 0.6.29

- **Amazon SSM Agent:**
  3.3.2299.0
- **Linux Kernel:**
  5.10.238-234.956.amzn2.x86_64
- **OSS NVIDIA driver:**
  550.163.01
- **NVIDIA CUDA:** 12.2
- **EFA Installer:** 1.38.0
- **GDRCopy:** 2.4.1
- **NVIDIA container toolkit:**
  1.17.8
- **AWS OFI NCCL:**
  1.13.0-aws
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
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.17.1.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.17.0.0_aacc27699-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-tools.x86_64:**
    2.25.145.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0

K8s v1.30
AMI Name: HyperPod EKS 1.30 x86_64 AMI Amazon Linux 2
2025080407

- **Amazon EKS Components**
  - Kubernetes Version: 1.30.11
  - Containerd Version: 1.7.\*
  - Runc Version: 1.2.6
  - AWS IAM Authenticator: 0.6.28

- **Amazon SSM Agent:**
  3.3.2299.0
- **Linux Kernel:**
  5.10.238-234.956.amzn2.x86_64
- **OSS NVIDIA driver:**
  550.163.01
- **NVIDIA CUDA:** 12.2
- **EFA Installer:** 1.38.0
- **GDRCopy:** 2.4.1
- **NVIDIA container toolkit:**
  1.17.8
- **AWS OFI NCCL:**
  1.13.0-aws
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
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.17.1.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.17.0.0_aacc27699-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-tools.x86_64:**
    2.25.145.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0

K8s v1.31
AMI Name: HyperPod EKS 1.31 x86_64 AMI Amazon Linux 2
2025080407

- **Amazon EKS Components**
  - Kubernetes Version: 1.31.7
  - Containerd Version: 1.7.\*
  - Runc Version: 1.2.6
  - AWS IAM Authenticator: 0.6.28

- **Amazon SSM Agent:**
  3.3.2299.0
- **Linux Kernel:**
  5.10.238-234.956.amzn2.x86_64
- **OSS NVIDIA driver:**
  550.163.01
- **NVIDIA CUDA:** 12.2
- **EFA Installer:** 1.38.0
- **GDRCopy:** 2.4.1
- **NVIDIA container toolkit:**
  1.17.8
- **AWS OFI NCCL:**
  1.13.0-aws
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
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.17.1.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.17.0.0_aacc27699-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-tools.x86_64:**
    2.25.145.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0

K8s v1.29
AMI Name: HyperPod EKS 1.29 x86_64 AMI Amazon Linux 2
2025080407

- **Amazon EKS Components**
  - Kubernetes Version: 1.29.15
  - Containerd Version: 1.7.\*
  - Runc Version: 1.2.6
  - AWS IAM Authenticator: 0.6.28

- **Amazon SSM Agent:**
  3.3.2299.0
- **Linux Kernel:**
  5.10.238-234.956.amzn2.x86_64
- **OSS NVIDIA driver:**
  550.163.01
- **NVIDIA CUDA:** 12.2
- **EFA Installer:** 1.38.0
- **GDRCopy:** 2.4.1
- **NVIDIA container toolkit:**
  1.17.8
- **AWS OFI NCCL:**
  1.13.0-aws
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
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.17.1.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.17.0.0_aacc27699-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-tools.x86_64:**
    2.25.145.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0

K8s v1.28
AMI Name: HyperPod EKS 1.28 x86_64 AMI Amazon Linux 2
2025080407

- **Amazon EKS Components**
  - Kubernetes Version: 1.28.15
  - Containerd Version: 1.7.\*
  - Runc Version: 1.2.6
  - AWS IAM Authenticator: 0.6.28

- **Amazon SSM Agent:**
  3.3.2299.0
- **Linux Kernel:**
  5.10.238-234.956.amzn2.x86_64
- **OSS NVIDIA driver:**
  550.163.01
- **NVIDIA CUDA:** 12.2
- **EFA Installer:** 1.38.0
- **GDRCopy:** 2.4.1
- **NVIDIA container toolkit:**
  1.17.8
- **AWS OFI NCCL:**
  1.13.0-aws
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
    2.27.34.0_ec8cd5e8b-1
  - **aws-neuronx-gpsimd-customop.x86_64:**
    0.2.3.0-1
  - **aws-neuronx-gpsimd-customop-lib.x86_64:**
    0.17.1.0-1
  - **aws-neuronx-gpsimd-tools.x86_64:**
    0.17.0.0_aacc27699-1
  - **aws-neuronx-k8-plugin.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-k8-scheduler.x86_64:**
    2.27.7.0-1
  - **aws-neuronx-runtime-lib.x86_64:**
    2.27.23.0_8deec4dbf-1
  - **aws-neuronx-tools.x86_64:**
    2.25.145.0-1
  - **tensorflow-model-server-neuron.x86_64:**
    2.8.0.2.3.0.0-0
  - **tensorflow-model-server-neuronx.x86_64:**
    2.10.1.2.12.2.0-0
