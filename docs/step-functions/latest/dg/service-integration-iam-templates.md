# How Step Functions generates IAM policies for integrated

services

When you create a state machine in the AWS Step Functions console, Step Functions produces an AWS Identity and Access Management
(IAM) policy based on the resources used in your state machine definition, as follows:

- For **optimized integrations**, Step Functions will create a policy with all the
  necessary permissions and roles for your state machine.

Tip: You can see example policies in each of the service pages under [Integrating optimized services](integrate-optimized.md "integrate-optimized.md").

- For **standard integrations** integrations, Step Functions will create an IAM role with partial permissions.

You must add any missing role policies that your state machine needs to interact with the service.

## Dynamic and static resources

_Static resources_ are defined **directly** in the task state of your state machine. When you include the information about the resources you want to call directly in your task states, Step Functions can create an IAM role for only those resources.

_Dynamic resources_ are **passed** as input when starting your state machine, or as input to an individual state, and accessed using JSONata or a JSONPath. When you are passing dynamic
resources to your task, Step Functions cannot automatically scope-down the permissions, so Step Functions will create a more permissive policy which specifies:`"Resource": "*"`.

## Additional permissions for tasks using .sync

Tasks that use the [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") pattern require additional permissions for monitoring and receiving
a response from the API of connected services.

Step Functions uses two approaches to monitor a job's status when a job is run on a connected
service: **polling** and **events**.

Polling requires permission for `Describe` or `Get` API actions. For example, for Amazon ECS the state machine must have allow permission for `ecs:DescribeTasks`, for AWS Glue the state machine requires allow permissions for `glue:GetJobRun`.
If the necessary permissions are missing from the role, Step Functions may be unable to determine the status
of your job. One reason for using the polling method is because some service integrations do not support EventBridge
events, and some services only send events on a best-effort basis.

Alternatively, you might use events sent from AWS services to Amazon EventBridge. Events are routed to Step Functions by EventBridge with a managed
rule, so the role requires permissions for `events:PutTargets`,
`events:PutRule`, and `events:DescribeRule`. If these
permissions are missing from the role, there may be a delay before Step Functions becomes aware
of the completion of your job. For more information about EventBridge events, see [Events from AWS services](../../../eventbridge/latest/userguide/eb-service-event.md "../../../eventbridge/latest/userguide/eb-service-event.md").

## Troubleshooting stuck .sync workflows

For Run a Job (.sync) tasks that support **both** polling and events, your task may
complete properly using events, even when the role lacks the required
permissions for polling.

In the previous scenario, you might not notice the
polling permissions are missing or incorrect. In the rare case that an event
fails to be delivered to or processed by Step Functions, your execution could become stuck.

To verify that your polling permissions are configured correctly, you can run an
execution in an environment without EventBridge events in the following ways

- Delete the managed rule in EventBridge that is responsible for forwarding
  events to Step Functions.

###### Note

Because managed rules are shared by all state machines in your
account, you should use a test or development
account to avoid unintentional impact to other state machines.

- You can
  identify the specific managed rule to delete by inspecting the
  `Resource` field used for `events:PutRule` in the
  policy template for the target service. The managed rule will be recreated
  the next time you create or update a state machine that uses that service
  integration.
- For more information on deleting EventBridge rules, see [Disabling or deleting a
  rule](../../../eventbridge/latest/userguide/eb-delete-rule.md "../../../eventbridge/latest/userguide/eb-delete-rule.md").

## Permissions for cancelling workflows

If a task that uses the Run a Job (.sync) pattern is stopped, Step Functions will make a best-effort
attempt to cancel the task.

Cancelling a task requires permission to `Cancel`,
`Stop`, `Terminate`, or `Delete` API actions, such
as `batch:TerminateJob` or `eks:DeleteCluster`. If these
permissions are missing from your role, Step Functions will be unable to cancel your task and you
may accrue additional charges while it continues to run. For more information on
stopping tasks, see [Run a Job](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync").

###### Learn more about integration patterns

To learn about synchronous tasks, see [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").
