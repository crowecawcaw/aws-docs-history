# Optimize Amazon ECS cluster auto scaling

Customers who run Amazon ECS on Amazon EC2 can take advantage of cluster auto scaling to manage the
scaling of Amazon EC2 Auto Scaling groups. With cluster auto scaling, you can configure Amazon ECS to scale your
Amazon EC2 Auto Scaling group automatically, and just focus on running your tasks. Amazon ECS ensures the Amazon EC2 Auto Scaling group scales in
and out as needed with no further intervention required. Amazon ECS capacity providers are used
to manage the infrastructure in your cluster by ensuring there are enough container
instances to meet the demands of your application. To learn how cluster auto scaling works
under the hood, see [Deep Dive on Amazon ECS
Cluster Auto Scaling](https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/ "https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/").

Cluster auto scaling relies on a CloudWatch based integration with Amazon EC2 Auto Scaling group for adjusting cluster
capacity. Therefore it has inherent latency associated with

- Publishing the CloudWatch metrics,
- The time taken for the metric `CapacityProviderReservation` to breach
  CloudWatch alarms (both high and low)
- The time taken by a newly launched Amazon EC2 instance to warm-up. You can take the
  following actions to make cluster auto scaling more responsive for faster
  deployments:

## Capacity provider step scaling sizes

Amazon ECS capacity providers will grow/shrink the container instances to meet the demands
of your application. The minimum number of instances that Amazon ECS will launch is set to 1
by default. This may add additional time to your deployments, if several instances are
required for placing your pending tasks. You can increase the [`minimumScalingStepSize`](../APIReference/API_ManagedScaling.md "../APIReference/API_ManagedScaling.md") via the Amazon ECS API to increase the
minimum number of instances that Amazon ECS scales in or out at a time. A [`maximumScalingStepSize`](../APIReference/API_ManagedScaling.md "../APIReference/API_ManagedScaling.md") that is too low can limit how many
container instances are scaled in or out at a time, which can slow down your
deployments.

###### Note

This configuration is currently only available via the [`CreateCapacityProvider`](../APIReference/API_CreateCapacityProvider.md "../APIReference/API_CreateCapacityProvider.md") or [`UpdateCapacityProvider`](../APIReference/API_UpdateCapacityProvider.md "../APIReference/API_UpdateCapacityProvider.md") APIs.

## Instance warm-up period

The instance warm-up period is the period of time after which a newly launched Amazon EC2
instance can contribute to CloudWatch metrics for the Amazon EC2 Auto Scaling group. After the specified warm-up
period expires, the instance is counted toward the aggregated metrics of the Amazon EC2 Auto Scaling group, and
cluster auto scaling proceeds with its next iteration of calculations to estimate the
number instances required.

The default value for [`instanceWarmupPeriod`](../APIReference/API_ManagedScaling.md#ECS-Type-ManagedScaling-instanceWarmupPeriod "../APIReference/API_ManagedScaling.md#ECS-Type-ManagedScaling-instanceWarmupPeriod") is 300 seconds, which you can configure to
a lower value via the [`CreateCapacityProvider`](../APIReference/API_CreateCapacityProvider.md "../APIReference/API_CreateCapacityProvider.md") or [`UpdateCapacityProvider`](../APIReference/API_UpdateCapacityProvider.md "../APIReference/API_UpdateCapacityProvider.md") APIs for more responsive scaling. We recommend that you set the value to
greater than 60 seconds so that you can avoid over-provisioning.

## Spare capacity

If your capacity provider has no container instances available for placing tasks,
then it needs to increase (scale out) cluster capacity by launching Amazon EC2 instances
on the fly, and wait for them to boot up before it can launch containers on them.
This can significantly lower the task launch rate. You have two options here.

In this case, having spare Amazon EC2 capacity already launched and ready to run tasks
will increase the effective task launch rate. You can use the `Target
 Capacity` configuration to indicate that you wish to maintain spare
capacity in your clusters. For example, by setting `Target Capacity` at
80%, you indicate that your cluster needs 20% spare capacity at all times. This
spare capacity can allow any standalone tasks to be immediately launched, ensuring
task launches are not throttled. The trade-off for this approach is potential
increased costs of keeping spare cluster capacity.

An alternate approach you can consider is adding headroom to your service, not to
the capacity provider. This means that instead of reducing `Target
 Capacity` configuration to launch spare capacity, you can increase the
number of replicas in your service by modifying the target tracking scaling metric
or the step scaling thresholds of the service auto scaling. Note that this approach
will only be helpful for spiky workloads, but won't have an effect when you’re
deploying new services and going from 0 to N tasks for the first time. For more
information about the related scaling policies, see [Target Tracking Scaling Policies](service-autoscaling-targettracking.md "service-autoscaling-targettracking.md") or [Step
Scaling Policies](service-autoscaling-stepscaling.md "service-autoscaling-stepscaling.md") in the _Amazon Elastic Container Service Developer
Guide_.
