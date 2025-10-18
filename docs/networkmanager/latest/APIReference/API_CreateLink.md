# CreateLink

Creates a new link for a specified site.


## Request Syntax



```
POST /global-networks/`globalNetworkId`/links HTTP/1.1
Content-type: application/json

{
   "Bandwidth": { 
      "DownloadSpeed": `number`,
      "UploadSpeed": `number`
   },
   "Description": "`string`",
   "Provider": "`string`",
   "SiteId": "`string`",
   "Tags": [ 
      { 
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "Type": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[globalNetworkId](#API_CreateLink_RequestSyntax "#API_CreateLink_RequestSyntax")**


The ID of the global network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[Bandwidth](#API_CreateLink_RequestSyntax "#API_CreateLink_RequestSyntax")**


 The upload speed and download speed in Mbps. 


Type: [Bandwidth](API_Bandwidth.md "API_Bandwidth.md") object


Required: Yes




**[Description](#API_CreateLink_RequestSyntax "#API_CreateLink_RequestSyntax")**


A description of the link.


Constraints: Maximum length of 256 characters.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**[Provider](#API_CreateLink_RequestSyntax "#API_CreateLink_RequestSyntax")**


The provider of the link.


Constraints: Maximum length of 128 characters. Cannot include the following characters: | \ ^


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




**[SiteId](#API_CreateLink_RequestSyntax "#API_CreateLink_RequestSyntax")**


The ID of the site.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[Tags](#API_CreateLink_RequestSyntax "#API_CreateLink_RequestSyntax")**


The tags to apply to the resource during creation.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Required: No




**[Type](#API_CreateLink_RequestSyntax "#API_CreateLink_RequestSyntax")**


The type of the link.


Constraints: Maximum length of 128 characters. Cannot include the following characters: | \ ^


Type: String


Length Constraints: Minimum length of 0. Maximum length of 256.


Pattern: `[\s\S]*`



Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "Link": { 
      "Bandwidth": { 
         "DownloadSpeed": ***number***,
         "UploadSpeed": ***number***
      },
      "CreatedAt": ***number***,
      "Description": "***string***",
      "GlobalNetworkId": "***string***",
      "LinkArn": "***string***",
      "LinkId": "***string***",
      "Provider": "***string***",
      "SiteId": "***string***",
      "State": "***string***",
      "Tags": [ 
         { 
            "Key": "***string***",
            "Value": "***string***"
         }
      ],
      "Type": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Link](#API_CreateLink_ResponseSyntax "#API_CreateLink_ResponseSyntax")**


Information about the link.


Type: [Link](API_Link.md "API_Link.md") object




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/CreateLink")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/CreateLink")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CreateLink")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/CreateLink")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CreateLink")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/CreateLink")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/CreateLink")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/CreateLink")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/CreateLink")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateLink "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CreateLink")
