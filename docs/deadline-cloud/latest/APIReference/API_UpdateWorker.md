# UpdateWorker

Updates a worker.


## Request Syntax



```
PATCH /2023-10-12/farms/`farmId`/fleets/`fleetId`/workers/`workerId` HTTP/1.1
Content-type: application/json

{
   "capabilities": { 
      "amounts": [ 
         { 
            "name": "`string`",
            "value": `number`
         }
      ],
      "attributes": [ 
         { 
            "name": "`string`",
            "values": [ "`string`" ]
         }
      ]
   },
   "hostProperties": { 
      "hostName": "`string`",
      "ipAddresses": { 
         "ipV4Addresses": [ "`string`" ],
         "ipV6Addresses": [ "`string`" ]
      }
   },
   "status": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_UpdateWorker_RequestSyntax "#API_UpdateWorker_RequestSyntax")**


The farm ID to update.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[fleetId](#API_UpdateWorker_RequestSyntax "#API_UpdateWorker_RequestSyntax")**


The fleet ID to update.


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**[workerId](#API_UpdateWorker_RequestSyntax "#API_UpdateWorker_RequestSyntax")**


The worker ID to update.


Pattern: `worker-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[capabilities](#API_UpdateWorker_RequestSyntax "#API_UpdateWorker_RequestSyntax")**


The worker capabilities to update.


Type: [WorkerCapabilities](API_WorkerCapabilities.md "API_WorkerCapabilities.md") object


Required: No




**[hostProperties](#API_UpdateWorker_RequestSyntax "#API_UpdateWorker_RequestSyntax")**


The host properties to update.


Type: [HostPropertiesRequest](API_HostPropertiesRequest.md "API_HostPropertiesRequest.md") object


Required: No




**[status](#API_UpdateWorker_RequestSyntax "#API_UpdateWorker_RequestSyntax")**


The worker status to update.


Type: String


Valid Values: `STARTED | STOPPING | STOPPED`



Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "hostConfiguration": { 
      "scriptBody": "***string***",
      "scriptTimeoutSeconds": ***number***
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
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[hostConfiguration](#API_UpdateWorker_ResponseSyntax "#API_UpdateWorker_ResponseSyntax")**


The script that runs as a worker is starting up that you can use to provide additional
 configuration for workers in your fleet.


Type: [HostConfiguration](API_HostConfiguration.md "API_HostConfiguration.md") object




**[log](#API_UpdateWorker_ResponseSyntax "#API_UpdateWorker_ResponseSyntax")**


The worker log to update.


Type: [LogConfiguration](API_LogConfiguration.md "API_LogConfiguration.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


You don't have permission to perform the action.





**context** 


Information about the resources in use when the exception was thrown.




HTTP Status Code: 403




**ConflictException** 


Your request has conflicting operations. This can occur if you're trying to perform more
 than one operation on the same resource at the same time.





**context** 


Information about the resources in use when the exception was thrown.




**reason** 


A description of the error.




**resourceId** 


The identifier of the resource in use.




**resourceType** 


The type of the resource in use.




HTTP Status Code: 409




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/UpdateWorker")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/UpdateWorker")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdateWorker")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/UpdateWorker")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdateWorker")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/UpdateWorker")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/UpdateWorker")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/UpdateWorker")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/UpdateWorker")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateWorker "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdateWorker")
