# SearchWorkers

Searches for workers.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/search/workers HTTP/1.1
Content-type: application/json

{
   "[filterExpressions](#deadlinecloud-SearchWorkers-request-filterExpressions "#deadlinecloud-SearchWorkers-request-filterExpressions")": { 
      "[filters](API_SearchGroupedFilterExpressions.md#deadlinecloud-Type-SearchGroupedFilterExpressions-filters "API_SearchGroupedFilterExpressions.md#deadlinecloud-Type-SearchGroupedFilterExpressions-filters")": [ 
         { ... }
      ],
      "[operator](API_SearchGroupedFilterExpressions.md#deadlinecloud-Type-SearchGroupedFilterExpressions-operator "API_SearchGroupedFilterExpressions.md#deadlinecloud-Type-SearchGroupedFilterExpressions-operator")": "`string`"
   },
   "[fleetIds](#deadlinecloud-SearchWorkers-request-fleetIds "#deadlinecloud-SearchWorkers-request-fleetIds")": [ "`string`" ],
   "[itemOffset](#deadlinecloud-SearchWorkers-request-itemOffset "#deadlinecloud-SearchWorkers-request-itemOffset")": `number`,
   "[pageSize](#deadlinecloud-SearchWorkers-request-pageSize "#deadlinecloud-SearchWorkers-request-pageSize")": `number`,
   "[sortExpressions](#deadlinecloud-SearchWorkers-request-sortExpressions "#deadlinecloud-SearchWorkers-request-sortExpressions")": [ 
      { ... }
   ]
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_SearchWorkers_RequestSyntax "#API_SearchWorkers_RequestSyntax")**


The farm ID in the workers search.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[filterExpressions](#API_SearchWorkers_RequestSyntax "#API_SearchWorkers_RequestSyntax")**


The filter expression, `AND` or `OR`, to use
when searching among a group of search strings in a resource.

You can use two groupings per search each within parenthesis `()`.


Type: [SearchGroupedFilterExpressions](API_SearchGroupedFilterExpressions.md "API_SearchGroupedFilterExpressions.md") object


Required: No




**[fleetIds](#API_SearchWorkers_RequestSyntax "#API_SearchWorkers_RequestSyntax")**


The fleet ID of the workers to search for.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 10 items.


Pattern: `fleet-[0-9a-f]{32}`



Required: Yes




**[itemOffset](#API_SearchWorkers_RequestSyntax "#API_SearchWorkers_RequestSyntax")**


Defines how far into the scrollable list to start the return of results.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.


Required: Yes




**[pageSize](#API_SearchWorkers_RequestSyntax "#API_SearchWorkers_RequestSyntax")**


Specifies the number of items per page for the resource.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 100.


Required: No




**[sortExpressions](#API_SearchWorkers_RequestSyntax "#API_SearchWorkers_RequestSyntax")**


The search terms for a resource.


Type: Array of [SearchSortExpression](API_SearchSortExpression.md "API_SearchSortExpression.md") objects


Array Members: Minimum number of 1 item. Maximum number of 5 items.


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[nextItemOffset](#deadlinecloud-SearchWorkers-response-nextItemOffset "#deadlinecloud-SearchWorkers-response-nextItemOffset")": ***number***,
   "[totalResults](#deadlinecloud-SearchWorkers-response-totalResults "#deadlinecloud-SearchWorkers-response-totalResults")": ***number***,
   "[workers](#deadlinecloud-SearchWorkers-response-workers "#deadlinecloud-SearchWorkers-response-workers")": [ 
      { 
         "[createdAt](API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-createdAt "API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-createdAt")": "***string***",
         "[createdBy](API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-createdBy "API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-createdBy")": "***string***",
         "[fleetId](API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-fleetId "API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-fleetId")": "***string***",
         "[hostProperties](API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-hostProperties "API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-hostProperties")": { 
            "[ec2InstanceArn](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceArn "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceArn")": "***string***",
            "[ec2InstanceType](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceType "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ec2InstanceType")": "***string***",
            "[hostName](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-hostName "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-hostName")": "***string***",
            "[ipAddresses](API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ipAddresses "API_HostPropertiesResponse.md#deadlinecloud-Type-HostPropertiesResponse-ipAddresses")": { 
               "[ipV4Addresses](API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV4Addresses "API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV4Addresses")": [ "***string***" ],
               "[ipV6Addresses](API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV6Addresses "API_IpAddresses.md#deadlinecloud-Type-IpAddresses-ipV6Addresses")": [ "***string***" ]
            }
         },
         "[status](API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-status "API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-status")": "***string***",
         "[updatedAt](API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-updatedAt "API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-updatedAt")": "***string***",
         "[updatedBy](API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-updatedBy "API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-updatedBy")": "***string***",
         "[workerId](API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-workerId "API_WorkerSearchSummary.md#deadlinecloud-Type-WorkerSearchSummary-workerId")": "***string***"
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[nextItemOffset](#API_SearchWorkers_ResponseSyntax "#API_SearchWorkers_ResponseSyntax")**


The next incremental starting point after the defined `itemOffset`.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.




**[totalResults](#API_SearchWorkers_ResponseSyntax "#API_SearchWorkers_ResponseSyntax")**


The total number of results in the search.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 10000.




**[workers](#API_SearchWorkers_ResponseSyntax "#API_SearchWorkers_ResponseSyntax")**


The workers for the search.


Type: Array of [WorkerSearchSummary](API_WorkerSearchSummary.md "API_WorkerSearchSummary.md") objects




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/SearchWorkers")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/SearchWorkers")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchWorkers")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/SearchWorkers")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchWorkers")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/SearchWorkers")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/SearchWorkers")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/SearchWorkers")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/SearchWorkers")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchWorkers "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchWorkers")
