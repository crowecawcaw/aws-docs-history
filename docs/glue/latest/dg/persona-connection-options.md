

# Persona connection options

The following are connection options for Persona:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Persona object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Persona for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Persona supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| inquiries | inquiry\_id, account\_id, note, reference\_id, inquiry\_template\_id, status, created\_at\_start, created\_at\_end | equals only | 

The filter fields for `inquiries` are filter-only. You can use them in a filter predicate, but they are not returned as columns. `created_at_start` returns inquiries created at or after the given timestamp, and `created_at_end` returns inquiries created at or before it.

AWS Glue applies filters on any other Persona entity after it reads records, through the Spark DataFrame filters.