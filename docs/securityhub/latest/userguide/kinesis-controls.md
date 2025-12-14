# Security Hub CSPM controls for Kinesis

These AWS Security Hub CSPM controls evaluate the Amazon Kinesis service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Kinesis.1] Kinesis streams should be encrypted at rest

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::Kinesis::Stream`

**AWS Config rule:**
[kinesis-stream-encrypted](../../../config/latest/developerguide/kinesis-stream-encrypted.md "../../../config/latest/developerguide/kinesis-stream-encrypted.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Kinesis Data Streams are encrypted at rest with server-side encryption. This control fails if a Kinesis stream is not encrypted
at rest with server-side encryption.

Server-side encryption is a feature in Amazon Kinesis Data Streams that automatically encrypts data before
it's at rest by using an AWS KMS key. Data is encrypted before it's written to
the Kinesis stream storage layer, and decrypted after it's retrieved from storage. As a
result, your data is encrypted at rest within the Amazon Kinesis Data Streams service.

### Remediation

For information about enabling server-side encryption for Kinesis streams, see [How do I get started with server-side encryption?](../../../streams/latest/dev/getting-started-with-sse.md "../../../streams/latest/dev/getting-started-with-sse.md") in
the _Amazon Kinesis Developer Guide_.

## [Kinesis.2] Kinesis streams should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Kinesis::Stream`

**AWS Configrule:** `tagged-kinesis-stream` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an Amazon Kinesis data stream has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the data stream doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the data stream isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to a Kinesis data stream, see [Tagging your streams in Amazon Kinesis Data Streams](../../../streams/latest/dev/tagging.md "../../../streams/latest/dev/tagging.md") in the _Amazon Kinesis Developer Guide_.

## [Kinesis.3] Kinesis streams should have an adequate data retention period

**Severity:** Medium

**Resource type:**
`AWS::Kinesis::Stream`

**AWS Configrule:** [kinesis-stream-backup-retention-check](../../../config/latest/developerguide/kinesis-stream-backup-retention-check.md "../../../config/latest/developerguide/kinesis-stream-backup-retention-check.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter                      | Description                                               | Type   | Allowed custom values | Security Hub CSPM default value |
| ------------------------------ | --------------------------------------------------------- | ------ | --------------------- | ------------------------------- |
| `minimumBackupRetentionPeriod` | Minimum number of hours that the data should be retained. | String | 24 to 8760            | 168                             |

This control checks whether an Amazon Kinesis data stream has a data retention period greater than or equal to the
specified time frame. The control fails if the data retention period is less than the specified time frame. Unless you provide a
custom parameter value for the data retention period, Security Hub CSPM uses a default value of 168 hours.

In Kinesis Data Streams, a data stream is an ordered sequence of data records meant to be written to and read from in
real time. Data records are stored in shards in your stream temporarily. The time period from when a record is added to when it is
no longer accessible is called the retention period. Kinesis Data Streams almost immediately makes records older than the new retention
period inaccessible after decreasing the retention period. For example, changing the retention period from 24 hours to 48 hours
means that records added to the stream 23 hours 55 minutes prior are still available after 24 hours.

### Remediation

To change the backup retention period for your Kinesis Data Streams, see [Change the data retention period](../../../streams/latest/dev/kinesis-extended-retention.md "../../../streams/latest/dev/kinesis-extended-retention.md")
in the _Amazon Kinesis Data Streams Developer Guide_.
