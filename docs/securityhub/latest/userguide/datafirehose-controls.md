# Security Hub CSPM controls for Amazon Data Firehose

These Security Hub CSPM controls evaluate the Amazon Data Firehose service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [DataFirehose.1] Firehose delivery streams should be encrypted at rest

**Related requirements:** NIST.800-53.r5 AC-3,
NIST.800-53.r5 AU-3,
NIST.800-53.r5 SC-12,
NIST.800-53.r5 SC-13,
NIST.800-53.r5 SC-28

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::KinesisFirehose::DeliveryStream`

**AWS Config rule:**
[`kinesis-firehose-delivery-stream-encrypted`](../../../config/latest/developerguide/kinesis-firehose-delivery-stream-encrypted.md "../../../config/latest/developerguide/kinesis-firehose-delivery-stream-encrypted.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon Data Firehose delivery stream is encrypted at rest with server-side encryption.
This control fails if a Firehose delivery stream isn't encrypted at rest with server-side encryption.

Server-side encryption is a feature in Amazon Data Firehose delivery streams that automatically encrypts data before
it's at rest by using a key created in AWS Key Management Service (AWS KMS). Data is encrypted before it's written to the Data Firehose stream storage layer,
and decrypted after it’s retrieved from storage. This allows you to comply with regulatory requirements and enhance the security of your data.

### Remediation

To enable server-side encryption on Firehose delivery streams,, see [Data Protection in Amazon Data Firehose](../../../firehose/latest/dev/encryption.md "../../../firehose/latest/dev/encryption.md") in
the _Amazon Data Firehose Developer Guide_.
