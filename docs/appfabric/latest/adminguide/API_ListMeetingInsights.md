

# ListMeetingInsights
<a name="API_ListMeetingInsights"></a>


|  | 
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. | 

Lists the most important actionable calendar events.

**Topics**
+ [Request body](#API_ListMeetingInsights_request)
+ [Response elements](#API_ListMeetingInsights_response)

## Request body
<a name="API_ListMeetingInsights_request"></a>

The request accepts the following data in JSON format.


| Parameter | Description | 
| --- | --- | 
| **nextToken** | If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*. | 

## Response elements
<a name="API_ListMeetingInsights_response"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.


| Parameter | Description | 
| --- | --- | 
| **MeetingInsightList** | Lists the actionable meeting insights. For more information, see [MeetingInsights](API_MeetingInsights.md). | 
| **nextToken** | If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*.<br />Type: String | 