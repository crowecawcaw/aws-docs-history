# Monitor AWS KMS keys

Monitoring is an important part of understanding the availability, state, and usage of your
AWS KMS keys in AWS KMS and maintaining the reliability, availability, and
performance of your AWS solutions. Collecting monitoring data from all the parts of your AWS
solution will help you debug a multipoint failure if one occurs. Before you start monitoring
your KMS keys, however, create a monitoring plan that includes answers to the following
questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What [monitoring tools](#monitoring-tools "#monitoring-tools") will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something happens?
  The next step is to monitor your KMS keys over time to establish a baseline for normal AWS KMS
  usage and expectations in your environment. As you monitor your KMS keys, store historical
  monitoring data so that you can compare it with current data, identify normal patterns and
  anomalies, and devise methods to address issues.

For example, you can monitor AWS KMS API activity and events that affect your KMS keys. When data
falls above or below your established norms, you might need to investigate or take corrective
action.

To establish a baseline for normal patterns, monitor the following items:

- AWS KMS API activity for _data plane_ operations. These are [cryptographic operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations") that use a KMS key, such as
  [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"), [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md"), [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md"), and [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md").
- AWS KMS API activity for _control plane_ operations that are important
  to you. These operations manage a KMS key, and you might want to monitor those that change a
  KMS key's availability (such as [ScheduleKeyDeletion](../APIReference/API_ScheduleKeyDeletion.md "../APIReference/API_ScheduleKeyDeletion.md"), [CancelKeyDeletion](../APIReference/API_CancelKeyDeletion.md "../APIReference/API_CancelKeyDeletion.md"), [DisableKey](../APIReference/API_DisableKey.md "../APIReference/API_DisableKey.md"), [EnableKey](../APIReference/API_EnableKey.md "../APIReference/API_EnableKey.md"),
  [ImportKeyMaterial](../APIReference/API_ImportKeyMaterial.md "../APIReference/API_ImportKeyMaterial.md"), and [DeleteImportedKeyMaterial](../APIReference/API_DeleteImportedKeyMaterial.md "../APIReference/API_DeleteImportedKeyMaterial.md"))
  or change a KMS key's access control (such as [PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md") and [RevokeGrant](../APIReference/API_RevokeGrant.md "../APIReference/API_RevokeGrant.md")).
- Other AWS KMS metrics (such as the amount of time remaining until your [imported key material](importing-keys.md "importing-keys.md") expires) and events (such as the
  expiration of imported key material or the deletion or key rotation of a KMS key).

## Monitoring tools

AWS provides various tools that you can use to monitor your KMS keys. You can configure some
of these tools to do the monitoring for you, while some of the tools require manual
intervention. We recommend that you automate monitoring tasks as much as possible.

### Automated monitoring tools

You can use the following automated monitoring tools to watch your KMS keys and report when
something has changed.

- **AWS CloudTrail Log Monitoring** – Share log files
  between accounts, monitor CloudTrail log files in real time by sending them to
  CloudWatch Logs, write log processing applications with the [CloudTrail Processing Library](../../../awscloudtrail/latest/userguide/use-the-cloudtrail-processing-library.md "../../../awscloudtrail/latest/userguide/use-the-cloudtrail-processing-library.md"), and validate that your log
  files have not changed after delivery by CloudTrail. For more information, see
  [Working with
  CloudTrail Log Files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the _AWS CloudTrail User Guide_.
- **Amazon CloudWatch Alarms** – Watch a single metric over a time period
  that you specify, and perform one or more actions based on the value of the metric relative
  to a given threshold over a number of time periods. The action is a notification sent to an
  Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. CloudWatch alarms do not invoke actions simply because
  they are in a particular state; the state must have changed and been maintained for a specified
  number of periods. For more information, see [Monitor KMS keys with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- **Amazon EventBridge** – Match events and route them to
  one or more target functions or streams to capture state information and, if necessary,
  make changes or take corrective action. For more information, see [Monitor KMS keys with Amazon EventBridge](kms-events.md "kms-events.md") and the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").
- **Amazon CloudWatch Logs** – Monitor, store, and access your
  log files from AWS CloudTrail or other sources. For more information, see the [Amazon CloudWatch Logs User
  Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").

### Manual monitoring tools

Another important part of monitoring KMS keys involves manually monitoring those items that
the CloudWatch alarms and events don't cover. The AWS KMS, CloudWatch, AWS Trusted Advisor, and other AWS
dashboards provide an at-a-glance view of the state of your AWS
environment.

You can [customize](viewing-console-customize.md#console-customize-tables "viewing-console-customize.md#console-customize-tables") the **AWS managed keys** and **Customer managed keys** pages of the [AWS KMS console](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms") to display the following information about
each KMS key:

- Key ID
- Status
- Creation date
- Expiration date (for KMS keys with [imported key
  material](importing-keys.md "importing-keys.md"))
- Origin
- Custom key store ID (for KMS keys in [custom key stores](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview"))

The [CloudWatch console dashboard](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home")
shows the following:

- Current alarms and status
- Graphs of alarms and resources
- Service health status

In addition, you can use CloudWatch to do the following:

- Create [customized
  dashboards](../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatch_Dashboards.md") to monitor the services you care about
- Graph metric data to troubleshoot issues and discover trends
- Search and browse all your AWS resource metrics
- Create and edit alarms to be notified of problems

AWS Trusted Advisor can help you monitor your AWS resources to improve performance,
reliability, security, and cost effectiveness. Four Trusted Advisor checks are available to all
users; more than 50 checks are available to users with a Business or Enterprise support
plan. For more information, see [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/ "https://aws.amazon.com/premiumsupport/trustedadvisor/").
