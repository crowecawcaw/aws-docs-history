# GetNetworkTelemetry

Gets the network telemetry of the specified global network.


## Request Syntax



```
GET /global-networks/`globalNetworkId`/network-telemetry?accountId=`AccountId`&awsRegion=`AwsRegion`&coreNetworkId=`CoreNetworkId`&maxResults=`MaxResults`&nextToken=`NextToken`&registeredGatewayArn=`RegisteredGatewayArn`&resourceArn=`ResourceArn`&resourceType=`ResourceType` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[AccountId](#API_GetNetworkTelemetry_RequestSyntax "#API_GetNetworkTelemetry_RequestSyntax")**


The AWS account ID.


Length Constraints: Fixed length of 12.


Pattern: `[\s\S]*`





**[AwsRegion](#API_GetNetworkTelemetry_RequestSyntax "#API_GetNetworkTelemetry_RequestSyntax")**


The AWS Region.


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`





**[CoreNetworkId](#API_GetNetworkTelemetry_RequestSyntax "#API_GetNetworkTelemetry_RequestSyntax")**


The ID of a core network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`





**[globalNetworkId](#API_GetNetworkTelemetry_RequestSyntax "#API_GetNetworkTelemetry_RequestSyntax")**


The ID of the global network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[MaxResults](#API_GetNetworkTelemetry_RequestSyntax "#API_GetNetworkTelemetry_RequestSyntax")**


The maximum number of results to return.


Valid Range: Minimum value of 1. Maximum value of 500.




**[NextToken](#API_GetNetworkTelemetry_RequestSyntax "#API_GetNetworkTelemetry_RequestSyntax")**


The token for the next page of results.


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





**[RegisteredGatewayArn](#API_GetNetworkTelemetry_RequestSyntax "#API_GetNetworkTelemetry_RequestSyntax")**


The ARN of the gateway.


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`





**[ResourceArn](#API_GetNetworkTelemetry_RequestSyntax "#API_GetNetworkTelemetry_RequestSyntax")**


The ARN of the resource.


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`





**[ResourceType](#API_GetNetworkTelemetry_RequestSyntax "#API_GetNetworkTelemetry_RequestSyntax")**


The resource type. The following are the supported resource types:



* `connect-peer`
* `transit-gateway-connect-peer`
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
   "NetworkTelemetry": [ 
      { 
         "AccountId": "***string***",
         "Address": "***string***",
         "AwsRegion": "***string***",
         "CoreNetworkId": "***string***",
         "Health": { 
            "Status": "***string***",
            "Timestamp": ***number***,
            "Type": "***string***"
         },
         "RegisteredGatewayArn": "***string***",
         "ResourceArn": "***string***",
         "ResourceId": "***string***",
         "ResourceType": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[NetworkTelemetry](#API_GetNetworkTelemetry_ResponseSyntax "#API_GetNetworkTelemetry_ResponseSyntax")**


The network telemetry.


Type: Array of [NetworkTelemetry](API_NetworkTelemetry.md "API_NetworkTelemetry.md") objects




**[NextToken](#API_GetNetworkTelemetry_ResponseSyntax "#API_GetNetworkTelemetry_ResponseSyntax")**


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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetNetworkTelemetry")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetNetworkTelemetry")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetNetworkTelemetry")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetNetworkTelemetry")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetNetworkTelemetry")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetNetworkTelemetry")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetNetworkTelemetry")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetNetworkTelemetry")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetNetworkTelemetry")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetNetworkTelemetry "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetNetworkTelemetry")
