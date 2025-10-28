For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# AccountSettingsNotificationConfiguration

Configuration settings for notifications related to account settings.

## Contents

**RoleArn**

An Amazon Resource Name (ARN) that grants Timestream permission to publish notifications. This field is only visible if SNS Topic is provided when updating the account settings.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

**SnsConfiguration**

Details on SNS that are required to send the notification.

Type: [SnsConfiguration](API_query_SnsConfiguration.md "API_query_SnsConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/AccountSettingsNotificationConfiguration.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/AccountSettingsNotificationConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/AccountSettingsNotificationConfiguration.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/AccountSettingsNotificationConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/AccountSettingsNotificationConfiguration.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/AccountSettingsNotificationConfiguration.md")
