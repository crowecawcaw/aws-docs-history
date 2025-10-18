# DescribeQuery

Returns metadata about a query, including query run time in milliseconds, number of
 events scanned and matched, and query status. If the query results were delivered to an S3 bucket, 
 the response also provides the S3 URI and the delivery status.

You must specify either `QueryId` or `QueryAlias`. Specifying the `QueryAlias` parameter 
 returns information about the last query run for the alias. You can provide 
 `RefreshId` along with `QueryAlias` to view the query results 
 of a dashboard query for the specified `RefreshId`.


## Request Syntax



```
{
   "EventDataStore": "`string`",
   "EventDataStoreOwnerAccountId": "`string`",
   "QueryAlias": "`string`",
   "QueryId": "`string`",
   "RefreshId": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[EventDataStore](#API_DescribeQuery_RequestSyntax "#API_DescribeQuery_RequestSyntax")**



*This parameter has been deprecated.*



The ARN (or the ID suffix of the ARN) of an event data store on which the specified
 query was run.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 256.


Pattern: `^[a-zA-Z0-9._/\-:]+$`



Required: No




**[EventDataStoreOwnerAccountId](#API_DescribeQuery_RequestSyntax "#API_DescribeQuery_RequestSyntax")**



The account ID of the event data store owner.



Type: String


Length Constraints: Minimum length of 12. Maximum length of 16.


Pattern: `\d+`



Required: No




**[QueryAlias](#API_DescribeQuery_RequestSyntax "#API_DescribeQuery_RequestSyntax")**



 The alias that identifies a query template.
 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Pattern: `^[a-zA-Z][a-zA-Z0-9._\-]*$`



Required: No




**[QueryId](#API_DescribeQuery_RequestSyntax "#API_DescribeQuery_RequestSyntax")**


The query ID.


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9\-]+$`



Required: No




**[RefreshId](#API_DescribeQuery_RequestSyntax "#API_DescribeQuery_RequestSyntax")**



The ID of the dashboard refresh.



Type: String


Length Constraints: Minimum length of 10. Maximum length of 20.


Pattern: `\d+`



Required: No




## Response Syntax



```
{
   "DeliveryS3Uri": "***string***",
   "DeliveryStatus": "***string***",
   "ErrorMessage": "***string***",
   "EventDataStoreOwnerAccountId": "***string***",
   "Prompt": "***string***",
   "QueryId": "***string***",
   "QueryStatistics": { 
      "BytesScanned": ***number***,
      "CreationTime": ***number***,
      "EventsMatched": ***number***,
      "EventsScanned": ***number***,
      "ExecutionTimeInMillis": ***number***
   },
   "QueryStatus": "***string***",
   "QueryString": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[DeliveryS3Uri](#API_DescribeQuery_ResponseSyntax "#API_DescribeQuery_ResponseSyntax")**


The URI for the S3 bucket where CloudTrail delivered query results, if
 applicable.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`





**[DeliveryStatus](#API_DescribeQuery_ResponseSyntax "#API_DescribeQuery_ResponseSyntax")**


The delivery status.


Type: String


Valid Values: `SUCCESS | FAILED | FAILED_SIGNING_FILE | PENDING | RESOURCE_NOT_FOUND | ACCESS_DENIED | ACCESS_DENIED_SIGNING_FILE | CANCELLED | UNKNOWN`





**[ErrorMessage](#API_DescribeQuery_ResponseSyntax "#API_DescribeQuery_ResponseSyntax")**


The error message returned if a query failed.


Type: String


Length Constraints: Minimum length of 4. Maximum length of 1000.


Pattern: `.*`





**[EventDataStoreOwnerAccountId](#API_DescribeQuery_ResponseSyntax "#API_DescribeQuery_ResponseSyntax")**



 The account ID of the event data store owner.



Type: String


Length Constraints: Minimum length of 12. Maximum length of 16.


Pattern: `\d+`





**[Prompt](#API_DescribeQuery_ResponseSyntax "#API_DescribeQuery_ResponseSyntax")**



 The prompt used for a generated query. For information about generated queries, see 
 [Create CloudTrail Lake queries from natural language prompts](../userguide/lake-query-generator.md "../userguide/lake-query-generator.md") 
 in the *AWS CloudTrail*  user guide.
 


Type: String


Length Constraints: Minimum length of 3. Maximum length of 500.


Pattern: `^[ -~\n]*$`





**[QueryId](#API_DescribeQuery_ResponseSyntax "#API_DescribeQuery_ResponseSyntax")**


The ID of the query.


Type: String


Length Constraints: Fixed length of 36.


Pattern: `^[a-f0-9\-]+$`





**[QueryStatistics](#API_DescribeQuery_ResponseSyntax "#API_DescribeQuery_ResponseSyntax")**


Metadata about a query, including the number of events that were matched, the total
 number of events scanned, the query run time in milliseconds, and the query's creation
 time.


Type: [QueryStatisticsForDescribeQuery](API_QueryStatisticsForDescribeQuery.md "API_QueryStatisticsForDescribeQuery.md") object




**[QueryStatus](#API_DescribeQuery_ResponseSyntax "#API_DescribeQuery_ResponseSyntax")**


The status of a query. Values for `QueryStatus` include `QUEUED`,
 `RUNNING`, `FINISHED`, `FAILED`,
 `TIMED_OUT`, or `CANCELLED`



Type: String


Valid Values: `QUEUED | RUNNING | FINISHED | FAILED | CANCELLED | TIMED_OUT`





**[QueryString](#API_DescribeQuery_ResponseSyntax "#API_DescribeQuery_ResponseSyntax")**


The SQL code of a query.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 10000.


Pattern: `(?s).*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**EventDataStoreARNInvalidException** 


The specified event data store ARN is not valid or does not map to an event data store
 in your account.


HTTP Status Code: 400




**EventDataStoreNotFoundException** 


The specified event data store was not found.


HTTP Status Code: 400




**InactiveEventDataStoreException** 


The event data store is inactive.


HTTP Status Code: 400




**InvalidParameterException** 


The request includes a parameter that is not valid.


HTTP Status Code: 400




**NoManagementAccountSLRExistsException** 


 This exception is thrown when the management account does not have a service-linked
 role. 


HTTP Status Code: 400




**OperationNotPermittedException** 


This exception is thrown when the requested operation is not permitted.


HTTP Status Code: 400




**QueryIdNotFoundException** 


The query ID does not exist or does not map to a query.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DescribeQuery")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/DescribeQuery")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DescribeQuery")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DescribeQuery")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DescribeQuery")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DescribeQuery")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DescribeQuery")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DescribeQuery")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DescribeQuery")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DescribeQuery "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DescribeQuery")
