For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ProvisionedCapacityRequest

A request to update the provisioned capacity settings for querying data.

## Contents

**TargetQueryTCU**

The target compute capacity for querying data, specified in Timestream Compute Units (TCUs).

Type: Integer

Required: Yes

**NotificationConfiguration**

Configuration settings for notifications related to the provisioned capacity update.

Type: [AccountSettingsNotificationConfiguration](API_query_AccountSettingsNotificationConfiguration.md "API_query_AccountSettingsNotificationConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ProvisionedCapacityRequest.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ProvisionedCapacityRequest.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ProvisionedCapacityRequest.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ProvisionedCapacityRequest.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ProvisionedCapacityRequest.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ProvisionedCapacityRequest.md")
