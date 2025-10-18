# CreateConnectPeer

Creates a core network Connect peer for a specified core network connect attachment between a core network and an appliance.
 The peer address and transit gateway address must be the same IP address family (IPv4 or IPv6).


## Request Syntax



```
POST /connect-peers HTTP/1.1
Content-type: application/json

{
   "BgpOptions": { 
      "PeerAsn": `number`
   },
   "ClientToken": "`string`",
   "ConnectAttachmentId": "`string`",
   "CoreNetworkAddress": "`string`",
   "InsideCidrBlocks": [ "`string`" ],
   "PeerAddress": "`string`",
   "SubnetArn": "`string`",
   "Tags": [ 
      { 
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[BgpOptions](#API_CreateConnectPeer_RequestSyntax "#API_CreateConnectPeer_RequestSyntax")**


The Connect peer BGP options. This only applies only when the protocol is `GRE`.


Type: [BgpOptions](API_BgpOptions.md "API_BgpOptions.md") object


Required: No




**[ClientToken](#API_CreateConnectPeer_RequestSyntax "#API_CreateConnectPeer_RequestSyntax")**


The client token associated with the request.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**[ConnectAttachmentId](#API_CreateConnectPeer_RequestSyntax "#API_CreateConnectPeer_RequestSyntax")**


The ID of the connection attachment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^attachment-([0-9a-f]{8,17})$`



Required: Yes




**[CoreNetworkAddress](#API_CreateConnectPeer_RequestSyntax "#API_CreateConnectPeer_RequestSyntax")**


A Connect peer core network address. This only applies only when the protocol is `GRE`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 50.


Pattern: `[\s\S]*`



Required: No




**[InsideCidrBlocks](#API_CreateConnectPeer_RequestSyntax "#API_CreateConnectPeer_RequestSyntax")**


The inside IP addresses used for BGP peering.


Type: Array of strings


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**[PeerAddress](#API_CreateConnectPeer_RequestSyntax "#API_CreateConnectPeer_RequestSyntax")**


The Connect peer address.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[SubnetArn](#API_CreateConnectPeer_RequestSyntax "#API_CreateConnectPeer_RequestSyntax")**


The subnet ARN for the Connect peer. This only applies only when the protocol is NO\_ENCAP.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`



Required: No




**[Tags](#API_CreateConnectPeer_RequestSyntax "#API_CreateConnectPeer_RequestSyntax")**


The tags associated with the peer request.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectPeer": { 
      "Configuration": { 
         "BgpConfigurations": [ 
            { 
               "CoreNetworkAddress": "***string***",
               "CoreNetworkAsn": ***number***,
               "PeerAddress": "***string***",
               "PeerAsn": ***number***
            }
         ],
         "CoreNetworkAddress": "***string***",
         "InsideCidrBlocks": [ "***string***" ],
         "PeerAddress": "***string***",
         "Protocol": "***string***"
      },
      "ConnectAttachmentId": "***string***",
      "ConnectPeerId": "***string***",
      "CoreNetworkId": "***string***",
      "CreatedAt": ***number***,
      "EdgeLocation": "***string***",
      "LastModificationErrors": [ 
         { 
            "Code": "***string***",
            "Message": "***string***",
            "RequestId": "***string***",
            "ResourceArn": "***string***"
         }
      ],
      "State": "***string***",
      "SubnetArn": "***string***",
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





**[ConnectPeer](#API_CreateConnectPeer_ResponseSyntax "#API_CreateConnectPeer_ResponseSyntax")**


The response to the request.


Type: [ConnectPeer](API_ConnectPeer.md "API_ConnectPeer.md") object




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateConnectPeer")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/CreateConnectPeer")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateConnectPeer")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateConnectPeer")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateConnectPeer")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateConnectPeer")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateConnectPeer")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateConnectPeer")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateConnectPeer")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateConnectPeer "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateConnectPeer")
