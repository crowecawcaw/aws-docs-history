# ListWorkers

Lists workers.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/fleets/`fleetId`/workers?maxResults=`maxResults`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_ListWorkers_RequestSyntax "#API_ListWorkers_RequestSyntax")**


The farm ID connected to the workers.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[fleetId](#API_ListWorkers_RequestSyntax "#API_ListWorkers_RequestSyntax")**


The fleet ID of the workers.


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**[maxResults](#API_ListWorkers_RequestSyntax "#API_ListWorkers_RequestSyntax")**


The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.


Valid Range: Minimum value of 1. Maximum value of 100.




**[nextToken](#API_ListWorkers_RequestSyntax "#API_ListWorkers_RequestSyntax")**


The token for the next set of results, or `null` to start from the beginning.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[nextToken](#deadlinecloud-ListWorkers-response-nextToken "#deadlinecloud-ListWorkers-response-nextToken")": "***string***",
   "[workers](#deadlinecloud-ListWorkers-response-workers "#deadlinecloud-ListWorkers-response-workers")": [ 
      { 
         "[createdAt](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-createdAt "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-createdAt")": "***string***",
         "[createdBy](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-createdBy "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-createdBy")": "***string***",
         "[farmId](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-farmId "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-farmId")": "***string***",
         "[fleetId](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-fleetId "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-fleetId")": "***string***",
         "[hostProperties](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-hostProperties "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-hostProperties")": { 
            "[ec2InstanceArn](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceArn "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceArn")": "***string***",
            "[ec2InstanceType](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceType "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceType")": "***string***",
            "[hostName](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-hostName "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-hostName")": "***string***",
            "[ipAddresses](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ipAddresses "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ipAddresses")": { 
               "[ipV4Addresses](API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV4Addresses "API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV4Addresses")": [ "***string***" ],
               "[ipV6Addresses](API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV6Addresses "API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV6Addresses")": [ "***string***" ]
            }
         },
         "[log](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-log "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-log")": { 
            "[error](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-error "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-error")": "***string***",
            "[logDriver](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-logDriver "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-logDriver")": "***string***",
            "[options](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-options "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-options")": { 
               "***string***" : "***string***" 
            },
            "[parameters](API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-parameters "API_LogConfiguration.md#deadlinecloud-Type-LogConfiguration-parameters")": { 
               "***string***" : "***string***" 
            }
         },
         "[status](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-status "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-status")": "***string***",
         "[updatedAt](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-updatedAt "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-updatedAt")": "***string***",
         "[updatedBy](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-updatedBy "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-updatedBy")": "***string***",
         "[workerId](API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-workerId "API_WorkerSummary.md#deadlinecloud-Type-WorkerSummary-workerId")": "***string***"
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[nextToken](#API_ListWorkers_ResponseSyntax "#API_ListWorkers_ResponseSyntax")**


If Deadline Cloud returns `nextToken`, then there are more results available. The value of `nextToken` is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then `nextToken` is set to `null`. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 `ValidationException` error.


Type: String




**[workers](#API_ListWorkers_ResponseSyntax "#API_ListWorkers_ResponseSyntax")**


The workers on the list.


Type: Array of [WorkerSummary](API_WorkerSummary.md "API_WorkerSummary.md") objects




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListWorkers")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/ListWorkers")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListWorkers")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListWorkers")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListWorkers")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListWorkers")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListWorkers")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListWorkers")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListWorkers")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListWorkers "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListWorkers")
