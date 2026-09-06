

# Troubleshooting Amazon ECS Managed Instances
<a name="troubleshooting-managed-instances"></a>

When launching tasks with Amazon ECS Managed Instances, Amazon ECS first attempts to place tasks on existing capacity and requests additional capacity for tasks that cannot be placed. If instance provisioning fails, the Amazon EC2 request ID is included in the task failure message. You can use this request ID to look up details of the failed request in CloudTrail for further troubleshooting.

**Note**  
If you choose to apply least-privilege permissions and specify your own permissions for the instance profile instead of using the `AmazonECSInstanceRolePolicyForManagedInstances` managed policy, you can add the following permissions to help with troubleshooting task-related issues with Amazon ECS Managed Instances:   
`ecs:StartTelemetrySession`
`ecs:PutSystemLogEvents`

## Task definition is incompatible with Amazon ECS Managed Instances
<a name="task-definition-incompatible"></a>

### Common cause
<a name="task-definition-incompatible-cause"></a>

This error occurs when your task definition contains parameters or configurations that are not supported by Amazon ECS Managed Instances. Common incompatibilities include unsupported network modes, task roles, or resource requirements.

### Resolution
<a name="task-definition-incompatible-resolution"></a>

1. Verify that your task definition uses `requiresCompatibilities` set to `MANAGED_INSTANCES`.

1. Ensure your task definition uses the `awsvpc` network mode.

1. Check that CPU and memory values are within supported ranges for Amazon ECS Managed Instances.

1. Review the detailed error message for specific incompatibility details.

## Capacity provider not associated with cluster
<a name="capacity-provider-missing"></a>

### Common cause
<a name="capacity-provider-missing-cause"></a>

This error occurs when the capacity provider specified in your capacity provider strategy is not associated with the cluster or does not exist.

### Resolution
<a name="capacity-provider-missing-resolution"></a>

1. Verify that the capacity provider exists in your account and region.

1. Associate the capacity provider with your cluster using the Amazon ECS console or CLI.

1. Ensure the capacity provider is in `ACTIVE` status before using it.

## Infrastructure role permission errors
<a name="infrastructure-role-errors"></a>

### Common cause
<a name="infrastructure-role-errors-cause"></a>

This error occurs when the Amazon ECS infrastructure role lacks the necessary permissions to perform Amazon EC2 operations on your behalf, or when the role cannot be assumed due to trust relationship issues.

### Resolution
<a name="infrastructure-role-errors-resolution"></a>

1. Verify that your infrastructure role has the proper trust relationship with Amazon ECS.

1. Ensure the role has the required Amazon EC2 permissions including `ec2:RunInstances`, `ec2:DescribeInstances`, and `iam:PassRole`.

1. Check the encoded authorization failure message in CloudTrail for specific permission details.

1. Update the role policy to include missing permissions identified in the error message.

## VcpuLimitExceeded error
<a name="vcpu-limit-exceeded"></a>

### Common cause
<a name="vcpu-limit-exceeded-cause"></a>

This error occurs when you've reached your vCPU service quota for the instance type family in the current region. Amazon ECS Managed Instances cannot launch additional instances until capacity is available.

### Resolution
<a name="vcpu-limit-exceeded-resolution"></a>

1. Request a service quota increase for the affected instance type family through the AWS Support Center.

1. Consider using different instance types that fall under a different vCPU quota category.

1. Terminate unused Amazon EC2 instances to free up vCPU capacity.

1. Review your capacity provider configuration to use instance types with lower vCPU requirements.

## InsufficientCapacity and related capacity errors
<a name="insufficient-capacity"></a>

### Common cause
<a name="insufficient-capacity-cause"></a>

These errors occur when AWS doesn't have sufficient capacity to fulfill your instance request. This can include insufficient instance capacity, address capacity, or volume capacity in the requested Availability Zone.

### Resolution
<a name="insufficient-capacity-resolution"></a>

1. Try launching instances in different Availability Zones by configuring multiple subnets in your capacity provider.

1. Consider using different instance types that may have more available capacity.

1. Wait and retry the operation as capacity availability changes frequently.

1. For persistent capacity needs, consider using Reserved Instances or Savings Plans.

## UnauthorizedOperation error
<a name="unauthorized-operation"></a>

### Common cause
<a name="unauthorized-operation-cause"></a>

This error occurs when the Amazon ECS service doesn't have the necessary permissions to perform Amazon EC2 operations or pass IAM roles. Common scenarios include missing `ec2:RunInstances` permissions or `iam:PassRole` permissions for the instance profile.

### Resolution
<a name="unauthorized-operation-resolution"></a>

1. Verify that your Amazon ECS infrastructure role has the necessary permissions to launch Amazon EC2 instances.

1. Ensure the infrastructure role has `iam:PassRole` permissions for the instance profile used by your Amazon ECS Managed Instances.

1. Check the encoded authorization failure message in CloudTrail for specific permission details.

1. Update the role policy to include the missing permissions identified in the error message.

## Task timed out waiting for capacity
<a name="task-timeout-capacity"></a>

### Common cause
<a name="task-timeout-capacity-cause"></a>

This error occurs when instances take longer than expected to launch and register with the cluster. This can happen due to Amazon EC2 capacity constraints, instance launch failures, or network connectivity issues.

### Resolution
<a name="task-timeout-capacity-resolution"></a>

1. Check Amazon EC2 service health in your region for any ongoing issues.

1. Verify that your subnets have sufficient IP addresses available.

1. Ensure your security groups allow the necessary traffic for Amazon ECS agent communication.

1. Consider using multiple Availability Zones to improve capacity availability.

1. Retry the task launch operation as capacity constraints are often temporary.

## Network configuration errors
<a name="network-configuration-errors"></a>

### Common cause
<a name="network-configuration-errors-cause"></a>

These errors occur when there are mismatches between your task's network requirements and the capacity provider's network configuration, such as VPC mismatches or missing network configuration.

### Resolution
<a name="network-configuration-errors-resolution"></a>

1. Verify that your capacity provider is configured with the correct VPC and subnets.

1. Ensure that security groups and subnets belong to the same VPC.

1. Check that your task definition's network configuration is compatible with the capacity provider.

1. Update your capacity provider configuration with the correct network settings.

## Capacity provider can't be deleted due to stuck instances
<a name="capacity-provider-deletion-errors"></a>

### Common cause
<a name="capacity-provider-deletion-errors-cause"></a>

These errors occur when Amazon ECS Managed Instances are stuck in an `ACTIVE` or `DRAINING` state but there are no running tasks on the instances.

### Resolution
<a name="capacity-provider-deletion-errors-resolution"></a>

To allow the deletion of the capacity provider to proceed, you can force deregister the instances that are stuck using the following command.

```
aws ecs deregister-container-instance \
    --cluster arn:aws:ecs:{{us-east-1}}:{{111122223333}}:cluster/MyCluster \
    --container-instance arn:aws:ecs:{{us-east-1}}:{{111122223333}}:container-instance/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
    --force
```