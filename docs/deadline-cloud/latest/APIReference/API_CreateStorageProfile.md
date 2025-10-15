# CreateStorageProfile

Creates a storage profile that specifies the operating system, file type, and file
 location of resources used on a farm.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/storage-profiles HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "[displayName](#deadlinecloud-CreateStorageProfile-request-displayName "#deadlinecloud-CreateStorageProfile-request-displayName")": "`string`",
   "[fileSystemLocations](#deadlinecloud-CreateStorageProfile-request-fileSystemLocations "#deadlinecloud-CreateStorageProfile-request-fileSystemLocations")": [ 
      { 
         "[name](API_FileSystemLocation.md#deadlinecloud-Type-FileSystemLocation-name "API_FileSystemLocation.md#deadlinecloud-Type-FileSystemLocation-name")": "`string`",
         "[path](API_FileSystemLocation.md#deadlinecloud-Type-FileSystemLocation-path "API_FileSystemLocation.md#deadlinecloud-Type-FileSystemLocation-path")": "`string`",
         "[type](API_FileSystemLocation.md#deadlinecloud-Type-FileSystemLocation-type "API_FileSystemLocation.md#deadlinecloud-Type-FileSystemLocation-type")": "`string`"
      }
   ],
   "[osFamily](#deadlinecloud-CreateStorageProfile-request-osFamily "#deadlinecloud-CreateStorageProfile-request-osFamily")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_CreateStorageProfile_RequestSyntax "#API_CreateStorageProfile_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_CreateStorageProfile_RequestSyntax "#API_CreateStorageProfile_RequestSyntax")**


The farm ID of the farm to connect to the storage profile.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[displayName](#API_CreateStorageProfile_RequestSyntax "#API_CreateStorageProfile_RequestSyntax")**


The display name of the storage profile.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: Yes




**[fileSystemLocations](#API_CreateStorageProfile_RequestSyntax "#API_CreateStorageProfile_RequestSyntax")**


File system paths to include in the storage profile.


Type: Array of [FileSystemLocation](API_FileSystemLocation.md "API_FileSystemLocation.md") objects


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Required: No




**[osFamily](#API_CreateStorageProfile_RequestSyntax "#API_CreateStorageProfile_RequestSyntax")**


The type of operating system (OS) for the storage profile.


Type: String


Valid Values: `WINDOWS | LINUX | MACOS`



Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[storageProfileId](#deadlinecloud-CreateStorageProfile-response-storageProfileId "#deadlinecloud-CreateStorageProfile-response-storageProfileId")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[storageProfileId](#API_CreateStorageProfile_ResponseSyntax "#API_CreateStorageProfile_ResponseSyntax")**


The storage profile ID.


Type: String


Pattern: `sp-[0-9a-f]{32}`





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




**ServiceQuotaExceededException** 


You exceeded your service quota. Service quotas, also referred to as limits, are the
 maximum number of service resources or operations for your AWS account.





**context** 


Information about the resources in use when the exception was thrown.




**quotaCode** 


Identifies the quota that has been exceeded.




**reason** 


A string that describes the reason the quota was exceeded.




**resourceId** 


The identifier of the affected resource.




**resourceType** 


The type of the affected resource




**serviceCode** 


Identifies the service that exceeded the quota.




HTTP Status Code: 402




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateStorageProfile")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateStorageProfile")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateStorageProfile")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateStorageProfile")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateStorageProfile")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateStorageProfile")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateStorageProfile")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateStorageProfile")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateStorageProfile")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateStorageProfile "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateStorageProfile")
