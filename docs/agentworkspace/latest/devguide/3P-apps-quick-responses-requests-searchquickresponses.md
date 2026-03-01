# Retrieve quick responses that match a search query in Amazon Connect Agent Workspace

Returns the SearchQuickResponsesResult object, which contains the matching quick
response results and a token to retrieve the next page of results, if available. The
SearchQuickResponsesRequest object is used to configure the search, allowing you to
filter by various criteria, as well as specify the channels, user-defined contact
attributes, and pagination options. If no queries are provided, the method will
return all quick responses associated with the agent's routing profile.

**Signature**

```
searchQuickResponses(queryRequest: SearchQuickResponsesRequest): Promise<SearchQuickResponsesResult>
```

**SearchQuickResponsesResult Properties**

| **Parameter** | **Type**                         | **Description**                                                                                                                                       |
| ------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| results       | QuickResponsesSearchResultData[] | The results of the quick responses search                                                                                                             |
| nextToken     | string                           | The token for the next set of results. Use the value returned in<br>the previous response in the next request to retrieve the next set<br>of results. |

**QuickResponsesSearchResultData Properties**

| **Parameter**             | **Type**              | **Description**                                                                                  |
| ------------------------- | --------------------- | ------------------------------------------------------------------------------------------------ |
| contents                  | QuickResponseContents | The contents of the quick response.                                                              |
| knowledgeBaseId           | string                | The identifier of the knowledge base.                                                            |
| name                      | string                | The name of the quick response.                                                                  |
| quickResponseArn          | string                | The Amazon Resource Name (ARN) of the quick response.                                            |
| quickResponseId           | string                | The identifier of the quick response.                                                            |
| description               | string                | The description of the quick response.                                                           |
| shortcutKey               | string                | The shortcut key of the quick response. The value should be<br>unique across the knowledge base. |
| attributesNotInterpolated | string[]              | The user defined contact attributes that are not resolved when<br>the search result is returned. |

**QuickResponseContents Properties**

| **Parameter** | **Type** | **Description**                                        |
| ------------- | -------- | ------------------------------------------------------ |
| markdown      | string   | The content of the quick response stored in markdown   |
| plainText     | string   | The content of the quick response stored in plain text |

**SearchQuickResponsesRequest Properties**

| **Parameter** | **Type**               | **Description**                                                                                                                                                 |
| ------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| queries       | QuickResponsesQuery[]  | Query used to filter quick responses; if no queries are provided,<br>the client will return all quick responses associated with the<br>agent's routing profile. |
| channels      | QuickResponseChannel[] | The channels to filter the request by. Supported values: "Chat"<br>or "Email"                                                                                   |
| attributes    | Record<string, string> | The user-defined Amazon Connect contact attributes to be resolved<br>when search results are returned.                                                          |
| debounceMS    | number                 | The default value is set to 250ms; set it to 0 to disable<br>debounced input change                                                                             |
| maxResults    | number                 | The number of results to be returned. Minimum value of 1. Maximum<br>value of 100.                                                                              |
| nextToken     | string                 | The token for the next set of results. Use the value returned in<br>the previous response in the next request to retrieve the next set<br>of results.           |

**QuickResponsesQuery Properties**

| **Parameter**  | **Type**                     | **Description**                                                                                                                                                                                                      |
| -------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name           | QuickResponsesQueryFieldName | The name of the attribute to query the quick responses by.<br>Supported values: "content", "name", "description", or<br>"shortcutKey"                                                                                |
| values         | string[]                     | The values of the attribute to query the quick responses<br>by.                                                                                                                                                      |
| operator       | QuickResponsesQueryOperator  | The operator to use for matching attribute field values in the<br>query. Supported values: "CONTAINS" or "CONTAINS_AND_PREFIX"                                                                                       |
| priority       | QuickResponsesQueryPriority  | The importance of the attribute field when calculating query<br>result relevancy scores. The value set for this parameter affects<br>the ordering of search results. Supported values: "HIGH", "MEDIUM",<br>or "LOW" |
| allowFuzziness | boolean                      | Whether the query expects only exact matches on the attribute<br>field values. The results of the query will only include exact<br>matches if this parameter is set to false.                                        |
