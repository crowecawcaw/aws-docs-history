# GAMEREL03-BP03 Monitor infrastructure events over time to

measure impact on player behavior

Monitor your game server process, game server instance metrics,
and game experience metrics to determine the root cause of issues.
In addition to monitoring CPU and memory, you can also set up
monitoring for network metrics related to network limitations of
EC2 instances to alert you of issues such as exceeding bandwidth,
packets-per-second, or other network-level issues that may
indicate your server resources are under provisioned.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use CloudWatch Synthetics to check critical path application
functionality for player experience, such as being unable to login
or other service impacting issues. For game servers hosted using
Amazon GameLift, consider monitoring
[metrics](../../../gamelift/latest/developerguide/monitoring-cloudwatch.md "../../../gamelift/latest/developerguide/monitoring-cloudwatch.md")
like:

- GameServerInterruptions and InstanceInterruptions, which can
  assist in understanding how limitations in Spot instance
  availability are impacting your game servers deployed using
  Spot.
- ServerProcessAbnormalTerminations, which can be used to detect
  abnormal terminations in your game server processes.

It is recommended to maintain historical metrics data of your game
server reliability. Use this historical data for reporting
purposes and join it with other datasets to uncover potential
trends and assess the impact on player behavior over time that may
be due to game server issues.

Amazon CloudWatch does not retain metrics indefinitely, and
the [storage
resolution of metrics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") is increased over time, so consider
exporting these metrics to cost-effective long-term storage such
as Amazon S3. You can
configure [CloudWatch
Metric Streams](https://aws.amazon.com/blogs/aws/cloudwatch-metric-streams-send-aws-metrics-to-partners-and-to-your-apps-in-real-time/ "https://aws.amazon.com/blogs/aws/cloudwatch-metric-streams-send-aws-metrics-to-partners-and-to-your-apps-in-real-time/") to automatically deliver your metrics from
[CloudWatch
Regions](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Cross-Account-Methods.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Cross-Account-Methods.md") to your own S3 bucket, where they can be stored
long-term in a storage tier such as S3 Intelligent-Tiering and
eventually archived using Amazon Glacier. By placing your
metrics in Amazon S3, they are readily available to be joined with
other datasets in your data lake for interactive querying
with [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/").

### Implementation steps

- Monitor game server, instance, and network metrics,
  including bandwidth and packet-per-second limits, using
  Amazon CloudWatch and CloudWatch Synthetics for critical
  path functionality checks.
- Track GameLift-specific metrics like
  _GameServerInterruptions_ and
  _ServerProcessAbnormalTerminations_ to
  assess the impact of Spot instance availability and detect
  abnormal server terminations.
- Export CloudWatch metrics to Amazon S3 for long-term
  storage, use cost-effective tiers like S3
  Intelligent-Tiering or Glacier, and analyze trends with
  tools like Amazon Athena.

### Resources

- [Amazon EC2 instance-level network performance metrics uncover new
  insights](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-ec2-instance-level-network-performance-metrics-uncover-new-insights/ "https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-ec2-instance-level-network-performance-metrics-uncover-new-insights/")
- [CloudWatch
  Metric Streams – Send AWS Metrics to Partners and to Your
  Apps in Real Time](https://aws.amazon.com/blogs/aws/cloudwatch-metric-streams-send-aws-metrics-to-partners-and-to-your-apps-in-real-time/ "https://aws.amazon.com/blogs/aws/cloudwatch-metric-streams-send-aws-metrics-to-partners-and-to-your-apps-in-real-time/")
