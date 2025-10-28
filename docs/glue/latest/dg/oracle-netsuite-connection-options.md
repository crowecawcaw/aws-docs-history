# Oracle NetSuite connection options

The following are connection options for Oracle NetSuite:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of the Oracle NetSuite entity. Example: deposit.
- `API_VERSION`(String) - (Required) Used for Read. Oracle NetSuite Rest API version you want to use. The value will be v1, as Oracle NetSuite currently supports only version v1.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Comma-separated list of columns you want to select for the selected entity.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition the query (field-based partitioning).
- `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field, used in field-based partitioning.
- `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field, used in field-based partitioning.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read. Used in both field- and record- based partitioning.
- `INSTANCEE_URL`(String) - A valid NetSuite instance URL with format https://{account-id}.suitetalk.api.netsuite.com.
