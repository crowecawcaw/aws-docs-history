

# Coda connection options

The following are connection options for Coda:
+ `ENTITY_NAME` – (Required) Used for Read. The entity path of the Coda object to read. For a nested entity, use the full path that AWS Glue returns, as described in [Reading from Coda entities](coda-reading-from-entities.md).
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Coda for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Coda supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| doc-analytics | query, workspaceId, isPublished, sinceDate, untilDate | equals only | 
| docs | sourceDocId, workspaceId, folderId, query, isOwner, isPublished, isStarred, inGallery, minimumAccess | equals only | 
| folders | workspaceId, isStarred | equals only | 
| rows | visibleOnly | equals only | 
| tables | tableType | equals only | 

On the `docs` and `doc-analytics` entities, the `query` field sends a search term to Coda instead of an exact match. On the `doc-analytics` entity, `sinceDate` and `untilDate` set the start and end of the analytics date range. Use these fields only for filtering; the connector doesn't return them as columns.

AWS Glue applies filters on any other Coda entity after it reads records, through the Spark DataFrame filters.