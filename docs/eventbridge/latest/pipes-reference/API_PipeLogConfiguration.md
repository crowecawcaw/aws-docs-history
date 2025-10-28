# PipeLogConfiguration

The logging configuration settings for the pipe.

## Contents

**CloudwatchLogsLogDestination**

The Amazon CloudWatch Logs logging configuration settings for the pipe.

Type: [CloudwatchLogsLogDestination](API_CloudwatchLogsLogDestination.md "API_CloudwatchLogsLogDestination.md") object

Required: No

**FirehoseLogDestination**

The Amazon Data Firehose logging configuration settings for the pipe.

Type: [FirehoseLogDestination](API_FirehoseLogDestination.md "API_FirehoseLogDestination.md") object

Required: No

**IncludeExecutionData**

Whether the execution data (specifically, the `payload`,
`awsRequest`, and `awsResponse` fields) is included in the log
messages for this pipe.

This applies to all log destinations for the pipe.

For more information, see [Including execution data in logs](../userguide/eb-pipes-logs.md#eb-pipes-logs-execution-data "../userguide/eb-pipes-logs.md#eb-pipes-logs-execution-data") in the _Amazon EventBridge User
Guide_.

Type: Array of strings

Valid Values: `ALL`

Required: No

**Level**

The level of logging detail to include. This applies to all log destinations for the pipe.

Type: String

Valid Values: `OFF | ERROR | INFO | TRACE`

Required: No

**S3LogDestination**

The Amazon S3 logging configuration settings for the pipe.

Type: [S3LogDestination](API_S3LogDestination.md "API_S3LogDestination.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeLogConfiguration.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeLogConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeLogConfiguration.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeLogConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeLogConfiguration.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeLogConfiguration.md")
