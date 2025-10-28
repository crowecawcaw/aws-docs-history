# Slack connection options

The following are connection options for Slack:

- `ENTITY_NAME`(String) - (Required) Used for Read. Supported entity name.
  Example: `conversations/C058W38R5J8`.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Fields you want to
  select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
