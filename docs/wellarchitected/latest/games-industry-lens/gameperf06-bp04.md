# GAMEPERF06-BP04 Implement log rotation and retention

policies

Establish log rotation and retention policies to manage the growth
of log data and optimize storage utilization.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Configure your game
servers to automatically rotate logs based on size or time
intervals. Define log retention policies in Amazon CloudWatch Logs
to automatically archive or delete older log data that is no
longer needed for active analysis or troubleshooting.
