# LinkedIn connection options

The following are connection options for LinkedIn:

- `ENTITY_NAME`(String) – (Required) Used for Read/Write. The name of your
  Object in LinkedIn. For example, adAccounts.
- `API_VERSION`(String) – (Required) Used for Read/Write. LinkedIn Rest
  API version you want to use. The value will be 202406, as LinkedIn currently
  supports only version 202406.
- `SELECTED_FIELDS`(List<String>) – Default: empty(SELECT \*). Used for
  Read. Columns you want to select for the selected entity.
- `FILTER_PREDICATE`(String) – Default: empty. Used for Read. It should be
  in the Spark SQL format.
- `QUERY`(String) – Default: empty. Used for Read. Full Spark SQL query.
