# Zoom Meetings connection options

The following are connection options for Zoom Meetings:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of the Zoom Meetings entity. For example, `group`.
- `API_VERSION`(String) - (Required) Used for Read. Zoom Meetings Rest API version you want to use. The value will be `v2`, as Zoom Meetings currently supports only version v2.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. A comma-separated list of columns you want to select for the selected entity.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
