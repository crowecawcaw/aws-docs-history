

# Bitbucket connection options

The following are connection options for Bitbucket:
+ `ENTITY_NAME` – (Required) Used for Read. The entity path of the Bitbucket object to read. Use `user-workspaces` by itself. For `members`, `projects`, `repositories`, and `workspace-permissions`, use `{{entity}}/{{workspace}}`. For the other entities, use `{{entity}}/{{workspace}}/{{repoSlug}}`. You can use the workspaces and repositories that AWS Glue discovers for your connection.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format. AWS Glue pushes down predicates on the fields in the following filtering table to Bitbucket.

Bitbucket supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| pull-requests | state, created\_on, updated\_on | equals only | 
| repositories | updated\_on | equals, greater than, greater than or equal to, less than, and less than or equal to | 

AWS Glue applies filters on any other Bitbucket entity after it reads records, through the Spark DataFrame filters.