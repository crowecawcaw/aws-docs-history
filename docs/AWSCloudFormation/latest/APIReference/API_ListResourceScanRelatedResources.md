# ListResourceScanRelatedResources

Lists the related resources for a list of resources from a resource scan. The response
 indicates whether each returned resource is already managed by CloudFormation.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**MaxResults** 


If the number of available results exceeds this maximum, the response includes a
 `NextToken` value that you can use for the `NextToken` parameter to
 get the next set of results. By default the `ListResourceScanRelatedResources` API
 action will return up to 100 results in each response. The maximum value is 100.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**NextToken** 


A string that identifies the next page of resource scan results.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**Resources.member.N**


The list of resources for which you want to get the related resources. Up to 100 resources
 can be provided.


Type: Array of [ScannedResourceIdentifier](API_ScannedResourceIdentifier.md "API_ScannedResourceIdentifier.md") objects


Required: Yes




**ResourceScanId** 


The Amazon Resource Name (ARN) of the resource scan.


Type: String


Required: Yes




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the request doesn't return all the remaining results, `NextToken` is set to
 a token. To retrieve the next set of results, call
 `ListResourceScanRelatedResources` again and use that value for the
 `NextToken` parameter. If the request returns all results, `NextToken`
 is set to an empty string.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**RelatedResources.member.N**


List of up to `MaxResults` resources in the specified resource scan related to
 the specified resources.


Type: Array of [ScannedResource](API_ScannedResource.md "API_ScannedResource.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**ResourceScanInProgress** 


A resource scan is currently in progress. Only one can be run at a time for an account in a Region.


HTTP Status Code: 400




**ResourceScanNotFound** 


The resource scan was not found.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListResourceScanRelatedResources")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListResourceScanRelatedResources")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListResourceScanRelatedResources")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListResourceScanRelatedResources")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListResourceScanRelatedResources")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListResourceScanRelatedResources")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListResourceScanRelatedResources")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListResourceScanRelatedResources")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListResourceScanRelatedResources")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListResourceScanRelatedResources "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListResourceScanRelatedResources")
