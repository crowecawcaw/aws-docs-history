For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ProvisionedCapacityResponse

The response to a request to update the provisioned capacity settings for querying data.

## Contents

**ActiveQueryTCU**

The number of Timestream Compute Units (TCUs) provisioned in the account. This field is only visible when the compute mode is `PROVISIONED`.

Type: Integer

Required: No

**LastUpdate**

Information about the last update to the provisioned capacity settings.

Type: [LastUpdate](API_query_LastUpdate.md "API_query_LastUpdate.md") object

Required: No

**NotificationConfiguration**

An object that contains settings for notifications that are sent whenever the provisioned capacity settings are modified. This field is only visible when the compute mode is `PROVISIONED`.

Type: [AccountSettingsNotificationConfiguration](API_query_AccountSettingsNotificationConfiguration.md "API_query_AccountSettingsNotificationConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ProvisionedCapacityResponse.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ProvisionedCapacityResponse.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ProvisionedCapacityResponse.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ProvisionedCapacityResponse.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ProvisionedCapacityResponse.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ProvisionedCapacityResponse.md")
