

# LaunchDarkly connection options

The following are connection options for LaunchDarkly:
+ `ENTITY_NAME` – (Required) Used for Read. The entity path of the LaunchDarkly object to read. Use the nested forms described in [Reading from LaunchDarkly entities](launchdarkly-reading-from-entities.md) for project-scoped and environment-scoped entities.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Server-side (pushed-down) filtering is not supported for LaunchDarkly. The connector reads all records of an entity; apply any filtering in your AWS Glue ETL job.