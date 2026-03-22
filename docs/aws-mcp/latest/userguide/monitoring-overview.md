# Monitoring AWS MCP Server (Preview)

Monitoring is an important part of maintaining the reliability, availability, and
performance of AWS MCP Server (Preview) and your other AWS solutions. AWS provides the following monitoring
tools to watch AWS MCP Server (Preview), report when something is wrong, and take automatic actions when
appropriate:

- _Amazon CloudWatch_ monitors your AWS resources and the applications you
  run on AWS in real time. You can collect and track metrics, create customized dashboards,
  and set alarms that notify you or take actions when a specified metric reaches a threshold
  that you specify. AWS MCP Server (Preview) automatically publishes metrics to CloudWatch at no additional cost.
  For more information, see [AWS MCP Server (Preview) CloudWatch metrics](cloudwatch-metrics.md "cloudwatch-metrics.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
