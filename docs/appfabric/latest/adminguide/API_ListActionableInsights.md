# ListActionableInsights

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Lists the most important actionable email messages, tasks, and other
updates.

###### Topics

- [Request body](#API_ListActionableInsights_request "#API_ListActionableInsights_request")
- [Response elements](#API_ListActionableInsights_response "#API_ListActionableInsights_response")

## Request body

The request accepts the following data in JSON format.

| Parameter     | Description                                                                                                                                                                                                                                                                                                                                                                              |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **nextToken** | If `nextToken` is returned, there are more results available. The value of<br>`nextToken` is a unique pagination token for each page. Make the call again<br>using the returned token to retrieve the next page. Keep all other arguments unchanged.<br>Each pagination token expires after 24 hours. Using an expired pagination token will return<br>an _HTTP 400 InvalidToken error_. |

## Response elements

If the action is successful, the service sends back an HTTP 201
response.

The following data is returned in JSON format by the service.

| Parameter                  | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ActionableInsightsList** | Lists the actionable insights, including a title,<br>description, actions, and created timestamp. For more<br>information, see [ActionableInsights](API_ActionableInsights.md "API_ActionableInsights.md").                                                                                                                                                                                              |
| **nextToken**              | If `nextToken` is returned, there are more results available. The value of<br>`nextToken` is a unique pagination token for each page. Make the call again<br>using the returned token to retrieve the next page. Keep all other arguments unchanged.<br>Each pagination token expires after 24 hours. Using an expired pagination token will return<br>an _HTTP 400 InvalidToken error_.<br>Type: String |
