# Speeding up Amazon ECS cluster capacity provisioning

with capacity providers on Amazon EC2

Customers who run Amazon ECS on Amazon EC2 can take advantage of [Amazon ECS Cluster Auto
Scaling (CAS)](cluster-auto-scaling.md "cluster-auto-scaling.md") to manage the scaling of Amazon EC2 Auto Scaling groups (ASG). With CAS, you
can configure Amazon ECS to scale your ASG automatically, and just focus on running your
tasks. Amazon ECS will ensure the ASG scales in and out as needed with no further
intervention required. Amazon ECS capacity providers are used to manage the infrastructure in
your cluster by ensuring there are enough container instances to meet the demands of
your application. To learn how Amazon ECS CAS works, see [Deep Dive on Amazon ECS
Cluster Auto Scaling](https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/ "https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/").

Since CAS relies on a CloudWatch based integration with ASG for adjusting cluster capacity,
it has inherent latency associated with publishing the CloudWatch metrics, the time taken for
the metric `CapacityProviderReservation` to breach CloudWatch alarms (both high and
low), and the time taken by a newly launched Amazon EC2 instance to warm-up. You can take the
following actions to make CAS more responsive for faster deployments:

## Capacity provider step scaling sizes

Amazon ECS capacity providers will eventually grow/shrink the container instances to
meet the demands of your application. The minimum number of instances that Amazon ECS
will launch is set to 1 by default. This may add additional time to your
deployments, if several instances are required for placing your pending tasks. You
can increase the [`minimumScalingStepSize`](../APIReference/API_ManagedScaling.md "../APIReference/API_ManagedScaling.md") by using the Amazon ECS API to
increase the minimum number of instances that Amazon ECS scales in or out at a time. A
[`maximumScalingStepSize`](../APIReference/API_ManagedScaling.md "../APIReference/API_ManagedScaling.md") that is too low can limit how
many container instances are scaled in or out at a time, which can slow down your
deployments.

###### Note

This configuration is currently only available by using the [`CreateCapacityProvider`](../APIReference/API_CreateCapacityProvider.md "../APIReference/API_CreateCapacityProvider.md") or [`UpdateCapacityProvider`](../APIReference/API_UpdateCapacityProvider.md "../APIReference/API_UpdateCapacityProvider.md") APIs.

## Instance warm-up period

The instance warm-up period is the period of time after which a newly launched
Amazon EC2 instance can contribute to CloudWatch metrics for the Auto Scaling group. After the specified
warm-up period expires, the instance is counted toward the aggregated metrics of the
ASG, and CAS proceeds with its next iteration of calculations to estimate the number
instances required.

The default value for [`instanceWarmupPeriod`](../APIReference/API_ManagedScaling.md#ECS-Type-ManagedScaling-instanceWarmupPeriod "../APIReference/API_ManagedScaling.md#ECS-Type-ManagedScaling-instanceWarmupPeriod") is 300 seconds, which you can
configure to a lower value by using the [`CreateCapacityProvider`](../APIReference/API_CreateCapacityProvider.md "../APIReference/API_CreateCapacityProvider.md") or [`UpdateCapacityProvider`](../APIReference/API_UpdateCapacityProvider.md "../APIReference/API_UpdateCapacityProvider.md") APIs for more responsive scaling.

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
Scaling Policies](service-autoscaling-stepscaling.md "service-autoscaling-stepscaling.md")
