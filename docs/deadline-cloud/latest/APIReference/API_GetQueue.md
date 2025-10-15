# GetQueue

Gets a queue.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/queues/`queueId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetQueue_RequestSyntax "#API_GetQueue_RequestSyntax")**


The farm ID of the farm in the queue.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_GetQueue_RequestSyntax "#API_GetQueue_RequestSyntax")**


The queue ID for the queue to retrieve.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[allowedStorageProfileIds](#deadlinecloud-GetQueue-response-allowedStorageProfileIds "#deadlinecloud-GetQueue-response-allowedStorageProfileIds")": [ "***string***" ],
   "[blockedReason](#deadlinecloud-GetQueue-response-blockedReason "#deadlinecloud-GetQueue-response-blockedReason")": "***string***",
   "[createdAt](#deadlinecloud-GetQueue-response-createdAt "#deadlinecloud-GetQueue-response-createdAt")": "***string***",
   "[createdBy](#deadlinecloud-GetQueue-response-createdBy "#deadlinecloud-GetQueue-response-createdBy")": "***string***",
   "[defaultBudgetAction](#deadlinecloud-GetQueue-response-defaultBudgetAction "#deadlinecloud-GetQueue-response-defaultBudgetAction")": "***string***",
   "[description](#deadlinecloud-GetQueue-response-description "#deadlinecloud-GetQueue-response-description")": "***string***",
   "[displayName](#deadlinecloud-GetQueue-response-displayName "#deadlinecloud-GetQueue-response-displayName")": "***string***",
   "[farmId](#deadlinecloud-GetQueue-response-farmId "#deadlinecloud-GetQueue-response-farmId")": "***string***",
   "[jobAttachmentSettings](#deadlinecloud-GetQueue-response-jobAttachmentSettings "#deadlinecloud-GetQueue-response-jobAttachmentSettings")": { 
      "[rootPrefix](API_JobAttachmentSettings.md#deadlinecloud-Type-JobAttachmentSettings-rootPrefix "API_JobAttachmentSettings.md#deadlinecloud-Type-JobAttachmentSettings-rootPrefix")": "***string***",
      "[s3BucketName](API_JobAttachmentSettings.md#deadlinecloud-Type-JobAttachmentSettings-s3BucketName "API_JobAttachmentSettings.md#deadlinecloud-Type-JobAttachmentSettings-s3BucketName")": "***string***"
   },
   "[jobRunAsUser](#deadlinecloud-GetQueue-response-jobRunAsUser "#deadlinecloud-GetQueue-response-jobRunAsUser")": { 
      "[posix](API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-posix "API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-posix")": { 
         "[group](API_PosixUser.md#deadlinecloud-Type-PosixUser-group "API_PosixUser.md#deadlinecloud-Type-PosixUser-group")": "***string***",
         "[user](API_PosixUser.md#deadlinecloud-Type-PosixUser-user "API_PosixUser.md#deadlinecloud-Type-PosixUser-user")": "***string***"
      },
      "[runAs](API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-runAs "API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-runAs")": "***string***",
      "[windows](API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-windows "API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-windows")": { 
         "[passwordArn](API_WindowsUser.md#deadlinecloud-Type-WindowsUser-passwordArn "API_WindowsUser.md#deadlinecloud-Type-WindowsUser-passwordArn")": "***string***",
         "[user](API_WindowsUser.md#deadlinecloud-Type-WindowsUser-user "API_WindowsUser.md#deadlinecloud-Type-WindowsUser-user")": "***string***"
      }
   },
   "[queueId](#deadlinecloud-GetQueue-response-queueId "#deadlinecloud-GetQueue-response-queueId")": "***string***",
   "[requiredFileSystemLocationNames](#deadlinecloud-GetQueue-response-requiredFileSystemLocationNames "#deadlinecloud-GetQueue-response-requiredFileSystemLocationNames")": [ "***string***" ],
   "[roleArn](#deadlinecloud-GetQueue-response-roleArn "#deadlinecloud-GetQueue-response-roleArn")": "***string***",
   "[status](#deadlinecloud-GetQueue-response-status "#deadlinecloud-GetQueue-response-status")": "***string***",
   "[updatedAt](#deadlinecloud-GetQueue-response-updatedAt "#deadlinecloud-GetQueue-response-updatedAt")": "***string***",
   "[updatedBy](#deadlinecloud-GetQueue-response-updatedBy "#deadlinecloud-GetQueue-response-updatedBy")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[allowedStorageProfileIds](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The storage profile IDs for the queue.


Type: Array of strings


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Pattern: `sp-[0-9a-f]{32}`





**[blockedReason](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The reason the queue was blocked.


Type: String


Valid Values: `NO_BUDGET_CONFIGURED | BUDGET_THRESHOLD_REACHED`





**[createdAt](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The date and time the resource was created.


Type: Timestamp




**[createdBy](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The user or system that created this resource.


Type: String




**[defaultBudgetAction](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The default action taken on a queue if a budget wasn't configured.


Type: String


Valid Values: `NONE | STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`





**[description](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The description of the queue.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.




**[displayName](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The display name of the queue.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.




**[farmId](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The farm ID for the queue.


Type: String


Pattern: `farm-[0-9a-f]{32}`





**[jobAttachmentSettings](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The job attachment settings for the queue.


Type: [JobAttachmentSettings](API_JobAttachmentSettings.md "API_JobAttachmentSettings.md") object




**[jobRunAsUser](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The jobs in the queue ran as this specified POSIX user.


Type: [JobRunAsUser](API_JobRunAsUser.md "API_JobRunAsUser.md") object




**[queueId](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The queue ID.


Type: String


Pattern: `queue-[0-9a-f]{32}`





**[requiredFileSystemLocationNames](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


A list of the required file system location names in the queue.


Type: Array of strings


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[0-9A-Za-z ]*`





**[roleArn](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The IAM role ARN.


Type: String


Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`





**[status](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The status of the queue.



* `ACTIVE`–The queue is active.
* `SCHEDULING`–The queue is scheduling.
* `SCHEDULING_BLOCKED`–The queue scheduling is blocked. See the
 provided reason.

Type: String


Valid Values: `IDLE | SCHEDULING | SCHEDULING_BLOCKED`





**[updatedAt](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The date and time the resource was updated.


Type: Timestamp




**[updatedBy](#API_GetQueue_ResponseSyntax "#API_GetQueue_ResponseSyntax")**


The user or system that updated this resource.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetQueue")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetQueue")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetQueue")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetQueue")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetQueue")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetQueue")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetQueue")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetQueue")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetQueue")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetQueue "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetQueue")
