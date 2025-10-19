# UntagResource

Removes the specified tag or tags from the specified AWS CloudHSM cluster.


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM resource in a different AWS account.


## Request Syntax



```
{
   "ResourceId": "`string`",
   "TagKeyList": [ "`string`" ]
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[ResourceId](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**


The cluster identifier (ID) for the cluster whose tags you are removing. To find the
 cluster ID, use [DescribeClusters](API_DescribeClusters.md "API_DescribeClusters.md").


Type: String


Pattern: `(?:cluster|backup)-[2-7a-zA-Z]{11,16}`



Required: Yes




**[TagKeyList](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**


A list of one or more tag keys for the tags that you are removing. Specify only the tag
 keys, not the tag values.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 50 items.


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`



Required: Yes




## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CloudHsmAccessDeniedException** 


The request was rejected because the requester does not have permission to perform the
 requested operation.


HTTP Status Code: 400




**CloudHsmInternalFailureException** 


The request was rejected because of an AWS CloudHSM internal failure. The request can
 be retried.


HTTP Status Code: 500




**CloudHsmInvalidRequestException** 


The request was rejected because it is not a valid request.


HTTP Status Code: 400




**CloudHsmResourceNotFoundException** 


The request was rejected because it refers to a resource that cannot be
 found.


HTTP Status Code: 400




**CloudHsmServiceException** 


The request was rejected because an error occurred.


HTTP Status Code: 400




**CloudHsmTagException** 


The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/UntagResource")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/UntagResource")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/UntagResource")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/UntagResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/UntagResource")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/UntagResource")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/UntagResource")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/UntagResource")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/UntagResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/UntagResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/UntagResource")
