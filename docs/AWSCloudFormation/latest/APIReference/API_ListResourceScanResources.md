# ListResourceScanResources

Lists the resources from a resource scan. The results can be filtered by resource
 identifier, resource type prefix, tag key, and tag value. Only resources that match all
 specified filters are returned. The response indicates whether each returned resource is
 already managed by CloudFormation.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**MaxResults** 


If the number of available results exceeds this maximum, the response includes a
 `NextToken` value that you can use for the `NextToken` parameter to
 get the next set of results. By default the `ListResourceScanResources` API action
 will return at most 100 results in each response. The maximum value is 100.


Type: Integer


Required: No




**NextToken** 


A string that identifies the next page of resource scan results.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ResourceIdentifier** 


If specified, the returned resources will have the specified resource identifier (or one
 of them in the case where the resource has multiple identifiers).


Type: String


Required: No




**ResourceScanId** 


The Amazon Resource Name (ARN) of the resource scan.


Type: String


Required: Yes




**ResourceTypePrefix** 


If specified, the returned resources will be of any of the resource types with the
 specified prefix.


Type: String


Required: No




**TagKey** 


If specified, the returned resources will have a matching tag key.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Required: No




**TagValue** 


If specified, the returned resources will have a matching tag value.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




## Response Elements


The following elements are returned by the service.





**NextToken** 


If the request doesn't return all the remaining results, `NextToken` is set to
 a token. To retrieve the next set of results, call `ListResourceScanResources`
 again and use that value for the `NextToken` parameter. If the request returns all
 results, `NextToken` is set to an empty string.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**Resources.member.N**


List of up to `MaxResults` resources in the specified resource scan that match
 all of the specified filters.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListResourceScanResources")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/ListResourceScanResources")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListResourceScanResources")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListResourceScanResources")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListResourceScanResources")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListResourceScanResources")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListResourceScanResources")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListResourceScanResources")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListResourceScanResources")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListResourceScanResources "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListResourceScanResources")
