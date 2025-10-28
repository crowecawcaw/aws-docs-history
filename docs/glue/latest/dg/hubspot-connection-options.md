# HubSpot connection options

The following are connection options for HubSpot:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in HubSpot.
- `API_VERSION`(String) - (Required) Used for Read. HubSpot Rest API version you want to use. For example: v1,v2,v3,v4.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query.
- `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field.
- `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
- `TRANSFER_MODE`(String) - Used to indicate whether the query should be run on Async mode.
- `WRITE_OPERATION`(String) - Default: INSERT. Used for write. Value should be INSERT or UPDATE.
- `ID_FIELD_NAMES`(String) - Default : null. Required for UPDATE.
