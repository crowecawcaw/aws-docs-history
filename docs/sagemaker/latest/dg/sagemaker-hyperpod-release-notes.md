# Amazon SageMaker HyperPod release notes

This topic covers release notes that track update, fixes, and new features for
Amazon SageMaker HyperPod. If you are looking for general feature releases, updates, and improvements
for Amazon SageMaker HyperPod, you might find this page helpful.

The HyperPod AMI releases are documented separately to include information of the
key components including general AMI releases, versions, and dependencies. If you are
looking for these information related to HyperPod AMI releases, see [Amazon SageMaker HyperPod AMI](sagemaker-hyperpod-release-ami.md "sagemaker-hyperpod-release-ami.md").

## SageMaker HyperPod release notes:

November 07, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features**

- Upgraded security patches
  [SageMaker HyperPod AMI
  releases for Amazon EKS: November 07, 2025](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20251107 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20251107").

## SageMaker HyperPod release notes:

September 29, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features**

- Released the new SageMaker HyperPod AMI for Amazon EKS 1.33. For more information,
  [SageMaker HyperPod AMI
  releases for Amazon EKS: September 29, 2025](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250929 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250929").

###### Important

    + The Dynamic Resource Allocation beta Kubernetes API is enabled by default in this release.




    	- This API improves scheduling and monitoring workloads that require resources such as GPUs.
    	- This API was developed by the open source Kubernetes community and might change in future versions of Kubernetes. Before you use the API,
    	 review the [Kubernetes documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/ "https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/") and understand how it affects your workloads.
    + HyperPod is not releasing a HyperPod Amazon Linux 2 AMI for Kubernetes 1.33. AWS recommends that you
     migrate to AL2023. For more information, see [Upgrade from Amazon Linux 2 to AL2023](../../../eks/latest/userguide/al2023.md "../../../eks/latest/userguide/al2023.md").

For more information, see [Kubernetes v1.33](https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/ "https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/").

## SageMaker HyperPod release notes:

August 4, 2025

SageMaker HyperPod releases new public AMIs for EKS orchestration. Public AMIs can be used
by themselves, or they can be used to create custom AMIs. For more information about
the public AMIs, see [Public AMI releases](sagemaker-hyperpod-release-public-ami.md "sagemaker-hyperpod-release-public-ami.md").
For more information about creating a custom AMI, see [Custom Amazon Machine Images (AMIs) for SageMaker HyperPod
clusters](hyperpod-custom-ami-support.md "hyperpod-custom-ami-support.md").

## SageMaker HyperPod release notes:

July 31, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features and improvements**

- Released a new AMI that updates the operating system from Amazon Linux 2 to
  Amazon Linux 2023 for EKS clusters. Key upgrades include Linux Kernel 6.1, Python
  3.10, NVIDIA Driver 560.35.03, and DNF package manager replacing YUM.

###### Important

The update from Amazon Linux 2 to AL2023 introduces significant changes
that might affect compatibility with software and configurations designed
for AL2. We strongly recommend testing your applications with AL2023 before fully
upgrading your clusters.

For more information about the new AMI and how to upgrade your clusters, see [SageMaker HyperPod AMI
releases for Amazon EKS: July 31, 2025](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250731 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250731").

## SageMaker HyperPod release notes:

May 13, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features and improvements**

- Released an updated AMI that supports Ubuntu 22.04 LTS for Slurm clusters.
  This release includes several system and software component upgrades to provide
  improved performance, updated features, and enhanced security.

###### Important

The update from Ubuntu 20.04 LTS to Ubuntu 22.04 LTS introduces changes
that might affect compatibility with software and configurations designed
for Ubuntu 20.04.

For more information, see:

    + [Key updates in
     the Ubuntu 22.04 AMI](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-ami-slurm-ubuntu22-updates "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-ami-slurm-ubuntu22-updates")
    + [Upgrading to the
     Ubuntu 22.04 AMI](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-ami-slurm-ubuntu22-upgrade "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-ami-slurm-ubuntu22-upgrade")
    + [Troubleshooting upgrade failures](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-ami-slurm-ubuntu22-troubleshoot "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-ami-slurm-ubuntu22-troubleshoot")

## SageMaker HyperPod release notes:

May 1, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features**

- Added usage reporting for EKS-orchestrated clusters, allowing organizations to
  implement transparent, usage-based cost allocation across teams, projects, or
  departments. This feature complements HyperPod’s [Task
  Governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance.md") functionality to ensure fair cost distribution in shared
  multi-tenant AI/ML environments. For more information, see [Reporting Compute Usage in
  HyperPod](sagemaker-hyperpod-usage-reporting.md "sagemaker-hyperpod-usage-reporting.md").

## SageMaker HyperPod release notes:

April 28, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md") and [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features and improvements**

- Upgraded NVIDIA driver from version 550.144.03 to 550.163.01. This upgrade is
  to address Common Vulnerabilities and Exposures (CVEs) present in the [NVIDIA GPU
  Display Security Bulletin for April 2025](https://nvidia.custhelp.com/app/answers/detail/a_id/5630 "https://nvidia.custhelp.com/app/answers/detail/a_id/5630").

For information about related AMI releases, see [SageMaker HyperPod AMI
releases for Slurm: April 28, 2025](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20250428 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20250428") and [SageMaker HyperPod AMI
releases for Amazon EKS: April 28, 2025](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250428 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250428").

## SageMaker HyperPod release notes:

April 18, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features**

- Released new SageMaker HyperPod AMI for Amazon EKS 1.32.1. For more information, see
  [SageMaker HyperPod AMI
  releases for Amazon EKS: April 18, 2025](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250418 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250418").

## SageMaker HyperPod release notes:

April 10, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features and improvements**

- Added a Direct Preference Optimization (DPO) recipe tutorial for SageMaker HyperPod
  with Slurm orchestration. This fine-tuning tutorial provides step-by-step
  guidance for optimizing model alignment using the DPO method on GPU-powered
  SageMaker HyperPod Slurm clusters. For more information, see [HyperPod Slurm cluster DPO
  tutorial (GPU)](hyperpod-gpu-slurm-dpo-tutorial.md "hyperpod-gpu-slurm-dpo-tutorial.md").

## SageMaker HyperPod release notes:

April 03, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md") and [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features and improvements**

- Added a [Quickstart](sagemaker-hyperpod-quickstart.md "sagemaker-hyperpod-quickstart.md") page
  for deploying SageMaker HyperPod clusters. The page leverages streamlined setup
  workflows from SageMaker HyperPod’s specialized workshops and automates deployment
  using prebuilt AWS CloudFormation templates. It supports infrastructure preferences like
  Slurm or Amazon EKS, for easy configuration and deployment of baseline
  clusters.
- SageMaker HyperPod now supports the following instance types for both Slurm and
  Amazon EKS clusters.
  - New instance types: I3en, M7i, R7i instances. For the full list of
    supported instances, see the `InstanceType` field in the
    `ClusterInstanceGroupDetails`.

## SageMaker HyperPod release notes:

March 16, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md") and [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features and improvements**

- Added the following IAM condition keys for more granular access control in
  the [`CreateCluster`](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") and [`UpdateCluster`](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") API operations.

| Condition key                                                                                                                                                                                                                                                                    | Description                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [`sagemaker:InstanceTypes`](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-sagemaker_InstanceTypes "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-sagemaker_InstanceTypes")                   | Control access based on the specified instance types.                   |
| [`sagemaker:VpcSubnets`](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-sagemaker_VpcSubnets "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-sagemaker_VpcSubnets")                            | Restrict cluster creation or updates to specific Amazon VPC<br>subnets. |
| [`sagemaker:VpcSecurityGroupIds`](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-sagemaker_VpcSecurityGroupIds "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-sagemaker_VpcSecurityGroupIds") | Manage access based on Amazon VPC security group IDs.                   |

## SageMaker HyperPod release notes:

February 20, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md") and [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features and improvements**

- Added support for deleting instance groups from your SageMaker HyperPod cluster. For
  more information, see [Delete instance groups](smcluster-scale-down.md#smcluster-remove-instancegroup "smcluster-scale-down.md#smcluster-remove-instancegroup") from
  EKS-orchestrated clusters and [Scale down a
  cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-scale-down "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-scale-down") for
  Slurm-orchestrated clusters.

## SageMaker HyperPod release notes:

February 18, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md") and [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features**

- This release of SageMaker HyperPod incorporates a security update from the Nvidia
  container toolkit (from version 1.17.3 to version 1.17.4). For more information,
  see [v1.17.4 release note](https://github.com/NVIDIA/nvidia-container-toolkit/releases/tag/v1.17.4 "https://github.com/NVIDIA/nvidia-container-toolkit/releases/tag/v1.17.4").

###### Note

For all container workloads in the Nvidia container toolkit version
1.17.4, the mounting of CUDA compatibility libraries is now disabled. To
ensure compatibility with multiple CUDA versions on container workflows,
update your `LD_LIBRARY_PATH` to include your CUDA compatibility
libraries. You can find the specific steps in [If you use a CUDA compatibility layer](inference-gpu-drivers.md#collapsible-cuda-compat "inference-gpu-drivers.md#collapsible-cuda-compat").

For information about related AMI releases, see [SageMaker HyperPod AMI
releases for Slurm: February 18, 2025](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20250218 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20250218") and [SageMaker HyperPod AMI
releases for Amazon EKS: February 18, 2025](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250218 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250218").

## SageMaker HyperPod release notes:

February 06, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md") and [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").

**New features and improvements**

- Enhanced SageMaker HyperPod multi-AZ support: You can specify different subnets and
  security groups, cutting across different Availability Zones, for individual
  instance groups within your cluster. For more information about SageMaker HyperPod
  multi-AZ support, see [Setting
  up SageMaker HyperPod clusters across multiple AZs](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-multiple-availability-zones "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-multiple-availability-zones").

## SageMaker HyperPod release notes:

January 22, 2025

**AMI releases**

- [SageMaker HyperPod AMI
  releases for Amazon EKS: January 22, 2025](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250122 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20250122")

## SageMaker HyperPod release notes:

January 09, 2025

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md") and [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features and improvements**

- Added IPv6 support: Clusters can use IPv6 addressing when configured with
  IPv6-enabled VPC and subnets. For more information, see [Setting up SageMaker HyperPod
  with a custom Amazon VPC](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc").

## SageMaker HyperPod release notes:

December 21, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md") and [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features**

- SageMaker HyperPod now supports the following instance types for both Slurm and
  Amazon EKS clusters.
  - New instance types: C6gn, C6i, M6i, R6i.
  - New Trainium instance types: Trn1 and Trn1n.

**Improvements**

- Enhanced error logging visibility when Slurm interrupts jobs, and prevented
  unnecessary job step termination during Slurm-initiated job
  cancellations.
- Updated base DLAMI for p5en for both Slurm and Amazon EKS clusters.

**AMI releases**

- [SageMaker HyperPod AMI
  releases for Slurm: December 21, 2024](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241221 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241221")
- [SageMaker HyperPod AMI
  releases for Amazon EKS: December 21, 2024](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241221 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241221")

## SageMaker HyperPod release notes:

December 13, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md") and [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New feature**

- SageMaker HyperPod releases a set of Amazon CloudWatch metrics to monitor the health and
  performance of SageMaker HyperPod Slurm clusters. These metrics are related to CPU,
  GPU, memory utilization, and cluster instance information such as node counts
  and failed nodes. This monitoring feature is enabled by default, and the metrics
  can be accessed under the `/aws/sagemaker/Clusters` CloudWatch namespace.
  You can also set up CloudWatch alarms based on these metrics to proactively detect and
  address potential issues within their Slurm-based HyperPod clusters.
  For more information, see [Amazon SageMaker HyperPod Slurm metrics](smcluster-slurm-metrics.md "smcluster-slurm-metrics.md").

**AMI releases**

- [SageMaker HyperPod AMI
  releases for Amazon EKS: December 13, 2024](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241213 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241213")

## SageMaker HyperPod release notes:

November 24, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md") and [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features**

- Added support for configuring SageMaker HyperPod clusters across multiple
  Availability Zones. For more information about SageMaker HyperPod multi-AZ support,
  see [Setting
  up SageMaker HyperPod clusters across multiple AZs](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-multiple-availability-zones "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-multiple-availability-zones").

**AMI releases**

- [SageMaker HyperPod AMI
  releases for Slurm: November 24, 2024](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241124 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241124")
- [SageMaker HyperPod AMI
  releases for Amazon EKS: November 24, 2024](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241124 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241124")

## SageMaker HyperPod release notes:

November 15, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md") and [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md"). For
more information, see and [SageMaker HyperPod AMI
releases for Amazon EKS: November 15, 2024](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241115 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241115").

**New features and improvements**

- Added support for trn1 and trn1n instance types for both Amazon EKS and Slurm
  orchestrated clusters.
- Improved log management for Slurm clusters:
  - Implemented log rotation: weekly or daily based on size.
  - Set log retention to 3 weeks.
  - Compressed logs to reduce storage impact.
  - Continued uploading logs to CloudWatch for long-term retention.

  ###### Note

  Some logs are still stored in syslogs.

- Adjusted Fluent Bit settings to prevent tracking issues with files containing
  long lines.

**Bug fixes**

- Prevented unintended truncation with Slurm controller node updates in
  configuration file `slurm.config`.

**AMI releases**

- [SageMaker HyperPod AMI
  releases for Slurm: November 15, 2024](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241115 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241115")
- [SageMaker HyperPod AMI
  releases for Amazon EKS: November 15, 2024](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241115 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241115")

## SageMaker HyperPod release notes:

November 11, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md") and [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New feature**

- SageMaker HyperPod AMI now supports G6e instance types.

**AMI releases**

- [SageMaker HyperPod AMI
  releases for Slurm: November 11, 2024](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241111 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241111")
- [SageMaker HyperPod AMI
  releases for Amazon EKS: November 11, 2024](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241111 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241111")

## SageMaker HyperPod release notes:

October 31, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md") and [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features**

- Added scaling down SageMaker HyperPod clusters at the instance group level and
  instance level for both Amazon EKS and Slurm orchestrated clusters. For more
  information about scaling down Amazon EKS clusters, see [Scaling down a SageMaker HyperPod cluster](smcluster-scale-down.md "smcluster-scale-down.md"). For
  more information about scaling down Slurm clusters, see _Scale down a cluster_ in [Managing SageMaker HyperPod
  Slurm clusters using the AWS CLI](sagemaker-hyperpod-operate-slurm-cli-command.md "sagemaker-hyperpod-operate-slurm-cli-command.md").
- SageMaker HyperPod now supports the P5e instance type for both Amazon EKS and Slurm
  orchestrated clusters.

## SageMaker HyperPod release notes:

October 21, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md") and [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New feature**

- SageMaker HyperPod now supports the P5e[n], G6, Gr6, and Trn2[n] instance types for
  both Slurm and Amazon EKS clusters.

**AMI releases**

- [SageMaker HyperPod AMI
  releases for Slurm: October 21, 2024](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241021 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20241021")
- [SageMaker HyperPod AMI
  releases for Amazon EKS: October 21, 2024](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241021 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20241021")

## SageMaker HyperPod release notes:

September 10, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md") and [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features**

- Added Amazon EKS support in SageMaker HyperPod. To learn more, see [Orchestrating SageMaker HyperPod clusters with
  Amazon EKS](sagemaker-hyperpod-eks.md "sagemaker-hyperpod-eks.md").
- Added support for managing SageMaker HyperPod clusters through CloudFormation and Terraform.
  For more information about managing HyperPod clusters through CloudFormation,
  see [CloudFormation documentation for
  `AWS::SageMaker::Cluster`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-cluster.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-cluster.md"). To learn about managing
  HyperPod clusters through Terraform, see [Terraform documentation for
  `awscc_sagemaker_cluster`](https://registry.terraform.io/providers/hashicorp/awscc/latest/docs/data-sources/sagemaker_cluster "https://registry.terraform.io/providers/hashicorp/awscc/latest/docs/data-sources/sagemaker_cluster").

**AMI releases**

- [SageMaker HyperPod AMI
  releases for Slurm: September 10, 2024](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20240910 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20240910")
- [SageMaker HyperPod AMI
  releases for Amazon EKS: September 10, 2024](sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20240910 "sagemaker-hyperpod-release-ami-eks.md#sagemaker-hyperpod-release-ami-eks-20240910")

## SageMaker HyperPod release notes:

August 20, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features**

- Enhanced the [SageMaker HyperPod auto-resume functionality](sagemaker-hyperpod-resiliency-slurm.md#sagemaker-hyperpod-resiliency-slurm-auto-resume "sagemaker-hyperpod-resiliency-slurm.md#sagemaker-hyperpod-resiliency-slurm-auto-resume"), extending the resiliency
  capability for Slurm nodes attached with Generic RESources (GRES).

When [Generic Resources
(GRES)](https://slurm.schedmd.com/gres.html "https://slurm.schedmd.com/gres.html") are attached to a Slurm node, Slurm typically doesn't permit
changes in the node allocation, such as replacing nodes, and thus doesn’t allow
to resume a failed job. Unless explicitly forbidden, the HyperPod
auto-resume functionality automatically re-queues any faulty job associated with
the GRES-enabled nodes. This process involves stopping the job, placing it back
into the job queue, and then restarting the job from the beginning.

**Other changes**

- Pre-packaged [`slurmrestd`](https://slurm.schedmd.com/slurmrestd.html "https://slurm.schedmd.com/slurmrestd.html") in the SageMaker HyperPod AMI.
- Changed the default values for `ResumeTimeout` and
  `UnkillableStepTimeout` from 60 seconds to 300 seconds in
  `slurm.conf` to improve system responsiveness and job
  handling.
- Made minor improvements on health checks for NVIDIA Data Center GPU Manager
  (DCGM) and The NVIDIA System Management Interface (nvidia-smi).

**Bug fixes**

- The HyperPod auto-resume plug-in can use idle nodes to resume a
  job.

## SageMaker HyperPod release notes:

June 20, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features**

- Added a new capability of attaching additional storage to SageMaker HyperPod cluster
  instances. With this capability, you can configure supplementary storage at the
  instance group configuration level during the cluster creation or update
  processes, either through the SageMaker HyperPod console or the [`CreateCluster`](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") and [`UpdateCluster`](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") APIs. The additional EBS volume is
  attached to each instance within a SageMaker HyperPod cluster and mounted to
  `/opt/sagemaker`. To learn more about implementing it in your
  SageMaker HyperPod cluster, see the updated documentation on the following
  pages.

      + [Getting started with SageMaker HyperPod](smcluster-getting-started-slurm.md "smcluster-getting-started-slurm.md")
      + [SageMaker HyperPod Slurm cluster operations](sagemaker-hyperpod-operate-slurm.md "sagemaker-hyperpod-operate-slurm.md")

  Note that you need to update the HyperPod cluster software to use this
  capability. After patching the HyperPod cluster software, you can
  utilize this capability for existing SageMaker HyperPod clusters created before June
  20, 2024 by adding new instance groups. This capability is fully effective for
  any SageMaker HyperPod clusters created after June 20, 2024.

**Upgrade steps**

- Run the following command to call the [UpdateClusterSoftware](../APIReference/API_UpdateClusterSoftware.md "../APIReference/API_UpdateClusterSoftware.md") API to update your existing HyperPod
  clusters with the latest HyperPod DLAMI. To find more instructions, see
  [Update the SageMaker HyperPod platform software of a cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software").

###### Important

Back up your work before running this API. The patching process replaces
the root volume with the updated AMI, which means that your previous data
stored in the instance root volume will be lost. Make sure that you back up
your data from the instance root volume to Amazon S3 or Amazon FSx for Lustre. For more
information, see [Use the backup script provided by SageMaker HyperPod](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software-backup "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software-backup").

```
 `aws sagemaker update-cluster-software --cluster-name `your-cluster-name``
```

###### Note

Note that you should run the AWS CLI command to update your
HyperPod cluster. Updating the HyperPod software through
SageMaker HyperPod console UI is currently not available.

## SageMaker HyperPod release notes:

April 24, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**Bug fixes**

- Fixed a bug with the `ThreadsPerCore` parameter in the [`ClusterInstanceGroupSpecification`](../APIReference/API_ClusterInstanceGroupSpecification.md "../APIReference/API_ClusterInstanceGroupSpecification.md") API. With the
  fix, the [`CreateCluster`](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") and [`UpdateCluster`](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") APIs properly take and apply the
  user input through `ThreadsPerCore`. This fix is effective on
  HyperPod clusters created after April 24, 2024. If you had issues with
  this bug and want to get this fix applied to your cluster, you need to create a
  new cluster. Make sure that you back up and restore your work while moving to a
  new cluster following the instructions at [Use the backup script provided by SageMaker HyperPod](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software-backup "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software-backup").

## SageMaker HyperPod release notes:

March 27, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**HyperPod software patch**

The HyperPod service team distributes software patches through [SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami"). See the following details about the
latest HyperPod DLAMI.

- In this release of the HyperPod DLAMI, Slurm is built with REST
  service (`slurmestd`) with JSON, YAML, and JWT support.
- Upgraded [Slurm](https://slurm.schedmd.com/documentation.html "https://slurm.schedmd.com/documentation.html") to v23.11.3.

**Improvements**

- Increased auto-resume service timeout to 60 minutes.
- Improved instance replacement process to not restart the Slurm
  controller.
- Improved error messages from running lifecycle scripts, such as download
  errors and instance health check errors on instance start-up.

**Bug fixes**

- Fixed a bug with chrony service that caused an issue with time
  synchronization.
- Fixed a bug with parsing `slurm.conf`.
- Fixed an issue with [NVIDIA
  `go-dcgm`](https://github.com/NVIDIA/go-dcgm "https://github.com/NVIDIA/go-dcgm") library.

## SageMaker HyperPod release notes:

March 14, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**Improvements**

- HyperPod now properly supports passing partition names provided
  through `provisioning_parameters.json` and creates partitions
  appropriately based on provided inputs. For more information about
  `provisioning_parameters.json`, see [Legacy configuration: provisioning_parameters.json](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-provisioning-forms "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-provisioning-forms") and [Customizing SageMaker HyperPod
  clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md").

**AMI releases**

- [SageMaker HyperPod AMI
  releases for Slurm: March 14, 2024](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20240314 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20240314")

## SageMaker HyperPod release notes:

February 15, 2024

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features**

- Added a new `UpdateClusterSoftware` API for SageMaker HyperPod security
  patching. When security patches become available, we recommend you to update
  existing SageMaker HyperPod clusters in your account by running `aws sagemaker
update-cluster-software --cluster-name
`your-cluster-name``. To follow up with
future security patches, keep tracking this Amazon SageMaker HyperPod release notes page.
To learn how the `UpdateClusterSoftware` API works, see [Update the SageMaker HyperPod platform software of a cluster](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-update-cluster-software").

## SageMaker HyperPod release notes:

November 29, 2023

SageMaker HyperPod releases the following for [Orchestrating SageMaker HyperPod clusters with
Slurm](sagemaker-hyperpod-slurm.md "sagemaker-hyperpod-slurm.md").

**New features**

- Launched Amazon SageMaker HyperPod at AWS re:Invent 2023.

**AMI releases**

- [SageMaker HyperPod AMI
  release for Slurm: November 29, 2023](sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20231129 "sagemaker-hyperpod-release-ami-slurm.md#sagemaker-hyperpod-release-ami-slurm-20231129")
