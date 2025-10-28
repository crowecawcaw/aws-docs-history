# Unmanaged compute environments

In an unmanaged compute environment, you manage your own compute resources. You must verify that the AMI you use
for your compute resources meets the Amazon ECS container instance AMI specification. For more information, see [Compute resource AMI specification](batch-ami-spec.md "batch-ami-spec.md") and [Tutorial: Create a compute resource AMI](create-batch-ami.md "create-batch-ami.md").

###### Note

AWS Fargate resources aren't supported in unmanaged compute environments.

After you created your unmanaged compute environment, use the [DescribeComputeEnvironments](../APIReference/API_DescribeComputeEnvironments.md "../APIReference/API_DescribeComputeEnvironments.md") API
operation to view the compute environment details. Find the Amazon ECS cluster that's associated with the environment and
then manually launch your container instances into that Amazon ECS cluster.

The following AWS CLI command also provides the Amazon ECS cluster ARN.

```
`$` `aws batch describe-compute-environments \
 --compute-environments `unmanagedCE` \
 --query "computeEnvironments[].ecsClusterArn"`
```

For more information, see [Launching an Amazon ECS
container instance](../../../AmazonECS/latest/developerguide/launch_container_instance.md "../../../AmazonECS/latest/developerguide/launch_container_instance.md") in the _Amazon Elastic Container Service Developer Guide_. When you launch your compute resources,
specify the Amazon ECS cluster ARN that the resources register with the following Amazon EC2 user data. Replace
`ecsClusterArn` with the cluster ARN that you obtained with the previous command.

```
#!/bin/bash
echo "ECS_CLUSTER=`ecsClusterArn`" >> /etc/ecs/ecs.config
```
