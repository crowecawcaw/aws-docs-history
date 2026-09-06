

# How to upgrade from EKS AL2 to EKS AL2023
<a name="eks-migration-2023"></a>

The Amazon EKS optimized AMIs are available in two families based on Amazon Linux 2 (AL2) and Amazon Linux 2023 (AL2023). AL2023 is a Linux-based operating system designed to provide a secure, stable, and high-performance environment for your cloud applications. For more information about the differences between AL2 and AL2023 see [Upgrade from Amazon Linux 2 to Amazon Linux 2023](https://docs.aws.amazon.com/eks/latest/userguide/al2023.html) in the *Amazon EKS User Guide*.

**Important**  
AWS ended support for Amazon EKS AL2-optimized and AL2-accelerated AMIs on November 26, 2025. AWS Batch Amazon EKS compute environments using Amazon Linux 2 no longer receive software updates, security patches, or bug fixes from AWS. We recommend migrating AWS Batch Amazon EKS compute environments to Amazon Linux 2023 to maintain optimal performance and security. It is your [responsibility to maintain](eks-ce-shared-responsibility.md) these compute environments on the Amazon EKS optimized Amazon Linux 2 AMI after end-of-life.

Depending on how your compute environment is configured you can use one of the following upgrade paths from AL2 to AL2023.

**Upgrade using Ec2Configuration.ImageType**
+ If you are not using a launch template or launch template overrides then change [Ec2Configuration.ImageType](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html#Batch-Type-Ec2Configuration-imageType) to `EKS_AL2023` or `EKS_AL2023_NVIDIA` and then run [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html). 
+ If you specify an [Ec2Configuration.ImageIdOverride](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html#Batch-Type-Ec2Configuration-imageIdOverride) then [Ec2Configuration.ImageType](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html#Batch-Type-Ec2Configuration-imageType) must match the AMI type specified in [Ec2Configuration.ImageIdOverride](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html#Batch-Type-Ec2Configuration-imageIdOverride). 

  If you mismatch `ImageIdOverride` and `ImageType` then the node won't join the cluster. 

**Upgrade using launch templates**
+ If you have any `kubelet` extra arguments defined in a launch template or launch template override, they need to be updated to the new [`kubelet` extra arguments format](eks-launch-templates.md#kubelet-extra-args).

  If you mismatch the `kubelet` extra arguments format then the extra arguments aren't applied.
+ For AL2023 AMIs, **containerd** is the only supported container runtime. You do not need to specify container runtime for `EKS_AL2023` in the launch template.

  You can't specify a customized container runtime with `EKS_AL2023`.
+ If you use a launch template or launch template override that specifies an AMI based on `EKS_AL2023` then you need to set [userdataType](https://docs.aws.amazon.com/batch/latest/APIReference/API_LaunchTemplateSpecification.html) to `EKS_NODEADM`. 

  If you mismatch the `userdataType` and AMI then the node won't join the EKS cluster.