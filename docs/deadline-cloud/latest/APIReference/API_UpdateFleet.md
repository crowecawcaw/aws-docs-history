# UpdateFleet

Updates a fleet.


## Request Syntax



```
PATCH /2023-10-12/farms/`farmId`/fleets/`fleetId` HTTP/1.1
X-Amz-Client-Token: `clientToken`
Content-type: application/json

{
   "[configuration](#deadlinecloud-UpdateFleet-request-configuration "#deadlinecloud-UpdateFleet-request-configuration")": { ... },
   "[description](#deadlinecloud-UpdateFleet-request-description "#deadlinecloud-UpdateFleet-request-description")": "`string`",
   "[displayName](#deadlinecloud-UpdateFleet-request-displayName "#deadlinecloud-UpdateFleet-request-displayName")": "`string`",
   "[hostConfiguration](#deadlinecloud-UpdateFleet-request-hostConfiguration "#deadlinecloud-UpdateFleet-request-hostConfiguration")": { 
      "[scriptBody](API_HostConfiguration.md#deadlinecloud-Type-HostConfiguration-scriptBody "API_HostConfiguration.md#deadlinecloud-Type-HostConfiguration-scriptBody")": "`string`",
      "[scriptTimeoutSeconds](API_HostConfiguration.md#deadlinecloud-Type-HostConfiguration-scriptTimeoutSeconds "API_HostConfiguration.md#deadlinecloud-Type-HostConfiguration-scriptTimeoutSeconds")": `number`
   },
   "[maxWorkerCount](#deadlinecloud-UpdateFleet-request-maxWorkerCount "#deadlinecloud-UpdateFleet-request-maxWorkerCount")": `number`,
   "[minWorkerCount](#deadlinecloud-UpdateFleet-request-minWorkerCount "#deadlinecloud-UpdateFleet-request-minWorkerCount")": `number`,
   "[roleArn](#deadlinecloud-UpdateFleet-request-roleArn "#deadlinecloud-UpdateFleet-request-roleArn")": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[clientToken](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


The unique token which the server uses to recognize retries of the same request.


Length Constraints: Minimum length of 1. Maximum length of 64.




**[farmId](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


The farm ID to update.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[fleetId](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


The fleet ID to update.


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[configuration](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


The fleet configuration to update.


Type: [FleetConfiguration](API_FleetConfiguration.md "API_FleetConfiguration.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: No




**[description](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


The description of the fleet to update.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.


Required: No




**[displayName](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


The display name of the fleet to update.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.


Required: No




**[hostConfiguration](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


Provides a script that runs as a worker is starting up that you can use to provide
 additional configuration for workers in your fleet.


Type: [HostConfiguration](API_HostConfiguration.md "API_HostConfiguration.md") object


Required: No




**[maxWorkerCount](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


The maximum number of workers in the fleet.



 Deadline Cloud limits the number of workers to less than or equal to the fleet's
 maximum worker count. The service maintains eventual consistency for the worker count. If
 you make multiple rapid calls to `CreateWorker` before the field updates, you
 might exceed your fleet's maximum worker count. For example, if your
 `maxWorkerCount` is 10 and you currently have 9 workers, making two quick
 `CreateWorker` calls might successfully create 2 workers instead of 1,
 resulting in 11 total workers.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: No




**[minWorkerCount](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


The minimum number of workers in the fleet.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.


Required: No




**[roleArn](#API_UpdateFleet_RequestSyntax "#API_UpdateFleet_RequestSyntax")**


The IAM role ARN that the fleet's workers assume while running jobs.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateFleet")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateFleet")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateFleet")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateFleet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateFleet")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateFleet")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateFleet")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateFleet")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateFleet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateFleet "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateFleet")
