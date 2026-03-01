# Automatically manage Amazon ECS capacity with cluster auto scaling

Amazon ECS can manage the scaling of Amazon EC2 instances that are registered to your cluster. This
is referred to as Amazon ECS _cluster auto scaling_. You turn on
managed scaling when you create the Amazon ECS Auto Scaling group capacity provider. Then, you set a target
percentage (the `targetCapacity`) for the instance utilization in this Auto Scaling group.
Amazon ECS creates two custom CloudWatch metrics and a target tracking scaling policy for your Auto Scaling group.
Amazon ECS then manages the scale-in and scale-out actions based on the resource utilization that
your tasks use.

For each Auto Scaling group capacity provider that's associated with a cluster, Amazon ECS creates
and manages the following resources:

- A low metric value CloudWatch alarm
- A high metric value CloudWatch alarm
- A target tracking scaling policy

###### Note

Amazon ECS creates the target tracking scaling policy and attaches it to
the Auto Scaling group. To update the target tracking scaling policy, update the
capacity provider managed scaling settings, rather than updating the
scaling policy directly.
When you turn off managed scaling or disassociate the capacity provider from a
cluster, Amazon ECS removes both CloudWatch metrics and the target tracking scaling policy
resources.

Amazon ECS uses the following metrics to determine what actions to take:

`CapacityProviderReservation`

The percent of container instances in use for a specific capacity
provider. Amazon ECS generates this metric.

Amazon ECS sets the `CapacityProviderReservation` value to a
number between 0-100. Amazon ECS uses the following formula to represent the
ratio of how much capacity remains in the Auto Scaling group. Then, Amazon ECS publishes the
metric to CloudWatch. For more information about how the metric is calculated, see
[Deep
Dive on Amazon ECS Cluster Auto Scaling](https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/ "https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/").

```
CapacityProviderReservation = (number of instances needed) / (number of running instances) x 100
```

`DesiredCapacity`

The amount of capacity for the Auto Scaling group. This metric isn't published to CloudWatch.

Amazon ECS publishes the `CapacityProviderReservation` metric to CloudWatch in the
`AWS/ECS/ManagedScaling` namespace. The
`CapacityProviderReservation` metric causes one of the following
actions to occur:

**The `CapacityProviderReservation` value equals
`targetCapacity`**

The Auto Scaling group doesn't need to scale in or scale out. The target
utilization percentage has been reached.

**The `CapacityProviderReservation` value is greater than
`targetCapacity`**

There are more tasks using a higher percentage of the capacity than
your `targetCapacity` percentage. The increased value of the
`CapacityProviderReservation` metric causes the
associated CloudWatch alarm to act. This alarm updates the
`DesiredCapacity` value for the Auto Scaling group. The Auto Scaling group
uses this value to launch EC2 instances, and then register them with the
cluster.

When the `targetCapacity` is the default value of 100 %,
the new tasks are in the `PENDING` state during the scale-out
because there is no available capacity on the instances to run the
tasks. After the new instances register with ECS, these tasks will start
on the new instances.

**The `CapacityProviderReservation` value is less than
`targetCapacity`**

There are less tasks using a lower percentage of the capacity than
your `targetCapacity` percentage and there is at least one
instance that can be terminated. The decreased value of the
`CapacityProviderReservation` metric causes the
associated CloudWatch alarm to act. This alarm updates the
`DesiredCapacity` value for the Auto Scaling group. The Auto Scaling group
uses this value to terminate EC2 container instances, and then
deregister them from the cluster.

The Auto Scaling group follows the group termination policy to determine which
instances it terminates first during scale-in events. Additionally it
avoids instances with the instance scale-in protection setting turned
on. Cluster auto scaling can manage which instances have the instance scale-in
protection setting if you turn on managed termination protection. For
more information about managed termination protection, see [Control the instances Amazon ECS terminates](managed-termination-protection.md "managed-termination-protection.md"). For more
information about how Auto Scaling groups terminate instances, see [Control which Auto Scaling instances terminate during scale in](../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.md") in
the _Amazon EC2 Auto Scaling User Guide_.

Consider the following when using cluster auto scaling:

- Don't change or manage the desired capacity for the Auto Scaling group that's associated
  with a capacity provider with any scaling policies other than the one Amazon ECS
  manages.
- When Amazon ECS scales out from 0 instances, it automatically launches 2
  instances.
- Amazon ECS uses the `AWSServiceRoleForECS` service-linked IAM role for
  the permissions that it requires to call AWS Auto Scaling on your behalf. For more
  information, see [Using service-linked roles for Amazon ECS](using-service-linked-roles.md "using-service-linked-roles.md").
- When using capacity providers with Auto Scaling groups, the user, group, or role that
  creates the capacity providers requires the
  `autoscaling:CreateOrUpdateTags` permission. This is because
  Amazon ECS adds a tag to the Auto Scaling group when it associates it with the capacity
  provider.

###### Important

Make sure any tooling that you use doesn't remove the
`AmazonECSManaged` tag from the Auto Scaling group. If this tag is
removed, Amazon ECS can't manage the scaling.

- Cluster auto scaling doesn't modify the **MinimumCapacity** or
  **MaximumCapacity** for the group. For the group to scale
  out, the value for **MaximumCapacity** must be greater than
  zero.
- When Auto Scaling (managed scaling) is turned on, a capacity provider can only be
  connected to one cluster at the same time. If your capacity provider has managed
  scaling turned off, you can associate it with multiple clusters.
- When managed scaling is turned off, the capacity provider doesn't scale in or
  scale out. You can use a capacity provider strategy to balance your tasks
  between capacity providers.
- The `binpack` strategy is the most efficient strategy in terms of
  capacity.
- When the target capacity is less than 100%, within the placement strategy,
  the `binpack` strategy must have a higher order than the
  `spread` strategy. This prevents the capacity provider from
  scaling out until each task has a dedicated instance or the limit is
  reached.

## Turn on cluster auto scaling

You can turn on cluster auto scaling by using the Console or the AWS CLI.

When you create a cluster that uses EC2 capacity providers using the console, Amazon ECS creates an Auto Scaling group on your behalf and sets the target capacity. For more information, see [Creating an Amazon ECS cluster for Amazon EC2 workloads](create-ec2-cluster-console-v2.md "create-ec2-cluster-console-v2.md").

You can also create an Auto Scaling group, and then assign it to a cluster. For more information, see [Updating an Amazon ECS capacity provider](update-capacity-provider-console-v2.md "update-capacity-provider-console-v2.md").

When you use the AWS CLI, after you create the cluster

1. Before you create the capacity provider, you need to create an Auto Scaling group. For more
   information, see [Auto Scaling groups](../../../autoscaling/ec2/userguide/auto-scaling-groups.md "../../../autoscaling/ec2/userguide/auto-scaling-groups.md") in the
   _Amazon EC2 Auto Scaling User Guide_.
2. Use `put-cluster-capacity-providers` to modify the cluster
   capacity provider. For more information, see [Turning on Amazon ECS cluster auto scaling](turn-on-cluster-auto-scaling.md "turn-on-cluster-auto-scaling.md").
