

# PipeLogConfigurationParameters
<a name="API_PipeLogConfigurationParameters"></a>

Specifies the logging configuration settings for the pipe.

When you call `UpdatePipe`, EventBridge updates the fields in the `PipeLogConfigurationParameters` object atomically as one and overrides existing values. This is by design. If you don't specify an optional field in any of the AWS service parameters objects (`CloudwatchLogsLogDestinationParameters`, `FirehoseLogDestinationParameters`, or `S3LogDestinationParameters`), EventBridge sets that field to its system-default value during the update. 

For example, suppose when you created the pipe you specified a Firehose stream log destination. You then update the pipe to add an Amazon S3 log destination. In addition to specifying the `S3LogDestinationParameters` for the new log destination, you must also specify the fields in the `FirehoseLogDestinationParameters` object in order to retain the Firehose stream log destination. 

For more information on generating pipe log records, see [Log EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html) in the *Amazon EventBridge User Guide*.

## Contents
<a name="API_PipeLogConfigurationParameters_Contents"></a>

 ** Level **   <a name="eventbridge-Type-PipeLogConfigurationParameters-Level"></a>
The level of logging detail to include. This applies to all log destinations for the pipe.  
For more information, see [Specifying EventBridge Pipes log level](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-level) in the *Amazon EventBridge User Guide*.  
Type: String  
Valid Values: `OFF | ERROR | INFO | TRACE`   
Required: Yes

 ** CloudwatchLogsLogDestination **   <a name="eventbridge-Type-PipeLogConfigurationParameters-CloudwatchLogsLogDestination"></a>
The Amazon CloudWatch Logs logging configuration settings for the pipe.  
Type: [CloudwatchLogsLogDestinationParameters](API_CloudwatchLogsLogDestinationParameters.md) object  
Required: No

 ** FirehoseLogDestination **   <a name="eventbridge-Type-PipeLogConfigurationParameters-FirehoseLogDestination"></a>
The Amazon Data Firehose logging configuration settings for the pipe.  
Type: [FirehoseLogDestinationParameters](API_FirehoseLogDestinationParameters.md) object  
Required: No

 ** IncludeExecutionData **   <a name="eventbridge-Type-PipeLogConfigurationParameters-IncludeExecutionData"></a>
Specify `ALL` to include the execution data (specifically, the `payload`, `awsRequest`, and `awsResponse` fields) in the log messages for this pipe.  
This applies to all log destinations for the pipe.  
For more information, see [Including execution data in logs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-execution-data) in the *Amazon EventBridge User Guide*.  
By default, execution data is not included.  
Type: Array of strings  
Valid Values: `ALL`   
Required: No

 ** S3LogDestination **   <a name="eventbridge-Type-PipeLogConfigurationParameters-S3LogDestination"></a>
The Amazon S3 logging configuration settings for the pipe.  
Type: [S3LogDestinationParameters](API_S3LogDestinationParameters.md) object  
Required: No

## See Also
<a name="API_PipeLogConfigurationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeLogConfigurationParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeLogConfigurationParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeLogConfigurationParameters) 