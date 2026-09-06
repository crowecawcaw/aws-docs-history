

# ListAppClients
<a name="API_ListAppClients"></a>


|  | 
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. | 

Returns a list of all AppClients.

**Topics**
+ [Request body](#API_ListAppClients_request)
+ [Response elements](#API_ListAppClients_response)

## Request body
<a name="API_ListAppClients_request"></a>

The request accepts the following data in JSON format.


| Parameter | Description | 
| --- | --- | 
| **maxResults** | The maximum number of results that are returned per call. You can use `nextToken` to obtain further pages of results.<br />This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.<br />Valid Range: Minimum value of 1. Maximum value of 100. | 
| **nextToken** | If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*. | 

## Response elements
<a name="API_ListAppClients_response"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.


| Parameter | Description | 
| --- | --- | 
| **appClientList** | Contains a list of AppClient results.<br />Type: Array of [AppClientSummary](API_AppClientSummary.md) objects | 
| **nextToken** | If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*.<br />Type: String | 