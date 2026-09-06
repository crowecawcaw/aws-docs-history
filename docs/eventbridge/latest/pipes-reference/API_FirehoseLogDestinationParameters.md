

# FirehoseLogDestinationParameters
<a name="API_FirehoseLogDestinationParameters"></a>

The Amazon Data Firehose logging configuration settings for the pipe.

## Contents
<a name="API_FirehoseLogDestinationParameters_Contents"></a>

 ** DeliveryStreamArn **   <a name="eventbridge-Type-FirehoseLogDestinationParameters-DeliveryStreamArn"></a>
Specifies the Amazon Resource Name (ARN) of the Firehose delivery stream to which EventBridge delivers the pipe log records.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `(^arn:aws([a-z]|\-)*:firehose:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):deliverystream/[a-zA-Z0-9_.-]{1,64})`   
Required: Yes

## See Also
<a name="API_FirehoseLogDestinationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/FirehoseLogDestinationParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/FirehoseLogDestinationParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/FirehoseLogDestinationParameters) 