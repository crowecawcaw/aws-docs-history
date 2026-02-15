# Monitoring AWS Backup

AWS Backup works with other AWS tools to empower you to monitor its workloads. These tools
include the following:

- [AWS Backup console dashboards](backup-dashboards.md "backup-dashboards.md")
  - The jobs dashboard brings job health monitoring, where you can view metrics showing
    job successes and failures, filtered by reasons, accounts, Region, and resource
    type.
  - The jobs dashboard is available in Regions where AWS Backup Audit Manager is supported.
    See [Feature availability by AWS Region](backup-feature-availability.md#features-by-region "backup-feature-availability.md#features-by-region") for those
    Regions. All other Regions will be able to access the [CloudWatch Dashboard](cloudwatch.md#cloudwatch-dashboard "cloudwatch.md#cloudwatch-dashboard").

- **Amazon CloudWatch** and **Amazon EventBridge**
  to monitor AWS Backup processes.
  - You can use CloudWatch to track metrics, create alarms, and view dashboards. For more information, see [AWS Backup metrics with Amazon CloudWatch](cloudwatch.md "cloudwatch.md").
  - You can use EventBridge to view and monitor AWS Backup events. For more information, see [Monitoring AWS Backup events using Amazon EventBridge](eventbridge.md "eventbridge.md").

- **AWS CloudTrail** to monitor AWS Backup API calls. You can identify
  the time, source IP, users, and accounts making those calls. For more information, see [Logging AWS Backup API calls with CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- **Amazon Simple Notification Service** (Amazon SNS) to subscribe to AWS Backup-related topics
  such as backup, restore, and copy events. For more information, see [Notification options with AWS Backup](backup-notifications.md "backup-notifications.md").
