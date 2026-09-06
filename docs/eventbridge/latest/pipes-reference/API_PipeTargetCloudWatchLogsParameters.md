

# PipeTargetCloudWatchLogsParameters
<a name="API_PipeTargetCloudWatchLogsParameters"></a>

The parameters for using an CloudWatch Logs log stream as a target.

## Contents
<a name="API_PipeTargetCloudWatchLogsParameters_Contents"></a>

 ** LogStreamName **   <a name="eventbridge-Type-PipeTargetCloudWatchLogsParameters-LogStreamName"></a>
The name of the log stream.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** Timestamp **   <a name="eventbridge-Type-PipeTargetCloudWatchLogsParameters-Timestamp"></a>
A [ dynamic path parameter](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html) to a field in the payload containing the time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.   
The value cannot be a static timestamp as the provided timestamp would be applied to all events delivered by the Pipe, regardless of when they are actually delivered.  
If no dynamic path parameter is provided, the default value is the time the invocation is processed by the Pipe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `\$(\.[\w/_-]+(\[(\d+|\*)\])*)*`   
Required: No

## See Also
<a name="API_PipeTargetCloudWatchLogsParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeTargetCloudWatchLogsParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetCloudWatchLogsParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetCloudWatchLogsParameters) 