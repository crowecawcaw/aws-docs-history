

# Trello connection options

The following are connection options for Trello:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Trello object to read. For a board-scoped or Workspace-scoped entity, append a forward slash and the parent identifier, as described in [Reading from Trello entities](trello-reading-from-entities.md).
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Server-side (pushed-down) filtering is not supported for Trello. The connector reads all records of an entity; apply any filtering in your AWS Glue ETL job.