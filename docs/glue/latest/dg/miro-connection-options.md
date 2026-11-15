

# Miro connection options
<a name="miro-connection-options"></a>

The following are connection options for Miro:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Miro object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Miro for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Miro supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| boards | team\_id, project\_id, query, owner\_id | equals only | 

These fields are filter-only and are not returned as columns. `query` sends a board search term to Miro and returns boards that match it. `owner_id` must be a Miro user ID, and Miro ignores it when you also filter on `team_id`. To filter on other values, apply the filter in your ETL job after the read.