# QuickBooks connection options

The following are connection options for QuickBooks:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in QuickBooks.
- `INSTANCE_URL`(String) - (Required) A valid QuickBooks instance URL.
- `API_VERSION`(String) - (Required) Used for Read. QuickBooks Rest API version you want to use.
- `REALM_ID`(String) - An ID that identifies an individual QuickBooks Online company where you send requests.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query.
- `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field.
- `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
