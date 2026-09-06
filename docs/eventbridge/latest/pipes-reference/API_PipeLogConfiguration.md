

# PipeLogConfiguration
<a name="API_PipeLogConfiguration"></a>

The logging configuration settings for the pipe.

## Contents
<a name="API_PipeLogConfiguration_Contents"></a>

 ** CloudwatchLogsLogDestination **   <a name="eventbridge-Type-PipeLogConfiguration-CloudwatchLogsLogDestination"></a>
The Amazon CloudWatch Logs logging configuration settings for the pipe.  
Type: [CloudwatchLogsLogDestination](API_CloudwatchLogsLogDestination.md) object  
Required: No

 ** FirehoseLogDestination **   <a name="eventbridge-Type-PipeLogConfiguration-FirehoseLogDestination"></a>
The Amazon Data Firehose logging configuration settings for the pipe.  
Type: [FirehoseLogDestination](API_FirehoseLogDestination.md) object  
Required: No

 ** IncludeExecutionData **   <a name="eventbridge-Type-PipeLogConfiguration-IncludeExecutionData"></a>
Whether the execution data (specifically, the `payload`, `awsRequest`, and `awsResponse` fields) is included in the log messages for this pipe.  
This applies to all log destinations for the pipe.  
For more information, see [Including execution data in logs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-execution-data) in the *Amazon EventBridge User Guide*.  
Type: Array of strings  
Valid Values: `ALL`   
Required: No

 ** Level **   <a name="eventbridge-Type-PipeLogConfiguration-Level"></a>
The level of logging detail to include. This applies to all log destinations for the pipe.  
Type: String  
Valid Values: `OFF | ERROR | INFO | TRACE`   
Required: No

 ** S3LogDestination **   <a name="eventbridge-Type-PipeLogConfiguration-S3LogDestination"></a>
The Amazon S3 logging configuration settings for the pipe.  
Type: [S3LogDestination](API_S3LogDestination.md) object  
Required: No

## See Also
<a name="API_PipeLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeLogConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeLogConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeLogConfiguration) 