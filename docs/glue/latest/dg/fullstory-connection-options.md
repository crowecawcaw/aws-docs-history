

# Fullstory connection options

The following are connection options for Fullstory:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Fullstory object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Fullstory for the fields listed in the filtering support table below. Supply it as an AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Fullstory supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| users | uid, display\_name, email, is\_identified | equals only | 

AWS Glue applies filters on any other Fullstory entity after it reads records, through the Spark DataFrame filters.