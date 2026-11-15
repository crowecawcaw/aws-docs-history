

# Todoist connection options
<a name="todoist-connection-options"></a>

The following are connection options for Todoist:
+ `ENTITY_NAME` – (Required) Used for Read. The entity path of the Todoist object to read. Use the nested forms described in [Reading from Todoist entities](todoist-reading-from-entities.md) for `collaborators`, `comments`, `folders`, and `workspace_invitations`.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format. AWS Glue pushes down predicates on the fields in the following filtering table to Todoist.

Todoist supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| projects | workspace\_id, folder\_id | equals only | 
| sections | project\_id | equals only | 
| tasks | project\_id, section\_id, parent\_id, label | equals only | 

For `tasks`, `label` is filter-only. Use one label name in `FILTER_PREDICATE`; the connector doesn't return `label` as a column. The labels assigned to each task are returned in the `labels` column.

AWS Glue applies filters on any other Todoist entity or field after it reads records, through the Spark DataFrame filters.