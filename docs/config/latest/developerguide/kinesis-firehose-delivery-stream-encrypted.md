

# kinesis-firehose-delivery-stream-encrypted
<a name="kinesis-firehose-delivery-stream-encrypted"></a>

Checks if Amazon Kinesis Data Firehose delivery streams are encrypted at rest with server-side encryption. The rule is NON\_COMPLIANT if a Kinesis Data Firehose delivery stream is not encrypted at rest with server-side encryption. 



**Identifier:** KINESIS\_FIREHOSE\_DELIVERY\_STREAM\_ENCRYPTED

**Resource Types:** AWS::KinesisFirehose::DeliveryStream

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), China (Ningxia) Region

**Parameters:**

kmsKeyArns (Optional)Type: CSV  
Comma-separated list of KMS Key Arns that are approved for Kinesis Firehose usage.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1043c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).