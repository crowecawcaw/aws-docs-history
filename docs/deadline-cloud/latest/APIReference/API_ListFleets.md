# ListFleets

Lists fleets.


## Request Syntax



```
GET /2023-10-12/farms/`farmId`/fleets?displayName=`displayName`&maxResults=`maxResults`&nextToken=`nextToken`&principalId=`principalId`&status=`status` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[displayName](#API_ListFleets_RequestSyntax "#API_ListFleets_RequestSyntax")**


The display names of a list of fleets.


###### Important

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.


Length Constraints: Minimum length of 1. Maximum length of 100.




**[farmId](#API_ListFleets_RequestSyntax "#API_ListFleets_RequestSyntax")**


The farm ID of the fleets.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




**[maxResults](#API_ListFleets_RequestSyntax "#API_ListFleets_RequestSyntax")**


The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.


Valid Range: Minimum value of 1. Maximum value of 100.




**[nextToken](#API_ListFleets_RequestSyntax "#API_ListFleets_RequestSyntax")**


The token for the next set of results, or `null` to start from the beginning.




**[principalId](#API_ListFleets_RequestSyntax "#API_ListFleets_RequestSyntax")**


The principal ID of the members to include in the fleet.


Length Constraints: Minimum length of 1. Maximum length of 47.


Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`





**[status](#API_ListFleets_RequestSyntax "#API_ListFleets_RequestSyntax")**


The status of the fleet.


Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | SUSPENDED`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[fleets](#deadlinecloud-ListFleets-response-fleets "#deadlinecloud-ListFleets-response-fleets")": [ 
      { 
         "[autoScalingStatus](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-autoScalingStatus "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-autoScalingStatus")": "***string***",
         "[configuration](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-configuration "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-configuration")": { ... },
         "[createdAt](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-createdAt "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-createdAt")": "***string***",
         "[createdBy](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-createdBy "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-createdBy")": "***string***",
         "[displayName](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-displayName "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-displayName")": "***string***",
         "[farmId](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-farmId "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-farmId")": "***string***",
         "[fleetId](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-fleetId "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-fleetId")": "***string***",
         "[maxWorkerCount](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-maxWorkerCount "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-maxWorkerCount")": ***number***,
         "[minWorkerCount](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-minWorkerCount "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-minWorkerCount")": ***number***,
         "[status](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-status "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-status")": "***string***",
         "[statusMessage](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-statusMessage "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-statusMessage")": "***string***",
         "[targetWorkerCount](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-targetWorkerCount "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-targetWorkerCount")": ***number***,
         "[updatedAt](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-updatedAt "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-updatedAt")": "***string***",
         "[updatedBy](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-updatedBy "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-updatedBy")": "***string***",
         "[workerCount](API_FleetSummary.md#deadlinecloud-Type-FleetSummary-workerCount "API_FleetSummary.md#deadlinecloud-Type-FleetSummary-workerCount")": ***number***
      }
   ],
   "[nextToken](#deadlinecloud-ListFleets-response-nextToken "#deadlinecloud-ListFleets-response-nextToken")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[fleets](#API_ListFleets_ResponseSyntax "#API_ListFleets_ResponseSyntax")**


The fleets on the list.


Type: Array of [FleetSummary](API_FleetSummary.md "API_FleetSummary.md") objects




**[nextToken](#API_ListFleets_ResponseSyntax "#API_ListFleets_ResponseSyntax")**


If Deadline Cloud returns `nextToken`, then there are more results available. The value of `nextToken` is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then `nextToken` is set to `null`. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 `ValidationException` error.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListFleets")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/ListFleets")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListFleets")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListFleets")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListFleets")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListFleets")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListFleets")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListFleets")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListFleets")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListFleets "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListFleets")
