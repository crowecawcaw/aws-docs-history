# Monitor Amazon Data Lifecycle Manager policies

You can use the following features to monitor the lifecycle of your snapshots and AMIs.

###### Features

- [Console and AWS CLI](#monitor-console-cli "#monitor-console-cli")
- [Monitor Data Lifecycle Manager policies using EventBridge](monitor-cloudwatch-events.md "monitor-cloudwatch-events.md")
- [Monitor Data Lifecycle Manager policies using CloudWatch](monitor-dlm-cw-metrics.md "monitor-dlm-cw-metrics.md")
- [Logging Amazon Data Lifecycle Manager API Calls Using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")

## Console and AWS CLI

You can view your lifecycle policies using the Amazon EC2 console or the AWS CLI. Each snapshot and AMI created by a policy has a timestamp
and policy-related tags. You can filter snapshots and AMIs using these tags to verify that your backups are being created as you intend.
