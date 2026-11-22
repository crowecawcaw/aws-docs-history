

# Harness connection options

The following are connection options for Harness:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Harness object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to Harness for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

Harness supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| connectors | orgIdentifier, projectIdentifier, type, branch, repoIdentifier, getDefaultFromOtherRepo, searchTerm, category, source\_category | equals only | 
| organizations | identifier, searchTerm | equals only | 
| projects | identifier, orgIdentifier, hasModule, moduleType, searchTerm | equals only | 
| user-groups | orgIdentifier, projectIdentifier, searchTerm | equals only | 

The `searchTerm` field is query-only on all four entities. On `projects`, `hasModule` and `moduleType` are query-only. On `connectors`, `branch`, `category`, `getDefaultFromOtherRepo`, `repoIdentifier`, and `source_category` are query-only. The connector doesn't return any of these query-only fields as columns. The `searchTerm` field performs a Harness search that can match part of a value, not an exact match.

AWS Glue applies filters on any other Harness field after it reads records, through the Spark DataFrame filters.