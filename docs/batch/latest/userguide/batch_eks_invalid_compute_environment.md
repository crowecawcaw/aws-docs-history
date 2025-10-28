# `INVALID` compute

environment

It's possible that you might have incorrectly configured a managed compute environment. If
you did, the compute environment enters an `INVALID` state and can't accept jobs for
placement. The following sections describe the possible causes and how to troubleshoot based on
the cause.

## Unsupported Kubernetes version

You might see an error message that resembles the following when you use the
`CreateComputeEnvironment` API operation or
`UpdateComputeEnvironment`API operation to create or update a compute environment.
This issue occurs if you specify an unsupported Kubernetes version in
`EC2Configuration`.

```
At least one imageKubernetesVersion in EC2Configuration is not supported.
```

To resolve this issue, delete the compute environment and then re-create it with a
supported Kubernetes version.

You can perform a minor version upgrade on your Amazon EKS cluster. For example, you can
upgrade the cluster from `1.xx` to `1.yy` even if the minor version isn't
supported.

However, the compute environment status might change to `INVALID` after a major
version update. For example, if you perform a major version upgrade from `1.xx` to
`2.yy`. If the major version isn't supported by AWS Batch, you see an error message
that resembles the following.

```
reason=CLIENT_ERROR - ... `EKS` Cluster version [`2.yy`] is unsupported
```

To resolve this issue, specify a supported Kubernetes version when you use an API operation to
create or update a compute environment.

AWS Batch on Amazon EKS currently supports the following Kubernetes versions:

- `1.33`
- `1.32`
- `1.31`
- `1.30`
- `1.29`
- `1.28`
- `1.27`
- `1.26`
- `1.25`

## Instance profile doesn't exist

If the specified instance profile does not exist, the AWS Batch on Amazon EKS compute environment
status is changed to `INVALID`. You see an error set in the
`statusReason` parameter that resembles the following.

```
CLIENT_ERROR - Instance profile arn:aws:iam::...:instance-profile/`<name>` does not exist
```

To resolve this issue, specify or create a working instance profile. For more information,
see [Amazon EKS node
IAM role](../../../eks/latest/userguide/create-node-role.md "../../../eks/latest/userguide/create-node-role.md") in the _Amazon EKS User Guide_.

## Invalid Kubernetes namespace

If AWS Batch on Amazon EKS can't validate the namespace for the compute environment, the compute
environment status is changed to `INVALID`. For example, this issue can occur if the
namespace doesn't exist.

You see an error message set in the `statusReason` parameter that resembles the
following.

```
CLIENT_ERROR - Unable to validate Kubernetes Namespace
```

This issue can occur if any of the following are true:

- The Kubernetes namespace string in the `CreateComputeEnvironment` call doesn't
  exist. For more information, see [CreateComputeEnvironment](../APIReference/API_CreateComputeEnvironment.md "../APIReference/API_CreateComputeEnvironment.md").
- The required Role-Based Access Control (RBAC) permissions to manage the namespace are
  not configured correctly.
- AWS Batch doesn't have access to the Amazon EKS Kubernetes API server endpoint.

To resolve this issue, see [Verify that the aws-auth ConfigMap is
configured correctly](verify-configmap-config.md "verify-configmap-config.md"). For more information, see [Getting started with AWS Batch on Amazon EKS](getting-started-eks.md "getting-started-eks.md").

## Deleted compute environment

Suppose that you delete an Amazon EKS cluster before you delete the attached AWS Batch on Amazon EKS
compute environment. Then, the compute environment status is changed to `INVALID`.
In this scenario, the compute environment doesn't work properly if you re-create the Amazon EKS
cluster with the same name.

To resolve this issue, delete and then re-create the AWS Batch on Amazon EKS compute
environment.

## Nodes don't join the Amazon EKS cluster

AWS Batch on Amazon EKS scales down a compute environment if it determines that not all nodes
joined the Amazon EKS cluster. When AWS Batch on Amazon EKS scales down the compute environment, the
compute environment status is changed to `INVALID`.

###### Note

AWS Batch doesn't change the compute environment status immediately so that you can debug
the issue.

You see an error message set in the `statusReason` parameter that resembles
ones of the following:

`Your compute environment has been INVALIDATED and scaled down because none of the
 instances joined the underlying ECS Cluster. Common issues preventing instances joining are
 the following: VPC/Subnet configuration preventing communication to ECS, incorrect Instance
 Profile policy preventing authorization to ECS, or customized AMI or LaunchTemplate
 configurations affecting ECS agent.`

`Your compute environment has been INVALIDATED and scaled down because none of the
 nodes joined the underlying Amazon EKS Cluster. Common issues preventing nodes joining are the
 following: networking configuration preventing communication to Amazon EKS Cluster, incorrect Amazon EKS
 Instance Profile or Kubernetes RBAC policy preventing authorization to Amazon EKS Cluster, customized
 AMI or LaunchTemplate configurations affecting Amazon EKS/Kubernetes node bootstrap.`

When using a default Amazon EKS AMI, the most common causes of this issue are the
following:

- The instance role isn't configured correctly. For more information, see [Amazon EKS node IAM
  role](../../../eks/latest/userguide/create-node-role.md "../../../eks/latest/userguide/create-node-role.md") in the _Amazon EKS User Guide_.
- The subnets aren't configured correctly. For more information, see [Amazon EKS VPC and subnet
  requirements and considerations](../../../eks/latest/userguide/network_reqs.md "../../../eks/latest/userguide/network_reqs.md") in the _Amazon EKS User Guide_.
- The security group isn't configured correctly. For more information, see [Amazon EKS security group
  requirements and considerations](../../../eks/latest/userguide/sec-group-reqs.md "../../../eks/latest/userguide/sec-group-reqs.md") in the _Amazon EKS User Guide_.

###### Note

You may also see an error notification in the Personal Health Dashboard (PHD).
