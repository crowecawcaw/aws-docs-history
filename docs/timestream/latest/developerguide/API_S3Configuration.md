For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# S3Configuration

The configuration that specifies an S3 location.

## Contents

**BucketName**

The bucket name of the customer S3 bucket.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 63.

Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`

Required: No

**EncryptionOption**

The encryption option for the customer S3 location. Options are S3 server-side encryption with an S3 managed key
or AWS managed key.

Type: String

Valid Values: `SSE_S3 | SSE_KMS`

Required: No

**KmsKeyId**

The AWS KMS key ID for the customer S3 location when encrypting with an AWS managed
key.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**ObjectKeyPrefix**

The object key preview for the customer S3 location.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 928.

Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/S3Configuration.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/S3Configuration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/S3Configuration.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/S3Configuration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/S3Configuration.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/S3Configuration.md")
