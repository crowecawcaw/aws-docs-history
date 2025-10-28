# kinesis-stream-encrypted

Checks if Amazon Kinesis streams are encrypted at rest with server-side encryption. The rule is NON_COMPLIANT for a Kinesis stream if 'StreamEncryption' is not present.

**Context**: Server-side encryption is a feature in Amazon Kinesis Data Streams that automatically encrypts data before
it's at rest by using an AWS KMS Key. Data is encrypted before it's written to the Kinesis stream storage layer, and decrypted after it's retrieved from storage.
As a result, your data is encrypted at rest within the Kinesis Data Streams service. This can help you to meet regulatory requirements
and enhance the security of your data. For more information, [Data Protection in Amazon Kinesis Data Streams](../../../streams/latest/dev/server-side-encryption.md "../../../streams/latest/dev/server-side-encryption.md").

**Identifier:** KINESIS_STREAM_ENCRYPTED

**Resource Types:** AWS::Kinesis::Stream

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
