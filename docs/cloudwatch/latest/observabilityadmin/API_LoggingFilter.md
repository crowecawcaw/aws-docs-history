

# LoggingFilter
<a name="API_LoggingFilter"></a>

 Configuration that determines which WAF log records to keep or drop based on specified conditions. 

## Contents
<a name="API_LoggingFilter_Contents"></a>

 ** DefaultBehavior **   <a name="cwoa-Type-LoggingFilter-DefaultBehavior"></a>
 The default action (KEEP or DROP) for log records that don't match any filter conditions.   
Type: String  
Valid Values: `KEEP | DROP`   
Required: No

 ** Filters **   <a name="cwoa-Type-LoggingFilter-Filters"></a>
 A list of filter conditions that determine log record handling behavior.   
Type: Array of [Filter](API_Filter.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## See Also
<a name="API_LoggingFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/LoggingFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/LoggingFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/LoggingFilter) 