

# ClickUp connection options
<a name="clickup-connection-options"></a>

The following are connection options for ClickUp:
+ `ENTITY_NAME` – (Required) Used for Read. The entity path of the ClickUp object to read. Use `workspaces` by itself. For `groups` and the `team-*` entities, use `{{entity}}/{{teamId}}`. For `space-folder` and `space-tag`, use `{{entity}}/{{teamId}}/{{spaceId}}`. You can use the workspaces and spaces that AWS Glue discovers for your connection.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format. AWS Glue pushes down predicates on the fields in the following filtering table to ClickUp.

ClickUp supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| team-time\_entries | start\_date, end\_date, assignee | equals only | 

The `team-time_entries` filter fields are request controls that ClickUp doesn't return as columns, so you can use them only in `FILTER_PREDICATE`. Use `start_date` and `end_date` with the equals operator to set the start and end of the date range that ClickUp returns. Use `assignee` with a ClickUp user ID to read that user's time entries.

AWS Glue applies filters on any other ClickUp entity after it reads records, through the Spark DataFrame filters.