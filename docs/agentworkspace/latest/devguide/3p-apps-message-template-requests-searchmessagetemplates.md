# Retrieve

message templates that match a search query in Amazon Connect Agent Workspace

Returns the SearchMessageTemplatesResponse object, which contains the matching
message templates and a token to retrieve the next page of results, if available.
The SearchMessageTemplatesParams object is used to configure the search, allowing
you to filter by various criteria, as well as specify the channels and pagination
options. If no filter text is provided, all active message templates for the agent's
routing profile and the channel(s) specified are returned.

**Signature**

```
searchMessageTemplates(request: SearchMessageTemplatesParams): Promise<SearchMessageTemplatesResponse>
```

**SearchMessageTemplatesResponse Properties**

| **Parameter**   | **Type**          | **Description**                                                                                                                                       |
| --------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| messageTemplate | MessageTemplate[] | List of message templates matching the search criteria specified<br>in the request                                                                    |
| nextToken       | string            | The token for the next set of results. Use the value returned in<br>the previous response in the next request to retrieve the next set<br>of results. |

**MessageTemplate Properties**

| **Parameter**      | **Type** | **Description**                                                                                                |
| ------------------ | -------- | -------------------------------------------------------------------------------------------------------------- |
| messageTemplateArn | string   | The ARN of the message template. This contains the active version<br>qualifier at the end of the ARN           |
| messageTemplateId  | string   | The ID of the message template. This does NOT contain a qualifier<br>with the version of the message template. |
| name               | string   | Name of the message template                                                                                   |
| description        | string   | Description of the message template                                                                            |

**SearchMessageTemplatesParams Properties**

| **Parameter** | **Type**                    | **Description**                                                                                                                                                                                 |
| ------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| channels      | MessageTemplateChannel[]    | The channel(s) to return message templates for. If the list is<br>empty, no message templates will be returned. Supported values:<br>"EMAIL"                                                    |
| queries       | MessageTemplateQueryField[] | Queries are used to filter the returned message templates by name<br>or description. Leaving the queries empty will return all message<br>templates associated with the agent's routing profile |
| maxResults    | number                      | Maximum number of message templates to return                                                                                                                                                   |
| nextToken     | string                      | The token for the next set of results. Use the value returned in<br>the previous response in the next request to retrieve the next set<br>of results.                                           |

**MessageTemplateQueryField Properties**

| **Parameter**  | **Type**   | **Description**                                                                                                                                                               |
| -------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name           | "name"     | "description"                                                                                                                                                                 | The message templates will be filtered by the values matching the<br>text in the name field provided      |
| values         | string[]   | The values of the attribute to query the message templates<br>by                                                                                                              |
| priority       | "HIGH"     | "MEDIUM"                                                                                                                                                                      | "LOW"                                                                                                     | The importance of the attribute field when calculating query<br>result relevancy scores. The value set for this parameter affects<br>the ordering of search results. |
| allowFuzziness | boolean    | Whether the query expects only exact matches on the attribute<br>field values. The results of the query will only include exact<br>matches if this parameter is set to false. |
| operator       | "CONTAINS" | "CONTAINS_AND_PREFIX"                                                                                                                                                         | Include all templates that contain the values or only templates<br>that contain the values as the prefix. |
