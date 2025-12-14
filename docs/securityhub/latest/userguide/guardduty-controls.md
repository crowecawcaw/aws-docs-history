# Security Hub CSPM controls for Amazon GuardDuty

These AWS Security Hub CSPM controls evaluate the Amazon GuardDuty service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [GuardDuty.1] GuardDuty should be enabled

**Related requirements:** NIST.800-53.r5 AC-2(12),
NIST.800-53.r5 AU-6(1), NIST.800-53.r5 AU-6(5), NIST.800-53.r5 CA-7, NIST.800-53.r5
CM-8(3), NIST.800-53.r5 RA-3(4), NIST.800-53.r5 SA-11(1), NIST.800-53.r5 SA-11(6),
NIST.800-53.r5 SA-15(2), NIST.800-53.r5 SA-15(8), NIST.800-53.r5 SA-8(19),
NIST.800-53.r5 SA-8(21), NIST.800-53.r5 SA-8(25), NIST.800-53.r5 SC-5, NIST.800-53.r5
SC-5(1), NIST.800-53.r5 SC-5(3), NIST.800-53.r5 SI-20, NIST.800-53.r5 SI-3(8),
NIST.800-53.r5 SI-4, NIST.800-53.r5 SI-4(1), NIST.800-53.r5 SI-4(13), NIST.800-53.r5
SI-4(2), NIST.800-53.r5 SI-4(22), NIST.800-53.r5 SI-4(25), NIST.800-53.r5 SI-4(4),
NIST.800-53.r5 SI-4(5), NIST.800-171.r2 3.4.2, NIST.800-171.r2 3.14.6, NIST.800-171.r2
3.14.7, PCI DSS v3.2.1/11.4, PCI DSS v4.0.1/11.5.1

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::::Account`

**AWS Config rule:**
[guardduty-enabled-centralized](../../../config/latest/developerguide/guardduty-enabled-centralized.md "../../../config/latest/developerguide/guardduty-enabled-centralized.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Amazon GuardDuty is enabled in your GuardDuty account and Region.

It is highly recommended that you enable GuardDuty in all supported AWS Regions. Doing so
allows GuardDuty to generate findings about unauthorized or unusual activity, even in Regions that
you do not actively use. This also allows GuardDuty to monitor CloudTrail events for global AWS services
such as IAM.

### Remediation

To enable GuardDuty, see [Getting started with GuardDuty](../../../guardduty/latest/ug/guardduty_settingup.md "../../../guardduty/latest/ug/guardduty_settingup.md") in the _Amazon GuardDuty User Guide_.

## [GuardDuty.2] GuardDuty filters should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::GuardDuty::Filter`

**AWS Config rule:** `tagged-guardduty-filter` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`              |

This control checks whether an Amazon GuardDuty filter has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the filter doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the filter isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to a GuardDuty filter, see [TagResource](../../../guardduty/latest/APIReference/API_TagResource.md "../../../guardduty/latest/APIReference/API_TagResource.md") in the _Amazon GuardDuty API Reference_.

## [GuardDuty.3] GuardDuty IPSets should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::GuardDuty::IPSet`

**AWS Config rule:** `tagged-guardduty-ipset` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`              |

This control checks whether an Amazon GuardDuty IPSet has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the IPSet doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the IPSet isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to a GuardDuty IPSet, see [TagResource](../../../guardduty/latest/APIReference/API_TagResource.md "../../../guardduty/latest/APIReference/API_TagResource.md") in the _Amazon GuardDuty API Reference_.

## [GuardDuty.4] GuardDuty detectors should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::GuardDuty::Detector`

**AWS Config rule:** `tagged-guardduty-detector` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`              |

This control checks whether an Amazon GuardDuty detector has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the detector doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the detector isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to a GuardDuty detector, see [TagResource](../../../guardduty/latest/APIReference/API_TagResource.md "../../../guardduty/latest/APIReference/API_TagResource.md") in the _Amazon GuardDuty API Reference_.

## [GuardDuty.5] GuardDuty EKS Audit Log Monitoring should be enabled

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::GuardDuty::Detector`

**AWS Config rule:**
[guardduty-eks-protection-audit-enabled](../../../config/latest/developerguide/guardduty-eks-protection-audit-enabled.md "../../../config/latest/developerguide/guardduty-eks-protection-audit-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether GuardDuty EKS Audit Log Monitoring is enabled. For a standalone account, the control fails
if GuardDuty EKS Audit Log Monitoring is disabled in the account. In a multi-account environment, the control fails if the delegated GuardDuty
administrator account and all member accounts don't have EKS Audit Log Monitoring enabled.

In a multi-account environment, the control generates findings in only the delegated GuardDuty administrator account.
Only the delegated administrator can enable or disable the EKS Audit Log Monitoring feature for the member accounts in the
organization. GuardDuty member accounts can't modify this configuration from their accounts. This control generates `FAILED`
findings if the delegated GuardDuty administrator has a suspended member account that doesn't have GuardDuty EKS Audit Log Monitoring enabled.
To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in GuardDuty.

GuardDuty EKS Audit Log Monitoring helps you detect potentially suspicious activities in your Amazon Elastic Kubernetes Service (Amazon EKS) clusters.
EKS Audit Log Monitoring uses Kubernetes audit logs to capture chronological activities from users, applications using the Kubernetes API, and
the control plane.

### Remediation

To enable GuardDuty EKS Audit Log Monitoring, see
[EKS Audit Log Monitoring](../../../guardduty/latest/ug/guardduty-eks-audit-log-monitoring.md "../../../guardduty/latest/ug/guardduty-eks-audit-log-monitoring.md") in the _Amazon GuardDuty User Guide_.

## [GuardDuty.6] GuardDuty Lambda Protection should be enabled

**Related requirements:** PCI DSS v4.0.1/11.5.1

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::GuardDuty::Detector`

**AWS Config rule:**
[guardduty-lambda-protection-enabled](../../../config/latest/developerguide/guardduty-lambda-protection-enabled.md "../../../config/latest/developerguide/guardduty-lambda-protection-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether GuardDuty Lambda Protection is enabled. For a standalone account, the control fails
if GuardDuty Lambda Protection is disabled in the account. In a multi-account environment, the control fails if the delegated GuardDuty
administrator account and all member accounts don't have Lambda Protection enabled.

In a multi-account environment, the control generates findings in only the delegated GuardDuty administrator account.
Only the delegated administrator can enable or disable the Lambda Protection feature for the member accounts in the
organization. GuardDuty member accounts can't modify this configuration from their accounts. This control generates `FAILED`
findings if the delegated GuardDuty administrator has a suspended member account that doesn't have GuardDuty Lambda Protection enabled.
To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in GuardDuty.

GuardDuty Lambda Protection helps you identify potential security threats when an AWS Lambda function gets invoked.
After your enable Lambda Protection, GuardDuty starts monitoring Lambda network activity logs associated with the Lambda functions in your
AWS account. When a Lambda function gets invoked and GuardDuty identifies suspicious network traffic that indicates the presence of a
potentially malicious piece of code in your Lambda function, GuardDuty generates a finding.

### Remediation

To enable GuardDuty Lambda Protection, see
[Configuring Lambda Protection](../../../guardduty/latest/ug/configuring-lambda-protection.md "../../../guardduty/latest/ug/configuring-lambda-protection.md") in the _Amazon GuardDuty User Guide_.

## [GuardDuty.7] GuardDuty EKS Runtime Monitoring should be enabled

**Related requirements:** PCI DSS v4.0.1/11.5.1

**Category:** Detect > Detection Services

**Severity:** High

**Resource type:** `AWS::GuardDuty::Detector`

**AWS Config rule:**
[guardduty-eks-protection-runtime-enabled](../../../config/latest/developerguide/guardduty-eks-protection-runtime-enabled.md "../../../config/latest/developerguide/guardduty-eks-protection-runtime-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether GuardDuty EKS Runtime Monitoring with automated agent management is enabled. For a standalone
account, the control fails if GuardDuty EKS Runtime Monitoring with automated agent management is disabled in the account.
In a multi-account environment, the control fails if the delegated GuardDuty administrator account and all member accounts
don't have EKS Runtime Monitoring with automated agent management enabled.

In a multi-account environment, the control generates findings in only the delegated GuardDuty administrator account.
Only the delegated administrator can enable or disable the EKS Runtime Monitoring feature with automated agent management
for the member accounts in the organization. GuardDuty member accounts can't modify this configuration from their accounts. This control generates `FAILED`
findings if the delegated GuardDuty administrator has a suspended member account that doesn't have GuardDuty EKS Runtime Monitoring enabled.
To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in GuardDuty.

EKS Protection in Amazon GuardDuty provides threat detection coverage to help you protect Amazon EKS clusters within your AWS
environment. EKS Runtime Monitoring uses operating system-level events to help you detect potential threats in EKS
nodes and containers within your EKS clusters.

### Remediation

To enable EKS Runtime Monitoring with automated agent management, see [Enabling GuardDuty Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring-configuration.md "../../../guardduty/latest/ug/runtime-monitoring-configuration.md") in the _Amazon GuardDuty User Guide_.

## [GuardDuty.8] GuardDuty Malware Protection for EC2 should be enabled

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::GuardDuty::Detector`

**AWS Config rule:**
[guardduty-malware-protection-enabled](../../../config/latest/developerguide/guardduty-malware-protection-enabled.md "../../../config/latest/developerguide/guardduty-malware-protection-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether GuardDuty Malware Protection is enabled. For a standalone account, the control fails
if GuardDuty Malware Protection is disabled in the account. In a multi-account environment, the control fails if the delegated GuardDuty
administrator account and all member accounts don't have Malware Protection enabled.

In a multi-account environment, the control generates findings in only the delegated GuardDuty administrator account.
Only the delegated administrator can enable or disable the Malware Protection feature for the member accounts in the
organization. GuardDuty member accounts can't modify this configuration from their accounts. This control generates `FAILED`
findings if the delegated GuardDuty administrator has a suspended member account that doesn't have GuardDuty Malware Protection enabled.
To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in GuardDuty.

GuardDuty Malware Protection for EC2 helps you detect the potential presence of malware by scanning the Amazon Elastic Block Store (Amazon EBS) volumes that
are attached to Amazon Elastic Compute Cloud (Amazon EC2) instances and container workloads. Malware Protection provides scan options where you can decide
if you want to include or exclude specific EC2 instances and container workloads at the time of scanning. It also provides
an option to retain the snapshots of EBS volumes attached to the EC2 instances or container workloads, in your GuardDuty accounts.
The snapshots get retained only when malware is found and Malware Protection findings are generated.

### Remediation

To enable GuardDuty Malware Protection for EC2, see [Configuring GuardDuty-initiated malware scan](../../../guardduty/latest/ug/gdu-initiated-malware-scan-configuration.md "../../../guardduty/latest/ug/gdu-initiated-malware-scan-configuration.md") in the _Amazon GuardDuty User Guide_.

## [GuardDuty.9] GuardDuty RDS Protection should be enabled

**Related requirements:** PCI DSS v4.0.1/11.5.1

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::GuardDuty::Detector`

**AWS Config rule:**
[guardduty-rds-protection-enabled](../../../config/latest/developerguide/guardduty-rds-protection-enabled.md "../../../config/latest/developerguide/guardduty-rds-protection-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether GuardDuty RDS Protection is enabled. For a standalone account, the control fails
if GuardDuty RDS Protection is disabled in the account. In a multi-account environment, the control fails if the delegated GuardDuty
administrator account and all member accounts don't have RDS Protection enabled.

In a multi-account environment, the control generates findings in only the delegated GuardDuty administrator account.
Only the delegated administrator can enable or disable the RDS Protection feature for the member accounts in the
organization. GuardDuty member accounts can't modify this configuration from their accounts. This control generates `FAILED`
findings if the delegated GuardDuty administrator has a suspended member account that doesn't have GuardDuty RDS Protection enabled.
To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in GuardDuty.

RDS Protection in GuardDuty analyzes and profiles RDS login activity for potential access threats to your
Amazon Aurora databases (Aurora MySQL-Compatible Edition and Aurora PostgreSQL-Compatible Edition). This feature allows you to
identify potentially suspicious login behavior. RDS Protection doesn't require additional infrastructure; it is designed so as not
to affect the performance of your database instances. When RDS Protection detects a potentially suspicious or anomalous login
attempt that indicates a threat to your database, GuardDuty generates a new finding with details about the potentially compromised
database.

### Remediation

To enable GuardDuty RDS Protection, see [GuardDuty RDS Protection](../../../guardduty/latest/ug/rds-protection.md "../../../guardduty/latest/ug/rds-protection.md")
in the _Amazon GuardDuty User Guide_.

## [GuardDuty.10] GuardDuty S3 Protection should be enabled

**Related requirements:** PCI DSS v4.0.1/11.5.1

**Category:** Detect > Detection services

**Severity:** High

**Resource type:** `AWS::GuardDuty::Detector`

**AWS Config rule:**
[guardduty-s3-protection-enabled](../../../config/latest/developerguide/guardduty-s3-protection-enabled.md "../../../config/latest/developerguide/guardduty-s3-protection-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether GuardDuty S3 Protection is enabled. For a standalone account, the control fails
if GuardDuty S3 Protection is disabled in the account. In a multi-account environment, the control fails if the delegated GuardDuty
administrator account and all member accounts don't have S3 Protection enabled.

In a multi-account environment, the control generates findings in only the delegated GuardDuty administrator account.
Only the delegated administrator can enable or disable the S3 Protection feature for the member accounts in the
organization. GuardDuty member accounts can't modify this configuration from their accounts. This control generates `FAILED`
findings if the delegated GuardDuty administrator has a suspended member account that doesn't have GuardDuty S3 Protection enabled.
To receive a `PASSED` finding, the delegated administrator must disassociate these suspended accounts in GuardDuty.

S3 Protection enables GuardDuty to monitor object-level API operations to identify potential security risks for data
within your Amazon Simple Storage Service (Amazon S3) buckets. GuardDuty monitors threats against your S3 resources by analyzing AWS CloudTrail management events and
CloudTrail S3 data events.

### Remediation

To enable GuardDuty S3 Protection, see [Amazon S3 Protection in Amazon GuardDuty](../../../guardduty/latest/ug/s3-protection.md "../../../guardduty/latest/ug/s3-protection.md")
in the _Amazon GuardDuty User Guide_.

## [GuardDuty.11] GuardDuty Runtime Monitoring should be enabled

**Category:** Detect > Detection Services

**Severity:** High

**Resource type:** `AWS::GuardDuty::Detector`

**AWS Config rule:** [guardduty-runtime-monitoring-enabled](../../../config/latest/developerguide/guardduty-runtime-monitoring-enabled.md "../../../config/latest/developerguide/guardduty-runtime-monitoring-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Runtime Monitoring is enabled in Amazon GuardDuty. For a standalone account, the control fails
if GuardDuty Runtime Monitoring is disabled for the account. In a multi-account environment, the control fails if GuardDuty Runtime Monitoring is
disabled for the delegated GuardDuty administrator account and all member accounts.

In a multi-account environment, only the delegated GuardDuty administrator can enable or disable GuardDuty Runtime Monitoring for accounts in their
organization. In addition, only the GuardDuty administrator can configure and manage the security agents that GuardDuty uses for runtime monitoring of
AWS workloads and resources for accounts in the organization. GuardDuty member accounts can't enable, configure, or disable Runtime Monitoring for
their own accounts.

GuardDuty Runtime Monitoring observes and analyzes operating system-level, networking, and
file events to help you detect potential threats in specific AWS workloads in your
environment. It uses GuardDuty security agents that add visibility into runtime behavior,
such as file access, process execution, command line arguments, and network connections.
You can enable and manage the security agent for each type of resource that you want to
monitor for potential threats, such as Amazon EKS clusters and Amazon EC2 instances.

### Remediation

For information about configuring and enabling GuardDuty Runtime Monitoring, see [GuardDuty Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring.md "../../../guardduty/latest/ug/runtime-monitoring.md") and [Enabling GuardDuty Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring-configuration.md "../../../guardduty/latest/ug/runtime-monitoring-configuration.md") in the _Amazon GuardDuty User Guide_.

## [GuardDuty.12] GuardDuty ECS Runtime Monitoring should be enabled

**Category:** Detect > Detection Services

**Severity:** Medium

**Resource type:**
`AWS::GuardDuty::Detector`

**AWS Config rule:**
[guardduty-ecs-protection-runtime-enabled](../../../config/latest/developerguide/guardduty-ecs-protection-runtime-enabled.md "../../../config/latest/developerguide/guardduty-ecs-protection-runtime-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether the Amazon GuardDuty automated security agent is enabled for
runtime monitoring of Amazon ECS clusters on AWS Fargate. For a standalone account, the
control fails if the security agent is disabled for the account. In a multi-account
environment, the control fails if the security agent is disabled for the delegated GuardDuty
administrator account and all member accounts.

In a multi-account environment, this control generates findings only in the delegated
GuardDuty administrator account. This is because only the delegated GuardDuty administrator can
enable or disable Runtime Monitoring of ECS-Fargate resources for accounts in their
organization. GuardDuty member accounts can't do this for their own accounts. In addition,
this control generates `FAILED` findings if GuardDuty is suspended for a member
account and Runtime Monitoring of ECS-Fargate resources is disabled for the member
account. To receive a `PASSED` finding, the GuardDuty administrator must
disassociate the suspended member account from their administrator account by using
GuardDuty.

GuardDuty Runtime Monitoring observes and analyzes operating system-level, networking, and
file events to help you detect potential threats in specific AWS workloads in your
environment. It uses GuardDuty security agents that add visibility into runtime behavior,
such as file access, process execution, command line arguments, and network connections.
You can enable and manage the security agent for each type of resource that you want to
monitor for potential threats. This includes Amazon ECS clusters on AWS Fargate.

### Remediation

To enable and manage the security agent for GuardDuty Runtime Monitoring of
ECS-Fargate resources, you must use GuardDuty directly. You can't enable or manage it
manually for ECS-Fargate resources. For information about enabling and managing the
security agent, see [Prerequisites for AWS Fargate (Amazon ECS only) support](../../../guardduty/latest/ug/prereq-runtime-monitoring-ecs-support.md "../../../guardduty/latest/ug/prereq-runtime-monitoring-ecs-support.md") and [Managing the
automated security agent for AWS Fargate (Amazon ECS only)](../../../guardduty/latest/ug/managing-gdu-agent-ecs-automated.md "../../../guardduty/latest/ug/managing-gdu-agent-ecs-automated.md") in the
_Amazon GuardDuty User Guide_.

## [GuardDuty.13] GuardDuty EC2 Runtime Monitoring should be

enabled

**Category:** Detect > Detection Services

**Severity:** Medium

**Resource type:**
`AWS::GuardDuty::Detector`

**AWS Config rule:**
[guardduty-ec2-protection-runtime-enabled](../../../config/latest/developerguide/guardduty-ec2-protection-runtime-enabled.md "../../../config/latest/developerguide/guardduty-ec2-protection-runtime-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether the Amazon GuardDuty automated security agent is enabled for
runtime monitoring of Amazon EC2 instances. For a standalone account, the control fails if
the security agent is disabled for the account. In a multi-account environment, the
control fails if the security agent is disabled for the delegated GuardDuty administrator
account and all member accounts.

In a multi-account environment, this control generates findings only in the delegated
GuardDuty administrator account. This is because only the delegated GuardDuty administrator can
enable or disable Runtime Monitoring of Amazon EC2 instances for accounts in their
organization. GuardDuty member accounts can't do this for their own accounts. In addition,
this control generates `FAILED` findings if GuardDuty is suspended for a member
account and Runtime Monitoring of EC2 instances is disabled for the member
account. To receive a `PASSED` finding, the GuardDuty administrator must
disassociate the suspended member account from their administrator account by using
GuardDuty.

GuardDuty Runtime Monitoring observes and analyzes operating system-level, networking, and
file events to help you detect potential threats in specific AWS workloads in your
environment. It uses GuardDuty security agents that add visibility into runtime behavior,
such as file access, process execution, command line arguments, and network connections.
You can enable and manage the security agent for each type of resource that you want to
monitor for potential threats. This includes Amazon EC2 instances.

### Remediation

For information about configuring and managing the automated security agent for
GuardDuty Runtime Monitoring of EC2 instances, see [Prerequisites for Amazon EC2 instance support](../../../guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.md "../../../guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.md") and [Enabling the
automated security agent for Amazon EC2 instances](../../../guardduty/latest/ug/managing-gdu-agent-ec2-automated.md "../../../guardduty/latest/ug/managing-gdu-agent-ec2-automated.md") in the _Amazon GuardDuty User Guide_.
