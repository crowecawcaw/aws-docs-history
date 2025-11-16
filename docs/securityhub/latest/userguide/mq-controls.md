# Security Hub controls for Amazon MQ

These AWS Security Hub controls evaluate the Amazon MQ service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [MQ.2] ActiveMQ brokers should stream audit logs to CloudWatch

**Related requirements:** NIST.800-53.r5 AU-2,
NIST.800-53.r5 AU-3,
NIST.800-53.r5 AU-12,
NIST.800-53.r5 SI-4, PCI DSS v4.0.1/10.3.3

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::AmazonMQ::Broker`

**AWS Config rule:**
[`mq-cloudwatch-audit-log-enabled`](../../../config/latest/developerguide/mq-cloudwatch-audit-log-enabled.md "../../../config/latest/developerguide/mq-cloudwatch-audit-log-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon MQ ActiveMQ broker streams audit logs to Amazon CloudWatch Logs. The control fails if the broker
doesn't stream audit logs to CloudWatch Logs.

By publishing ActiveMQ broker logs to CloudWatch Logs, you can create CloudWatch alarms and metrics that increase the visibility of
security-related information.

### Remediation

To stream ActiveMQ broker logs to CloudWatch Logs, see [Configuring Amazon MQ for ActiveMQ logs](../../../amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.md "../../../amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.md") in the _Amazon MQ Developer Guide_.

## [MQ.3] Amazon MQ brokers should have automatic minor version upgrade enabled

**Related requirements:** NIST.800-53.r5 CM-3, NIST.800-53.r5 SI-2, PCI DSS v4.0.1/6.3.3

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** Medium

**Resource type:** `AWS::AmazonMQ::Broker`

**AWS Config rule:**
[`mq-auto-minor-version-upgrade-enabled`](../../../config/latest/developerguide/mq-auto-minor-version-upgrade-enabled.md "../../../config/latest/developerguide/mq-auto-minor-version-upgrade-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon MQ broker has automatic minor version upgrade enabled. The control fails if
the broker doesn't have automatic minor version upgrade enabled.

As Amazon MQ releases and supports new broker engine versions, the changes are backward-compatible with an existing
application and don't deprecate existing functionality. Automatic broker engine version updates protect you against security
risks, help fix bugs, and improve functionality.

###### Note

When the broker associated with automatic minor version upgrade is on its latest patch and becomes unsupported,
you must take manual action to upgrade.

### Remediation

To enable automatic minor version upgrade for an MQ broker, see [Automatically upgrading the minor engine version](../../../amazon-mq/latest/developer-guide/upgrading-brokers.md#upgrading-brokers-automatic-upgrades.html "../../../amazon-mq/latest/developer-guide/upgrading-brokers.md#upgrading-brokers-automatic-upgrades.html") in the _Amazon MQ Developer Guide_.

## [MQ.4] Amazon MQ brokers should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::AmazonMQ::Broker`

**AWS Config rule:** `tagged-amazonmq-broker` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`         |

This control checks whether an Amazon MQ broker has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the broker doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the broker isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an Amazon MQ broker, see [Tagging resources](../../../amazon-mq/latest/developer-guide/amazon-mq-tagging.md "../../../amazon-mq/latest/developer-guide/amazon-mq-tagging.md") in the _Amazon MQ Developer Guide_.

## [MQ.5] ActiveMQ brokers should use active/standby deployment mode

**Related requirements:** NIST.800-53.r5 CP-10,
NIST.800-53.r5 CP-6(2),
NIST.800-53.r5 SC-36,
NIST.800-53.r5 SC-5(2),
NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Low

**Resource type:** `AWS::AmazonMQ::Broker`

**AWS Config rule:**
[`mq-active-deployment-mode`](../../../config/latest/developerguide/mq-active-deployment-mode.md "../../../config/latest/developerguide/mq-active-deployment-mode.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the deployment mode for an Amazon MQ ActiveMQ broker is set to active/standby. The control
fails if a single-instance broker (enabled by default) is set as the deployment mode.

Active/standby deployment provides high availability for your Amazon MQ ActiveMQ brokers in an AWS Region. The
active/standby deployment mode includes two broker instances in two different Availability Zones, configured in a redundant pair.
These brokers communicate synchronously with your application, which can reduce downtime and loss of data in the event of a failure.

### Remediation

To create a new ActiveMQ broker with active/standby deployment mode, see [Creating and configuring an ActiveMQ broker](../../../amazon-mq/latest/developer-guide/amazon-mq-creating-configuring-broker.md "../../../amazon-mq/latest/developer-guide/amazon-mq-creating-configuring-broker.md") in the _Amazon MQ Developer Guide_. For
**Deployment mode**, choose **Active/standby broker**. You can't change the
deployment mode for an existing broker. Instead, you must create a new broker and copy the settings over from the old
broker.

## [MQ.6] RabbitMQ brokers should use cluster deployment mode

**Related requirements:** NIST.800-53.r5 CP-10,
NIST.800-53.r5 CP-6(2),
NIST.800-53.r5 SC-36,
NIST.800-53.r5 SC-5(2),
NIST.800-53.r5 SI-13(5

**Category:** Recover > Resilience > High availability

**Severity:** Low

**Resource type:** `AWS::AmazonMQ::Broker`

**AWS Config rule:**
[`mq-rabbit-deployment-mode`](../../../config/latest/developerguide/mq-rabbit-deployment-mode.md "../../../config/latest/developerguide/mq-rabbit-deployment-mode.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the deployment mode for an Amazon MQ RabbitMQ broker is set to cluster deployment. The
control fails if a single-instance broker (enabled by default) is set as the deployment mode.

Cluster deployment provides high availability for your Amazon MQ RabbitMQ brokers in an AWS Region. The cluster
deployment is a logical grouping of three RabbitMQ broker nodes, each with its own Amazon Elastic Block Store (Amazon EBS) volume and a shared state.
The cluster deployment ensures that data is replicated to all nodes in the cluster, which can reduce downtime and loss of data in
the event of a failure.

### Remediation

To create a new RabbitMQ broker with cluster deployment mode, see [Creating and connecting to a RabbitMQ broker](../../../amazon-mq/latest/developer-guide/getting-started-rabbitmq.md "../../../amazon-mq/latest/developer-guide/getting-started-rabbitmq.md") in the _Amazon MQ Developer Guide_. For
**Deployment mode**, choose **Cluster deployment**. You can't change the
deployment mode for an existing broker. Instead, you must create a new broker and copy the settings over from the old
broker.
