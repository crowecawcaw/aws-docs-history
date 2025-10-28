# Protect your Amazon ECS tasks from being terminated by

scale-in events

You can use Amazon ECS task scale-in protection to protect your tasks from being terminated by
scale-in events from either service auto scaling or deployments.

Certain applications require a mechanism to safeguard mission-critical tasks from
termination by scale-in events during times of low utilization or during service
deployments. For example:

- You have a queue-processing asynchronous application such as a video transcoding
  job where some tasks need to run for hours even when cumulative service utilization
  is low.
- You have a gaming application that runs game servers as Amazon ECS tasks that need to
  continue running even if all users have logged-out to reduce start-up latency of a
  server reboot.
- When you deploy a new code version, you need tasks to continue running because it
  would be expensive to reprocess.
  To protect tasks that belong to your service from terminating in a scale-in event, set the
  `ProtectionEnabled` attribute to `true`. When you set `ProtectionEnabled` to true, tasks are
  protected for 2 hours by default. You can then customize the protection period by using the
  `ExpiresInMinutes` attribute. You can protect your tasks for a minimum of 1
  minute and up to a maximum of 2880 minutes (48 hours). If you're using the AWS CLI, you can specify the `--protection-enabled` option.

After a task finishes its requisite work, you can set the `ProtectionEnabled`
attribute to `false`, allowing the task to be terminated by subsequent scale-in
events. If you're using the AWS CLI, you can specify the `--no-protection-enabled` option.

## Task scale-in protection

mechanisms

You can set and get task scale-in protection using either the Amazon ECS container agent
endpoint or the Amazon ECS API.

- **Amazon ECS container agent endpoint**

We recommend using the Amazon ECS container agent endpoint for tasks that can
self-determine the need to be protected. Use this approach for queue-based
or job-processing workloads.

When a container starts processing work, for example by consuming an SQS
message, you can set the `ProtectionEnabled` attribute through the
task scale-in protection endpoint path
`$ECS_AGENT_URI/task-protection/v1/state` from within the
container. Amazon ECS will not terminate this task during scale-in events. After your
task finishes its work, you can clear the `ProtectionEnabled`
attribute using the same endpoint, making the task eligible for termination
during subsequent scale-in events.

For more information about the Amazon ECS container
agent endpoint, see [Amazon ECS task scale-in protection
endpoint](task-scale-in-protection-endpoint.md "task-scale-in-protection-endpoint.md").

- **Amazon ECS API**

You can use the Amazon ECS API to set and retrieve task scale-in protection if
your application has a component that tracks the status of active tasks. Use
`UpdateTaskProtection` to mark one or more tasks as protected.
Use `GetTaskProtection` to retrieve the protection status.

An example of this approach would be if your application is hosting game
server sessions as Amazon ECS tasks. When a user logs in to a session on the
server (task), you can mark the task as protected. After the user logs out,
you can either clear the protection specifically for this task or
periodically clear protection for similar tasks that no longer have active
sessions, depending on your requirement to keep idle servers.

For more information, see [UpdateTaskProtection](../APIReference/API_UpdateTaskProtection.md "../APIReference/API_UpdateTaskProtection.md") and [GetTaskProtection](../APIReference/API_GetTaskProtection.md "../APIReference/API_GetTaskProtection.md") in the _Amazon Elastic Container Service API Reference_.

You can combine both approaches. For example, use the Amazon ECS agent endpoint to set
task protection from within a container and use the Amazon ECS API to remove task
protection from your external controller service.

## Considerations

Consider the following points before using task scale-in protection:

- Task scale-in protection is only supported with tasks deployed from a service.
- Task scale-in protection is supported with tasks deployed from a service running on Amazon ECS Managed Instances.
- We recommend using the Amazon ECS container agent endpoint because the Amazon ECS agent
  has built-in retry mechanisms and a simpler interface.
- You can reset the task scale-in protection expiration period by calling
  `UpdateTaskProtection` for a task that already has protection
  turned on.
- Determine how long a task would need to complete its requisite work and set
  the `expiresInMinutes` property accordingly. If you set the
  protection expiration longer than necessary, then you will incur costs and face
  delays in the deployment of new tasks.
- Task scale-in protection is supported on Amazon ECS container agent
  `1.65.0` or later. You can add support for this feature on Amazon EC2 instances
  using older versions of the Amazon ECS container agent by updating the agent to
  the latest version. For more information, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").
- Deployment considerations:
  - If the service uses a rolling update, new tasks will be created but
    tasks running older version will not be terminated until
    `protectionEnabled` is cleared or expires. You can adjust
    the `maximumPercentage` parameter in deployment configuration
    to a value that allows new tasks to be created when old tasks are
    protected.
  - If a blue/green update is applied, the blue deployment with protected
    tasks will not be removed if tasks have `protectionEnabled`.
    Traffic will be diverted to the new tasks that come up and older tasks
    will only be removed when `protectionEnabled` is cleared or
    expires. Depending on the timeout of the CodeDeploy or CloudFormation updates,
    the deployment may timeout and the older Blue tasks may still be
    present.
  - If you use CloudFormation, the update-stack has a 3 hour timeout.
    Therefore, if you set your task protection for longer than 3 hours, then
    your CloudFormation deployment may result in failure and rollback.

  During the time your old tasks are protected, the CloudFormation stack
  shows `UPDATE_IN_PROGRESS`. If task scale-in protection is
  removed or expires within the 3 hour window, your deployment will
  succeed and move to the `UPDATE_COMPLETE` status. If the
  deployment is stuck in `UPDATE_IN_PROGRESS` for more than 3
  hours, it will fail and show `UPDATE_FAILED` state, and will
  then be rolled back to old task set.
  - Amazon ECS sends service events when protected tasks keep a deployment
    (rolling or blue/green) from reaching the steady state, so that you can
    take remedial actions. While trying to update the protection status of a
    task, if you receive a `DEPLOYMENT_BLOCKED` error message, it
    means the service has more protected tasks than the desired count of
    tasks for the service. To resolve this error, do one the
    following:
    - Wait for the current task protection to expire. Then set task
      protection.
    - Determine which tasks can be stopped. Then use
      `UpdateTaskProtection`with the
      `protectionEnabled` option set to
      `false` for these tasks.
    - Increase the desired task count of the service to more than
      the number of protected tasks.

## IAM permissions required for task

scale-in protection

The task must have the Amazon ECS task role with the following permissions:

- `ecs:GetTaskProtection`: Allows the Amazon ECS container agent to call
  `GetTaskProtection`.
- `ecs:UpdateTaskProtection`: Allows the Amazon ECS container agent to
  call `UpdateTaskProtection`.
