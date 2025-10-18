# CreateDirectConnectGatewayAttachment

Creates an AWS Direct Connect gateway attachment 


## Request Syntax



```
POST /direct-connect-gateway-attachments HTTP/1.1
Content-type: application/json

{
   "ClientToken": "`string`",
   "CoreNetworkId": "`string`",
   "DirectConnectGatewayArn": "`string`",
   "EdgeLocations": [ "`string`" ],
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





**[ClientToken](#API_CreateDirectConnectGatewayAttachment_RequestSyntax "#API_CreateDirectConnectGatewayAttachment_RequestSyntax")**


client token


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**[CoreNetworkId](#API_CreateDirectConnectGatewayAttachment_RequestSyntax "#API_CreateDirectConnectGatewayAttachment_RequestSyntax")**


The ID of the Cloud WAN core network that the Direct Connect gateway attachment should be attached to.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^core-network-([0-9a-f]{8,17})$`



Required: Yes




**[DirectConnectGatewayArn](#API_CreateDirectConnectGatewayAttachment_RequestSyntax "#API_CreateDirectConnectGatewayAttachment_RequestSyntax")**


The ARN of the Direct Connect gateway attachment.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 500.


Pattern: `^arn:[^:]{1,63}:directconnect::[^:]{0,63}:dx-gateway\/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$`



Required: Yes




**[EdgeLocations](#API_CreateDirectConnectGatewayAttachment_RequestSyntax "#API_CreateDirectConnectGatewayAttachment_RequestSyntax")**


One or more core network edge locations that the Direct Connect gateway attachment is associated with. 


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 63.


Pattern: `[\s\S]*`



Required: Yes




**[Tags](#API_CreateDirectConnectGatewayAttachment_RequestSyntax "#API_CreateDirectConnectGatewayAttachment_RequestSyntax")**


The key value tags to apply to the Direct Connect gateway attachment during creation.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "DirectConnectGatewayAttachment": { 
      "Attachment": { 
         "AttachmentId": "***string***",
         "AttachmentPolicyRuleNumber": ***number***,
         "AttachmentType": "***string***",
         "CoreNetworkArn": "***string***",
         "CoreNetworkId": "***string***",
         "CreatedAt": ***number***,
         "EdgeLocation": "***string***",
         "EdgeLocations": [ "***string***" ],
         "LastModificationErrors": [ 
            { 
               "Code": "***string***",
               "Message": "***string***",
               "RequestId": "***string***",
               "ResourceArn": "***string***"
            }
         ],
         "NetworkFunctionGroupName": "***string***",
         "OwnerAccountId": "***string***",
         "ProposedNetworkFunctionGroupChange": { 
            "AttachmentPolicyRuleNumber": ***number***,
            "NetworkFunctionGroupName": "***string***",
            "Tags": [ 
               { 
                  "Key": "***string***",
                  "Value": "***string***"
               }
            ]
         },
         "ProposedSegmentChange": { 
            "AttachmentPolicyRuleNumber": ***number***,
            "SegmentName": "***string***",
            "Tags": [ 
               { 
                  "Key": "***string***",
                  "Value": "***string***"
               }
            ]
         },
         "ResourceArn": "***string***",
         "SegmentName": "***string***",
         "State": "***string***",
         "Tags": [ 
            { 
               "Key": "***string***",
               "Value": "***string***"
            }
         ],
         "UpdatedAt": ***number***
      },
      "DirectConnectGatewayArn": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[DirectConnectGatewayAttachment](#API_CreateDirectConnectGatewayAttachment_ResponseSyntax "#API_CreateDirectConnectGatewayAttachment_ResponseSyntax")**


Describes the details of a `CreateDirectConnectGatewayAttachment` request.


Type: [DirectConnectGatewayAttachment](API_DirectConnectGatewayAttachment.md "API_DirectConnectGatewayAttachment.md") object




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateDirectConnectGatewayAttachment")
