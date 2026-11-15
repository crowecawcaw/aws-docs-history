

# Nimble connection options
<a name="nimble-connection-options"></a>

The following are connection options for Nimble:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Nimble object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Nimble for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Nimble supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| contacts | record\_type | equals only | 

AWS Glue applies filters on any other Nimble entity after it reads records, through the Spark DataFrame filters.