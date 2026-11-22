

# LiveChatAI connection options

The following are connection options for LiveChatAI:
+ `ENTITY_NAME` – (Required) Used for Read. The entity path of the LiveChatAI object to read. For `contacts`, `conversations`, `ai-suggestions`, and `data-sources`, append the agent ID as described in [Reading from LiveChatAI entities](livechatai-reading-from-entities.md).
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to LiveChatAI for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

LiveChatAI supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| ai-suggestions | createdAt | greater than or equal to, less than or equal to, and between | 
| conversations | createdAt | greater than or equal to, less than or equal to, and between | 
| conversations | status, sentiment, resolutionStatus, resolutionVerdict, handledBy | equals only | 
| data-sources | source | equals only | 

For `conversations`, `status`, `sentiment`, `resolutionStatus`, `resolutionVerdict`, and `handledBy` are filter-only fields. The connector doesn't return them as columns.

AWS Glue applies filters on any other LiveChatAI entity or field after it reads records, through the Spark DataFrame filters.