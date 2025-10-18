# UpdateConnection

Updates the information for an existing connection. To remove information for any of the parameters,
 specify an empty string.


## Request Syntax



```
PATCH /global-networks/`globalNetworkId`/connections/`connectionId` HTTP/1.1
Content-type: application/json

{
   "ConnectedLinkId": "`string`",
   "Description": "`string`",
   "LinkId": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[connectionId](#API_UpdateConnection_RequestSyntax "#API_UpdateConnection_RequestSyntax")**


The ID of the connection.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[globalNetworkId](#API_UpdateConnection_RequestSyntax "#API_UpdateConnection_RequestSyntax")**


The ID of the global network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[ConnectedLinkId](#API_UpdateConnection_RequestSyntax "#API_UpdateConnection_RequestSyntax")**


The ID of the link for the second device in the connection.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**[Description](#API_UpdateConnection_RequestSyntax "#API_UpdateConnection_RequestSyntax")**


A description of the connection.


Length Constraints: Maximum length of 256 characters.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**[LinkId](#API_UpdateConnection_RequestSyntax "#API_UpdateConnection_RequestSyntax")**


The ID of the link for the first device in the connection.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "Connection": { 
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
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Connection](#API_UpdateConnection_ResponseSyntax "#API_UpdateConnection_ResponseSyntax")**


Information about the connection.


Type: [Connection](API_Connection.md "API_Connection.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You do not have sufficient access to perform this action.


HTTP Status Code: 403




**ConflictException** 


There was a conflict processing the request. Updating or deleting the resource can
 cause an inconsistent state.





**ResourceId** 


The ID of the resource.




**ResourceType** 


The resource type.




HTTP Status Code: 409




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/UpdateConnection")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/UpdateConnection")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/UpdateConnection")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/UpdateConnection")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/UpdateConnection")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/UpdateConnection")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/UpdateConnection")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/UpdateConnection")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/UpdateConnection")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/UpdateConnection "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/UpdateConnection")
