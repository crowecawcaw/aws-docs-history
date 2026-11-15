

# Twenty CRM connection options
<a name="twenty-connection-options"></a>

The following are connection options for Twenty CRM:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Twenty CRM object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Server-side (pushed-down) filtering is not supported for Twenty CRM. The connector reads all records of an entity; apply any filtering in your AWS Glue ETL job.