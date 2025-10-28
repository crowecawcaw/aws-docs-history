# Dynatrace connection options

The following are connection options for Dynatrace:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in Dynatrace.
- `API_VERSION`(String) - (Required) Used for Read. Dynatrace Rest API version you want to use.
- `INSTANCE_URL`(String) - Used for Read. A valid Dynatrace instance URL.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
