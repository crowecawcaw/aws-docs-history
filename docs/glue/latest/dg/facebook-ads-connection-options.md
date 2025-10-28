# Facebook Ads connection options

The following are connection options for Facebook Ads:

- `ENTITY_NAME`(String) - (Required) Used for read. The name of your object in Facebook Ads.
- `API_VERSION`(String) - (Required) Used for read. Facebook Ads Rest API version you want to use. For example: v1.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for read. Full Spark SQL query.
- `PARTITION_FIELD`(String) - Used for read. Field to be used to partition query.
- `LOWER_BOUND`(String)- Used for read. An inclusive lower bound value of the chosen partition field.
- `UPPER_BOUND`(String) - Used for read. An exclusive upper bound value of the chosen partition field.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for read. Number of partitions for read.
- `TRANSFER_MODE`(String) - Default: SYNC. Used for asynchronous read.
