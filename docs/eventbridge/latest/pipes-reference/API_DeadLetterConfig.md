

# DeadLetterConfig
<a name="API_DeadLetterConfig"></a>

A `DeadLetterConfig` object that contains information about a dead-letter queue configuration.

## Contents
<a name="API_DeadLetterConfig_Contents"></a>

 ** Arn **   <a name="eventbridge-Type-DeadLetterConfig-Arn"></a>
The ARN of the specified target for the dead-letter queue.   
For Amazon Kinesis stream and Amazon DynamoDB stream sources, specify either an Amazon SNS topic or Amazon SQS queue ARN.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`   
Required: No

## See Also
<a name="API_DeadLetterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/DeadLetterConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/DeadLetterConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/DeadLetterConfig) 