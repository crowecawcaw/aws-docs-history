# PipeTargetCloudWatchLogsParameters

The parameters for using an CloudWatch Logs log stream as a target.

## Contents

**LogStreamName**

The name of the log stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**Timestamp**

A [dynamic path parameter](../userguide/eb-pipes-event-target.md "../userguide/eb-pipes-event-target.md") to a field in the payload containing the time the event
occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

The value cannot be a static timestamp as the provided timestamp would be applied to all
events delivered by the Pipe, regardless of when they are actually delivered.

If no dynamic path parameter is provided, the default value is the time the invocation is
processed by the Pipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\$(\.[\w/_-]+(\[(\d+|\*)\])*)*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetCloudWatchLogsParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetCloudWatchLogsParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetCloudWatchLogsParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetCloudWatchLogsParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetCloudWatchLogsParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetCloudWatchLogsParameters.md")
