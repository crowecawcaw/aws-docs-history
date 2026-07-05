# Amazon SageMaker HyperPod AMI support policy

Amazon SageMaker HyperPod provides pre-built Amazon Machine Images (AMIs) optimized for distributed
training and inference workloads. This page details the support policy for HyperPod
AMI releases.

## Scope

This support policy applies to the following HyperPod AMI components:

- EFA (Elastic Fabric Adapter)
- NVIDIA Driver
- NCCL (aws-ofi-nccl)
- CUDA
- OS Kernel

The policy defines the window during which HyperPod will ship security
patches for a given AMI version.

## Support policy

The following table outlines the release schedule for HyperPod AMI versions
and their planned support timelines. AWS provides ongoing security patches for
supported AMI versions. In some cases, an AMI version may need to be designated end of
support earlier than originally planned if:

1. security issues cannot be addressed while maintaining semantic versioning
   guidelines,
2. any of the core dependencies (for example, NVIDIA driver, CUDA, OS kernel)
   reach end-of-life, or
3. upstream vendors discontinue support for a bundled component.

| Version   | Description                                                                                                                                                                                                                                                                                                                                                                                    | Support window                        |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Major** | HyperPod AMI major version releases involve upgrading core<br>components (EFA, NVIDIA driver, NCCL, CUDA, OS kernel) to new major<br>versions. These releases may introduce breaking changes, such as<br>NVIDIA driver changes from 570.x to 580.x, that require workload<br>validation. Major versions are denoted by the first number in the<br>version string (for example, 1.0, 2.0, 3.0). | 12 months                             |
| **Minor** | HyperPod AMI minor version releases include upgrading core<br>components to newer compatible minor versions within the same major<br>version. Minor versions are denoted by the second number in the<br>version string (for example, 1.1, 1.2, 2.1).                                                                                                                                           | 6 months                              |
| **Patch** | HyperPod AMI patch version releases include security fixes<br>and bug fixes for the supported components. Patch releases do not<br>change the major or minor versions of any bundled component. Patch<br>versions are denoted by the third number in the version string (for<br>example, 1.1.1, 1.2.1, 2.1.3).                                                                                 | Until a new patch version is released |

## Vulnerability management

AWS continuously monitors supported HyperPod AMI versions for security
vulnerabilities affecting the in-scope components (EFA, NVIDIA driver, NCCL, CUDA, OS
kernel). When vulnerabilities are detected and a fix is available that satisfies the
semantic versioning constraints for the given AMI version, AWS will release a patch
update to remediate the issue.

## HyperPod EKS

HyperPod EKS AMIs are versioned independently of the Kubernetes version
they ship with. A given AMI version (for example, 1.1.2) is built for each supported
Kubernetes minor version (for example, 1.33, 1.34, 1.35), with identical core component
versions across the Kubernetes lines.

### Major versions support policy

| AMI version | Supported until |
| ----------- | --------------- |
| 1.x.x       | January 2027    |

### AMI version list

The following table lists the supported HyperPod EKS AMI versions, the
Kubernetes minor versions they ship with, and their planned end of support dates.
When creating or updating clusters, we recommend that you choose supported AMI
versions from the table below. The **Supported package
versions** column lists the in-scope components covered by this support
policy; for the full list of bundled packages in each release, see the
Amazon SageMaker HyperPod AMI release notes for Amazon EKS in [SageMaker HyperPod AMI releases for Amazon EKS](sagemaker-hyperpod-release-ami-eks.md "sagemaker-hyperpod-release-ami-eks.md").

| AMI version | Latest patch | Supported EKS versions             | Supported package versions                                                                           | First released   |
| ----------- | ------------ | ---------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------- |
| 1.3.x       | 1.3.0        | 1.30, 1.31, 1.32, 1.33, 1.34, 1.35 | • NVIDIA Driver: 580.167.08<br>• CUDA Toolkit: 12.8<br>• EFA Installer: 1.47.0<br>• OS Kernel: 6.1.x | June 29, 2026    |
| 1.2.x       | 1.2.0        | 1.30, 1.31, 1.32, 1.33, 1.34, 1.35 | • NVIDIA Driver: 580.159.04<br>• CUDA Toolkit: 12.8<br>• EFA Installer: 1.47.0<br>• OS Kernel: 6.1.x | June 26, 2026    |
| 1.1.x       | 1.1.6        | 1.30, 1.31, 1.32, 1.33, 1.34, 1.35 | • NVIDIA Driver: 580.126.09<br>• CUDA Toolkit: 12.8<br>• EFA Installer: 1.47.0<br>• OS Kernel: 6.1.x | April 23, 2026   |
| 1.0.x       | 1.0.3        | 1.30, 1.31, 1.32, 1.33, 1.34       | • NVIDIA Driver: 580.150<br>• CUDA Toolkit: 12.8<br>• EFA Installer: 1.47.0<br>• OS Kernel: 6.1.x    | January 25, 2026 |

## Frequently asked questions

**Can I still use an older AMI after it is no longer
supported?**

Older AMIs remain available on existing HyperPod clusters after they reach
end of support. However, you cannot create a new cluster using an end-of-support AMI. We
strongly recommend upgrading to a supported AMI version, which continues to receive
security patches. Customers are responsible for managing any vulnerabilities that may
arise from running an AMI version no longer supported by AWS.

**What happens when a new patch version is
released?**

When a new patch version is released, the previous patch version within the same minor
version reaches end of support. If auto-patching is enabled, patch updates will be
applied automatically without disrupting running workloads.

**How will I be notified about new AMI versions or end-of-support
dates?**

AWS will notify customers through Personal Health Dashboard (PHD) notifications and
the HyperPod console when AMI updates are available or when their current AMI
version is approaching end of support.

**Does this policy apply to custom AMIs?**

No. This support policy applies only to AWS-vended HyperPod AMIs. If you use
a custom AMI, you are responsible for maintaining and patching all components. For more
information about custom AMIs, see [Custom Amazon Machine Images (AMIs) for SageMaker HyperPod clusters](hyperpod-custom-ami-support.md "hyperpod-custom-ami-support.md").
