# Amazon EC2 container instance security

considerations for Amazon ECS

You should consider a single container instance and its access within your threat
model. For example, a single affected task might be able to leverage the IAM
permissions of a non-infected task on the same instance.

We recommend that you use the following to help prevent this:

- Do not use administrator privileges when running your tasks.
- Assign a task role with least-privileged access to your tasks.

The container agent automatically creates a token with a unique credential ID
which are used to access Amazon ECS resources.

- To prevent containers run by tasks that use the `awsvpc` network
  mode from accessing the credential information supplied to the Amazon EC2 instance
  profile, while still allowing the permissions that are provided by the task role
  set the `ECS_AWSVPC_BLOCK_IMDS` agent configuration variable to true
  in the agent configuration file and restart the agent.
- Use Amazon GuardDuty Runtime Monitoring to detect threats for clusters and containers within
  your AWS environment. Runtime Monitoring uses a GuardDuty security agent that adds
  runtime visibility into individual Amazon ECS workloads, for example, file access,
  process execution, and network connections. For more information, see [GuardDuty
  Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring.md "../../../guardduty/latest/ug/runtime-monitoring.md") in the _GuardDuty User
  Guide_.
