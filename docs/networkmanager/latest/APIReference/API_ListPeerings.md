# ListPeerings

Lists the peerings for a core network.


## Request Syntax



```
GET /peerings?coreNetworkId=`CoreNetworkId`&edgeLocation=`EdgeLocation`&maxResults=`MaxResults`&nextToken=`NextToken`&peeringType=`PeeringType`&state=`State` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[CoreNetworkId](#API_ListPeerings_RequestSyntax "#API_ListPeerings_RequestSyntax")**


The ID of a core network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`





**[EdgeLocation](#API_ListPeerings_RequestSyntax "#API_ListPeerings_RequestSyntax")**


Returns a list edge locations for the 


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`





**[MaxResults](#API_ListPeerings_RequestSyntax "#API_ListPeerings_RequestSyntax")**


The maximum number of results to return.


Valid Range: Minimum value of 1. Maximum value of 500.




**[NextToken](#API_ListPeerings_RequestSyntax "#API_ListPeerings_RequestSyntax")**


The token for the next page of results.


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





**[PeeringType](#API_ListPeerings_RequestSyntax "#API_ListPeerings_RequestSyntax")**


Returns a list of a peering requests.


Valid Values: `TRANSIT_GATEWAY`





**[State](#API_ListPeerings_RequestSyntax "#API_ListPeerings_RequestSyntax")**


Returns a list of the peering request states.


Valid Values: `CREATING | FAILED | AVAILABLE | DELETING`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Peerings": [ 
      { 
         "CoreNetworkArn": "***string***",
         "CoreNetworkId": "***string***",
         "CreatedAt": ***number***,
         "EdgeLocation": "***string***",
         "LastModificationErrors": [ 
            { 
               "Code": "***string***",
               "Message": "***string***",
               "MissingPermissionsContext": { 
                  "MissingPermission": "***string***"
               },
               "RequestId": "***string***",
               "ResourceArn": "***string***"
            }
         ],
         "OwnerAccountId": "***string***",
         "PeeringId": "***string***",
         "PeeringType": "***string***",
         "ResourceArn": "***string***",
         "State": "***string***",
         "Tags": [ 
            { 
               "Key": "***string***",
               "Value": "***string***"
            }
         ]
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[NextToken](#API_ListPeerings_ResponseSyntax "#API_ListPeerings_ResponseSyntax")**


The token for the next page of results.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





**[Peerings](#API_ListPeerings_ResponseSyntax "#API_ListPeerings_ResponseSyntax")**


Lists the transit gateway peerings for the `ListPeerings` request.


Type: Array of [Peering](API_Peering.md "API_Peering.md") objects




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/ListPeerings")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/ListPeerings")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ListPeerings")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/ListPeerings")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ListPeerings")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/ListPeerings")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/ListPeerings")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/ListPeerings")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/ListPeerings")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListPeerings "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ListPeerings")
