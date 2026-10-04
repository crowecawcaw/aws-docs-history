

# `INVALID` compute environment
<a name="batch_eks_invalid_compute_environment"></a>

It's possible that you might have incorrectly configured a managed compute environment. If you did, the compute environment enters an `INVALID` state and can't accept jobs for placement. The following sections describe the possible causes and how to troubleshoot based on the cause.

## Unsupported Kubernetes version
<a name="invalid_kubernetes_version"></a>

You might see an error message that resembles the following when you use the `CreateComputeEnvironment` API operation or `UpdateComputeEnvironment`API operation to create or update a compute environment. This issue occurs if you specify an unsupported Kubernetes version in `EC2Configuration`.

```
At least one imageKubernetesVersion in EC2Configuration is not supported.
```

To resolve this issue, delete the compute environment and then re-create it with a supported Kubernetes version. 

You can perform a minor version upgrade on your Amazon EKS cluster. For example, you can upgrade the cluster from `1.xx` to `1.yy` even if the minor version isn't supported. 

However, the compute environment status might change to `INVALID` after a major version update. For example, if you perform a major version upgrade from `1.xx` to `2.yy`. If the major version isn't supported by AWS Batch, you see an error message that resembles the following.

```
reason=CLIENT_ERROR - ... EKS Cluster version [{{2.yy}}] is unsupported
```

To resolve this issue, specify a supported Kubernetes version when you use an API operation to create or update a compute environment.

AWS Batch on Amazon EKS currently supports the following Kubernetes versions:
+ `1.36`
+ `1.35`
+ `1.34`
+ `1.33`
+ `1.32`
+ `1.31`
+ `1.30`

## Instance profile doesn't exist
<a name="instance_profile_not_exist"></a>

If the specified instance profile does not exist, the AWS Batch on Amazon EKS compute environment status is changed to `INVALID`. You see an error set in the `statusReason` parameter that resembles the following.

```
CLIENT_ERROR - Instance profile arn:aws:iam::...:instance-profile/{{<name>}} does not exist
```

To resolve this issue, specify or create a working instance profile. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) in the *Amazon EKS User Guide*.

## Invalid Kubernetes namespace
<a name="invalid_kubernetes_namespace"></a>

If AWS Batch on Amazon EKS can't validate the namespace for the compute environment, the compute environment status is changed to `INVALID`. For example, this issue can occur if the namespace doesn't exist. 

You see an error message set in the `statusReason` parameter that resembles the following.

```
CLIENT_ERROR - Unable to validate Kubernetes Namespace
```

This issue can occur if any of the following are true:
+ The Kubernetes namespace string in the `CreateComputeEnvironment` call doesn't exist. For more information, see [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html).
+ The required Role-Based Access Control (RBAC) permissions to manage the namespace are not configured correctly.
+ AWS Batch doesn't have access to the Amazon EKS Kubernetes API server endpoint. 

To resolve this issue, see [Verify that the `aws-auth ConfigMap` is configured correctly](verify-configmap-config.md). For more information, see [Getting started with AWS Batch on Amazon EKS](getting-started-eks.md).

## Amazon EKS access entry setup is incomplete
<a name="batch_eks_access_entry_incomplete"></a>

If AWS Batch created an Amazon EKS access entry on the cluster but couldn't finish associating the access policy that makes it usable, the compute environment status changes to `INVALID`. To resolve this issue, grant the missing Amazon EKS permissions and retry the operation.

The `statusReason` parameter contains an error message that resembles the following.

```
CLIENT_ERROR - Access Entry setup incomplete on cluster [{{my-cluster}}]. Retry by calling UpdateComputeEnvironment.
```

This state can occur if AWS Batch couldn't associate the access policy with the new access entry. AWS Batch then couldn't delete the access entry to roll back. The usual cause is that the IAM identity that called `CreateComputeEnvironment` or `UpdateComputeEnvironment` isn't allowed to call `eks:AssociateAccessPolicy`, `eks:DeleteAccessEntry`, or both. If only the policy association fails, AWS Batch removes the access entry and the request fails with an error instead of leaving the compute environment `INVALID`.

Verify that your IAM identity that calls `CreateComputeEnvironment` and `UpdateComputeEnvironment` is allowed to call all of the Amazon EKS actions that AWS Batch uses to manage an access entry. The first two actions read cluster state, and the remaining actions manage the access entry itself.
+ `eks:DescribeCluster`
+ `eks:DescribeAccessEntry`
+ `eks:CreateAccessEntry`
+ `eks:AssociateAccessPolicy`
+ `eks:DeleteAccessEntry`

After you update the identity's permissions, call `UpdateComputeEnvironment` on the compute environment to retry the operation. For more information about the permissions that AWS Batch needs, see [Required permissions](eks-access-entries.md#eks-access-entries-permissions).

## Deleted compute environment
<a name="deleted_compute_environment"></a>

Suppose that you delete an Amazon EKS cluster before you delete the attached AWS Batch on Amazon EKS compute environment. Then, the compute environment status is changed to `INVALID`. In this scenario, the compute environment doesn't work properly if you re-create the Amazon EKS cluster with the same name.

To resolve this issue, delete and then re-create the AWS Batch on Amazon EKS compute environment.

## Nodes don't join the Amazon EKS cluster
<a name="batch_eks_node_not_join_cluster"></a>

AWS Batch on Amazon EKS scales down a compute environment if it determines that not all nodes joined the Amazon EKS cluster. When AWS Batch on Amazon EKS scales down the compute environment, the compute environment status is changed to `INVALID`.

**Note**  
AWS Batch doesn't change the compute environment status immediately so that you can debug the issue.

You see an error message set in the `statusReason` parameter that resembles ones of the following:

`Your compute environment has been INVALIDATED and scaled down because none of the instances joined the underlying ECS Cluster. Common issues preventing instances joining are the following: VPC/Subnet configuration preventing communication to ECS, incorrect Instance Profile policy preventing authorization to ECS, or customized AMI or LaunchTemplate configurations affecting ECS agent.`

`Your compute environment has been INVALIDATED and scaled down because none of the nodes joined the underlying Amazon EKS Cluster. Common issues preventing nodes joining are the following: networking configuration preventing communication to Amazon EKS Cluster, incorrect Amazon EKS Instance Profile or Kubernetes RBAC policy preventing authorization to Amazon EKS Cluster, customized AMI or LaunchTemplate configurations affecting Amazon EKS/Kubernetes node bootstrap.`

When using a default Amazon EKS AMI, the most common causes of this issue are the following:
+ The instance role isn't configured correctly. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) in the *Amazon EKS User Guide*.
+ The subnets aren't configured correctly. For more information, see [Amazon EKS VPC and subnet requirements and considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) in the *Amazon EKS User Guide*.
+ The security group isn't configured correctly. For more information, see [Amazon EKS security group requirements and considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide*.
**Note**  
You may also see an error notification in the Personal Health Dashboard (PHD).