

# Brex connection options

The following are connection options for Brex:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Brex object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Brex for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Brex supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| card-transaction | posted\_at\_date, user\_ids | equals and greater than or equal to | 

AWS Glue applies filters on any other Brex entity after it reads records, through the Spark DataFrame filters.