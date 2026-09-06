

# Amazon EKS default AMI
<a name="eks-ce-ami-selection"></a>

When you create an Amazon EKS compute environment, you don't need to specify an Amazon Machine Image (AMI). AWS Batch selects an Amazon EKS optimized AMI based on the Kubernetes version and instance types that are specified in your [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) request. In general, we recommend that you use the default AMI selection. For information about AMI selection precedence, see [AMI selection order](ami-selection-order.md). For more information about Amazon EKS optimized AMIs, see [Amazon EKS optimized Amazon Linux AMIs](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html) in the *Amazon EKS User Guide*.

**Important**  
Amazon Linux 2023 AMIs are the default on AWS Batch for Amazon EKS.  
AWS will end support for Amazon EKS AL2-optimized and AL2-accelerated AMIs, starting 11/26/25. You can continue using AWS Batch-provided Amazon EKS optimized Amazon Linux 2 AMIs on your Amazon EKS compute environments beyond the 11/26/25 end-of-support date, however these compute environments will no longer receive any new software updates, security patches, or bug fixes from AWS. For more information on upgrading from AL2 to AL2023, see [How to upgrade from EKS AL2 to EKS AL2023](eks-migration-2023.md) in the *AWS Batch User Guide*.

Run the following command to see which AMI type AWS Batch selected for your Amazon EKS compute environment. The following example is a non-GPU instance type.

```
# compute CE example: indicates Batch has chosen the AL2023 x86 or ARM EKS 1.36 AMI, depending on instance types
    $ aws batch describe-compute-environments --compute-environments {{My-Eks-CE1}} \
        | jq '.computeEnvironments[].computeResources.ec2Configuration'
    [
      {
        "imageType": "EKS_AL2023",
        "imageKubernetesVersion": "1.36"
      }
    ]
```

The following example is a GPU instance type.

```
# GPU CE example: indicates Batch has chosen the AL2023 x86 EKS Accelerated 1.36 AMI
    $ aws batch describe-compute-environments --compute-environments {{My-Eks-GPU-CE}} \
        | jq '.computeEnvironments[].computeResources.ec2Configuration'
    [
      {
        "imageType": "EKS_AL2023_NVIDIA",
        "imageKubernetesVersion": "1.36"
      }
    ]
```