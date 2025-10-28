# PipeLogConfigurationParameters

Specifies the logging configuration settings for the pipe.

When you call `UpdatePipe`, EventBridge updates the fields in the
`PipeLogConfigurationParameters` object atomically as one and overrides
existing values. This is by design. If you don't specify an optional field in any of the
AWS service parameters objects
(`CloudwatchLogsLogDestinationParameters`,
`FirehoseLogDestinationParameters`, or
`S3LogDestinationParameters`), EventBridge sets that field to its
system-default value during the update.

For example, suppose when you created the pipe you specified a Firehose stream
log destination. You then update the pipe to add an Amazon S3 log destination. In
addition to specifying the `S3LogDestinationParameters` for the new log
destination, you must also specify the fields in the
`FirehoseLogDestinationParameters` object in order to retain the Firehose stream log destination.

For more information on generating pipe log records, see [Log EventBridge
Pipes](eventbridge/latest/userguide/eb-pipes-logs.md "eventbridge/latest/userguide/eb-pipes-logs.md") in the _Amazon EventBridge User Guide_.

## Contents

**Level**

The level of logging detail to include. This applies to all log destinations for the pipe.

For more information, see [Specifying
EventBridge Pipes log level](../userguide/eb-pipes-logs.md#eb-pipes-logs-level "../userguide/eb-pipes-logs.md#eb-pipes-logs-level") in the _Amazon EventBridge User
Guide_.

Type: String

Valid Values: `OFF | ERROR | INFO | TRACE`

Required: Yes

**CloudwatchLogsLogDestination**

The Amazon CloudWatch Logs logging configuration settings for the pipe.

Type: [CloudwatchLogsLogDestinationParameters](API_CloudwatchLogsLogDestinationParameters.md "API_CloudwatchLogsLogDestinationParameters.md") object

Required: No

**FirehoseLogDestination**

The Amazon Data Firehose logging configuration settings for the pipe.

Type: [FirehoseLogDestinationParameters](API_FirehoseLogDestinationParameters.md "API_FirehoseLogDestinationParameters.md") object

Required: No

**IncludeExecutionData**

Specify `ALL` to include the execution data (specifically, the
`payload`, `awsRequest`, and `awsResponse` fields) in
the log messages for this pipe.

This applies to all log destinations for the pipe.

For more information, see [Including execution data in logs](../userguide/eb-pipes-logs.md#eb-pipes-logs-execution-data "../userguide/eb-pipes-logs.md#eb-pipes-logs-execution-data") in the _Amazon EventBridge User
Guide_.

By default, execution data is not included.

Type: Array of strings

Valid Values: `ALL`

Required: No

**S3LogDestination**

The Amazon S3 logging configuration settings for the pipe.

Type: [S3LogDestinationParameters](API_S3LogDestinationParameters.md "API_S3LogDestinationParameters.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeLogConfigurationParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeLogConfigurationParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeLogConfigurationParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeLogConfigurationParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeLogConfigurationParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeLogConfigurationParameters.md")
