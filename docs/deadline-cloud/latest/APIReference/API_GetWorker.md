# GetWorker

Gets a worker.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/fleets/`fleetId`/workers/`workerId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetWorker_RequestSyntax "#API_GetWorker_RequestSyntax")**


The farm ID for the worker.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[fleetId](#API_GetWorker_RequestSyntax "#API_GetWorker_RequestSyntax")**


The fleet ID of the worker.


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**[workerId](#API_GetWorker_RequestSyntax "#API_GetWorker_RequestSyntax")**


The worker ID.


Pattern: `worker-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "***string***",
   "createdBy": "***string***",
   "farmId": "***string***",
   "fleetId": "***string***",
   "hostProperties": { 
      "ec2InstanceArn": "***string***",
      "ec2InstanceType": "***string***",
      "hostName": "***string***",
      "ipAddresses": { 
         "ipV4Addresses": [ "***string***" ],
         "ipV6Addresses": [ "***string***" ]
      }
   },
   "log": { 
      "error": "***string***",
      "logDriver": "***string***",
      "options": { 
         "***string***" : "***string***" 
      },
      "parameters": { 
         "***string***" : "***string***" 
      }
   },
   "status": "***string***",
   "updatedAt": "***string***",
   "updatedBy": "***string***",
   "workerId": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[createdAt](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The date and time the resource was created.


Type: Timestamp




**[createdBy](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The user or system that created this resource.


Type: String




**[farmId](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The farm ID.


Type: String


Pattern: `farm-[0-9a-f]{32}`





**[fleetId](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The fleet ID.


Type: String


Pattern: `fleet-[0-9a-f]{32}`





**[hostProperties](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The host properties for the worker.


Type: [HostPropertiesResponse](API_HostPropertiesResponse.md "API_HostPropertiesResponse.md") object




**[log](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The logs for the associated worker.


Type: [LogConfiguration](API_LogConfiguration.md "API_LogConfiguration.md") object




**[status](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The status of the worker.


Type: String


Valid Values: `CREATED | STARTED | STOPPING | STOPPED | NOT_RESPONDING | NOT_COMPATIBLE | RUNNING | IDLE`





**[updatedAt](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The date and time the resource was updated.


Type: Timestamp




**[updatedBy](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The user or system that updated this resource.


Type: String




**[workerId](#API_GetWorker_ResponseSyntax "#API_GetWorker_ResponseSyntax")**


The worker ID.


Type: String


Pattern: `worker-[0-9a-f]{32}`





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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetWorker")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetWorker")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetWorker")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetWorker")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetWorker")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetWorker")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetWorker")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetWorker")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetWorker")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetWorker "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetWorker")
