# Jira Cloud connection options

The following are connection options for Jira Cloud:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in Jira Cloud.
- `API_VERSION`(String) - (Required) Used for Read. Jira Cloud Rest API version you want to use. For example: v3.
- `DOMAIN_URL`(String) - (Required) The Jira Cloud ID you want to use.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
