

# WAFLoggingParameters
<a name="API_WAFLoggingParameters"></a>

 Configuration parameters for WAF logging, including redacted fields and logging filters. 

## Contents
<a name="API_WAFLoggingParameters_Contents"></a>

 ** LoggingFilter **   <a name="cwoa-Type-WAFLoggingParameters-LoggingFilter"></a>
 A filter configuration that determines which WAF log records to include or exclude.   
Type: [LoggingFilter](API_LoggingFilter.md) object  
Required: No

 ** LogType **   <a name="cwoa-Type-WAFLoggingParameters-LogType"></a>
 The type of WAF logs to collect (currently supports WAF\_LOGS).   
Type: String  
Valid Values: `WAF_LOGS`   
Required: No

 ** RedactedFields **   <a name="cwoa-Type-WAFLoggingParameters-RedactedFields"></a>
 The fields to redact from WAF logs to protect sensitive information.   
Type: Array of [FieldToMatch](API_FieldToMatch.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: No

## See Also
<a name="API_WAFLoggingParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/WAFLoggingParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/WAFLoggingParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/WAFLoggingParameters) 