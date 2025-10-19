# UpdateNetworkResourceMetadata

Updates the resource metadata for the specified global network.


## Request Syntax



```
PATCH /global-networks/`globalNetworkId`/network-resources/`resourceArn`/metadata HTTP/1.1
Content-type: application/json

{
   "Metadata": { 
      "`string`" : "`string`" 
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[globalNetworkId](#API_UpdateNetworkResourceMetadata_RequestSyntax "#API_UpdateNetworkResourceMetadata_RequestSyntax")**


The ID of the global network.


Length Constraints: Minimum length of 0. Maximum length of 50.


Pattern: `[\s\S]*`



Required: Yes




**[resourceArn](#API_UpdateNetworkResourceMetadata_RequestSyntax "#API_UpdateNetworkResourceMetadata_RequestSyntax")**


The ARN of the resource.


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[Metadata](#API_UpdateNetworkResourceMetadata_RequestSyntax "#API_UpdateNetworkResourceMetadata_RequestSyntax")**


The resource metadata.


Type: String to string map


Key Length Constraints: Minimum length of 0. Maximum length of 256.


Key Pattern: `[\s\S]*`



Value Length Constraints: Minimum length of 0. Maximum length of 256.


Value Pattern: `[\s\S]*`



Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "Metadata": { 
      "***string***" : "***string***" 
   },
   "ResourceArn": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Metadata](#API_UpdateNetworkResourceMetadata_ResponseSyntax "#API_UpdateNetworkResourceMetadata_ResponseSyntax")**


The updated resource metadata.


Type: String to string map


Key Length Constraints: Minimum length of 0. Maximum length of 256.


Key Pattern: `[\s\S]*`



Value Length Constraints: Minimum length of 0. Maximum length of 256.


Value Pattern: `[\s\S]*`





**[ResourceArn](#API_UpdateNetworkResourceMetadata_ResponseSyntax "#API_UpdateNetworkResourceMetadata_ResponseSyntax")**


The ARN of the resource.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1500.


Pattern: `[\s\S]*`





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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/DotNetSDKV3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata "https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/UpdateNetworkResourceMetadata")
