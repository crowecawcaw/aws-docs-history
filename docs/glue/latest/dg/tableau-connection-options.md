

# Tableau connection options
<a name="tableau-connection-options"></a>

The following are connection options for Tableau:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Tableau object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Tableau for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Tableau supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| jobs | status, jobType | equals only | 
| users | siteRole | equals only | 

AWS Glue applies filters on any other Tableau entity after it reads records, through the Spark DataFrame filters.