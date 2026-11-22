

# Omnisend connection options

The following are connection options for Omnisend:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Omnisend object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format.

Omnisend supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| campaigns | createdAt | greater than or equal to and less than or equal to | 

AWS Glue applies filters on any other Omnisend entity after it reads records, through the Spark DataFrame filters.