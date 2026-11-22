

# Increasing pods per node with dynamic ENI attachment

SageMaker HyperPod clusters orchestrated by Amazon EKS can run more pods per node, up to the maximum for the instance type listed in the table in [Getting started with Amazon EKS support in SageMaker HyperPod](sagemaker-hyperpod-eks-prerequisites.md). The Amazon VPC CNI attaches more elastic network interfaces (ENIs) to a node as it needs them. It calls the [AttachClusterNodeNetworkInterface](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AttachClusterNodeNetworkInterface.html) API, up to the limit for the instance type. This feature is available only for clusters orchestrated by Amazon EKS.

## How pod density is calculated
<a name="sagemaker-hyperpod-eks-dynamic-eni-attachment-density"></a>

The maximum number of pods a node can run depends on the number of ENIs it can attach and the number of IPv4 addresses each ENI supports. The Amazon VPC CNI uses the following formula:

```
maxPods = (number of ENIs × (IPv4 addresses per ENI − 1)) + 2
```

The formula subtracts one address per ENI, which is reserved and not used for pods, and adds two for the pods that use host networking.

**Note**  
The maximum is also capped at the Amazon EKS per-node limit: 110 pods for instance types with 30 or fewer vCPUs, and 250 pods for instance types with more than 30 vCPUs. This ceiling, not the number of IP addresses, determines the maximum for larger instance types, so their value is lower than the formula alone would produce.

For the maximum number of pods for each instance type, see the table in [Getting started with Amazon EKS support in SageMaker HyperPod](sagemaker-hyperpod-eks-prerequisites.md).

## Prerequisites
<a name="sagemaker-hyperpod-eks-dynamic-eni-attachment-prerequisites"></a>

Before you enable dynamic ENI attachment, make sure that your environment meets the following requirements:
+ Your SageMaker HyperPod cluster is orchestrated by Amazon EKS.
+ Your nodes run the updated SageMaker HyperPod AMI. The updated AMI sets `maxPods` automatically. Nodes that are not updated keep the previous one-ENI limit.
+ Your Amazon VPC CNI add-on is version `v1.23.3-eksbuild.1` or later.
+ The instance group execution role has the `sagemaker:AttachClusterNodeNetworkInterface`, `ec2:AttachNetworkInterface`, and `ec2:CreateNetworkInterfacePermission` permissions. For the full policy, see [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod).

## Enable dynamic ENI attachment
<a name="sagemaker-hyperpod-eks-dynamic-eni-attachment-enable"></a>

To enable dynamic ENI attachment, update your instance group execution role, update your cluster software, and update your Amazon VPC CNI add-on.

**To enable dynamic ENI attachment**

1. Make sure that the instance group execution role has the `sagemaker:AttachClusterNodeNetworkInterface`, `ec2:AttachNetworkInterface`, and `ec2:CreateNetworkInterfacePermission` permissions. For the full policy, see [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod).

1. Update your cluster software to the latest AMI, or create a new cluster. For more information, see [Updating the SageMaker HyperPod platform software](sagemaker-hyperpod-eks-operate-cli-command-update-cluster-software.md).

   ```
   aws sagemaker update-cluster-software --cluster-name {{my-cluster}}
   ```

1. Update the Amazon VPC CNI add-on to version `v1.23.3-eksbuild.1` or later.

   ```
   aws eks update-addon --cluster-name {{my-eks-cluster}} --addon-name vpc-cni --addon-version v1.23.3-eksbuild.1 --resolve-conflicts PRESERVE
   ```

## Considerations and limitations
<a name="sagemaker-hyperpod-eks-dynamic-eni-attachment-considerations"></a>

Review the following considerations and limitations before you use dynamic ENI attachment:
+ Dynamic ENI attachment is not supported for nodes in a restricted instance group (RIG).
+ Dynamic ENI attachment is not supported for Slurm-orchestrated clusters.
+ Elastic Fabric Adapter (EFA) ENIs are not supported. The network interface must be a standard, non-EFA ENI.
+ The ENI must be in your account and in the same Amazon VPC and Availability Zone as the node.
+ ENIs attached with the `AttachClusterNodeNetworkInterface` API are customer-managed. To detach an ENI, use the Amazon EC2 [DetachNetworkInterface](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachNetworkInterface.html) API with the `AttachmentId`.
+ Instances with many EFA network cards, such as ml.p5.48xlarge, ml.p6 types, and ml.trn2 types, use many subnet IP addresses. Size your subnets for the expected pod density.
+ As pod count grows, dynamic ENI attachment uses more ENIs, which count against the **Network interfaces per Region** quota. For more information about this quota, see [Setting up SageMaker HyperPod with a custom Amazon VPC](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc).

## Availability
<a name="sagemaker-hyperpod-eks-dynamic-eni-attachment-availability"></a>

Dynamic ENI attachment is available in all AWS Regions where SageMaker HyperPod is supported. There is no additional charge for this feature.