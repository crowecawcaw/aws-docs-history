

# PipeTargetHttpParameters
<a name="API_PipeTargetHttpParameters"></a>

These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.

## Contents
<a name="API_PipeTargetHttpParameters_Contents"></a>

 ** HeaderParameters **   <a name="eventbridge-Type-PipeTargetHttpParameters-HeaderParameters"></a>
The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.  
Type: String to string map  
Key Length Constraints: Minimum length of 0. Maximum length of 512.  
Key Pattern: `[!#$%&'*+-.^_`|~0-9a-zA-Z]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 512.  
Value Pattern: `[ \t]*[\x20-\x7E]+([ \t]+[\x20-\x7E]+)*[ \t]*|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`   
Required: No

 ** PathParameterValues **   <a name="eventbridge-Type-PipeTargetHttpParameters-PathParameterValues"></a>
The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards ("\*").  
Type: Array of strings  
Pattern: `(?!\s*$).+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`   
Required: No

 ** QueryStringParameters **   <a name="eventbridge-Type-PipeTargetHttpParameters-QueryStringParameters"></a>
The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.  
Type: String to string map  
Key Length Constraints: Minimum length of 0. Maximum length of 512.  
Key Pattern: `[^\x00-\x1F\x7F]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`   
Value Length Constraints: Minimum length of 0. Maximum length of 512.  
Value Pattern: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F]+|(\$(\.[\w/_-]+(\[(\d+|\*)\])*)*)`   
Required: No

## See Also
<a name="API_PipeTargetHttpParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeTargetHttpParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetHttpParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetHttpParameters) 