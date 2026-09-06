

# MQBrokerAccessCredentials
<a name="API_MQBrokerAccessCredentials"></a>

The AWS Secrets Manager secret that stores your broker credentials.

## Contents
<a name="API_MQBrokerAccessCredentials_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BasicAuth **   <a name="eventbridge-Type-MQBrokerAccessCredentials-BasicAuth"></a>
The ARN of the Secrets Manager secret.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`   
Required: No

## See Also
<a name="API_MQBrokerAccessCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/MQBrokerAccessCredentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/MQBrokerAccessCredentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/MQBrokerAccessCredentials) 