# LookupEvents

Looks up [management events](../userguide/cloudtrail-concepts.md#cloudtrail-concepts-management-events "../userguide/cloudtrail-concepts.md#cloudtrail-concepts-management-events") or [CloudTrail Insights events](../userguide/cloudtrail-concepts.md#cloudtrail-concepts-insights-events "../userguide/cloudtrail-concepts.md#cloudtrail-concepts-insights-events") that are captured by CloudTrail. 
 You can look up events that occurred in a Region within the last 90 days.

###### Note


`LookupEvents` returns recent Insights events for trails that enable Insights. To view Insights events for an event data store, you can run queries on your 
 Insights event data store, and you can also view the Lake dashboard for Insights.

Lookup supports the following attributes for management events:


* AWS access key
* Event ID
* Event name
* Event source
* Read only
* Resource name
* Resource type
* User name
Lookup supports the following attributes for Insights events:


* Event ID
* Event name
* Event source
All attributes are optional. The default number of results returned is 50, with a
 maximum of 50 possible. The response includes a token that you can use to get the next page
 of results.

###### Important

The rate of lookup requests is limited to two per second, per account, per Region. If
 this limit is exceeded, a throttling error occurs.


## Request Syntax



```
{
   "EndTime": `number`,
   "EventCategory": "`string`",
   "LookupAttributes": [ 
      { 
         "AttributeKey": "`string`",
         "AttributeValue": "`string`"
      }
   ],
   "MaxResults": `number`,
   "NextToken": "`string`",
   "StartTime": `number`
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[EndTime](#API_LookupEvents_RequestSyntax "#API_LookupEvents_RequestSyntax")**


Specifies that only events that occur before or at the specified time are returned. If
 the specified end time is before the specified start time, an error is returned.


Type: Timestamp


Required: No




**[EventCategory](#API_LookupEvents_RequestSyntax "#API_LookupEvents_RequestSyntax")**


Specifies the event category. If you do not specify an event category, events of the
 category are not returned in the response. For example, if you do not specify
 `insight` as the value of `EventCategory`, no Insights events are
 returned.


Type: String


Valid Values: `insight`



Required: No




**[LookupAttributes](#API_LookupEvents_RequestSyntax "#API_LookupEvents_RequestSyntax")**


Contains a list of lookup attributes. Currently the list can contain only one
 item.


Type: Array of [LookupAttribute](API_LookupAttribute.md "API_LookupAttribute.md") objects


Required: No




**[MaxResults](#API_LookupEvents_RequestSyntax "#API_LookupEvents_RequestSyntax")**


The number of events to return. Possible values are 1 through 50. The default is
 50.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 50.


Required: No




**[NextToken](#API_LookupEvents_RequestSyntax "#API_LookupEvents_RequestSyntax")**


The token to use to get the next page of results after a previous API call. This token
 must be passed in with the same parameters that were specified in the original call. For
 example, if the original call specified an AttributeKey of 'Username' with a value of
 'root', the call with NextToken should include those same parameters.


Type: String


Required: No




**[StartTime](#API_LookupEvents_RequestSyntax "#API_LookupEvents_RequestSyntax")**


Specifies that only events that occur after or at the specified time are returned. If
 the specified start time is after the specified end time, an error is returned.


Type: Timestamp


Required: No




## Response Syntax



```
{
   "Events": [ 
      { 
         "AccessKeyId": "***string***",
         "CloudTrailEvent": "***string***",
         "EventId": "***string***",
         "EventName": "***string***",
         "EventSource": "***string***",
         "EventTime": ***number***,
         "ReadOnly": "***string***",
         "Resources": [ 
            { 
               "ResourceName": "***string***",
               "ResourceType": "***string***"
            }
         ],
         "Username": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Events](#API_LookupEvents_ResponseSyntax "#API_LookupEvents_ResponseSyntax")**


A list of events returned based on the lookup attributes specified and the CloudTrail event. The events list is sorted by time. The most recent event is listed
 first.


Type: Array of [Event](API_Event.md "API_Event.md") objects




**[NextToken](#API_LookupEvents_ResponseSyntax "#API_LookupEvents_ResponseSyntax")**


The token to use to get the next page of results after a previous API call. If the token
 does not appear, there are no more results to return. The token must be passed in with the
 same parameters as the previous call. For example, if the original call specified an
 AttributeKey of 'Username' with a value of 'root', the call with NextToken should include
 those same parameters.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidEventCategoryException** 


Occurs if an event category that is not valid is specified as a value of
 `EventCategory`.


HTTP Status Code: 400




**InvalidLookupAttributesException** 


Occurs when a lookup attribute is specified that is not valid.


HTTP Status Code: 400




**InvalidMaxResultsException** 


This exception is thrown if the limit specified is not valid.


HTTP Status Code: 400




**InvalidNextTokenException** 


A token that is not valid, or a token that was previously used in a request with
 different parameters. This exception is thrown if the token is not valid.


HTTP Status Code: 400




**InvalidTimeRangeException** 


Occurs if the timestamp values are not valid. Either the start time occurs after the end
 time, or the time range is outside the range of possible values.


HTTP Status Code: 400




**OperationNotPermittedException** 


This exception is thrown when the requested operation is not permitted.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/LookupEvents")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/LookupEvents")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/LookupEvents")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/LookupEvents")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/LookupEvents")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/LookupEvents")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/LookupEvents")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/LookupEvents")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/LookupEvents")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/LookupEvents "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/LookupEvents")
