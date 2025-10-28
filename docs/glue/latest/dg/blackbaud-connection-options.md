# Blackbaud Raiser's Edge NXT connection options

The following are connection options for Blackbaud Raiser's Edge NXT:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in Blackbaud Raiser's Edge NXT.
- `API_VERSION`(String) - (Required) Used for Read. Blackbaud Raiser's Edge NXT Rest API version you want to use.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read. Example value: 10.
- `SUBSCRIPTION_KEY`(String) - (Required) Default: empty. Used for Read. Subscription key associated with one's developer account.
