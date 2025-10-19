# AssociateConnectPeer

Associates a core network Connect peer with a device and optionally, with a link. 

If you specify a link, it must be associated with the specified device. You can only
 associate core network Connect peers that have been created on a core network Connect
 attachment on a core network. 


## Request Syntax



```
POST /global-networks/`globalNetworkId`/connect-peer-associations HTTP/1.1
Content-type: application/json

{
   "ConnectPeerId": "`string`",
   "DeviceId": "`string`",
   "LinkId": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[globalNetworkId](#API_AssociateConnectPeer_RequestSyntax "#API_AssociateConnectPeer_RequestSyntax")**


The ID of your global network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[ConnectPeerId](#API_AssociateConnectPeer_RequestSyntax "#API_AssociateConnectPeer_RequestSyntax")**


The ID of the Connect peer.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^connect-peer-([0-9a-f]{8,17})$`



Required: Yes




**[DeviceId](#API_AssociateConnectPeer_RequestSyntax "#API_AssociateConnectPeer_RequestSyntax")**


The ID of the device.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[LinkId](#API_AssociateConnectPeer_RequestSyntax "#API_AssociateConnectPeer_RequestSyntax")**


The ID of the link.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectPeerAssociation": { 
      "ConnectPeerId": "***string***",
      "DeviceId": "***string***",
      "GlobalNetworkId": "***string***",
      "LinkId": "***string***",
      "State": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[ConnectPeerAssociation](#API_AssociateConnectPeer_ResponseSyntax "#API_AssociateConnectPeer_ResponseSyntax")**


The response to the Connect peer request.


Type: [ConnectPeerAssociation](API_ConnectPeerAssociation.md "API_ConnectPeerAssociation.md") object




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




**ServiceQuotaExceededException** 


A service limit was exceeded.





**LimitCode** 


The limit code.




**Message** 


The error message.




**ResourceId** 


The ID of the resource.




**ResourceType** 


The resource type.




**ServiceCode** 


The service code.




HTTP Status Code: 402




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/AssociateConnectPeer")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/AssociateConnectPeer")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AssociateConnectPeer")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/AssociateConnectPeer")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AssociateConnectPeer")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/AssociateConnectPeer")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/AssociateConnectPeer")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/AssociateConnectPeer")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/AssociateConnectPeer")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AssociateConnectPeer "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AssociateConnectPeer")
