

# Filter
<a name="API_Filter"></a>

 A single filter condition that specifies behavior, requirement, and matching conditions for WAF log records. 

## Contents
<a name="API_Filter_Contents"></a>

 ** Behavior **   <a name="cwoa-Type-Filter-Behavior"></a>
 The action to take for log records matching this filter (KEEP or DROP).   
Type: String  
Valid Values: `KEEP | DROP`   
Required: No

 ** Conditions **   <a name="cwoa-Type-Filter-Conditions"></a>
 The list of conditions that determine if a log record matches this filter.   
Type: Array of [Condition](API_Condition.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

 ** Requirement **   <a name="cwoa-Type-Filter-Requirement"></a>
 Whether the log record must meet all conditions (MEETS\_ALL) or any condition (MEETS\_ANY) to match this filter.   
Type: String  
Valid Values: `MEETS_ALL | MEETS_ANY`   
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/Filter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/Filter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/Filter) 