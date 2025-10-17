# GetLicenseEndpoint

Gets a licence endpoint.


## Request Syntax



```
GET /2023-10-12/license-endpoints/`licenseEndpointId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[licenseEndpointId](#API_GetLicenseEndpoint_RequestSyntax "#API_GetLicenseEndpoint_RequestSyntax")**


The license endpoint ID.


Pattern: `le-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "dnsName": "***string***",
   "licenseEndpointId": "***string***",
   "securityGroupIds": [ "***string***" ],
   "status": "***string***",
   "statusMessage": "***string***",
   "subnetIds": [ "***string***" ],
   "vpcId": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[dnsName](#API_GetLicenseEndpoint_ResponseSyntax "#API_GetLicenseEndpoint_ResponseSyntax")**


The DNS name.


Type: String




**[licenseEndpointId](#API_GetLicenseEndpoint_ResponseSyntax "#API_GetLicenseEndpoint_ResponseSyntax")**


The license endpoint ID.


Type: String


Pattern: `le-[0-9a-f]{32}`





**[securityGroupIds](#API_GetLicenseEndpoint_ResponseSyntax "#API_GetLicenseEndpoint_ResponseSyntax")**


The security group IDs for the license endpoint.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Pattern: `sg-[\w]{1,120}`





**[status](#API_GetLicenseEndpoint_ResponseSyntax "#API_GetLicenseEndpoint_ResponseSyntax")**


The status of the license endpoint.


Type: String


Valid Values: `CREATE_IN_PROGRESS | DELETE_IN_PROGRESS | READY | NOT_READY`





**[statusMessage](#API_GetLicenseEndpoint_ResponseSyntax "#API_GetLicenseEndpoint_ResponseSyntax")**


The status message of the license endpoint.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.




**[subnetIds](#API_GetLicenseEndpoint_ResponseSyntax "#API_GetLicenseEndpoint_ResponseSyntax")**


The subnet IDs.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Length Constraints: Minimum length of 1. Maximum length of 32.


Pattern: `subnet-[\w]{1,120}`





**[vpcId](#API_GetLicenseEndpoint_ResponseSyntax "#API_GetLicenseEndpoint_ResponseSyntax")**


The VPC (virtual private cloud) ID associated with the license endpoint.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 32.


Pattern: `vpc-[\w]{1,120}`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You don't have permission to perform the action.





**context** 


Information about the resources in use when the exception was thrown.




HTTP Status Code: 403




**InternalServerErrorException** 


Deadline Cloud can't process your request right now. Try again later.





**retryAfterSeconds** 


The number of seconds a client should wait before retrying the request.




HTTP Status Code: 500




**ResourceNotFoundException** 


The requested resource can't be found.





**context** 


Information about the resources in use when the exception was thrown.




**resourceId** 


The identifier of the resource that couldn't be found.




**resourceType** 


The type of the resource that couldn't be found.




HTTP Status Code: 404




**ThrottlingException** 


Your request exceeded a request rate quota.





**context** 


Information about the resources in use when the exception was thrown.




**quotaCode** 


Identifies the quota that is being throttled.




**retryAfterSeconds** 


The number of seconds a client should wait before retrying the request.




**serviceCode** 


Identifies the service that is being throttled.




HTTP Status Code: 429




**ValidationException** 


The request isn't valid. This can occur if your request contains malformed JSON or
 unsupported characters.





**context** 


Information about the resources in use when the exception was thrown.




**fieldList** 


A list of fields that failed validation.




**reason** 


The reason that the request failed validation.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetLicenseEndpoint")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetLicenseEndpoint")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetLicenseEndpoint")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetLicenseEndpoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetLicenseEndpoint")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetLicenseEndpoint")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetLicenseEndpoint")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetLicenseEndpoint")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetLicenseEndpoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetLicenseEndpoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetLicenseEndpoint")
