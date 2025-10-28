# Removing Runtime Monitoring for Amazon ECS from an

account

When you no longer want to use Runtime Monitoring, disable the feature in GuardDuty. For
information about how to disable the feature, see [Enabling
Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring-configuration.md "../../../guardduty/latest/ug/runtime-monitoring-configuration.md") in the _Amazon GuardDuty User
Guide_.

GuardDuty performs the following operations:

- Deletes the VPC endpoints for GuardDuty for each VPC that hosts a
  cluster.
- No longer deploys the GuardDuty security agent to new standalone Fargate
  tasks, or new service deployments.

In order to preserve the immutability constraint, existing tasks and
deployments are not affected until they are stopped, replicated, or
scaled.

- Stops billing and no longer accepts run time events for tasks.
