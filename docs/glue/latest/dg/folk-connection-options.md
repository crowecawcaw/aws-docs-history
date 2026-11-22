

# Folk connection options

The following are connection options for Folk:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Folk object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Server-side (pushed-down) filtering is not supported for Folk. The connector reads all records of an entity; apply any filtering in your AWS Glue ETL job.