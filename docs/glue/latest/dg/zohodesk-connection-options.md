

# Zoho Desk connection options
<a name="zohodesk-connection-options"></a>

The following are connection options for Zoho Desk:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Zoho Desk object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Zoho Desk for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Zoho Desk supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| agents | status | equals only | 
| calls | departmentId | equals only | 
| tasks | departmentId | equals only | 
| tickets | status, priority, channel, departmentId, assigneeId | equals only | 

AWS Glue applies filters on any other Zoho Desk entity after it reads records, through the Spark DataFrame filters.