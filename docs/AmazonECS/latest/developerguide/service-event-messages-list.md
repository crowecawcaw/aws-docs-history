# Amazon ECS service event messages

The following are examples of service event messages you may see in the Amazon ECS console.

## service

(`service-name`) has reached a steady state.

The service scheduler sends a `service (`service-name`) has
 reached a steady state.` service event when the service is healthy and at the desired
number of tasks, thus reaching a steady state.

The service scheduler reports the status periodically, so you might receive this message
multiple times.

## service (`service-name`)

was unable to place a task because no container instance met all of its
requirements.

The service scheduler sends this event message when it couldn't find the available resources
to add another task. The possible causes for this are:

Use capacity providers to automatically scale your EC2 instances. For
more information, see [Amazon ECS capacity providers for EC2 workloads](asg-capacity-providers.md "asg-capacity-providers.md").
If you intended to use a capacity provider, make sure that you’re either passing a capacity
provider strategy or have a default capacity provider strategy
associated with your cluster and are not passing launch type and
capacity provider strategy as input

No container instances were found in your cluster

If no container instances are registered in the cluster you attempt to run a task
in, you receive this error. You should add container instances to your cluster. For
more information, see [Launching an Amazon ECS Linux container
instance](launch_container_instance.md "launch_container_instance.md").

Not enough ports

If your task uses fixed host port mapping (for example, your task uses port 80 on
the host for a web server), you must have at least one container instance per task,
because only one container can use a single host port at a time. You should add
container instances to your cluster or reduce your number of desired tasks.

Too many ports registered

The closest matching container instance for task placement can't exceed the
maximum allowed reserved port limit of 100 host ports per container instance. Using
dynamic host port mapping may remediate the issue.

Port already in-use

The task definition of this task uses the same port in its port mapping as a task
already running on the container instance that was chosen. The service event
message would have the chosen container instance ID as part of the message
below.

```
The closest matching container-instance is already using a port required by your task.
```

Not enough memory

If your task definition specifies 1000 MiB of memory, and the container instances
in your cluster each have 1024 MiB of memory, you can only run one copy of this
task per container instance. You can experiment with less memory in your task
definition so that you could launch more than one task per container instance, or
launch more container instances into your cluster.

###### Note

If you're trying to maximize your resource utilization by providing your
tasks as much memory as possible for a particular instance type, see [Reserving Amazon ECS Linux container instance memory](memory-management.md "memory-management.md").

Not enough CPU

A container instance has 1,024 CPU units for every CPU core. If your task
definition specifies 1,000 CPU units, and the container instances in your cluster
each have 1,024 CPU units, you can only run one copy of this task per container
instance. You can experiment with fewer CPU units in your task definition so that
you could launch more than one task per container instance, or launch more
container instances into your cluster.

Not enough available ENI attachment points

Tasks that use the `awsvpc` network mode each receive their own
elastic network interface (ENI), which is attached to the container instance that
hosts it. Amazon EC2 instances have a limit to the number of ENIs that can be attached
to them and there are no container instances in the cluster that have ENI capacity
available.

The ENI limit for individual container instances depends on the following
conditions:

- If you **have not** opted in to the
  `awsvpcTrunking` account setting, the ENI limit for each
  container instance depends on the instance type. For more information, see
  [IP Addresses Per Network
  Interface Per Instance Type](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the
  _Amazon EC2 User Guide_.
- If you **have** opted in to the
  `awsvpcTrunking` account setting but you **have not** launched new container instances using
  a supported instance type after opting in, the ENI limit for each container
  instance is still at the default value. For more information, see [IP Addresses Per Network Interface
  Per Instance Type](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the
  _Amazon EC2 User Guide_.
- If you **have** opted in to the
  `awsvpcTrunking` account setting and you **have** launched new container instances using a
  supported instance type after opting in, additional ENIs are available. For
  more information, see [Supported instances for
  increased Amazon ECS container network interfaces](eni-trunking-supported-instance-types.md "eni-trunking-supported-instance-types.md").

For more information about opting in to the `awsvpcTrunking` account
setting, see [Increasing Amazon ECS Linux container instance network
interfaces](container-instance-eni.md "container-instance-eni.md").

You can add container instances to your cluster to provide more available network
adapters.

Container instance missing required attribute

Some task definition parameters require a specific Docker remote API version to
be installed on the container instance. Others, such as the logging driver options,
require the container instances to register those log drivers with the
`ECS_AVAILABLE_LOGGING_DRIVERS` agent configuration variable. If
your task definition contains a parameter that requires a specific container
instance attribute, and you don't have any available container instances that can
satisfy this requirement, the task can't be placed.

A common cause of this error is if your service is using tasks that use the
`awsvpc` network mode and EC2. The
cluster you specified doesn't have a container instance registered to it in the
same subnet that was specified in the `awsvpcConfiguration` when the
service was created.

You can use the AWSSupport-TroubleshootECSContainerInstance runbook
to troubleshoot. The runbook reviews whether the user data for the
instance contains the correct cluster information, whether the instance
profile contains the required permissions, and network configuration
issues. For more information, see [AWSSupport-TroubleshootECSContainerInstance](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshoot-ecs-container-instance.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshoot-ecs-container-instance.md") in the
_AWS Systems Manager Automation runbook reference User
Guide_.

For more information on which attributes are required for specific task
definition parameters and agent configuration variables, see [Amazon ECS task definition parameters for Fargate](task_definition_parameters.md "task_definition_parameters.md") and [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").

## service (`service-name`)

was unable to place a task because no container instance met all of its requirements. The
closest matching container-instance `container-instance-id` has
insufficient CPU units available.

The closest matching container instance for task placement doesn't contain enough CPU units
to meet the requirements in the task definition. Review the CPU requirements in both the task
size and container definition parameters of the task definition.

## service (`service-name`)

was unable to place a task because no container instance met all of its requirements. The
closest matching container-instance `container-instance-id`
encountered error "AGENT".

The Amazon ECS container agent on the closest matching container instance for task placement is
disconnected. If you can connect to the container instance with SSH, you can examine the agent
logs; for more information, see [Amazon ECS container agent log configuration parameters](ecs-agent-versions.md#agent-logs "ecs-agent-versions.md#agent-logs"). You
should also verify that the agent is running on the instance. If you are using the
Amazon ECS-optimized AMI, you can try stopping and restarting the agent with the following
command.

- For the Amazon ECS-optimized Amazon Linux 2 AMI and Amazon ECS-optimized Amazon Linux 2023 AMI

```
`sudo systemctl restart ecs`
```

- For the Amazon ECS-optimized Amazon Linux AMI

```
`sudo stop ecs && sudo start ecs`
```

## service (`service-name`)

(task `task-id`) (instance `instance-id`) is unhealthy in (elb
`elb-name`) due to (reason Instance has failed at least the
UnhealthyThreshold number of health checks consecutively.)

This service is registered with a load balancer and the load balancer health checks are
failing. The message includes the task ID to help identify which specific task is failing health checks.
For more information, see [Troubleshooting service load
balancers in Amazon ECS](troubleshoot-service-load-balancers.md "troubleshoot-service-load-balancers.md").

## service (`service-name`) is

unable to consistently start tasks successfully.

This service contains tasks that have failed to start after consecutive attempts. At this
point, the service scheduler begins to incrementally increase the time between retries. You
should troubleshoot why your tasks are failing to launch. For more information, see [Amazon ECS service throttle logic](service-throttle-logic.md "service-throttle-logic.md").

After the service is updated, for example with an updated task definition, the service
scheduler resumes normal behavior.

## service (`service-name`)

operations are being throttled. Will try again later.

This service is unable to launch more tasks due to API throttling limits. Once the service
scheduler is able to launch more tasks, it will resume.

To request an API rate limit quota increase, open the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") page, sign in if necessary, and choose
**Create case**. Choose **Service limit increase**.
Complete and submit the form.

## service (`service-name`)

was unable to stop or start tasks during a deployment because of the service deployment
configuration. Update the minimumHealthyPercent or maximumPercent value and try
again.

This service is unable to stop or start tasks during a service deployment due to the
deployment configuration. The deployment configuration consists of the
`minimumHealthyPercent` and `maximumPercent` values, which are
defined when the service is created. Those values can also be updated on an existing
service.

The `minimumHealthyPercent` represents the lower limit on the number of tasks that
should be running for a service during a deployment or when a container instance is draining.
It's a percent of the desired number of tasks for the service. This value is rounded up. For
example, if the minimum healthy percent is `50` and the desired task count is four,
then the scheduler can stop two existing tasks before starting two new tasks. Likewise, if the
minimum healthy percent is 75% and the desired task count is two, then the scheduler can't stop
any tasks due to the resulting value also being two.

The `maximumPercent` represents the upper limit on the number of tasks that should
be running for a service during a deployment or when a container instance is draining. It's a
percent of the desired number of tasks for a service. This value is rounded down. For example,
if the maximum percent is `200` and the desired task count is four, then the
scheduler can start four new tasks before stopping four existing tasks. Likewise, if the
maximum percent is `125` and the desired task count is three, the scheduler can't
start any tasks due to the resulting value also being three.

When setting a minimum healthy percent or a maximum percent, you should ensure that the
scheduler can stop or start at least one task when a deployment is triggered.

## service (`service-name`)

was unable to place a task. Reason: You've reached the limit on the number of tasks you can
run concurrently

You can request a quota increase for the resource that caused the error. For more
information, see [Amazon ECS service quotas](service-quotas.md "service-quotas.md"). To request a quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## service (`service-name`)

was unable to place a task. Reason: Internal error.

The following is the possible reason for this error:

The service is unable to start a task due to a subnet being in an unsupported Availability
Zone.

For information about the supported Fargate Regions and Availability Zones,
see [Supported Regions for Amazon ECS on
AWS Fargate](AWS_Fargate-Regions.md "AWS_Fargate-Regions.md").

For information about how to view the subnet Availability Zone, see [View your subnet](../../../vpc/latest/userguide/working-with-vpcs.md#view-subnet "../../../vpc/latest/userguide/working-with-vpcs.md#view-subnet") in the
_Amazon VPC User Guide_.

## service (`service-name`)

was unable to place a task. Reason: The requested CPU configuration is above your
limit.

You can request a quota increase for the resource that caused the error. For more
information, see [Amazon ECS service quotas](service-quotas.md "service-quotas.md"). To request a quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## service (`service-name`)

was unable to place a task. Reason: The requested MEMORY configuration is above your
limit.

You can request a quota increase for the resource that caused the error. For more
information, see [Amazon ECS service quotas](service-quotas.md "service-quotas.md"). To request a quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## service (`service-name`)

was unable to place a task. Reason: You’ve reached the limit on the number of vCPUs you can
run concurrently

AWS Fargate is transitioning from task count-based quotas to vCPU-based quotas.

You can request a quota increase for Fargate vCPU-based quota. For more information,
see [Amazon ECS service quotas](service-quotas.md "service-quotas.md"). To request a Fargate quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## service

(`service-name`) was unable to reach steady state
because task set (`taskSet-ID`) was unable to scale in.
Reason: The number of protected tasks are more than the desired count of
tasks

The service has more protected tasks than the desirednumber of tasks. You can do one the
following:

- Wait until the protection on the current tasks expire, enabling them to be
  terminated.
- Determine which tasks can be stopped and use the `UpdateTaskProtection`
  API with the `protectionEnabled` option set to `false` to unset
  protection for these tasks.
- Increase the desired task count of the service to more than the number of protected
  tasks.

## service (`service-name`)

was unable to reach steady state. Reason: No Container Instances were found in your
capacity provider.

The service scheduler sends this event message when it couldn't find the available resources
to add another task. The possible causes for this are:

There is no capacity provider associated with the cluster

Use `describe-services` to verify that you have a
capacity provider associated with the cluster You can update the
capacity provider strategy for the service.

Verify that there is available capacity in the capacity provider,
In the case of EC2, make sure that the container
instances meet the task definition requirements.

No container instances were found in your cluster

If no container instances are registered in the cluster you attempt to run a task
in, you receive this error. You should add container instances to your cluster. For
more information, see [Launching an Amazon ECS Linux container
instance](launch_container_instance.md "launch_container_instance.md").

Not enough ports

If your task uses fixed host port mapping (for example, your task uses port 80 on
the host for a web server), you must have at least one container instance per task.
Only one container can use a single host port at a time. You should add container
instances to your cluster or reduce your number of desired tasks.

Too many ports registered

The closest matching container instance for task placement can't exceed the
maximum allowed reserved port limit of 100 host ports per container instance. Using
dynamic host port mapping may remediate the issue.

Port already in-use

The task definition of this task uses the same port in its port mapping as a task
already running on the container instance that was chosen. The service event
message would have the chosen container instance ID as part of the message
below.

```
The closest matching container-instance is already using a port required by your task.
```

Not enough memory

If your task definition specifies 1000 MiB of memory, and the container instances
in your cluster each have 1024 MiB of memory, you can only run one copy of this
task per container instance. You can experiment with less memory in your task
definition so that you could launch more than one task per container instance, or
launch more container instances into your cluster.

###### Note

If you are trying to maximize your resource utilization by providing your
tasks as much memory as possible for a particular instance type, see [Reserving Amazon ECS Linux container instance memory](memory-management.md "memory-management.md").

Not enough available ENI attachment points

Tasks that use the `awsvpc` network mode each receive their own
elastic network interface (ENI), which is attached to the container instance that
hosts it. Amazon EC2 instances have a limit to the number of ENIs that can be attached
to them, and there are no container instances in the cluster that have ENI capacity
available.

The ENI limit for individual container instances depends on the following
conditions:

- If you **have not** opted in to the
  `awsvpcTrunking` account setting, the ENI limit for each
  container instance depends on the instance type. For more information, see
  [IP Addresses Per Network
  Interface Per Instance Type](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the
  _Amazon EC2 User Guide_.
- If you **have** opted in to the
  `awsvpcTrunking` account setting but you **have not** launched new container instances using
  a supported instance type after opting in, the ENI limit for each container
  instance is still at the default value. For more information, see [IP Addresses Per Network Interface
  Per Instance Type](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the
  _Amazon EC2 User Guide_.
- If you **have** opted in to the
  `awsvpcTrunking` account setting and you **have** launched new container instances using a
  supported instance type after opting in, additional ENIs are available. For
  more information, see [Supported instances for
  increased Amazon ECS container network interfaces](eni-trunking-supported-instance-types.md "eni-trunking-supported-instance-types.md").

For more information about opting in to the `awsvpcTrunking` account
setting, see [Increasing Amazon ECS Linux container instance network
interfaces](container-instance-eni.md "container-instance-eni.md").

You can add container instances to your cluster to provide more available network
adapters.

Container instance missing required attribute

Some task definition parameters require a specific Docker remote API version to
be installed on the container instance. Others, such as the logging driver options,
require the container instances to register those log drivers with the
`ECS_AVAILABLE_LOGGING_DRIVERS` agent configuration variable. If
your task definition contains a parameter that requires a specific container
instance attribute, and you don't have any available container instances that can
satisfy this requirement, the task cannot be placed.

A common cause of this error is if your service is using tasks that use the
`awsvpc` network mode and EC2 and the
cluster you specified doesn't have a container instance registered to it in the
same subnet that was specified in the `awsvpcConfiguration` when the
service was created.

You can use the AWSSupport-TroubleshootECSContainerInstance runbook
to troubleshoot. The runbook reviews whether the user data for the
instance contains the correct cluster information, whether the instance
profile contains the required permissions, and network configuration
issues. For more information, see [AWSSupport-TroubleshootECSContainerInstance](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshoot-ecs-container-instance.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshoot-ecs-container-instance.md") in the
_AWS Systems Manager Automation runbook reference User
Guide_.

For more information on which attributes are required for specific task
definition parameters and agent configuration variables, see [Amazon ECS task definition parameters for Fargate](task_definition_parameters.md "task_definition_parameters.md") and [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").

## service (`service-name`)

was unable to place a task. Reason: Capacity is unavailable at this time. Please try again
later or in a different availability zone.

There is currently no available capacity to run your service on.

You can do one the following:

- Wait until the Fargate capacity or EC2 container instances become available.
- Relaunch the service and specify additional subnets.

## service (`service-name`)

deployment failed: tasks failed to start.

The tasks in your service failed to start.

For information about how to debug stopped tasks. see [Amazon ECS stopped tasks error messages](stopped-task-error-codes.md "stopped-task-error-codes.md").

## service (`service-name`)

Timed out waiting for Amazon ECS Agent to start. Please check logs at
/var/log/ecs/ecs-agent.log".

The Amazon ECS container agent on the closest matching container instance for task placement is
disconnected. If you can connect to the container instance with SSH, you can examine the agent
logs. For more information, see [Amazon ECS container agent log configuration parameters](ecs-agent-versions.md#agent-logs "ecs-agent-versions.md#agent-logs"). You
should also verify that the agent is running on the instance. If you are using the
Amazon ECS-optimized AMI, you can try stopping and restarting the agent with the following
command.

- For the Amazon ECS-optimized Amazon Linux 2 AMI

```
`sudo systemctl restart ecs`
```

- For the Amazon ECS-optimized Amazon Linux AMI

```
`sudo stop ecs && sudo start ecs`
```

## service (`service-name`) task set

(`taskSet-ID`) (task `task-id`) is not healthy in target-group
(`targetGroup-ARN)`) due to `TARGET GROUP IS NOT FOUND`.

The task set for the service is failing health checks because the target group isn't found. The message includes the task ID to help identify which specific task is failing health checks. You should
delete and recreate the service. Don't delete any Elastic Load Balancing target group unless the corresponding Amazon ECS service
is already deleted.

## service (`service-name`) task set

(`taskSet-ID`) (task `task-id`) is not healthy in target-group
(`targetGroup-ARN)`) due to `TARGET IS NOT FOUND`.

The task set for the service is failing health checks because the target isn't found. The message includes the task ID to help identify which specific task is failing health checks.

## IAM permissions policies have been misconfigured or changed, and ECS can no longer maintain your service

The service is unable to maintain tasks due to misconfigured or changed IAM permissions policies. The IAM role associated with your ECS service or tasks may be missing required permissions.

To resolve this issue, add the necessary permissions to the IAM role. For more information about managing IAM permissions policies, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

## IAM trust relationship has been misconfigured or changed, and ECS can no longer maintain your service

The service is unable to maintain tasks due to a misconfigured or changed IAM trust relationship. The IAM role associated with your ECS service or tasks may have an incorrect trust policy.

To resolve this issue, configure a trust policy for the role used in your task definition. For more information about creating trust policies for custom roles, see [Creating a role for a custom use case](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _IAM User Guide_.
