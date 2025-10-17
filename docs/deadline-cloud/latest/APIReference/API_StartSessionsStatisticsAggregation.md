# StartSessionsStatisticsAggregation

Starts an asynchronous request for getting aggregated statistics about queues and farms.
 Get the statistics using the `GetSessionsStatisticsAggregation` operation. You
 can only have one running aggregation for your Deadline Cloud farm. Call the
 `GetSessionsStatisticsAggregation` operation and check the
 `status` field to see if an aggregation is running. Statistics are available
 for 1 hour after you call the `StartSessionsStatisticsAggregation`
 operation.


## Request Syntax



```
POST /2023-10-12/farms/`farmId`/sessions-statistics-aggregation HTTP/1.1
Content-type: application/json

{
   "endTime": "`string`",
   "groupBy": [ "`string`" ],
   "period": "`string`",
   "resourceIds": { ... },
   "startTime": "`string`",
   "statistics": [ "`string`" ],
   "timezone": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[farmId](#API_StartSessionsStatisticsAggregation_RequestSyntax "#API_StartSessionsStatisticsAggregation_RequestSyntax")**


The identifier of the farm that contains queues or fleets to return statistics
 for.


Pattern: `farm-[0-9a-f]{32}`



Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[endTime](#API_StartSessionsStatisticsAggregation_RequestSyntax "#API_StartSessionsStatisticsAggregation_RequestSyntax")**


The Linux timestamp of the date and time that the statistics end.


Type: Timestamp


Required: Yes




**[groupBy](#API_StartSessionsStatisticsAggregation_RequestSyntax "#API_StartSessionsStatisticsAggregation_RequestSyntax")**


The field to use to group the statistics.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 2 items.


Valid Values: `QUEUE_ID | FLEET_ID | JOB_ID | USER_ID | USAGE_TYPE | INSTANCE_TYPE | LICENSE_PRODUCT`



Required: Yes




**[period](#API_StartSessionsStatisticsAggregation_RequestSyntax "#API_StartSessionsStatisticsAggregation_RequestSyntax")**


The period to aggregate the statistics.


Type: String


Valid Values: `HOURLY | DAILY | WEEKLY | MONTHLY`



Required: No




**[resourceIds](#API_StartSessionsStatisticsAggregation_RequestSyntax "#API_StartSessionsStatisticsAggregation_RequestSyntax")**


A list of fleet IDs or queue IDs to gather statistics for.


Type: [SessionsStatisticsResources](API_SessionsStatisticsResources.md "API_SessionsStatisticsResources.md") object



**Note:** This object is a Union. Only one member of this object can be specified or returned.


Required: Yes




**[startTime](#API_StartSessionsStatisticsAggregation_RequestSyntax "#API_StartSessionsStatisticsAggregation_RequestSyntax")**


The Linux timestamp of the date and time that the statistics start.


Type: Timestamp


Required: Yes




**[statistics](#API_StartSessionsStatisticsAggregation_RequestSyntax "#API_StartSessionsStatisticsAggregation_RequestSyntax")**


One to four statistics to return.


Type: Array of strings


Array Members: Minimum number of 1 item. Maximum number of 4 items.


Valid Values: `SUM | MIN | MAX | AVG`



Required: Yes




**[timezone](#API_StartSessionsStatisticsAggregation_RequestSyntax "#API_StartSessionsStatisticsAggregation_RequestSyntax")**


The timezone to use for the statistics. Use UTC notation such as "UTC+8."


Type: String


Length Constraints: Fixed length of 9.


Pattern: `UTC[-+][01][0-9]:(30|00)`



Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "aggregationId": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[aggregationId](#API_StartSessionsStatisticsAggregation_ResponseSyntax "#API_StartSessionsStatisticsAggregation_ResponseSyntax")**


A unique identifier for the aggregated statistics. Use this identifier with the
 `GetAggregatedStatisticsForSessions` operation to return the
 statistics.


Type: String


Pattern: `[0-9a-f]{32}`





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/StartSessionsStatisticsAggregation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/DotNetSDKV3/deadline-2023-10-12/StartSessionsStatisticsAggregation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StartSessionsStatisticsAggregation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/StartSessionsStatisticsAggregation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StartSessionsStatisticsAggregation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/StartSessionsStatisticsAggregation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/StartSessionsStatisticsAggregation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/StartSessionsStatisticsAggregation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/StartSessionsStatisticsAggregation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StartSessionsStatisticsAggregation "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StartSessionsStatisticsAggregation")
