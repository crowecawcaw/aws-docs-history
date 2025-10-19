# GetNetworkResourceCounts

Gets the count of network resources, by resource type, for the specified global network.


## Request Syntax



```
GET /global-networks/`globalNetworkId`/network-resource-count?maxResults=`MaxResults`&nextToken=`NextToken`&resourceType=`ResourceType` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[globalNetworkId](#API_GetNetworkResourceCounts_RequestSyntax "#API_GetNetworkResourceCounts_RequestSyntax")**


The ID of the global network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[MaxResults](#API_GetNetworkResourceCounts_RequestSyntax "#API_GetNetworkResourceCounts_RequestSyntax")**


The maximum number of results to return.


Valid Range: Minimum value of 1. Maximum value of 500.




**[NextToken](#API_GetNetworkResourceCounts_RequestSyntax "#API_GetNetworkResourceCounts_RequestSyntax")**


The token for the next page of results.


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





**[ResourceType](#API_GetNetworkResourceCounts_RequestSyntax "#API_GetNetworkResourceCounts_RequestSyntax")**


The resource type.


The following are the supported resource types for AWS Direct Connect:



* `dxcon`
* `dx-gateway`
* `dx-vif`

The following are the supported resource types for Network Manager:



* `attachment`
* `connect-peer`
* `connection`
* `core-network`
* `device`
* `link`
* `peering`
* `site`

The following are the supported resource types for Amazon VPC:



* `customer-gateway`
* `transit-gateway`
* `transit-gateway-attachment`
* `transit-gateway-connect-peer`
* `transit-gateway-route-table`
* `vpn-connection`

Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "NetworkResourceCounts": [ 
      { 
         "Count": ***number***,
         "ResourceType": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[NetworkResourceCounts](#API_GetNetworkResourceCounts_ResponseSyntax "#API_GetNetworkResourceCounts_ResponseSyntax")**


The count of resources.


Type: Array of [NetworkResourceCount](API_NetworkResourceCount.md "API_NetworkResourceCount.md") objects




**[NextToken](#API_GetNetworkResourceCounts_ResponseSyntax "#API_GetNetworkResourceCounts_ResponseSyntax")**


The token for the next page of results.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You do not have sufficient access to perform this action.


HTTP Status Code: 403




**InternalServerException** 


The request has failed due to an internal error.





**RetryAfterSeconds** 


Indicates when to retry the request.




HTTP Status Code: 500




**ThrottlingException** 


The request was denied due to request throttling.





**RetryAfterSeconds** 


Indicates when to retry the request.




HTTP Status Code: 429




**ValidationException** 


The input fails to satisfy the constraints.





**Fields** 


The fields that caused the error, if applicable.




**Reason** 


The reason for the error.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetNetworkResourceCounts")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetNetworkResourceCounts")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetNetworkResourceCounts")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetNetworkResourceCounts")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetNetworkResourceCounts")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetNetworkResourceCounts")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetNetworkResourceCounts")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetNetworkResourceCounts")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetNetworkResourceCounts")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetNetworkResourceCounts "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetNetworkResourceCounts")
