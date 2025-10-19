# ListTagsForResource

Displays the tags associated with a CloudWatch resource. Currently, alarms and
 Contributor Insights rules support tagging.


## Request Parameters





**ResourceARN** 


The ARN of the CloudWatch resource that you want to view tags for.


The ARN format of an alarm is
 `arn:aws:cloudwatch:*Region*:*account-id*:alarm:*alarm-name*`



The ARN format of a Contributor Insights rule is
 `arn:aws:cloudwatch:*Region*:*account-id*:insight-rule/*insight-rule-name*`



For more information about ARN format, see  [Resource Types Defined by Amazon CloudWatch](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies") in the *Amazon Web
 Services General Reference*.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




## Response Elements


The following element is returned by the service.





**Tags** 


The list of tag keys and values associated with the resource you specified.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InternalServiceError** 


Request processing has failed due to some unknown error, exception, or
 failure.





**Message** 





HTTP Status Code: 500




**InvalidParameterValue** 


The value of an input parameter is bad or out-of-range.





**message** 





HTTP Status Code: 400




**ResourceNotFoundException** 


The named resource does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/ListTagsForResource")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/ListTagsForResource")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListTagsForResource")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/ListTagsForResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListTagsForResource")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/ListTagsForResource")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/ListTagsForResource")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/ListTagsForResource")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListTagsForResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListTagsForResource")
