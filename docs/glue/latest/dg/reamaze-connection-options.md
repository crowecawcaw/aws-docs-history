

# Re:amaze connection options

The following are connection options for Re:amaze:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Re:amaze object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Server-side (pushed-down) filtering is not supported for Re:amaze. Apply any filtering in your AWS Glue ETL job.