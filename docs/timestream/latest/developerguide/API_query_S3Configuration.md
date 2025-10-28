For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# S3Configuration

Details on S3 location for error reports that result from running a query.

## Contents

**BucketName**

Name of the S3 bucket under which error reports will be created.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 63.

Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`

Required: Yes

**EncryptionOption**

Encryption at rest options for the error reports. If no encryption option is
specified, Timestream will choose SSE_S3 as default.

Type: String

Valid Values: `SSE_S3 | SSE_KMS`

Required: No

**ObjectKeyPrefix**

Prefix for the error report key. Timestream by default adds the following prefix to
the error report path.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 896.

Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/S3Configuration.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/S3Configuration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/S3Configuration.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/S3Configuration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/S3Configuration.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/S3Configuration.md")
