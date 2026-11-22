

# Weaviate connection options

The following are connection options for Weaviate:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Weaviate object to read. For `objects`, append a forward slash and the collection name, as described in [Reading from Weaviate entities](weaviate-reading-from-entities.md).
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Weaviate for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Weaviate supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| objects | tenant, include | equals only | 

The `tenant` filter selects the tenant to read in a multi-tenant collection. A read of a multi-tenant collection requires a `tenant` filter. The `include` filter is filter-only and is not returned as a column. It requests additional object data. For example, `include = 'vector'` populates the `vector` column, which is otherwise empty.

AWS Glue applies filters on any other Weaviate entity after it reads records, through the Spark DataFrame filters.