# GetMonitor

Gets information about the specified monitor.


## Request Syntax



```
GET /2023-10-12/monitors/`monitorId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[monitorId](#API_GetMonitor_RequestSyntax "#API_GetMonitor_RequestSyntax")**


The unique identifier for the monitor. This ID is returned by the
 `CreateMonitor` operation.


Pattern: `monitor-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[createdAt](#deadlinecloud-GetMonitor-response-createdAt "#deadlinecloud-GetMonitor-response-createdAt")": "***string***",
   "[createdBy](#deadlinecloud-GetMonitor-response-createdBy "#deadlinecloud-GetMonitor-response-createdBy")": "***string***",
   "[displayName](#deadlinecloud-GetMonitor-response-displayName "#deadlinecloud-GetMonitor-response-displayName")": "***string***",
   "[identityCenterApplicationArn](#deadlinecloud-GetMonitor-response-identityCenterApplicationArn "#deadlinecloud-GetMonitor-response-identityCenterApplicationArn")": "***string***",
   "[identityCenterInstanceArn](#deadlinecloud-GetMonitor-response-identityCenterInstanceArn "#deadlinecloud-GetMonitor-response-identityCenterInstanceArn")": "***string***",
   "[monitorId](#deadlinecloud-GetMonitor-response-monitorId "#deadlinecloud-GetMonitor-response-monitorId")": "***string***",
   "[roleArn](#deadlinecloud-GetMonitor-response-roleArn "#deadlinecloud-GetMonitor-response-roleArn")": "***string***",
   "[subdomain](#deadlinecloud-GetMonitor-response-subdomain "#deadlinecloud-GetMonitor-response-subdomain")": "***string***",
   "[updatedAt](#deadlinecloud-GetMonitor-response-updatedAt "#deadlinecloud-GetMonitor-response-updatedAt")": "***string***",
   "[updatedBy](#deadlinecloud-GetMonitor-response-updatedBy "#deadlinecloud-GetMonitor-response-updatedBy")": "***string***",
   "[url](#deadlinecloud-GetMonitor-response-url "#deadlinecloud-GetMonitor-response-url")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[createdAt](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The UNIX timestamp of the date and time that the monitor was created.


Type: Timestamp




**[createdBy](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The user name of the person that created the monitor.


Type: String




**[displayName](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The name used to identify the monitor on the Deadline Cloud console.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.




**[identityCenterApplicationArn](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The Amazon Resource Name (ARN) that the IAM Identity Center assigned to the monitor when it was created.


Type: String




**[identityCenterInstanceArn](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The Amazon Resource Name (ARN) of the IAM Identity Center instance responsible for authenticating monitor users.


Type: String


Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`





**[monitorId](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The unique identifier for the monitor.


Type: String


Pattern: `monitor-[0-9a-f]{32}`





**[roleArn](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The Amazon Resource Name (ARN) of the IAM role for the monitor. Users of the monitor use this role to
 access Deadline Cloud resources.


Type: String


Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`





**[subdomain](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The subdomain used for the monitor URL. The full URL of the monitor is
 subdomain.Region.deadlinecloud.amazonaws.com.


Type: String


Pattern: `[a-z0-9-]{1,100}`





**[updatedAt](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The UNIX timestamp of the last date and time that the monitor was updated.


Type: Timestamp




**[updatedBy](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The user name of the person that last updated the monitor.


Type: String




**[url](#API_GetMonitor_ResponseSyntax "#API_GetMonitor_ResponseSyntax")**


The complete URL of the monitor. The full URL of the monitor is
 subdomain.Region.deadlinecloud.amazonaws.com.


Type: String




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetMonitor")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetMonitor")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetMonitor")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetMonitor")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetMonitor")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetMonitor")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetMonitor")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetMonitor")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetMonitor")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetMonitor "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetMonitor")
