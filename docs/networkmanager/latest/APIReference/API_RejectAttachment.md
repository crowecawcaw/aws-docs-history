# RejectAttachment

Rejects a core network attachment request.


## Request Syntax



```
POST /attachments/`attachmentId`/reject HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[attachmentId](#API_RejectAttachment_RequestSyntax "#API_RejectAttachment_RequestSyntax")**


The ID of the attachment.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `^attachment-([0-9a-f]{8,17})$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
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
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Attachment](#API_RejectAttachment_ResponseSyntax "#API_RejectAttachment_ResponseSyntax")**


Describes the rejected attachment request.


Type: [Attachment](API_Attachment.md "API_Attachment.md") object




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/RejectAttachment")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/RejectAttachment")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/RejectAttachment")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/RejectAttachment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/RejectAttachment")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/RejectAttachment")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/RejectAttachment")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/RejectAttachment")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/RejectAttachment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RejectAttachment "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/RejectAttachment")
