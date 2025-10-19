# TagResource

Assigns one or more tags (key-value pairs) to the specified CloudWatch resource.
 Currently, the only CloudWatch resources that can be tagged are alarms and Contributor
 Insights rules.

Tags can help you organize and categorize your resources. You can also use them to
 scope user permissions by granting a user permission to access or change only resources
 with certain tag values.

Tags don't have any semantic meaning to AWS and are interpreted
 strictly as strings of characters.

You can use the `TagResource` action with an alarm that already has tags.
 If you specify a new tag key for the alarm, this tag is appended to the list of tags
 associated with the alarm. If you specify a tag key that is already associated with the
 alarm, the new tag value that you specify replaces the previous value for that
 tag.

You can associate as many as 50 tags with a CloudWatch resource.


## Request Parameters





**ResourceARN** 


The ARN of the CloudWatch resource that you're adding tags to.


The ARN format of an alarm is
 `arn:aws:cloudwatch:*Region*:*account-id*:alarm:*alarm-name*`



The ARN format of a Contributor Insights rule is
 `arn:aws:cloudwatch:*Region*:*account-id*:insight-rule/*insight-rule-name*`



For more information about ARN format, see  [Resource Types Defined by Amazon CloudWatch](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies") in the *Amazon Web
 Services General Reference*.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: Yes




**Tags** 


The list of key-value pairs to associate with the alarm.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: Yes




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ConcurrentModificationException** 


More than one process tried to modify a resource at the same time.


HTTP Status Code: 429




**ConflictException** 


This operation attempted to create a resource that already exists.


HTTP Status Code: 409




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/TagResource")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/DotNetSDKV3/monitoring-2010-08-01/TagResource")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/TagResource")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/TagResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/TagResource")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/TagResource")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/TagResource")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/TagResource")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/TagResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/TagResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/TagResource")
