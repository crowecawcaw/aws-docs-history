# UploaderConfig

The configuration that consists of the `ScheduleExpression`
and the `DurationInMinutes` details that specify the scheduling to record from a camera,
or local media file, onto the Edge Agent. If the `ScheduleConfig`
is not provided in the `UploaderConfig`, then the Edge Agent will upload at regular intervals (every 1 hour).

## Contents

**ScheduleConfig**

The configuration that consists of the `ScheduleExpression` and the
`DurationInMinutes` details that specify the scheduling to record from a camera, or
local media file, onto the Edge Agent. If the `ScheduleConfig` is not provided in this `UploaderConfig`,
then the Edge Agent will upload at regular intervals (every 1 hour).

Type: [ScheduleConfig](API_ScheduleConfig.md "API_ScheduleConfig.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UploaderConfig.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/UploaderConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UploaderConfig.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/UploaderConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UploaderConfig.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/UploaderConfig.md")
