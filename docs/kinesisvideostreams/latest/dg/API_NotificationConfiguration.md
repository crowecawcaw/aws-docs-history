# NotificationConfiguration

Use this API to configure Amazon Simple Notification Service (Amazon SNS)
notifications for when fragments become available in a stream. If this parameter is
null, the configuration will be deleted from the stream.

See [Notifications in Kinesis
Video Streams](notifications.md "notifications.md") for more information.

## Contents

**DestinationConfig**

The destination information required to deliver a notification to a customer.

Type: [NotificationDestinationConfig](API_NotificationDestinationConfig.md "API_NotificationDestinationConfig.md") object

Required: Yes

**Status**

Indicates if a notification configuration is enabled or disabled.

Type: String

Valid Values: `ENABLED | DISABLED`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/NotificationConfiguration.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/NotificationConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/NotificationConfiguration.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/NotificationConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/NotificationConfiguration.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/NotificationConfiguration.md")
