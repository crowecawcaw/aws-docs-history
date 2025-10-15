# UpdateQueue

Updates a queue.


## Request Syntax



```
PATCH /2023-10-12/farms/`farmId`/queues/`queueId` HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "[allowedStorageProfileIdsToAdd](#deadlinecloud-UpdateQueue-request-allowedStorageProfileIdsToAdd "#deadlinecloud-UpdateQueue-request-allowedStorageProfileIdsToAdd")": [ "`string`" ],
   "[allowedStorageProfileIdsToRemove](#deadlinecloud-UpdateQueue-request-allowedStorageProfileIdsToRemove "#deadlinecloud-UpdateQueue-request-allowedStorageProfileIdsToRemove")": [ "`string`" ],
   "[defaultBudgetAction](#deadlinecloud-UpdateQueue-request-defaultBudgetAction "#deadlinecloud-UpdateQueue-request-defaultBudgetAction")": "`string`",
   "[description](#deadlinecloud-UpdateQueue-request-description "#deadlinecloud-UpdateQueue-request-description")": "`string`",
   "[displayName](#deadlinecloud-UpdateQueue-request-displayName "#deadlinecloud-UpdateQueue-request-displayName")": "`string`",
   "[jobAttachmentSettings](#deadlinecloud-UpdateQueue-request-jobAttachmentSettings "#deadlinecloud-UpdateQueue-request-jobAttachmentSettings")": { 
      "[rootPrefix](API_JobAttachmentSettings.md#deadlinecloud-Type-JobAttachmentSettings-rootPrefix "API_JobAttachmentSettings.md#deadlinecloud-Type-JobAttachmentSettings-rootPrefix")": "`string`",
      "[s3BucketName](API_JobAttachmentSettings.md#deadlinecloud-Type-JobAttachmentSettings-s3BucketName "API_JobAttachmentSettings.md#deadlinecloud-Type-JobAttachmentSettings-s3BucketName")": "`string`"
   },
   "[jobRunAsUser](#deadlinecloud-UpdateQueue-request-jobRunAsUser "#deadlinecloud-UpdateQueue-request-jobRunAsUser")": { 
      "[posix](API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-posix "API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-posix")": { 
         "[group](API_PosixUser.md#deadlinecloud-Type-PosixUser-group "API_PosixUser.md#deadlinecloud-Type-PosixUser-group")": "`string`",
         "[user](API_PosixUser.md#deadlinecloud-Type-PosixUser-user "API_PosixUser.md#deadlinecloud-Type-PosixUser-user")": "`string`"
      },
      "[runAs](API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-runAs "API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-runAs")": "`string`",
      "[windows](API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-windows "API_JobRunAsUser.md#deadlinecloud-Type-JobRunAsUser-windows")": { 
         "[passwordArn](API_WindowsUser.md#deadlinecloud-Type-WindowsUser-passwordArn "API_WindowsUser.md#deadlinecloud-Type-WindowsUser-passwordArn")": "`string`",
         "[user](API_WindowsUser.md#deadlinecloud-Type-WindowsUser-user "API_WindowsUser.md#deadlinecloud-Type-WindowsUser-user")": "`string`"
      }
   },
   "[requiredFileSystemLocationNamesToAdd](#deadlinecloud-UpdateQueue-request-requiredFileSystemLocationNamesToAdd "#deadlinecloud-UpdateQueue-request-requiredFileSystemLocationNamesToAdd")": [ "`string`" ],
   "[requiredFileSystemLocationNamesToRemove](#deadlinecloud-UpdateQueue-request-requiredFileSystemLocationNamesToRemove "#deadlinecloud-UpdateQueue-request-requiredFileSystemLocationNamesToRemove")": [ "`string`" ],
   "[roleArn](#deadlinecloud-UpdateQueue-request-roleArn "#deadlinecloud-UpdateQueue-request-roleArn")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The idempotency token to update in the queue.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The farm ID to update in the queue.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The queue ID to update.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[allowedStorageProfileIdsToAdd](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The storage profile IDs to add.


Type: Array of strings


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Pattern: `sp-[0-9a-f]{32}`



Required: No




**[allowedStorageProfileIdsToRemove](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The storage profile ID to remove.


Type: Array of strings


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Pattern: `sp-[0-9a-f]{32}`



Required: No




**[defaultBudgetAction](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The default action to take for a queue update if a budget isn't configured.


Type: String


Valid Values: `NONE | STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`



Required: No




**[description](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The description of the queue to update.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.


Required: No




**[displayName](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The display name of the queue to update.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: No




**[jobAttachmentSettings](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The job attachment settings to update for the
 queue.


Type: [JobAttachmentSettings](API_JobAttachmentSettings.md "API_JobAttachmentSettings.md") object


Required: No




**[jobRunAsUser](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


Update the jobs in the queue to run as a specified POSIX user.


Type: [JobRunAsUser](API_JobRunAsUser.md "API_JobRunAsUser.md") object


Required: No




**[requiredFileSystemLocationNamesToAdd](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The required file system location names to add to the queue.


Type: Array of strings


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[0-9A-Za-z ]*`



Required: No




**[requiredFileSystemLocationNamesToRemove](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The required file system location names to remove from the queue.


Type: Array of strings


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[0-9A-Za-z ]*`



Required: No




**[roleArn](#API_UpdateQueue_RequestSyntax "#API_UpdateQueue_RequestSyntax")**


The IAM role ARN that's used to run jobs from this queue.


Type: String


Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`



Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateQueue")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateQueue")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateQueue")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateQueue")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateQueue")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateQueue")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateQueue")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateQueue")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateQueue")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateQueue "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateQueue")
