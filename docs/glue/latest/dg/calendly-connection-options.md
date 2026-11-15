

# Calendly connection options
<a name="calendly-connection-options"></a>

The following are connection options for Calendly:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Calendly object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Calendly for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Calendly supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| scheduled\_events | status, start\_time | equals only | 

AWS Glue applies filters on any other Calendly entity after it reads records, through the Spark DataFrame filters.