

# Security Hub CSPM controls for Amazon MQ
<a name="mq-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon MQ service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [MQ.2] ActiveMQ brokers should stream audit logs to CloudWatch
<a name="mq-2"></a>

**Related requirements:** NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-12, NIST.800-53.r5 SI-4, PCI DSS v4.0.1/10.3.3

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::AmazonMQ::Broker`

**AWS Config rule:** [`mq-cloudwatch-audit-log-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/mq-cloudwatch-audit-log-enabled.html) 

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon MQ ActiveMQ broker streams audit logs to Amazon CloudWatch Logs. The control fails if the broker doesn't stream audit logs to CloudWatch Logs.

By publishing ActiveMQ broker logs to CloudWatch Logs, you can create CloudWatch alarms and metrics that increase the visibility of security-related information.

### Remediation
<a name="mq-2-remediation"></a>

To stream ActiveMQ broker logs to CloudWatch Logs, see [ Configuring Amazon MQ for ActiveMQ logs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.html) in the *Amazon MQ Developer Guide*.

## [MQ.4] Amazon MQ brokers should be tagged
<a name="mq-4"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::AmazonMQ::Broker`

**AWS Config rule:** `tagged-amazonmq-broker` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an Amazon MQ broker has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the broker doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the broker isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="mq-4-remediation"></a>

To add tags to an Amazon MQ broker, see [Tagging resources](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-tagging.html) in the *Amazon MQ Developer Guide*.

## [MQ.5] ActiveMQ brokers should use active/standby deployment mode
<a name="mq-5"></a>

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Low

**Resource type:** `AWS::AmazonMQ::Broker`

**AWS Config rule:** [`mq-active-deployment-mode`](https://docs.aws.amazon.com/config/latest/developerguide/mq-active-deployment-mode.html) 

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the deployment mode for an Amazon MQ ActiveMQ broker is set to active/standby. The control fails if a single-instance broker (enabled by default) is set as the deployment mode.

Active/standby deployment provides high availability for your Amazon MQ ActiveMQ brokers in an AWS Region. The active/standby deployment mode includes two broker instances in two different Availability Zones, configured in a redundant pair. These brokers communicate synchronously with your application, which can reduce downtime and loss of data in the event of a failure.

### Remediation
<a name="mq-5-remediation"></a>

To create a new ActiveMQ broker with active/standby deployment mode, see [ Creating and configuring an ActiveMQ broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-creating-configuring-broker.html) in the *Amazon MQ Developer Guide*. For **Deployment mode**, choose **Active/standby broker**. You can't change the deployment mode for an existing broker. Instead, you must create a new broker and copy the settings over from the old broker.

## [MQ.6] RabbitMQ brokers should use cluster deployment mode
<a name="mq-6"></a>

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5

**Category:** Recover > Resilience > High availability

**Severity:** Low

**Resource type:** `AWS::AmazonMQ::Broker`

**AWS Config rule:** [`mq-rabbit-deployment-mode`](https://docs.aws.amazon.com/config/latest/developerguide/mq-rabbit-deployment-mode.html) 

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the deployment mode for an Amazon MQ RabbitMQ broker is set to cluster deployment. The control fails if a single-instance broker (enabled by default) is set as the deployment mode.

Cluster deployment provides high availability for your Amazon MQ RabbitMQ brokers in an AWS Region. The cluster deployment is a logical grouping of three RabbitMQ broker nodes, each with its own Amazon Elastic Block Store (Amazon EBS) volume and a shared state. The cluster deployment ensures that data is replicated to all nodes in the cluster, which can reduce downtime and loss of data in the event of a failure.

### Remediation
<a name="mq-6-remediation"></a>

To create a new RabbitMQ broker with cluster deployment mode, see [ Creating and connecting to a RabbitMQ broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/getting-started-rabbitmq.html) in the *Amazon MQ Developer Guide*. For **Deployment mode**, choose **Cluster deployment**. You can't change the deployment mode for an existing broker. Instead, you must create a new broker and copy the settings over from the old broker.