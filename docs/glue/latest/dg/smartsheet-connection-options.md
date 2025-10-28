# Smartsheet connection options

The following are connection options for Smartsheet:

- `ENTITY_NAME`(String) – (Required) Used for Read/Write. The name of your
  Object in Smartsheet.
- `API_VERSION`(String) – (Required) Used for Read/Write. Smartsheet Rest
  API version you want to use. For example: v2.0.
- `INSTANCE_URL`(String) – (Required) Used for Read. Smartsheet instance
  URL.
- `SELECTED_FIELDS`(List<String>) – Default: empty(SELECT \*). Used for
  Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) – Default: empty. Used for Read. It should be
  in the Spark SQL format.
- `QUERY`(String) – Default: empty. Used for Read. Full Spark SQL query.
