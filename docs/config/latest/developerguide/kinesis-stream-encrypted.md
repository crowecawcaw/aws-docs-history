

# kinesis-stream-encrypted
<a name="kinesis-stream-encrypted"></a>

Checks if Amazon Kinesis streams are encrypted at rest with server-side encryption. The rule is NON\_COMPLIANT for a Kinesis stream if 'StreamEncryption' is not present. 

**Context**: Server-side encryption is a feature in Amazon Kinesis Data Streams that automatically encrypts data before it's at rest by using an AWS KMS Key. Data is encrypted before it's written to the Kinesis stream storage layer, and decrypted after it's retrieved from storage. As a result, your data is encrypted at rest within the Kinesis Data Streams service. This can help you to meet regulatory requirements and enhance the security of your data. For more information, [Data Protection in Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html).

**Identifier:** KINESIS\_STREAM\_ENCRYPTED

**Resource Types:** AWS::Kinesis::Stream

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Israel (Tel Aviv), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1047c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).