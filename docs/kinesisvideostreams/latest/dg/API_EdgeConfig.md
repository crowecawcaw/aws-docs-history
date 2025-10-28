# EdgeConfig

A description of the stream's edge configuration that will be used to sync
with the Edge Agent IoT Greengrass component. The Edge Agent component will run
on an IoT Hub Device setup at your premise.

## Contents

**HubDeviceArn**

The "**Internet of Things (IoT) Thing**" Arn of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:iot:[a-z0-9-]+:[0-9]+:thing/[a-zA-Z0-9_.-]+`

Required: Yes

**RecorderConfig**

The recorder configuration consists of the local `MediaSourceConfig` details, that are used as
credentials to access the local media files streamed on the camera.

Type: [RecorderConfig](API_RecorderConfig.md "API_RecorderConfig.md") object

Required: Yes

**DeletionConfig**

The deletion configuration is made up of the retention time (`EdgeRetentionInHours`) and local size configuration
(`LocalSizeConfig`) details that are used to make the deletion.

Type: [DeletionConfig](API_DeletionConfig.md "API_DeletionConfig.md") object

Required: No

**UploaderConfig**

The uploader configuration contains the `ScheduleExpression` details that are used to
schedule upload jobs for the recorded media files from the Edge Agent to a Kinesis Video Stream.

Type: [UploaderConfig](API_UploaderConfig.md "API_UploaderConfig.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/EdgeConfig.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/EdgeConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/EdgeConfig.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/EdgeConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/EdgeConfig.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/EdgeConfig.md")
