

# Constant Contact connection options
<a name="constantcontact-connection-options"></a>

The following are connection options for Constant Contact:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Constant Contact object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Constant Contact for the fields listed in the following filtering support table. Supply it as an AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Constant Contact supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| account-emails | email\_address, confirm\_status | equals only | 
| activities | state | equals only | 
| contacts | created\_at, updated\_at | greater than or equal to and less than or equal to | 

AWS Glue applies filters on any other Constant Contact entity after it reads records, through the Spark DataFrame filters.