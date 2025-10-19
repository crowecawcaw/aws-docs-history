# GetTransitGatewayRegistrations

Gets information about the transit gateway registrations in a specified
 global network.


## Request Syntax



```
GET /global-networks/`globalNetworkId`/transit-gateway-registrations?maxResults=`MaxResults`&nextToken=`NextToken`&transitGatewayArns=`TransitGatewayArns` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[globalNetworkId](#API_GetTransitGatewayRegistrations_RequestSyntax "#API_GetTransitGatewayRegistrations_RequestSyntax")**


The ID of the global network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[MaxResults](#API_GetTransitGatewayRegistrations_RequestSyntax "#API_GetTransitGatewayRegistrations_RequestSyntax")**


The maximum number of results to return.


Valid Range: Minimum value of 1. Maximum value of 500.




**[NextToken](#API_GetTransitGatewayRegistrations_RequestSyntax "#API_GetTransitGatewayRegistrations_RequestSyntax")**


The token for the next page of results.


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





**[TransitGatewayArns](#API_GetTransitGatewayRegistrations_RequestSyntax "#API_GetTransitGatewayRegistrations_RequestSyntax")**


The Amazon Resource Names (ARNs) of one or more transit gateways. The maximum is
 10.


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `[\s\S]*`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "TransitGatewayRegistrations": [ 
      { 
         "GlobalNetworkId": "***string***",
         "State": { 
            "Code": "***string***",
            "Message": "***string***"
         },
         "TransitGatewayArn": "***string***"
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[NextToken](#API_GetTransitGatewayRegistrations_ResponseSyntax "#API_GetTransitGatewayRegistrations_ResponseSyntax")**


The token for the next page of results.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 2048.


Pattern: `[\s\S]*`





**[TransitGatewayRegistrations](#API_GetTransitGatewayRegistrations_ResponseSyntax "#API_GetTransitGatewayRegistrations_ResponseSyntax")**


The transit gateway registrations.


Type: Array of [TransitGatewayRegistration](API_TransitGatewayRegistration.md "API_TransitGatewayRegistration.md") objects




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetTransitGatewayRegistrations "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetTransitGatewayRegistrations")
