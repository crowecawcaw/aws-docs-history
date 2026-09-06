

# Security Hub CSPM controls for Amazon SNS
<a name="sns-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon Simple Notification Service (Amazon SNS) service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [SNS.1] SNS topics should be encrypted at-rest using AWS KMS
<a name="sns-1"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6), NIST.800-171.r2 3.13.11, NIST.800-171.r2 3.13.16

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:** `AWS::SNS::Topic`

**AWS Config rule:** [`sns-encrypted-kms`](https://docs.aws.amazon.com/config/latest/developerguide/sns-encrypted-kms.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SNS topic is encrypted at rest using keys managed in AWS Key Management Service (AWS KMS). The controls fails if the SNS topic doesn't use a KMS key for server-side encryption (SSE). By default, SNS stores messages and files using disk encryption. To pass this control, you must choose to use a KMS key for encryption instead. This adds an additional layer of security and provides more access control flexibility.

Encrypting data at rest reduces the risk of data stored on disk being accessed by a user not authenticated to AWS. API permissions are required to decrypt the data before it can be read. We recommend encrypting SNS topics with KMS keys for an added layer of security.

### Remediation
<a name="sns-1-remediation"></a>

To enable SSE for an SNS topic, see [Enabling server-side encryption (SSE) for an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-enable-encryption-for-topic.html) in the *Amazon Simple Notification Service Developer Guide*. Before you can use SSE, you must also configure AWS KMS key policies to allow encryption of topics and encryption and decryption of messages. For more information, see [Configuring AWS KMS permissions](https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html#sns-what-permissions-for-sse) in the *Amazon Simple Notification Service Developer Guide*.

## [SNS.2] Logging of delivery status should be enabled for notification messages sent to a topic
<a name="sns-2"></a>

**Important**  
Security Hub CSPM retired this control in April 2024. For more information, see [Change log for Security Hub CSPM controls](controls-change-log.md).

**Related requirements:** NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::SNS::Topic`

**AWS Config rule:** [`sns-topic-message-delivery-notification-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-message-delivery-notification-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether logging is enabled for the delivery status of notification messages sent to an Amazon SNS topic for the endpoints. This control fails if the delivery status notification for messages is not enabled.

Logging is an important part of maintaining the reliability, availability, and performance of services. Logging message delivery status helps provide operational insights, such as the following:
+ Knowing whether a message was delivered to the Amazon SNS endpoint.
+ Identifying the response sent from the Amazon SNS endpoint to Amazon SNS.
+ Determining the message dwell time (the time between the publish timestamp and the hand off to an Amazon SNS endpoint).

### Remediation
<a name="sns-2-remediation"></a>

To configure delivery status logging for a topic, see [Amazon SNS message delivery status](https://docs.aws.amazon.com/sns/latest/dg/sns-topic-attributes.html) in the *Amazon Simple Notification Service Developer Guide*.

## [SNS.3] SNS topics should be tagged
<a name="sns-3"></a>

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::SNS::Topic`

**AWS Config rule:** `tagged-sns-topic` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
|  requiredTagKeys  | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList (maximum of 6 items)  | 1–6 tag keys that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions).  |  No default value  | 

This control checks whether an Amazon SNS topic has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the topic doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the topic isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

**Note**  
Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-best-practices) in the *AWS General Reference*.

### Remediation
<a name="sns-3-remediation"></a>

To add tags to an SNS topic, see [Configuring Amazon SNS topic tags](https://docs.aws.amazon.com/sns/latest/dg/sns-tags-configuring.html) in the *Amazon Simple Notification Service Developer Guide*.

## [SNS.4] SNS topic access policies should not allow public access
<a name="sns-4"></a>

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** Critical

**Resource type:** `AWS::SNS::Topic`

**AWS Config rule:** [sns-topic-no-public-access](https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-no-public-access.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if the Amazon SNS topic access policy allows public access. This control fails if the SNS topic access policy allows public access.

You use an Amazon SNS access policy with a particular topic to restrict who can work with that topic (for example, who can publish messages to it or who can subscribe to it). SNS policies can grant access to other AWS accounts, or to users within your own AWS account. Providing a wildcard (\*) in the `Principal` field of the topic policy and a lack of conditions to limit the topic policy can result in data exfiltration, denial of service, or undesired injection of messages into your service by an attacker.

**Note**  
This control doesn't evaluate policy conditions that use wildcard characters or variables. To produce a `PASSED` finding, conditions in the Amazon SNS access policy for a topic must only use fixed values, which are values that don't contain wildcard characters or policy variables. For information about policy variables, see [Variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) in the *AWS Identity and Access Management User Guide*.

### Remediation
<a name="sns-4-remediation"></a>

To update access policies for an SNS topic, see [Overview of managing access in Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-overview-of-managing-access.html) in the *Amazon Simple Notification Service Developer Guide*.