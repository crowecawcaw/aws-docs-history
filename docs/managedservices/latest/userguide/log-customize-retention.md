# Altering CloudWatch log retention

You can change the log data retention setting for CloudWatch logs.

By default, logs are kept indefinitely and never expire. You can adjust the retention policy for each log group, keeping the indefinite retention, or
choosing a retention period between 10 years and one day. To view the allowed minimum retention period in AMS, see the AMS Technical Standards
document available through AWS Artifact. To access AWS Artifact, contact your CSDM for instructions or go to
[Getting Started with AWS Artifact](https://aws.amazon.com/artifact/getting-started/ "https://aws.amazon.com/artifact/getting-started/").

The CloudWatch Logs log retention feature deletes the log events in a stream based on retention policy. It doesn't delete log streams or log groups.
For general information, see the _Amazon CloudWatch Logs User Guide_
[What is Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

For information on customizing a log retention period, and to learn more, see
[Change Log Data Retention in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention").
