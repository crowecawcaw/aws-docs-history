

# ShipBob connection options

The following are connection options for ShipBob:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the ShipBob object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to ShipBob for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

ShipBob supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| invoices | invoice\_date | greater than or equal to and less than or equal to | 
| orders | created\_date, updated\_date | greater than or equal to and less than or equal to | 
| products | updated\_on | greater than or equal to | 
| receiving | insert\_date | greater than or equal to and less than or equal to | 
| returns | insert\_date, completed\_date | greater than or equal to and less than or equal to | 

AWS Glue applies filters on any other ShipBob entity after it reads records, through the Spark DataFrame filters.