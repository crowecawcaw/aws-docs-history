# Adobe Analytics connection options

The following are connection options for Adobe Analytics:

- `ENTITY_NAME`(String) – (Required) Used for Read/Write. The name of your Object in Adobe Analytics.
- `API_VERSION`(String) – (Required) Used for Read/Write. Adobe Analytics Rest API version you want to use.
  For example: v2.0.
- `X_API_KEY`(String) – (Required) Used for Read/Write. It is required to authenticate the
  developer or application making requests to the API.
- `SELECTED_FIELDS`(List<String>) – Default: empty(SELECT \*). Used for Read. Columns you want to select
  for the object.
- `FILTER_PREDICATE`(String) – Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) – Default: empty. Used for Read. Full Spark SQL query.
