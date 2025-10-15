# GetSession

Gets a session.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/queues/`queueId`/jobs/`jobId`/sessions/`sessionId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetSession_RequestSyntax "#API_GetSession_RequestSyntax")**


The farm ID for the session.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[jobId](#API_GetSession_RequestSyntax "#API_GetSession_RequestSyntax")**


The job ID for the session.


Pattern: `job-[0-9a-f]{32}`



Required: Yes




**[queueId](#API_GetSession_RequestSyntax "#API_GetSession_RequestSyntax")**


The queue ID for the session.


Pattern: `queue-[0-9a-f]{32}`



Required: Yes




**[sessionId](#API_GetSession_RequestSyntax "#API_GetSession_RequestSyntax")**


The session ID.


Pattern: `session-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[endedAt](#deadlinecloud-GetSession-response-endedAt "#deadlinecloud-GetSession-response-endedAt")": "***string***",
   "[fleetId](#deadlinecloud-GetSession-response-fleetId "#deadlinecloud-GetSession-response-fleetId")": "***string***",
   "[hostProperties](#deadlinecloud-GetSession-response-hostProperties "#deadlinecloud-GetSession-response-hostProperties")": { 
      "[ec2InstanceArn](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceArn "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceArn")": "***string***",
      "[ec2InstanceType](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceType "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceType")": "***string***",
      "[hostName](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-hostName "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-hostName")": "***string***",
      "[ipAddresses](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ipAddresses "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ipAddresses")": { 
         "[ipV4Addresses](API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV4Addresses "API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV4Addresses")": [ "***string***" ],
         "[ipV6Addresses](API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV6Addresses "API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV6Addresses")": [ "***string***" ]
      }
   },
   "[lifecycleStatus](#deadlinecloud-GetSession-response-lifecycleStatus "#deadlinecloud-GetSession-response-lifecycleStatus")": "***string***",
   "[log](#deadlinecloud-GetSession-response-log "#deadlinecloud-GetSession-response-log")": { 
      "[error](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-error "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-error")": "***string***",
      "[logDriver](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-logDriver "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-logDriver")": "***string***",
      "[options](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-options "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-options")": { 
         "***string***" : "***string***" 
      },
      "[parameters](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-parameters "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-parameters")": { 
         "***string***" : "***string***" 
      }
   },
   "[sessionId](#deadlinecloud-GetSession-response-sessionId "#deadlinecloud-GetSession-response-sessionId")": "***string***",
   "[startedAt](#deadlinecloud-GetSession-response-startedAt "#deadlinecloud-GetSession-response-startedAt")": "***string***",
   "[targetLifecycleStatus](#deadlinecloud-GetSession-response-targetLifecycleStatus "#deadlinecloud-GetSession-response-targetLifecycleStatus")": "***string***",
   "[updatedAt](#deadlinecloud-GetSession-response-updatedAt "#deadlinecloud-GetSession-response-updatedAt")": "***string***",
   "[updatedBy](#deadlinecloud-GetSession-response-updatedBy "#deadlinecloud-GetSession-response-updatedBy")": "***string***",
   "[workerId](#deadlinecloud-GetSession-response-workerId "#deadlinecloud-GetSession-response-workerId")": "***string***",
   "[workerLog](#deadlinecloud-GetSession-response-workerLog "#deadlinecloud-GetSession-response-workerLog")": { 
      "[error](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-error "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-error")": "***string***",
      "[logDriver](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-logDriver "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-logDriver")": "***string***",
      "[options](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-options "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-options")": { 
         "***string***" : "***string***" 
      },
      "[parameters](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-parameters "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-parameters")": { 
         "***string***" : "***string***" 
      }
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[endedAt](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The date and time the resource ended running.


Type: Timestamp




**[fleetId](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The fleet ID for the session.


Type: String


Pattern: `fleet-[0-9a-f]{32}`





**[hostProperties](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


Provides the Amazon EC2 properties of the host.


Type: [HostPropertiesResponse](API_HostPropertiesResponse.md "API_HostPropertiesResponse.md") object




**[lifecycleStatus](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The life cycle status of the session.


Type: String


Valid Values: `STARTED | UPDATE_IN_PROGRESS | UPDATE_SUCCEEDED | UPDATE_FAILED | ENDED`





**[log](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The session log.


Type: [LogConfiguration](API_LogConfiguration.md "API_LogConfiguration.md") object




**[sessionId](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The session ID.


Type: String


Pattern: `session-[0-9a-f]{32}`





**[startedAt](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The date and time the resource started running.


Type: Timestamp




**[targetLifecycleStatus](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The life cycle status with which the session started.


Type: String


Valid Values: `ENDED`





**[updatedAt](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The date and time the resource was updated.


Type: Timestamp




**[updatedBy](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The user or system that updated this resource.


Type: String




**[workerId](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The worker ID for the session.


Type: String


Pattern: `worker-[0-9a-f]{32}`





**[workerLog](#API_GetSession_ResponseSyntax "#API_GetSession_ResponseSyntax")**


The worker log for the session.


Type: [LogConfiguration](API_LogConfiguration.md "API_LogConfiguration.md") object




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetSession")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetSession")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetSession")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetSession")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetSession")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetSession")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetSession")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetSession")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetSession")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetSession "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetSession")
