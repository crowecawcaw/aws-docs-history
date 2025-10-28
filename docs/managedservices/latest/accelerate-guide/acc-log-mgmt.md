# Log management in AMS Accelerate

AMS Accelerate configures supported AWS services to collect logs. These logs are used by AMS Accelerate to
ensure compliance and auditing of resources within your account.

AMS Accelerate provides a range of operational services to help you achieve operational excellence on AWS.
To gain a quick understanding of how AMS helps your teams achieve overall operational excellence in AWS Cloud with some of our key operational
capabilities including 24x7 helpdesk, proactive monitoring, security, patching, logging and backup, see
[AMS Reference Architecture Diagrams](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/AWS-managed-services-for-operational-excellence-ra.pdf "https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/AWS-managed-services-for-operational-excellence-ra.pdf").

###### Topics

- [Log management — AWS CloudTrail](#acc-lm-cloudtrail "#acc-lm-cloudtrail")
- [Log management — Amazon EC2](#acc-lm-ec2 "#acc-lm-ec2")
- [Log management — Amazon VPC Flow Logs](#acc-lm-vpc "#acc-lm-vpc")

## Log management — AWS CloudTrail

[AWS CloudTrail](https://aws.amazon.com/cloudtrail/features/ "https://aws.amazon.com/cloudtrail/features/") is a service that is used for account
governance: compliance, operational auditing, and risk auditing. With CloudTrail, you can log, continuously monitor, and
retain account activity related to actions across your AWS infrastructure.

AMS Accelerate requires AWS CloudTrail logging to manage audits and compliance for all resources
in your account. While onboarding, you can choose one of the following options:

- AMS deployed trail: If you choose this option, AMS creates, deploys, and manages a
  CloudTrail multi-Region trail in your primary AWS Region, independent of any existing trails
  in your account.
- Bring your own trail: If you choose to provide your own account or organization CloudTrail
  trail, then you must work with your Cloud Architect (CA) to make sure it meet required
  configurations for Accelerate. If you choose this option but don’t provide your own
  trail, then Accelerate automatically deploys its own CloudTrail trail to maintain continuous
  security and audit coverage. If you provide your own trail later, AMS removes its
  deployed trail to avoid redundancy and additional costs. This approach helps maintain a
  single active CloudTrail trail in your account and prevents duplicate logging costs.

###### Note

If your account has an existing CloudTrail trail and you have not specifically configured or requested an AMS managed trail during onboarding, AMS Accelerate automatically removes the AMS deployed trail from your account. This prevents duplicate logging, optimizes resource usage, and saves additional cost.

AMS Accelerate creates an Amazon S3 bucket for an Accelerate deployed CloudTrail trail as the events delivery destination and uses AWS Key Management Service (AWS KMS) encryption. Your trail events are accessed by AMS Accelerate
operators for investigation and diagnosis purposes. If the account already has an existing CloudTrail trail
enabled, this trail is in addition to that, if you chose to have Accelerate deploy an Accelerate managed trail during onboarding.

AMS Accelerate deploys AWS Config rules to ensure that your CloudTrail account trails, including an Accelerate deployed CloudTrail trail are correctly set up and encrypted. To learn more, see [AWS Config](https://aws.amazon.com/config/features/ "https://aws.amazon.com/config/features/"). These are the rules used, presented as links to the AWS documentation
describing them:

- [multi-region-cloudtrail-enabled](../../../config/latest/developerguide/multi-region-cloudtrail-enabled.md "../../../config/latest/developerguide/multi-region-cloudtrail-enabled.md").
  Checks that AMS Accelerate CloudTrail is properly set up with the correct configurations.
- [cloud-trail-encryption-enabled](../../../config/latest/developerguide/cloud-trail-encryption-enabled.md "../../../config/latest/developerguide/cloud-trail-encryption-enabled.md"). Checks that AWS CloudTrail is configured to use the
  server-side encryption (SSE) with AWS KMS customer master key (CMK) encryption.
- [cloud-trail-log-file-validation-enabled](../../../config/latest/developerguide/cloud-trail-log-file-validation-enabled.md "../../../config/latest/developerguide/cloud-trail-log-file-validation-enabled.md"). When enabled, checks that AWS CloudTrail
  creates a signed digest file with logs. We strongly recommend that you enable file
  validation on all trails.
- [s3-bucket-default-lock-enabled](../../../config/latest/developerguide/s3-bucket-default-lock-enabled.md "../../../config/latest/developerguide/s3-bucket-default-lock-enabled.md"). When
  enabled, checks that the Amazon S3 bucket has lock enabled.
- [s3-bucket-logging-enabled](../../../config/latest/developerguide/s3-bucket-logging-enabled.md "../../../config/latest/developerguide/s3-bucket-logging-enabled.md"). When enabled, checks whether logging is enabled for Amazon S3
  buckets.

AMS Accelerate uses AWS KMS to encrypt the logged events for an Accelerate deployed CloudTrail trail in your account. This key is controlled by, and is
accessible to, the account administrators, AMS Accelerate operators, and CloudTrail. For more information
about AWS KMS, see [AWS Key Management Service features](https://aws.amazon.com/kms/features/ "https://aws.amazon.com/kms/features/")
product documentation.

### Accessing and auditing CloudTrail logs

CloudTrail logs for an AMS Accelerate deployed CloudTrail trail are stored in an Amazon S3 bucket within your account. Trail data stored in the Amazon S3 bucket is
encrypted using a AWS KMS key created when CloudTrail resources are provisioned.

Amazon S3 buckets leverage a naming pattern of
**ams-a`aws account id`-cloudtrail-`AWS Region`**,
(example: **ams-a123456789-cloudtrail-us-east-1a**)
and all
the events are stored with the **AWS/CloudTrail** prefix. All access to the primary bucket is logged and
the log objects are encrypted and versioned for auditing purposes.

For more information about tracking changes and querying the logs, see [Tracking changes in your AMS Accelerate accounts](acc-change-record.md "acc-change-record.md").

### Protecting and retaining CloudTrail logs

AMS Accelerate enables Amazon S3 object locking with Governance Mode for an Accelerate deployed CloudTrail trail to
ensure that users can't overwrite or delete an object version or alter its lock settings
without special permissions. For more information, see [Amazon S3 object locking](../../../AmazonS3/latest/dev/object-lock.md "../../../AmazonS3/latest/dev/object-lock.md").

By default, all logs in this bucket are kept indefinitely. If you want to change the retention period, you can submit
a service request through the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to set up a different retention policy.

### Accessing Amazon EC2 logs

You can access Amazon EC2 instance logs by using the AWS Management Console. Logs produced by instances
and AWS services are available in CloudWatch Logs, which is available in each account managed by
AMS Accelerate. For information about accessing your logs, see the [CloudWatch Logs
documentation](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

### Retaining Amazon EC2 logs

Amazon EC2 instance logs are kept indefinitely, by default. If you want to change the retention period, you can submit
a service request through the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to set up a different retention policy.

## Log management — Amazon EC2

AMS Accelerate installs the CloudWatch agent on all Amazon EC2 instances that you have identified as AMS Accelerate-managed.
This agent sends system-level logs to Amazon CloudWatch Logs. For information, see
[What are
Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")

The following log files are sent to CloudWatch Logs, into a log group of the same name as the log. Within each log group, a
log stream is created for each Amazon EC2 instance, named according to the Amazon EC2 instance ID.

**Linux**

- /var/log/amazon/ssm/amazon-ssm-agent.log
- /var/log/amazon/ssm/errors.log
- /var/log/audit/audit.log
- /var/log/auth.log
- /var/log/cloud-init-output.log
- /var/log/cron
- /var/log/dnf.log
- /var/log/dpkg.log
- /var/log/maillog
- /var/log/messages
- /var/log/secure
- /var/log/spooler
- /var/log/syslog
- /var/log/yum.log
- /var/log/zypper.log

For more information, see [Manually Create or Edit
the CloudWatch Agent Configuration File](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md").

**Windows**

- AmazonSSMAgentLog
- AmazonCloudWatchAgentLog
- AmazonSSMErrorLog
- AmazonCloudFormationLog
- ApplicationEventLog
- EC2ConfigServiceEventLog
- MicrosoftWindowsAppLockerEXEAndDLLEventLog
- MicrosoftWindowsAppLockerMSIAndScriptEventLog
- MicrosoftWindowsGroupPolicyOperationalEventLog
- SecurityEventLog
- SystemEventLog

For more information, see [Quick Start: Enable Your Amazon EC2 Instances Running Windows Server 2016 to Send Logs to CloudWatch Logs Using
the CloudWatch Logs Agent](../../../AmazonCloudWatch/latest/logs/QuickStartWindows2016.md#send_logs_to_cwl_json "../../../AmazonCloudWatch/latest/logs/QuickStartWindows2016.md#send_logs_to_cwl_json").

## Log management — Amazon VPC Flow Logs

[VPC Flow
Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") is a feature that captures information about the IP traffic going
to and from network interfaces in your VPC. Flow log data can be published to Amazon
CloudWatch logs or Amazon S3. Flow log data collection does not affect network throughput or latency. You can create or
delete flow logs without any impact to network performance.

Flow logs can help you with a number of
tasks, such as:

- Diagnosing overly restrictive Security Group rules
- Monitoring traffic that reaches your instance
- Determining the direction of the traffic to and from the network interfaces

You do not have to enable VPC flow logs for each newly created VPC in Accelerate
accounts. AMS will automatically detect whether a VPC has a flow log using the [ams-nist-cis-vpc-flow-logs-enabled](../../../config/latest/developerguide/vpc-flow-logs-enabled.md "../../../config/latest/developerguide/vpc-flow-logs-enabled.md") Config rule. If VPC flow logs are not enabled,
AMS will automatically remediate it by creating a VPC flow log with [custom
fields](../../../vpc/latest/userguide/flow-logs.md#flow-logs-custom "../../../vpc/latest/userguide/flow-logs.md#flow-logs-custom"). Having these additional fields will enable AMS and customers to better
monitor VPC traffic, understand network dependencies, troubleshoot network connectivity
issues, and identify network threats.

For information on viewing and searching flow logs, see
[Work with flow logs](../../../vpc/latest/userguide/working-with-flow-logs.md "../../../vpc/latest/userguide/working-with-flow-logs.md").
