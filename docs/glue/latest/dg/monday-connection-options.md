# Monday connection option reference

The following are connection options for Monday:

- `ENTITY_NAME`(String) - (Required) Used for Read/Write. The name of your Object in Monday.
- `API_VERSION`(String) - (Required) Used for Read/Write. Monday Rest API version you want to use.
  Example: v2.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select
  for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
