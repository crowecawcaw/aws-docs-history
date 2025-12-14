# Logging and monitoring in AWS Key Management Service

Monitoring is an important part of understanding the availability, state, and usage of your
AWS KMS keys in AWS KMS. Monitoring helps maintain the security, reliability, availability, and
performance of your AWS solutions. AWS provides several tools for monitoring your
KMS keys.

**AWS CloudTrail Logs**

Every call to an AWS KMS API operation is captured as an event in an AWS CloudTrail log. These
logs record all API calls from the AWS KMS console, and calls made by AWS KMS and other AWS
services. Cross-account API calls, such as a call to use a KMS key in a different
AWS account, are recorded in the CloudTrail logs of both accounts.

When troubleshooting or auditing, you can use the log to reconstruct the lifecycle of
a KMS key. You can also view its management and use of the KMS key in cryptographic
operations. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**Amazon CloudWatch Logs**

Monitor, store, and access your log files from AWS CloudTrail and other sources. For more
information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

For AWS KMS, CloudWatch stores useful information that helps you to prevent problems with your
KMS keys and the resources that they protect. For more information, see [Monitor KMS keys with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

**Amazon EventBridge**

AWS KMS generates EventBridge events when your KMS key is [rotated](rotate-keys.md "rotate-keys.md") or [deleted](deleting-keys.md "deleting-keys.md") or the [imported key material](importing-keys.md "importing-keys.md") in your KMS key expires. Search
for AWS KMS events (API operations) and route them to one or more target functions or
streams to capture state information. For more information, see [Monitor KMS keys with Amazon EventBridge](kms-events.md "kms-events.md") and the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

**Amazon CloudWatch Metrics**

You can monitor your KMS keys using CloudWatch metrics, which collects and processes raw
data from AWS KMS into performance metrics. The data are recorded in two-week intervals so
you can view trends of current and historical information. This helps you to understand
how your KMS keys are used and how their use changes over time. For information about
using CloudWatch metrics to monitor KMS keys, see [AWS KMS metrics and dimensions](monitoring-cloudwatch.md#kms-metrics "monitoring-cloudwatch.md#kms-metrics").

**Amazon CloudWatch Alarms**

Watch a single metric change over a time period that you specify. Then perform actions
based on the value of the metric relative to a threshold over a number of time periods.
For example, you can create a CloudWatch alarm that is triggered when someone tries to use a
KMS key that is scheduled to be deleted in a cryptographic operation. This indicates
that the KMS key is still being used and probably should not be deleted. For more
information, see [Create an alarm that detects use of a
KMS key pending deletion](deleting-keys-creating-cloudwatch-alarm.md "deleting-keys-creating-cloudwatch-alarm.md").

**AWS Security Hub CSPM**

You can monitor your AWS KMS usage for security industry standards and best practices
compliance using AWS Security Hub CSPM. Security Hub CSPM uses security controls to evaluate resource
configurations and security standards to help you comply with various compliance
frameworks. For more information, see
[AWS Key Management Service controls](../../../securityhub/latest/userguide/kms-controls.md "../../../securityhub/latest/userguide/kms-controls.md") in the
_AWS Security Hub CSPM User Guide_.
