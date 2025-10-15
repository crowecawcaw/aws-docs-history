# CreateMonitor

Creates an AWS Deadline Cloud monitor that you can use to view your farms, queues, and
 fleets. After you submit a job, you can track the progress of the tasks and steps that make
 up the job, and then download the job's results. 


## Request Syntax



```
POST /2023-10-12/monitors HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "[displayName](#deadlinecloud-CreateMonitor-request-displayName "#deadlinecloud-CreateMonitor-request-displayName")": "`string`",
   "[identityCenterInstanceArn](#deadlinecloud-CreateMonitor-request-identityCenterInstanceArn "#deadlinecloud-CreateMonitor-request-identityCenterInstanceArn")": "`string`",
   "[roleArn](#deadlinecloud-CreateMonitor-request-roleArn "#deadlinecloud-CreateMonitor-request-roleArn")": "`string`",
   "[subdomain](#deadlinecloud-CreateMonitor-request-subdomain "#deadlinecloud-CreateMonitor-request-subdomain")": "`string`",
   "[tags](#deadlinecloud-CreateMonitor-request-tags "#deadlinecloud-CreateMonitor-request-tags")": { 
      "`string`" : "`string`" 
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_CreateMonitor_RequestSyntax "#API_CreateMonitor_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




## Request Body


The request accepts the following data in JSON format.





**[displayName](#API_CreateMonitor_RequestSyntax "#API_CreateMonitor_RequestSyntax")**


The name that you give the monitor that is displayed in the Deadline Cloud console.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: Yes




**[identityCenterInstanceArn](#API_CreateMonitor_RequestSyntax "#API_CreateMonitor_RequestSyntax")**


The Amazon Resource Name (ARN) of the IAM Identity Center instance that authenticates monitor users.


Type: String


Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`



Required: Yes




**[roleArn](#API_CreateMonitor_RequestSyntax "#API_CreateMonitor_RequestSyntax")**


The Amazon Resource Name (ARN) of the IAM role that the monitor uses to connect to Deadline Cloud. Every user
 that signs in to the monitor using IAM Identity Center uses this role to access Deadline Cloud
 resources.


Type: String


Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`



Required: Yes




**[subdomain](#API_CreateMonitor_RequestSyntax "#API_CreateMonitor_RequestSyntax")**


The subdomain to use when creating the monitor URL. The full URL of the monitor is
 subdomain.Region.deadlinecloud.amazonaws.com.


Type: String


Pattern: `[a-z0-9-]{1,100}`



Required: Yes




**[tags](#API_CreateMonitor_RequestSyntax "#API_CreateMonitor_RequestSyntax")**


The tags to add to your monitor. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.


Type: String to string map


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[identityCenterApplicationArn](#deadlinecloud-CreateMonitor-response-identityCenterApplicationArn "#deadlinecloud-CreateMonitor-response-identityCenterApplicationArn")": "***string***",
   "[monitorId](#deadlinecloud-CreateMonitor-response-monitorId "#deadlinecloud-CreateMonitor-response-monitorId")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[identityCenterApplicationArn](#API_CreateMonitor_ResponseSyntax "#API_CreateMonitor_ResponseSyntax")**


The Amazon Resource Name (ARN) that IAM Identity Center assigns to the monitor.


Type: String




**[monitorId](#API_CreateMonitor_ResponseSyntax "#API_CreateMonitor_ResponseSyntax")**


The unique identifier of the monitor.


Type: String


Pattern: `monitor-[0-9a-f]{32}`





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateMonitor")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateMonitor")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateMonitor")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateMonitor")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateMonitor")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateMonitor")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateMonitor")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateMonitor")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateMonitor")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateMonitor "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateMonitor")
