# GetFleet

Get a fleet.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/fleets/`fleetId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_GetFleet_RequestSyntax "#API_GetFleet_RequestSyntax")**


The farm ID of the farm in the fleet.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[fleetId](#API_GetFleet_RequestSyntax "#API_GetFleet_RequestSyntax")**


The fleet ID of the fleet to get.


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "autoScalingStatus": "***string***",
   "capabilities": { 
      "amounts": [ 
         { 
            "max": ***number***,
            "min": ***number***,
            "name": "***string***"
         }
      ],
      "attributes": [ 
         { 
            "name": "***string***",
            "values": [ "***string***" ]
         }
      ]
   },
   "configuration": { ... },
   "createdAt": "***string***",
   "createdBy": "***string***",
   "description": "***string***",
   "displayName": "***string***",
   "farmId": "***string***",
   "fleetId": "***string***",
   "hostConfiguration": { 
      "scriptBody": "***string***",
      "scriptTimeoutSeconds": ***number***
   },
   "maxWorkerCount": ***number***,
   "minWorkerCount": ***number***,
   "roleArn": "***string***",
   "status": "***string***",
   "statusMessage": "***string***",
   "targetWorkerCount": ***number***,
   "updatedAt": "***string***",
   "updatedBy": "***string***",
   "workerCount": ***number***
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[autoScalingStatus](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The AWS Auto Scaling status of the fleet. Either `GROWING`, `STEADY`, or
 `SHRINKING`.


Type: String


Valid Values: `GROWING | STEADY | SHRINKING`





**[capabilities](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


Outlines what the fleet is capable of for minimums, maximums, and naming, in addition to
 attribute names and values.


Type: [FleetCapabilities](API_FleetCapabilities.md "API_FleetCapabilities.md") object




**[configuration](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The configuration setting for the fleet.


Type: [FleetConfiguration](API_FleetConfiguration.md "API_FleetConfiguration.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.




**[createdAt](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The date and time the resource was created.


Type: Timestamp




**[createdBy](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The user or system that created this resource.


Type: String




**[description](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The description of the fleet.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 100.




**[displayName](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The display name of the fleet.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 100.




**[farmId](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The farm ID of the farm in the fleet.


Type: String


Pattern: `farm-[0-9a-f]{32}`





**[fleetId](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The fleet ID.


Type: String


Pattern: `fleet-[0-9a-f]{32}`





**[hostConfiguration](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The script that runs as a worker is starting up that you can use to provide additional
 configuration for workers in your fleet.


Type: [HostConfiguration](API_HostConfiguration.md "API_HostConfiguration.md") object




**[maxWorkerCount](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The maximum number of workers specified in the fleet.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.




**[minWorkerCount](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The minimum number of workers specified in the fleet.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 2147483647.




**[roleArn](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The IAM role ARN.


Type: String


Pattern: `arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+`





**[status](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The status of the fleet.


Type: String


Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | SUSPENDED`





**[statusMessage](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


A message that communicates a suspended status of the fleet.


Type: String




**[targetWorkerCount](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The number of target workers in the fleet.


Type: Integer




**[updatedAt](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The date and time the resource was updated.


Type: Timestamp




**[updatedBy](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The user or system that updated this resource.


Type: String




**[workerCount](#API_GetFleet_ResponseSyntax "#API_GetFleet_ResponseSyntax")**


The number of workers in the fleet.


Type: Integer




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/GetFleet")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/GetFleet")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/GetFleet")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/GetFleet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/GetFleet")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/GetFleet")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/GetFleet")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/GetFleet")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/GetFleet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetFleet "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/GetFleet")
