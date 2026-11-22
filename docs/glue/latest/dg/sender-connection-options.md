

# Sender connection options

The following are connection options for Sender:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Sender object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Sender for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Sender supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| campaigns | status | equals only | 
| workflows | status | equals only | 

AWS Glue applies filters on any other Sender entity after it reads records, through the Spark DataFrame filters.