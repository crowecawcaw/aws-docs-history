# GAMEPERF06-BP01 Centralize log collection and storage

Implement a centralized log collection and storage solution to gather logs from game server
instances and GameLift.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Use services like Amazon CloudWatch Logs to collect, monitor, and store log data from your game
servers and GameLift instances. CloudWatch Logs provides a scalable and fully managed solution for log
management, facilitating efficient storage and retrieval of log data without impacting game
server performance. If you are running the [CloudWatch Logs agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md"), consider the
various install types and configuration options like batch size, buffer duration to minimize
impact to the game server. Consider the game server instances ephemeral and reduce dependency
on localized logging where possible. Establish a centralized policy for implementation of
[Logging best practices](../../../prescriptive-guidance/latest/logging-monitoring-for-application-owners/logging-best-practices.md "../../../prescriptive-guidance/latest/logging-monitoring-for-application-owners/logging-best-practices.md").

### Implementation steps

- Use Amazon CloudWatch Logs to collect, monitor, and store log data from game server instances
  and GameLift, facilitating centralized and scalable log management.
