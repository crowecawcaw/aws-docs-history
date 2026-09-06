

# CloudwatchLogsLogDestinationParameters
<a name="API_CloudwatchLogsLogDestinationParameters"></a>

The Amazon CloudWatch Logs logging configuration settings for the pipe.

## Contents
<a name="API_CloudwatchLogsLogDestinationParameters_Contents"></a>

 ** LogGroupArn **   <a name="eventbridge-Type-CloudwatchLogsLogDestinationParameters-LogGroupArn"></a>
The AWS Resource Name (ARN) for the CloudWatch log group to which EventBridge sends the log records.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `(^arn:aws([a-z]|\-)*:logs:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):log-group:[\.\-_/#A-Za-z0-9]{1,512}(:\*)?)`   
Required: Yes

## See Also
<a name="API_CloudwatchLogsLogDestinationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/CloudwatchLogsLogDestinationParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/CloudwatchLogsLogDestinationParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/CloudwatchLogsLogDestinationParameters) 