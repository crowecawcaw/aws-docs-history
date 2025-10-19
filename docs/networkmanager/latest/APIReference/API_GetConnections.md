# GetConnections

Gets information about one or more of your connections in a global network.


## Request Syntax



```
GET /global-networks/`globalNetworkId`/connections?connectionIds=`ConnectionIds`&deviceId=`DeviceId`&maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[ConnectionIds](#API_GetConnections_RequestSyntax "#API_GetConnections_RequestSyntax")**


One or more connection IDs.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`





**[DeviceId](#API_GetConnections_RequestSyntax "#API_GetConnections_RequestSyntax")**


The ID of the device.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`





**[globalNetworkId](#API_GetConnections_RequestSyntax "#API_GetConnections_RequestSyntax")**


The ID of the global network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[MaxResults](#API_GetConnections_RequestSyntax "#API_GetConnections_RequestSyntax")**


The maximum number of results to return.


Valid Range: Minimum value of 1. Maximum value of 500.




**[NextToken](#API_GetConnections_RequestSyntax "#API_GetConnections_RequestSyntax")**


The token for the next page of results.


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "Connections": [ 
      { 
         "ConnectedDeviceId": "***string***",
         "ConnectedLinkId": "***string***",
         "ConnectionArn": "***string***",
         "ConnectionId": "***string***",
         "CreatedAt": ***number***,
         "Description": "***string***",
         "DeviceId": "***string***",
         "GlobalNetworkId": "***string***",
         "LinkId": "***string***",
         "State": "***string***",
         "Tags": [ 
            { 
               "Key": "***string***",
               "Value": "***string***"
            }
         ]
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Connections](#API_GetConnections_ResponseSyntax "#API_GetConnections_ResponseSyntax")**


Information about the connections.


Type: Array of [Connection](API_Connection.md "API_Connection.md") objects




**[NextToken](#API_GetConnections_ResponseSyntax "#API_GetConnections_ResponseSyntax")**


The token to use for the next page of results.


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




**ResourceNotFoundException** 


The specified resource could not be found.





**Context** 


The specified resource could not be found.




**ResourceId** 


The ID of the resource.




**ResourceType** 


The resource type.




HTTP Status Code: 404




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetConnections")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetConnections")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetConnections")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetConnections")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetConnections")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetConnections")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetConnections")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetConnections")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetConnections")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetConnections "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetConnections")
