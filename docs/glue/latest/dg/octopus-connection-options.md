

# Octopus Deploy connection options
<a name="octopus-connection-options"></a>

The following are connection options for Octopus Deploy:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Octopus Deploy object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Octopus Deploy for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Octopus Deploy supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| feeds | FeedType, Id, Name, partialName | equals only | 
| project-groups | Id, Name, partialName | equals only | 
| spaces | Id, Name, partialName | equals only | 

Use the equals operator with each field. `partialName` is filter-only and isn't returned as a column. It returns resources whose name contains the value. For `feeds` and `project-groups`, filters apply within the space in `ENTITY_NAME`. To filter on other values, apply the filter in your ETL job after the read.