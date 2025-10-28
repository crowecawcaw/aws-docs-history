For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# S3ReportLocation

S3 report location for the scheduled query run.

## Contents

**BucketName**

S3 bucket name.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 63.

Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`

Required: No

**ObjectKey**

S3 key.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/S3ReportLocation.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/S3ReportLocation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/S3ReportLocation.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/S3ReportLocation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/S3ReportLocation.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/S3ReportLocation.md")
