# GAMEPERF07-BP04 Regularly monitor networking

performance

For competitive games, it is important to have a consistent player
experience.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

A game that is reliably 50ms for a larger player base
is fairer and more fun than a match where one player has 10ms ping
and another who has 70ms ping. ISP routing changes may impact part
of the player population, and your matchmaking system will need to
adapt.
[Amazon CloudWatch Network Monitoring](https://aws.amazon.com/cloudwatch/features/network-monitoring/ "https://aws.amazon.com/cloudwatch/features/network-monitoring/") assists in determining
whether the issue is with your game or the player internet
provider.

### Implementation steps

- Use Amazon Cloudwatch Network Monitoring to track network
  performance and identify routing issues.
- Use VPC Flow Logs to identify abnormal traffic patterns or
  dropped packets, which can indicate network congestion, ISP
  issues, or misconfigurations impacting player latency.
