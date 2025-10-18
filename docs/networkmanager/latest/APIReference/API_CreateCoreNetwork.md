# CreateCoreNetwork

Creates a core network as part of your global network, and optionally, with a core network policy.


## Request Syntax



```
POST /core-networks HTTP/1.1
Content-type: application/json

{
   "ClientToken": "`string`",
   "Description": "`string`",
   "GlobalNetworkId": "`string`",
   "PolicyDocument": "`string`",
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





**[ClientToken](#API_CreateCoreNetwork_RequestSyntax "#API_CreateCoreNetwork_RequestSyntax")**


The client token associated with a core network request.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**[Description](#API_CreateCoreNetwork_RequestSyntax "#API_CreateCoreNetwork_RequestSyntax")**


The description of a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**[GlobalNetworkId](#API_CreateCoreNetwork_RequestSyntax "#API_CreateCoreNetwork_RequestSyntax")**


The ID of the global network that a core network will be a part of. 


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[PolicyDocument](#API_CreateCoreNetwork_RequestSyntax "#API_CreateCoreNetwork_RequestSyntax")**


The policy document for creating a core network.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 10000000.


Pattern: `[\s\S]*`



Required: No




**[Tags](#API_CreateCoreNetwork_RequestSyntax "#API_CreateCoreNetwork_RequestSyntax")**


Key-value tags associated with a core network request.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "CoreNetwork": { 
      "CoreNetworkArn": "***string***",
      "CoreNetworkId": "***string***",
      "CreatedAt": ***number***,
      "Description": "***string***",
      "Edges": [ 
         { 
            "Asn": ***number***,
            "EdgeLocation": "***string***",
            "InsideCidrBlocks": [ "***string***" ]
         }
      ],
      "GlobalNetworkId": "***string***",
      "NetworkFunctionGroups": [ 
         { 
            "EdgeLocations": [ "***string***" ],
            "Name": "***string***",
            "Segments": { 
               "SendTo": [ "***string***" ],
               "SendVia": [ "***string***" ]
            }
         }
      ],
      "Segments": [ 
         { 
            "EdgeLocations": [ "***string***" ],
            "Name": "***string***",
            "SharedSegments": [ "***string***" ]
         }
      ],
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





**[CoreNetwork](#API_CreateCoreNetwork_ResponseSyntax "#API_CreateCoreNetwork_ResponseSyntax")**


Returns details about a core network.


Type: [CoreNetwork](API_CoreNetwork.md "API_CoreNetwork.md") object




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




**CoreNetworkPolicyException** 


Describes a core network policy exception.





**Errors** 


Describes a core network policy exception.




HTTP Status Code: 400




**InternalServerException** 


The request has failed due to an internal error.





**RetryAfterSeconds** 


Indicates when to retry the request.




HTTP Status Code: 500




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateCoreNetwork")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/CreateCoreNetwork")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateCoreNetwork")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateCoreNetwork")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateCoreNetwork")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateCoreNetwork")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateCoreNetwork")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateCoreNetwork")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateCoreNetwork")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateCoreNetwork "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateCoreNetwork")
