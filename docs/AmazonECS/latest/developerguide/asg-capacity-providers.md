# Amazon ECS capacity providers for EC2 workloads

When you use Amazon EC2 instances for your capacity, you use Amazon EC2 Auto Scaling groups to manage the
Amazon EC2 instances registered to their clusters. Amazon EC2 Auto Scaling helps ensure that you have the
correct number of Amazon EC2 instances available to handle the application load.

You can use the managed scaling feature to have Amazon ECS manage the scale-in and
scale-out actions of the Amazon EC2 Auto Scaling group, or you can manage the scaling actions yourself. For
more information, see [Automatically manage Amazon ECS capacity with
cluster auto scaling](cluster-auto-scaling.md "cluster-auto-scaling.md").

We recommend that you create a new empty Amazon EC2 Auto Scaling group. If you use an existing Amazon EC2 Auto Scaling
group, any Amazon EC2 instances that are associated with the group that were already running
and registered to an Amazon ECS cluster before the Amazon EC2 Auto Scaling group being used to create a capacity
provider might not be properly registered with the capacity provider. This might cause
issues when using the capacity provider in a capacity provider strategy. Use
`DescribeContainerInstances` to confirm whether a container instance is
associated with a capacity provider or not.

###### Note

To create an empty Amazon EC2 Auto Scaling group, set the desired count to zero. After you created
the capacity provider and associated it with a cluster, you can then scale it
out.

When you use the Amazon ECS console, Amazon ECS creates an Amazon EC2 launch template and Amazon EC2 Auto Scaling group
on your behalf as part of the CloudFormation stack. They are prefixed with
`EC2ContainerService-<`ClusterName`>`.
You can use the Amazon EC2 Auto Scaling group as a capacity provider for that cluster.

We recommend you use managed instance draining to allow for graceful termination of
Amazon EC2 instances that won't disrupt your workloads. This feature is on by default. For
more information, see [Safely stop Amazon ECS workloads running on EC2 instances](managed-instance-draining.md "managed-instance-draining.md")

Consider the following when using Amazon EC2 Auto Scaling group capacity providers in the console:

- An Amazon EC2 Auto Scaling group must have a `MaxSize` greater than zero to scale
  out.
- The Amazon EC2 Auto Scaling group can't have instance weighting settings.
- If the Amazon EC2 Auto Scaling group can't scale out to accommodate the number of tasks run, the
  tasks fails to transition beyond the `PROVISIONING` state.
- Don't modify the scaling policy resource associated with your Amazon EC2 Auto Scaling groups that
  are managed by capacity providers.
- If managed scaling is turned on when you create a capacity provider, the Amazon EC2 Auto Scaling group
  desired count can be set to `0`. When managed scaling is turned on,
  Amazon ECS manages the scale-in and scale-out actions of the Amazon EC2 Auto Scaling group.
- You must associate capacity provider with a cluster before you associate it
  with the capacity provider strategy.
- You can specify a maximum of 20 capacity providers for a capacity provider
  strategy.
- You can't update a service using an Amazon EC2 Auto Scaling group capacity provider to use a Fargate
  capacity provider. The opposite is also the case.
- In a capacity provider strategy, if no `weight` value is specified
  for a capacity provider in the console, then the default value of `1`
  is used. If using the API or AWS CLI, the default value of `0` is
  used.
- When multiple capacity providers are specified within a capacity provider
  strategy, at least one of the capacity providers must have a weight value that's
  greater than zero. Any capacity providers with a weight of zero aren't used to
  place tasks. If you specify multiple capacity providers in a strategy with all
  the same weight of zero, then any `RunTask` or
  `CreateService` actions using the capacity provider strategy
  fail.
- In a capacity provider strategy, only one capacity provider can have a defined
  _base_ value. If no base value is specified, the default
  value of zero is used.
- A cluster can contain a mix of both Amazon EC2 Auto Scaling group capacity providers and
  Fargate capacity providers. However, a capacity provider strategy can only
  contain Amazon EC2 Auto Scaling group or Fargate capacity providers, but not both.
- A cluster can contain a mix of services and standalone tasks that use both
  capacity providers and launch types. A service can be updated to use a capacity
  provider strategy rather than a launch type. However, you must force a new
  deployment when doing so.
- Amazon ECS supports Amazon EC2 Auto Scaling warm pools. A warm pool is a group of pre-initialized
  Amazon EC2 instances ready to be placed into service. Whenever your application needs
  to scale out, Amazon EC2 Auto Scaling uses the pre-initialized instances from the warm pool
  rather than launching cold instances. This allows for any final initialization
  process to run before the instance is placed into service. For more information,
  see [Configuring pre-initialized instances for your Amazon ECS Amazon EC2 Auto Scaling
  group](using-warm-pool.md "using-warm-pool.md").
  For more information about creating an Amazon EC2 Auto Scaling launch template, see [Amazon EC2 Auto Scaling launch
  templates](../../../autoscaling/ec2/userguide/launch-templates.md "../../../autoscaling/ec2/userguide/launch-templates.md") in the _Amazon EC2 Auto Scaling User Guide_. For more information
  about creating an Amazon EC2 Auto Scaling group, see [Amazon EC2 Auto Scaling groups](../../../autoscaling/ec2/userguide/auto-scaling-groups.md "../../../autoscaling/ec2/userguide/auto-scaling-groups.md") in the
  _Amazon EC2 Auto Scaling User Guide_.
