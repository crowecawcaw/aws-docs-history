# ScheduleConfig

This API enables you to specify the duration that the camera,
or local media file, should record onto the Edge Agent. The `ScheduleConfig` consists of the `ScheduleExpression` and the
`DurationInMinutes` attributes.

If the `ScheduleConfig` is not provided in the `RecorderConfig`,
then the Edge Agent will always be set to recording mode.

If the `ScheduleConfig` is not provided in the `UploaderConfig`,
then the Edge Agent will upload at regular intervals (every 1 hour).

## Contents

**DurationInSeconds**

The total duration to record the media. If the `ScheduleExpression` attribute is provided, then the
`DurationInSeconds` attribute should also be specified.

Type: Integer

Valid Range: Minimum value of 60. Maximum value of 3600.

Required: Yes

**ScheduleExpression**

The Quartz cron expression that takes care of scheduling jobs to record from the
camera, or local media file, onto the Edge Agent. If the `ScheduleExpression` is not provided for the `RecorderConfig`,
then the Edge Agent will always be set to recording mode.

For more information about Quartz, refer to the
[_Cron Trigger Tutorial_](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html "https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html") page to understand the valid expressions and its use.

Type: String

Length Constraints: Minimum length of 11. Maximum length of 100.

Pattern: `[^\n]{11,100}`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ScheduleConfig.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ScheduleConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ScheduleConfig.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ScheduleConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ScheduleConfig.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ScheduleConfig.md")
