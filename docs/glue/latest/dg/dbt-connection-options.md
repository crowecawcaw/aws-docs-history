

# dbt Cloud connection options

The following are connection options for dbt Cloud:
+ `ENTITY_NAME` – (Required) Used for Read. The full entity path of the dbt Cloud object to read, including the account ID, as described in [Reading from dbt Cloud entities](dbt-reading-from-entities.md).
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to dbt Cloud for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

dbt Cloud supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| groups | id, name, name\_contains, include\_related, state | equals only | 

On the `groups` entity, `name_contains` matches group names that contain the value, ignoring case. The `name_contains` and `include_related` fields are used only for filtering and are not returned as columns.

AWS Glue applies filters on any other dbt Cloud entity after it reads records, through the Spark DataFrame filters.