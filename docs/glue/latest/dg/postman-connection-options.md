

# Postman connection options
<a name="postman-connection-options"></a>

The following are connection options for Postman:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Postman object to read. For a parent-scoped entity, append a forward slash and the parent identifier, as described in [Reading from Postman entities](postman-reading-from-entities.md).
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Postman for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Postman supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| collections | workspace | equals only | 
| mock-call-logs | servedAt | greater than or equal to, less than or equal to, and BETWEEN | 
| mock-servers | workspace | equals only | 
| monitors | workspace | equals only | 
| workspaces | visibility | equals only | 

The `workspace` filter field for `collections`, `mock-servers`, and `monitors` is filter-only. Set it to a workspace ID in a filter predicate to scope the results to that workspace. It is not returned as a column.

AWS Glue applies filters on any other Postman entity after it reads records, through the Spark DataFrame filters.