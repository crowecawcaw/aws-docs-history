# CreateQueue

Creates a queue to coordinate the order in which jobs run on a farm. A queue can also
 specify where to pull resources and indicate where to output completed jobs.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/queues HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "allowedStorageProfileIds": [ "`string`" ],
   "defaultBudgetAction": "`string`",
   "description": "`string`",
   "displayName": "`string`",
   "jobAttachmentSettings": { 
      "rootPrefix": "`string`",
      "s3BucketName": "`string`"
   },
   "jobRunAsUser": { 
      "posix": { 
         "group": "`string`",
         "user": "`string`"
      },
      "runAs": "`string`",
      "windows": { 
         "passwordArn": "`string`",
         "user": "`string`"
      }
   },
   "requiredFileSystemLocationNames": [ "`string`" ],
   "roleArn": "`string`",
   "tags": { 
      "`string`" : "`string`" 
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The farm ID of the farm to connect to the queue.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[allowedStorageProfileIds](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The storage profile IDs to include in the queue.


Type: Array of strings


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Pattern: `sp-[0-9a-f]{32}`



Required: No




**[defaultBudgetAction](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The default action to take on a queue if a budget isn't configured.


Type: String


Valid Values: `NONE | STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`



Required: No




**[description](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The description of the queue.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.


Required: No




**[displayName](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The display name of the queue.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: Yes




**[jobAttachmentSettings](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The job attachment settings for the queue. These are the Amazon S3 bucket name and the Amazon S3
 prefix.


Type: [JobAttachmentSettings](API_JobAttachmentSettings.md "API_JobAttachmentSettings.md") object


Required: No




**[jobRunAsUser](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The jobs in the queue run as the specified POSIX user.


Type: [JobRunAsUser](API_JobRunAsUser.md "API_JobRunAsUser.md") object


Required: No




**[requiredFileSystemLocationNames](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The file system location name to include in the queue.


Type: Array of strings


Array Members: Minimum number of 0 items. Maximum number of 20 items.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[0-9A-Za-z ]*`



Required: No




**[roleArn](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


The IAM role ARN that workers will use while running jobs for this queue.


Type: String


Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`



Required: No




**[tags](#API_CreateQueue_RequestSyntax "#API_CreateQueue_RequestSyntax")**


Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.


Type: String to string map


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "queueId": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[queueId](#API_CreateQueue_ResponseSyntax "#API_CreateQueue_ResponseSyntax")**


The queue ID.


Type: String


Pattern: `queue-[0-9a-f]{32}`





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/CreateQueue")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/CreateQueue")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/CreateQueue")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/CreateQueue")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/CreateQueue")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/CreateQueue")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/CreateQueue")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/CreateQueue")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/CreateQueue")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateQueue "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/CreateQueue")
