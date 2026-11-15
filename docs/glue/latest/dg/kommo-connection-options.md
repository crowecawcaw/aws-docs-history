

# Kommo connection options
<a name="kommo-connection-options"></a>

The following are connection options for Kommo:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Kommo object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Kommo for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Kommo supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| companies | created\_at, updated\_at | greater than or equal to and less than or equal to | 
| contacts | created\_at, updated\_at | greater than or equal to and less than or equal to | 
| events | created\_at | greater than or equal to and less than or equal to | 
| leads | created\_at, updated\_at | greater than or equal to and less than or equal to | 
| tasks | updated\_at | greater than or equal to and less than or equal to | 

AWS Glue applies filters on any other Kommo entity after it reads records, through the Spark DataFrame filters.