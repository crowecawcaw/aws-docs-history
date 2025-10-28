For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# NotificationConfiguration

Notification configuration for a scheduled query. A notification is sent by Timestream
when a scheduled query is created, its state is updated or when it is deleted.

## Contents

**SnsConfiguration**

Details about the Amazon Simple Notification Service (SNS) configuration. This field is visible only when SNS Topic is provided when updating the account settings.

Type: [SnsConfiguration](API_query_SnsConfiguration.md "API_query_SnsConfiguration.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/NotificationConfiguration.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/NotificationConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/NotificationConfiguration.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/NotificationConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/NotificationConfiguration.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/NotificationConfiguration.md")
