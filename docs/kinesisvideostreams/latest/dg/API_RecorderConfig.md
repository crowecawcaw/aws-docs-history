# RecorderConfig

The recorder configuration consists of the local `MediaSourceConfig` details that are used as
credentials to access the local media files streamed on the camera.

## Contents

**MediaSourceConfig**

The configuration details that consist of the credentials required
(`MediaUriSecretArn` and `MediaUriType`) to access the media files
streamed to the camera.

Type: [MediaSourceConfig](API_MediaSourceConfig.md "API_MediaSourceConfig.md") object

Required: Yes

**ScheduleConfig**

The configuration that consists of the `ScheduleExpression` and the
`DurationInMinutes` details that specify the scheduling to record from a camera, or
local media file, onto the Edge Agent. If the `ScheduleExpression` attribute is not provided,
then the Edge Agent will always be set to recording mode.

Type: [ScheduleConfig](API_ScheduleConfig.md "API_ScheduleConfig.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/RecorderConfig.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/RecorderConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/RecorderConfig.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/RecorderConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/RecorderConfig.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/RecorderConfig.md")
