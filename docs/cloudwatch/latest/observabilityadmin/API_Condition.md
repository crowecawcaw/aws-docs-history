

# Condition
<a name="API_Condition"></a>

 A single condition that can match based on WAF rule action or label name. 

## Contents
<a name="API_Condition_Contents"></a>

 ** ActionCondition **   <a name="cwoa-Type-Condition-ActionCondition"></a>
 Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.).   
Type: [ActionCondition](API_ActionCondition.md) object  
Required: No

 ** LabelNameCondition **   <a name="cwoa-Type-Condition-LabelNameCondition"></a>
 Matches log records based on WAF rule labels applied to the request.   
Type: [LabelNameCondition](API_LabelNameCondition.md) object  
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/Condition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/Condition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/Condition) 