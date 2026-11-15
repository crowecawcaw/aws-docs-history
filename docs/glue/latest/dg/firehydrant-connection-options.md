

# FireHydrant connection options
<a name="firehydrant-connection-options"></a>

The following are connection options for FireHydrant:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the FireHydrant object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to FireHydrant for the fields listed in the filtering support table below. Supply it as an AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

FireHydrant supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| alerts | status, starts\_at | equals, greater than or equal to, and less than or equal to | 
| incident\_events | type | equals only | 
| incident\_role\_assignments | status | equals only | 
| incidents | created\_at, updated\_at, started\_at | greater than or equal to and less than or equal to | 

AWS Glue applies filters on any other FireHydrant entity after it reads records, through the Spark DataFrame filters.