

# Crisp connection options

The following are connection options for Crisp:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Crisp object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Server-side (pushed-down) filtering is not supported for Crisp. Apply any filtering in your AWS Glue ETL job.