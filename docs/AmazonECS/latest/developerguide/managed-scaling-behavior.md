# Amazon ECS managed scaling behavior

When you have Amazon EC2 Auto Scaling group capacity providers that use managed scaling, Amazon ECS estimates the
optimal number of instances to add to your cluster and uses the value to determine
how many instances to request or release.

## Managed scale-out behavior

Amazon ECS selects a capacity provider for each task by following the capacity
provider strategy from the service, standalone task, or the cluster default.
Amazon ECS follows the rest of these steps for a single capacity provider.

Tasks without a capacity provider strategy are ignored by capacity providers. A
pending task that doesn't have a capacity provider strategy won't cause any
capacity provider to scale out. Tasks or services can't set a capacity
provider strategy if that task or service sets a launch type.

The following describes the scale-out behavior in more detail.

- Group all of the provisioning tasks for this capacity provider so that each
  group has the same exact resource requirements.
- When you use multiple instance types in an Amazon EC2 Auto Scaling group, the instance types in the
  Amazon EC2 Auto Scaling group are sorted by their parameters. These parameters include vCPU, memory,
  elastic network interfaces (ENIs), ports, and GPUs. The smallest and the largest
  instance types for each parameter are selected. For more information about how
  to choose the instance type, see [Amazon EC2 container instances for Amazon ECS](create-capacity.md "create-capacity.md").

###### Important

If a group of tasks have resource requirements that are greater than the
smallest instance type in the Amazon EC2 Auto Scaling group, then that group of tasks can’t run
with this capacity provider. The capacity provider doesn’t scale the
Amazon EC2 Auto Scaling group. The tasks remain in the `PROVISIONING`
state.

To prevent tasks from staying in the `PROVISIONING` state, we
recommend that you create separate Amazon EC2 Auto Scaling groups and capacity providers
for different minimum resource requirements. When you run tasks or
create services, only add capacity providers to the capacity provider
strategy that can run the task on the smallest instance type in the
Amazon EC2 Auto Scaling group. For other parameters, you can use placement constraints

- For each group of tasks, Amazon ECS calculates the number of instances that are
  required to run the unplaced tasks. This calculation uses a `binpack`
  strategy. This strategy accounts for the vCPU, memory, elastic network
  interfaces (ENI), ports, and GPUs requirements of the tasks. It also accounts
  for the resource availability of the Amazon EC2 instances. The values for the largest
  instance types are treated as the maximum calculated instance count. The values
  for the smallest instance type are used as protection. If the smallest instance
  type can't run at least one instance of the task, the calculation considers the
  task as not compatible. As a result, the task is excluded from scale-out
  calculation. When all the tasks aren't compatible with the smallest instance
  type, cluster auto scaling stops and the `CapacityProviderReservation` value remains
  at the `targetCapacity` value.
- Amazon ECS publishes the `CapacityProviderReservation` metric to CloudWatch
  with respect to the `minimumScalingStepSize` if either of the
  following is the case.
  - The maximum calculated instance count is less than the minimum
    scaling step size.
  - The lower value of either the `maximumScalingStepSize`
    or the maximum calculated instance count.

- CloudWatch alarms use the `CapacityProviderReservation` metric for
  capacity providers. When the `CapacityProviderReservation` metric is
  greater than the `targetCapacity` value, alarms also increase the
  `DesiredCapacity` of the Amazon EC2 Auto Scaling group. The `targetCapacity`
  value is a capacity provider setting that's sent to the CloudWatch alarm during the
  cluster auto scaling activation phase.

The default `targetCapacity` is 100%.

- The Amazon EC2 Auto Scaling group launches additional EC2 instances. To prevent over-provisioning, Amazon EC2 Auto Scaling makes sure that recently launched EC2 instance
  capacity is stabilized before it launches new instances. Amazon EC2 Auto Scaling checks if all
  existing instances have passed the `instanceWarmupPeriod` (now
  minus the instance launch time). The scale-out is blocked for instances that
  are within the `instanceWarmupPeriod`.

The default number of seconds for a newly launched instance to warm up is 300.

For more information, see [Deep dive on Amazon ECS cluster auto scaling](https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/ "https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/").

### Scale-out considerations

Consider the following for the scale-out process:

- Although there are multiple placement constraints, we recommend that you
  only use the `distinctInstance` task placement constraint. This
  prevents the scale-out process from stopping because you're using a
  placement constraint that's not compatible with the sampled
  instances.
- Managed scaling works best if your Amazon EC2 Auto Scaling group uses the same or similar
  instance types.
- When a scale-out process is required and there are no currently running
  container instances, Amazon ECS always scales-out to two instances initially, and
  then performs additional scale-out or scale-in processes. Any additional
  scale-out waits for the instance warmup period. For scale-in processes,
  Amazon ECS waits 15 minutes after a scale-out process before starting scale-in
  processes at all times.
- The second scale-out step needs to wait until the
  `instanceWarmupPeriod` expires, which might affect the
  overall scale limit. If you need to reduce this time, make sure that
  `instanceWarmupPeriod` is large enough for the EC2
  instance to launch and start the Amazon ECS agent (which prevents over
  provisioning).
- Cluster auto scaling supports Launch Configuration, Launch Templates, and multiple
  instance types in the capacity provider Amazon EC2 Auto Scaling group. You can also use
  attribute-based instance type selection without multiple instances
  types.
- When using an Amazon EC2 Auto Scaling group with On-Demand instances and multiple instance types
  or Spot Instances, place the larger instance types higher in the priority list and
  don't specify a weight. Specifying a weight isn't supported at this time.
  For more information, see [Amazon EC2 Auto Scaling groups
  with multiple instance types](../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.md") in the
  _AWS Auto Scaling User Guide_.
- Amazon ECS then launch either the `minimumScalingStepSize`, if the
  maximum calculated instance count is less than the minimum scaling step
  size, or the lower of either the `maximumScalingStepSize` or the
  maximum calculated instance count value.
- If an Amazon ECS service or `run-task` launches a task and the
  capacity provider container instances don't have enough resources to
  start the task, then Amazon ECS limits the number of tasks with this status
  for each cluster and prevents any tasks from exceeding this limit. For
  more information, see [Amazon ECS service quotas](service-quotas.md "service-quotas.md").

## Managed scale-in behavior

Amazon ECS monitors container instances for each capacity provider within a cluster. When a
container instance isn't running any tasks, the container instance is considered
empty and Amazon ECS starts the scale-in process.

CloudWatch scale-in alarms require 15 data points (15 minutes) before the scale-in
process for the Amazon EC2 Auto Scaling group starts. After the scale-in process starts until Amazon ECS needs to
reduce the number of registered container instances, the Amazon EC2 Auto Scaling group sets the
`DesireCapacity` value to be greater than one instance and less than
50% each minute.

When Amazon ECS requests a scale-out (when `CapacityProviderReservation` is
greater than 100) while a scale-in process is in progress, the scale-in process is
stopped and starts from the beginning if required.

The following describes the scale-in behavior in more detail:

1. Amazon ECS calculates the number of container instances that are empty. A container
   instance is considered empty even when daemon tasks are running.
2. Amazon ECS sets the `CapacityProviderReservation` value to a number
   between 0-100 that uses the following formula to represent the ratio of how big
   the Amazon EC2 Auto Scaling group needs to be relative to how big it actually is, expressed as a
   percentage. Then, Amazon ECS publishes the metric to CloudWatch. For more information about
   how the metric is calculated, see [Deep Dive on
   Amazon ECS Cluster Auto Scaling](https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/ "https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/")

```
CapacityProviderReservation = (number of instances needed) / (number of running instances) x 100
```

3. The `CapacityProviderReservation` metric generates a CloudWatch alarm.
   This alarm updates the `DesiredCapacity` value for the Amazon EC2 Auto Scaling group. Then,
   one of the following actions occurs:
   - If you don't use capacity provider managed termination, the Amazon EC2 Auto Scaling group
     selects EC2 instances using the Amazon EC2 Auto Scaling group termination policy and terminates
     the instances until the number of EC2 instances reaches the
     `DesiredCapacity`. The container instances are then
     deregistered from the cluster.
   - If all the container instances use managed termination protection,
     Amazon ECS removes the scale-in protection on the container instances that
     are empty. The Amazon EC2 Auto Scaling group will then be able to terminate the EC2 instances.
     The container instances are then deregistered from the cluster.
