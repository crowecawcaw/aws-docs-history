# Amazon EKS default AMI

When you create an Amazon EKS compute environment, you don't need to specify an Amazon Machine
Image (AMI). AWS Batch selects an Amazon EKS optimized AMI based on the Kubernetes version and instance
types that are specified in your [CreateComputeEnvironment](../APIReference/API_CreateComputeEnvironment.md "../APIReference/API_CreateComputeEnvironment.md") request. In general, we recommend that you use the
default AMI selection. For more information about Amazon EKS optimized AMIs, see [Amazon EKS optimized
Amazon Linux AMIs](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md") in the _Amazon EKS User Guide_.

###### Important

Starting end of October 2025 Amazon EKS optimized Amazon Linux 2023 AMIs will be the
default on AWS Batch for EKS versions prior to 1.33. Starting from Kubernetes version 1.33,
EKS optimized Amazon Linux 2023 AMIs will be the default when it becomes supported on
AWS Batch.

AWS will end support for Amazon EKS AL2-optimized and AL2-accelerated AMIs, starting
11/26/25. You can continue using AWS Batch-provided Amazon EKS optimized Amazon Linux 2 AMIs on
your Amazon EKS compute environments beyond the 11/26/25 end-of-support date, however these
compute environments will no longer receive any new software updates, security patches,
or bug fixes from AWS. For more information on upgrading from AL2 to AL2023, see
[How to upgrade from EKS AL2 to EKS AL2023](eks-migration-2023.md "eks-migration-2023.md") in the
_AWS Batch User Guide_.

Run the following command to see which AMI type AWS Batch selected for your Amazon EKS compute
environment. This following example is a non-GPU instance type.

```
`# compute CE example: indicates Batch has chosen the AL2 x86 or ARM EKS 1.32 AMI, depending on instance types`
    `$` `aws batch describe-compute-environments --compute-environments `My-Eks-CE1` \
 | jq '.computeEnvironments[].computeResources.ec2Configuration'`
    `[
 {
 "imageType": "EKS_AL2",
 "imageKubernetesVersion": "1.32"
 }
 ]`
```

This following example is a GPU instance type.

```
`# GPU CE example: indicates Batch has choosen the AL2 x86 EKS Accelerated 1.32 AMI`
    `$` `aws batch describe-compute-environments --compute-environments `My-Eks-GPU-CE` \
 | jq '.computeEnvironments[].computeResources.ec2Configuration'`
    `[
 {
 "imageType": "EKS_AL2_NVIDIA",
 "imageKubernetesVersion": "1.32"
 }
 ]`
```
