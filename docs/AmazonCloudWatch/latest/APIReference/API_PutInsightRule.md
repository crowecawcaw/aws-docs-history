# PutInsightRule

Creates a Contributor Insights rule. Rules evaluate log events in a CloudWatch Logs
 log group, enabling you to find contributor data for the log events in that log group.
 For more information, see [Using Contributor
 Insights to Analyze High-Cardinality Data](../monitoring/ContributorInsights.md "../monitoring/ContributorInsights.md").

If you create a rule, delete it, and then re-create it with the same name, historical
 data from the first time the rule was created might not be available.


## Request Parameters





**ApplyOnTransformedLogs** 


Specify `true` to have this rule evaluate log events after they have been transformed by 
 [Log transformation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html"). If you specify `true`, then the log events in log groups that have transformers will 
 be evaluated by Contributor Insights after being transformed. Log groups that don't have
 transformers will still have their original log events evaluated by Contributor Insights.


The default is `false`



###### Note

If a log group has a transformer, and transformation fails for some log events, those log events won't be evaluated by
 Contributor Insights. For information about investigating log transformation failures, see
 [Transformation metrics and errors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Transformation-Errors-Metrics.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Transformation-Errors-Metrics.html").


Type: Boolean


Required: No




**RuleDefinition** 


The definition of the rule, as a JSON object. For details on the valid syntax, see
 [Contributor Insights Rule Syntax](../monitoring/ContributorInsights-RuleSyntax.md "../monitoring/ContributorInsights-RuleSyntax.md").


Type: String


Length Constraints: Minimum length of 1. Maximum length of 8192.


Pattern: `[\x00-\x7F]+`



Required: Yes




**RuleName** 


A unique name for the rule.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[\x20-\x7E]+`



Required: Yes




**RuleState** 


The state of the rule. Valid values are ENABLED and DISABLED.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 32.


Pattern: `[\x20-\x7E]+`



Required: No




**Tags** 


A list of key-value pairs to associate with the Contributor Insights rule. You can
 associate as many as 50 tags with a rule.


Tags can help you organize and categorize your resources. You can also use them to
 scope user permissions, by granting a user permission to access or change only the
 resources that have certain tag values.


To be able to associate tags with a rule, you must have the
 `cloudwatch:TagResource` permission in addition to the
 `cloudwatch:PutInsightRule` permission.


If you are using this operation to update an existing Contributor Insights rule, any
 tags you specify in this parameter are ignored. To change the tags of an existing rule,
 use [TagResource](API_TagResource.md "API_TagResource.md").


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




**LimitExceededException** 


The operation exceeded one or more limits.


HTTP Status Code: 400




**MissingParameter** 


An input parameter that is required is missing.





**message** 





HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutInsightRule")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/PutInsightRule")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutInsightRule")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutInsightRule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutInsightRule")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutInsightRule")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutInsightRule")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutInsightRule")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutInsightRule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutInsightRule "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutInsightRule")
