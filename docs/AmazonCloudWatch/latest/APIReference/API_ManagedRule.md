# ManagedRule

 Contains the information that's required to enable a managed Contributor Insights
 rule for an AWS resource.
 
 


## Contents





**ResourceARN** 


 The ARN of an AWS resource that has managed Contributor Insights
 rules. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**TemplateName** 


 The template name for the managed Contributor Insights rule, as returned by
 `ListManagedInsightRules`. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[0-9A-Za-z][\-\.\_0-9A-Za-z]{0,126}[0-9A-Za-z]`



Required: Yes




**Tags** 


 A list of key-value pairs that you can associate with a managed Contributor Insights
 rule. You can associate as many as 50 tags with a rule. Tags can help you organize and
 categorize your resources. You also can use them to scope user permissions by granting a
 user permission to access or change only the resources that have certain tag values. To
 associate tags with a rule, you must have the `cloudwatch:TagResource`
 permission in addition to the `cloudwatch:PutInsightRule` permission. If you
 are using this operation to update an existing Contributor Insights rule, any tags that
 you specify in this parameter are ignored. To change the tags of an existing rule, use
 `TagResource`. 


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ManagedRule "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ManagedRule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ManagedRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ManagedRule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ManagedRule "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ManagedRule")
