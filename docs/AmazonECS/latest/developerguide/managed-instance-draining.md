# Safely stop Amazon ECS workloads running on EC2 instances

Managed instance draining facilitates graceful termination of Amazon EC2 instances. This allows your workloads
to stop safely and be rescheduled to non-terminating instances. Infrastructure maintenance and updates are
performed without worrying about disruption to workloads. By using managed instance draining, you simplify
your infrastructure management workflows that require replacement of Amazon EC2 instances while you ensure
resilience and availability of your applications.

Amazon ECS managed instance draining works with Auto Scaling group instance replacements. Based on instance refresh and
maximum instance lifetime, customers can ensure that they stay compliant with the latest OS and security
mandates for their capacity.

Managed instance draining can only be used with Amazon ECS capacity providers. You can turn on managed
instance draining when you create or update your Auto Scaling group capacity providers using the Amazon ECS console, AWS CLI,
or SDK.

The following events are covered by Amazon ECS managed instance draining.

- [Auto Scaling group
  instance refresh](../../../autoscaling/ec2/userguide/asg-instance-refresh.md "../../../autoscaling/ec2/userguide/asg-instance-refresh.md") ‐ Use instance refresh to perform rolling replacement of your
  Amazon EC2 instances in your Auto Scaling group instead of manually doing it in batches. This is useful when you need
  to replace a large number of instances. An instance refresh is initiated through the Amazon EC2 console
  or the `StartInstanceRefresh` API. Make sure you select `Replace` for
  Scale-in protection when calling `StartInstanceRefresh` if you're using managed
  termination protection.
- [Maximum instance lifetime](../../../autoscaling/ec2/userguide/asg-max-instance-lifetime.md "../../../autoscaling/ec2/userguide/asg-max-instance-lifetime.md") ‐ You can define a maximum lifetime when it comes to
  replacing Auto Scaling group instances. This is helpful for scheduling replacement instances based on internal
  security policies or compliance.
- Auto Scaling group scale-in ‐ Based on scaling policies and scheduled scaling actions, Auto Scaling group supports
  automatic scaling of instances. By using an Auto Scaling group as an Amazon ECS capacity provider, you can scale-in
  Auto Scaling group instances when no tasks are running in them.
- [Auto Scaling group health checks](../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md") ‐ Auto Scaling group supports many health checks to manage termination of
  unhealthy instances.
- [CloudFormation stack
  updates](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md") ‐ You can add an `UpdatePolicy` attribute to your CloudFormation stack
  to perform rolling updates when group changes.
- [Spot capacity
  rebalancing](../../../AWSEC2/latest/UserGuide/spot-interruptions.md "../../../AWSEC2/latest/UserGuide/spot-interruptions.md") ‐ The Auto Scaling group tries to proactively replace Spot Instances that have a higher risk
  of interruption based on Amazon EC2 capacity rebalance notice. The Auto Scaling group terminates the old instance
  when the replacement is launched and healthy. Amazon ECS managed instance draining drains the Spot Instance the
  same way it drains a non-Spot Instance.
- [Spot
  interruption](../../../autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.md") ‐ Spot Instances are terminated with a two minute notice. Amazon ECS-managed
  instance draining puts the instance in draining state in response.

###### Amazon EC2 Auto Scaling lifecycle hooks with managed instance draining

Auto Scaling group lifecycle hooks enable customer to create solutions that are triggered by certain events in the
instance lifecycle and perform a custom action when that certain event occurs. An Auto Scaling group allows for up
to 50 hooks. Multiple termination hooks can exist and are performed in parallel, and Auto Scaling group waits for
all hooks to finish before terminating an instance.

In addition to the Amazon ECS-managed hook termination, you can also configure your own lifecycle termination
hooks. Lifecycle hooks have a `default action`, and we recommend setting `continue`
as the default to ensure other hooks, such as the Amazon ECS managed hook, aren't impacted by any errors from
custom hooks.

If you've already configured an Auto Scaling group termination lifecycle hook and also enabled Amazon ECS managed instance
draining, both lifecycle hooks are performed. The relative timings, however, are not guaranteed. Lifecycle
hooks have a `default action` setting to specify the action to take when timeout elapses. In
case of failures we recommend using `continue` as the default result in your custom hook. This
ensures other hooks, particularly the Amazon ECS managed hooks, aren't impacted by any errors in your custom
lifecycle hook. The alternative result of `abandon` causes all other hooks to be skipped and
should be avoided. For more information about Auto Scaling group lifecycle hooks see [Amazon EC2 Auto Scaling lifecycle hooks](../../../autoscaling/ec2/userguide/lifecycle-hooks.md "../../../autoscaling/ec2/userguide/lifecycle-hooks.md") in the
_Amazon EC2_ Auto Scaling User Guide.

###### Tasks and managed instance draining

Amazon ECS managed instance draining uses the existing draining feature found in container instances. The
[container instance draining](container-instance-draining.md "container-instance-draining.md") feature performs replacement and stops for replica tasks that
belong to an Amazon ECS service. A standalone task, like one invoked by `RunTask`, that is in the
`PENDING` or `RUNNING` state remain unaffected. You have to wait for these to
either complete or stop them manually. The container instance remains in the `DRAINING`
state until either all tasks are stopped or 48 hours has passed. Daemon tasks are the last to stop
after all replica tasks have stopped.

###### Managed instance draining and managed termination protection

Managed instance draining works even if managed termination is disabled. For information about
managed termination protection, see [Control the instances Amazon ECS terminates](managed-termination-protection.md "managed-termination-protection.md").

The following table summarizes the behavior for different combinations of managed termination and managed
draining.

| Managed termination | Managed draining | Outcome                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Enabled             | Enabled          | Amazon ECS protects Amazon EC2 instances that are running tasks from being terminated by scale-in<br>events. Any instances undergoing termination, such as those that don't have termination<br>protection set, have received Spot interruption, or are forced by instance refresh are<br>gracefully drained.                                                                  |
| Disabled            | Enabled          | Amazon ECS doesn't protect Amazon EC2 instances running tasks from being scaled-in. However, any<br>instances that are being terminated are gracefully drained.                                                                                                                                                                                                                |
| Enabled             | Disabled         | Amazon ECS protects Amazon EC2 instances that are running tasks from being terminated by scale-in<br>events. However, instances can still get terminated by Spot interruption or forced instance<br>refresh, or if they aren't running any tasks. Amazon ECS doesn't perform graceful draining for<br>these instances, and launches replacement service tasks after they stop. |
| Disabled            | Disabled         | Amazon EC2 instances can be scaled-in or terminated at any time, even if they are running<br>Amazon ECS tasks. Amazon ECS will launch replacement service tasks after they stop.                                                                                                                                                                                               |

###### Managed instance draining and Spot Instance draining

With Spot Instance draining, you can set an environment variable
`ECS_ENABLE_SPOT_INSTANCE_DRAINING` on the Amazon ECS agent which enables Amazon ECS to place an
instance in the draining status in response to the two-minute Spot interruption. Amazon ECS managed instance
draining facilitates graceful shutdown of Amazon EC2 instances undergoing termination due to many reasons,
not just Spot interruption. For instance, you can use Amazon EC2 Auto Scaling capacity rebalancing to proactively
replace Spot Instance at elevated risk of interruption, and managed instance draining performs graceful shutdown
of Spot Instance being replaced. When you use managed instance draining, you don't need to enable Spot instance
draining separately, so `ECS_ENABLE_SPOT_INSTANCE_DRAINING` in Auto Scaling group user data is redundant.
For more information about Spot Instance draining, see [Spot Instances](create-capacity.md#container-instance-spot "create-capacity.md#container-instance-spot").

## How managed instance draining works with EventBridge

Amazon ECS managed instance draining events are published to Amazon EventBridge, and Amazon ECS creates an EventBridge managed
rule in your account’s default bus to support managed instance draining. You can filter these events to
other AWS services like Lambda, Amazon SNS, and Amazon SQS to monitor and troubleshoot.

- Amazon EC2 Auto Scaling sends an event to EventBridge when a lifecycle hook is invoked.
- Spot interruption notices are published to EventBridge.
- Amazon ECS generates error messages that you can retrieve through the Amazon ECS console and
  APIs.
- EventBridge has retry mechanisms built in as mitigations for temporary failures.

## Amazon ECS Managed instance draining troubleshooting

You might need to troubleshoot issues with managed instance draining. The following is an example of
an issue and resolution you may come across while using it.

###### Instances don't terminate after exceeding maximum instance lifetime when using auto scaling.

If your instances aren't terminating even after reaching and exceeding the maximum instance
lifetime while using an auto scaling group, it may be because they're protected from scale-in. You
can turn off managed termination and allow managed draining to handle instance recycling.

## Draining behavior for Amazon ECS Managed Instances

Amazon ECS Managed Instances termination ensures graceful workload transitions while
optimizing costs and maintaining system health. The termination system provides three
distinct decision paths for instance termination, each with different timing
characteristics and customer impact profiles.

### Termination decision paths

Customer-initiated termination

Provides direct control over instance removal when you need to remove container instances from service immediately. You invoke the DeregisterContainerInstance API with the force flag set to true, indicating that immediate termination is required despite any running workloads.

System-initiated idle termination

Amazon ECS Managed Instances continuously monitors and proactively optimizes costs by terminating idle Amazon ECS container instances not running any tasks. ECS uses a heuristic delay to give container instances a chance to acquire newly launched tasks before being terminated. This can be customized with the `scaleInAfter` Amazon ECS Managed Instances capacity provider configuration parameter.

Infrastructure refresh termination

Amazon ECS Managed Instances automatically manages and updates software on managed container instances to ensure security and compliance while maintaining workload availability. For more information, see [patching in Amazon ECS Managed Instances](managed-instances-patching.md "managed-instances-patching.md").

### Graceful draining and workload migration

The graceful draining system implements sophisticated coordination with Amazon ECS service management to ensure that service-managed tasks are properly migrated away from instances scheduled for termination.

###### Service task draining coordination

When an instance transitions to DRAINING state, the Amazon ECS scheduler automatically stops placing new tasks on the instance while implementing graceful shutdown procedures for existing service tasks. The service task draining includes coordination with service deployment strategies, health check requirements, and your draining preferences to ensure optimal migration timing and success rates.

###### Standalone task handling

Standalone tasks require different handling because they do not benefit from automatic service management. The system evaluates standalone task characteristics including task duration estimates, completion probability analysis, and customer impact assessment. The graceful completion strategy allows standalone tasks to complete naturally during an extended grace period, while forced termination ensures infrastructure refresh occurs within acceptable timeframes when tasks have not completed naturally.

### Two-phase completion strategy

The termination system implements a two-phase approach that balances workload continuity against infrastructure management requirements.

###### Phase 1: Graceful completion period

During this phase, the system implements graceful draining strategies that prioritize workload continuity. Service tasks are gracefully drained through normal Amazon ECS scheduling processes, standalone tasks continue running and may complete naturally, and the system monitors for all tasks to reach stopped state through natural completion processes.

###### Phase 2: Hard deadline enforcement

When graceful completion does not achieve termination objectives within acceptable timeframes, the system implements hard deadline enforcement. The hard deadline is typically set to draining initiation time plus seven days, providing substantial time for graceful completion while maintaining operational requirements. The enforcement includes automatic invocation of force deregistration procedures and immediate termination of all remaining tasks regardless of completion status.
