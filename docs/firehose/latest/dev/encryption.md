

# Data protection in Amazon Data Firehose
<a name="encryption"></a>

Amazon Data Firehose encrypts all data in transit using TLS protocol. Furthermore, for data stored in interim storage during processing, Amazon Data Firehose encrypts data using [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) and verifies data integrity using checksum verification.

If you have sensitive data, you can enable server-side data encryption when you use Amazon Data Firehose. How you do this depends on the source of your data.

**Note**  
If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/).

## Server-side encryption with Kinesis Data Streams
<a name="sse-with-data-stream-as-source"></a>

When you send data from your data producers to your data stream, Kinesis Data Streams encrypts your data using an AWS Key Management Service (AWS KMS) key before storing the data at rest. When your Firehose stream reads the data from your data stream, Kinesis Data Streams first decrypts the data and then sends it to Amazon Data Firehose. Amazon Data Firehose buffers the data in memory based on the buffering hints that you specify. It then delivers it to your destinations without storing the unencrypted data at rest.

For information about how to enable server-side encryption for Kinesis Data Streams, see [Using Server-Side Encryption](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html) in the *Amazon Kinesis Data Streams Developer Guide*.

## Server-side encryption with Direct PUT or other data sources
<a name="sse-with-direct-put"></a>

If you send data to your Firehose stream using [PutRecord](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecord.html) or [PutRecordBatch](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html), or if you send the data using AWS IoT, Amazon CloudWatch Logs, or CloudWatch Events, you can turn on server-side encryption by using the [StartDeliveryStreamEncryption](https://docs.aws.amazon.com/firehose/latest/APIReference/API_StartDeliveryStreamEncryption.html) operation. 

To stop server-side-encryption, use the [StopDeliveryStreamEncryption](https://docs.aws.amazon.com/firehose/latest/APIReference/API_StopDeliveryStreamEncryption.html) operation.

You can also enable SSE when you create the Firehose stream. To do that, specify [DeliveryStreamEncryptionConfigurationInput](https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeliveryStreamEncryptionConfigurationInput.html) when you invoke [CreateDeliveryStream](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html).

To successfully use `CUSTOMER_MANAGED_CMK`, both the caller's IAM policy and the KMS key policy must allow `kms:GenerateDataKey` and `kms:Decrypt` operations. Firehose validates these permissions when you call PutRecord or PutRecordBatch with `CUSTOMER_MANAGED_CMK` encryption. Additionally, `kms:CreateGrant` permission is required when calling CreateDeliveryStream or StartDeliveryStreamEncryption with `CUSTOMER_MANAGED_CMK` encryption.

When the CMK is of type `CUSTOMER_MANAGED_CMK`, if the Amazon Data Firehose service is unable to decrypt records because of a `KMSNotFoundException`, a `KMSInvalidStateException`, a `KMSDisabledException`, or a `KMSAccessDeniedException`, the service waits up to 24 hours (the retention period) for you to resolve the problem. If the problem persists beyond the retention period, the service skips those records that have passed the retention period and couldn't be decrypted, and then discards the data. Amazon Data Firehose provides the following four CloudWatch metrics that you can use to track the four AWS KMS exceptions:
+ `KMSKeyAccessDenied`
+ `KMSKeyDisabled`
+ `KMSKeyInvalidState`
+ `KMSKeyNotFound`

For more information about these four metrics, see [Monitor Amazon Data Firehose with CloudWatch metrics](monitoring-with-cloudwatch-metrics.md).

**Important**  
To encrypt your Firehose stream, use symmetric CMKs. Amazon Data Firehose doesn't support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see [About Symmetric and Asymmetric CMKs](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html) in the AWS Key Management Service developer guide.

**Note**  
When you use a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) (CUSTOMER\_MANAGED\_CMK) to enable server-side encryption (SSE) for your Firehose stream, the Firehose service sets an encryption context whenever it uses your key. Since this encryption context represents an occurrence where a key owned by your AWS account was used, it is logged as part of AWS CloudTrail event logs for your AWS account. This encryption context is system generated by the Firehose service. Your application should not make any assumptions about the format or content of the encryption context set by the Firehose service.