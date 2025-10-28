# AwsKinesis resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsKinesis`
resources.

AWS Security Hub normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsKinesisStream

The `AwsKinesisStream` object provides details about Amazon Kinesis Data Streams.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsKinesisStream` object. To view descriptions of
`AwsKinesisStream` attributes, see [AwsKinesisStreamDetails](../../1.0/APIReference/API_AwsKinesisStreamDetails.md "../../1.0/APIReference/API_AwsKinesisStreamDetails.md") in the _AWS Security Hub API Reference_.

**Example**

```
"AwsKinesisStream": {
	"Name": "test-vir-kinesis-stream",
	"Arn": "arn:aws:kinesis:us-east-1:293279581038:stream/test-vir-kinesis-stream",
	"RetentionPeriodHours": 24,
	"ShardCount": 2,
	"StreamEncryption": {
		"EncryptionType": "KMS",
		"KeyId": "arn:aws:kms:us-east-1:293279581038:key/849cf029-4143-4c59-91f8-ea76007247eb"
	}
}
```
