

# Webflow connection options

The following are connection options for Webflow:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Webflow object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Webflow for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Webflow supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| collection\_items | createdOn, lastUpdated, lastPublished | greater than or equal to, less than or equal to, and BETWEEN | 

AWS Glue applies filters on any other Webflow entity after it reads records, through the Spark DataFrame filters.