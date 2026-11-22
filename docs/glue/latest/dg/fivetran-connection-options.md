

# Fivetran connection options

The following are connection options for Fivetran:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Fivetran object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Fivetran for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Fivetran supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| connections | schema, group\_id | equals only | 
| group-users | active | equals only | 
| team-users | active | equals only | 
| transformations | type, group\_id, project\_id | equals only | 
| users | active, user\_type, has\_api\_key | equals only | 

AWS Glue applies filters on any other Fivetran entity after it reads records, through the Spark DataFrame filters.