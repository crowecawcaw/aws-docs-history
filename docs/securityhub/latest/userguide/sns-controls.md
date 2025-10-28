# Security Hub controls for Amazon SNS

These AWS Security Hub controls evaluate the Amazon Simple Notification Service (Amazon SNS) service and resources. The
controls might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [SNS.1] SNS topics should be encrypted at-rest using AWS KMS

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5
SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6), NIST.800-171.r2 3.13.11,
NIST.800-171.r2 3.13.16

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::SNS::Topic`

**AWS Config rule:**
[`sns-encrypted-kms`](../../../config/latest/developerguide/sns-encrypted-kms.md "../../../config/latest/developerguide/sns-encrypted-kms.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SNS topic is encrypted at rest using keys managed in
AWS Key Management Service (AWS KMS). The controls fails if the SNS topic doesn't use a KMS key for
server-side encryption (SSE). By default, SNS stores messages and files using disk
encryption. To pass this control, you must choose to use a KMS key for encryption
instead. This adds an additional layer of security and provides more access control
flexibility.

Encrypting data at rest reduces the risk of data stored on disk being accessed by a user
not authenticated to AWS. API permissions are required to decrypt the
data before it can be read. We recommend encrypting SNS topics with KMS keys for an added layer of
security.

### Remediation

To enable SSE for an SNS topic, see [Enabling server-side encryption (SSE) for an Amazon SNS topic](../../../sns/latest/dg/sns-enable-encryption-for-topic.md "../../../sns/latest/dg/sns-enable-encryption-for-topic.md") in the _Amazon Simple Notification Service Developer Guide_.
Before you can use SSE, you must also configure AWS KMS key policies to allow encryption of topics and encryption and decryption of
messages. For more information, see [Configuring AWS KMS permissions](../../../sns/latest/dg/sns-key-management.md#sns-what-permissions-for-sse "../../../sns/latest/dg/sns-key-management.md#sns-what-permissions-for-sse") in the _Amazon Simple Notification Service Developer Guide_.

## [SNS.2] Logging of delivery status should be enabled for notification messages sent to a topic

###### Important

Security Hub retired this control in April 2024.
For more information, see [Change log for Security Hub CSPM controls](controls-change-log.md "controls-change-log.md").

**Related requirements:** NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::SNS::Topic`

**AWS Config rule:**
[`sns-topic-message-delivery-notification-enabled`](../../../config/latest/developerguide/sns-topic-message-delivery-notification-enabled.md "../../../config/latest/developerguide/sns-topic-message-delivery-notification-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether logging is enabled for the delivery status of notification messages sent to an Amazon SNS topic for the endpoints.
This control fails if the delivery status notification for messages is not enabled.

Logging is an important part of maintaining the reliability, availability, and performance of services. Logging message delivery status helps
provide operational insights, such as the following:

- Knowing whether a message was delivered to the Amazon SNS endpoint.

- Identifying the response sent from the Amazon SNS endpoint to Amazon SNS.

- Determining the message dwell time (the time between the publish timestamp and the hand off to an Amazon SNS endpoint).

### Remediation

To configure delivery status logging for a topic, see [Amazon SNS message delivery status](../../../sns/latest/dg/sns-topic-attributes.md "../../../sns/latest/dg/sns-topic-attributes.md") in the _Amazon Simple Notification Service Developer Guide_.

## [SNS.3] SNS topics should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::SNS::Topic`

**AWS Config rule:** `tagged-sns-topic` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`         | This control checks whether an Amazon SNS topic has tags with the specific keys defined in the parameter `requiredTagKeys`. The control fails if the topic doesn’t have any tag keys or if it doesn’t have all the keys specified in the parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence of a tag key and fails if the topic isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`, are ignored. A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources. Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles) and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC policies to allow operations when the principal's tag matches the resource tag. For more information, see [What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. ###### Note Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including AWS Billing. For more tagging best practices, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the _AWS General Reference_. ### Remediation To add tags to an SNS topic, see [Configuring Amazon SNS topic tags](../../../sns/latest/dg/sns-tags-configuring.md "../../../sns/latest/dg/sns-tags-configuring.md") in the _Amazon Simple Notification Service Developer Guide_. ## [SNS.4] SNS topic access policies should not allow public access **Category:** Protect > Secure network configuration > Resources not publicly accessible **Severity:** High **Resource type:** `AWS::SNS::Topic` **AWS Config rule:** [sns-topic-no-public-access](../../../config/latest/developerguide/sns-topic-no-public-access.md "../../../config/latest/developerguide/sns-topic-no-public-access.md") **Schedule type:** Change triggered **Parameters:** None This control checks if the Amazon SNS topic access policy allows public access. This control fails if the SNS topic access policy allows public access. You use an Amazon SNS access policy with a particular topic to restrict who can work with that topic (for example, who can publish messages to it or who can subscribe to it). SNS policies can grant access to other AWS accounts, or to users within your own AWS account. Providing a wildcard (\*) in the `Principal` field of the topic policy and a lack of conditions to limit the topic policy can result in data exfiltration, denial of service, or undesired injection of messages into your service by an attacker. ###### Note This control doesn't evaluate policy conditions that use wildcard characters or variables. To produce a `PASSED` finding, conditions in the Amazon SNS access policy for a topic must only use fixed values, which are values that don't contain wildcard characters or policy variables. For information about policy variables, see [Variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _AWS Identity and Access Management User Guide_. ### Remediation To update access policies for an SNS topic, see [Overview of managing access in Amazon SNS](../../../sns/latest/dg/sns-overview-of-managing-access.md "../../../sns/latest/dg/sns-overview-of-managing-access.md") in the _Amazon Simple Notification Service Developer Guide_. |
