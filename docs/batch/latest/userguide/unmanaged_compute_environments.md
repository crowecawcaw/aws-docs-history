# Unmanaged compute environments

In an unmanaged compute environment, you manage your own compute resources. AWS Batch supports unmanaged compute
environments for both Amazon ECS and Amazon EKS, allowing you to maintain control over your infrastructure while leveraging
Batch's job scheduling capabilities.

###### Note

AWS Fargate resources aren't supported in unmanaged compute environments.

###### Unmanaged Amazon ECS compute environments

For unmanaged Amazon ECS compute environments, you must verify that the AMI you use for your compute resources
meets the Amazon ECS container instance AMI specification. For more information, see [Compute resource AMI specification](batch-ami-spec.md "batch-ami-spec.md") and [Tutorial: Create a compute resource AMI](create-batch-ami.md "create-batch-ami.md").

After you created your unmanaged compute environment, use the [DescribeComputeEnvironments](../APIReference/API_DescribeComputeEnvironments.md "../APIReference/API_DescribeComputeEnvironments.md") API
operation to view the compute environment details. Find the Amazon ECS cluster that's associated with the environment
and then manually launch your container instances into that Amazon ECS cluster.

The following AWS CLI command also provides the Amazon ECS cluster ARN.

```
`$` `aws batch describe-compute-environments \
 --compute-environments `unmanagedCE` \
 --query "computeEnvironments[].ecsClusterArn"`
```

For more information, see [Launching an Amazon ECS container instance](../../../AmazonECS/latest/developerguide/launch_container_instance.md "../../../AmazonECS/latest/developerguide/launch_container_instance.md") in the
_Amazon Elastic Container Service Developer Guide_. When you launch your compute resources, specify the Amazon ECS cluster ARN that
the resources register with the following Amazon EC2 user data. Replace `ecsClusterArn` with
the cluster ARN that you obtained with the previous command.

```
#!/bin/bash
echo "ECS_CLUSTER=`ecsClusterArn`" >> /etc/ecs/ecs.config
```

###### Unmanaged Amazon EKS compute environments

In an unmanaged Amazon EKS compute environment, you manage your own Kubernetes nodes while AWS Batch handles job
scheduling and placement. It allows you to directly control your Kubernetes infrastructure for security,
compliance, or operational requirements. You are responsible for provisioning and configuring your Amazon EKS nodes,
while AWS Batch integrates with your existing Amazon EKS cluster to schedule and run jobs.

For more information, see [Tutorial: Create an unmanaged compute
environment using Amazon EKS resources](create-compute-environment-unmanaged-eks.md "create-compute-environment-unmanaged-eks.md").

###### Amazon EKS Auto Mode compatibility

AWS Batch does not run jobs on [Amazon EKS
Auto Mode](../../../eks/latest/userguide/automode.md "../../../eks/latest/userguide/automode.md") worker nodes today — AWS Batch's unmanaged Amazon EKS compute environment requires persistent,
customer-labeled nodes, whereas Auto Mode provisions nodes dynamically via Karpenter based on pending-pod
pressure.

An unmanaged Amazon EKS compute environment can coexist with an Amazon EKS cluster that has Auto Mode enabled for
other workloads, as long as the AWS Batch compute environment points at a dedicated node group not managed by
Auto Mode. Auto Mode will continue to manage the non-AWS Batch workloads independently without interfering with
the AWS Batch node group.
