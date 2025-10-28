For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# LastUpdate

Configuration object that contains the most recent account settings update, visible only if settings have been updated previously.

## Contents

**Status**

The status of the last update. Can be either `PENDING`, `FAILED`, or `SUCCEEDED`.

Type: String

Valid Values: `PENDING | FAILED | SUCCEEDED`

Required: No

**StatusMessage**

Error message describing the last account settings update status, visible only if an error occurred.

Type: String

Required: No

**TargetQueryTCU**

The number of TimeStream Compute Units (TCUs) requested in the last account settings update.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/LastUpdate.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/LastUpdate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/LastUpdate.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/LastUpdate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/LastUpdate.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/LastUpdate.md")
