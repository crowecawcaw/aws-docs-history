

# Recurly connection options

The following are connection options for Recurly:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Recurly object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Recurly for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Recurly supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| accounts | email | equals only | 
| invoices | type, state | equals only | 
| items | state | equals only | 
| line\_items | type, state | equals only | 
| plans | state | equals only | 
| subscriptions | state | equals only | 
| transactions | type | equals only | 

AWS Glue applies filters on any other Recurly entity after it reads records, through the Spark DataFrame filters.