# Salesforce Marketing Cloud Account Engagement connection options

The following are connection options for Salesforce Marketing Cloud Account Engagement:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in Salesforce Marketing Cloud Account Engagement.
- `PARDOT_BUSINESS_UNIT_ID` - (Required) Used for creating a connection. The business unit ID of the Salesforce Marketing Cloud Account Engagement instance you want to connect to.
- `API_VERSION`(String) - (Required) Used for Read. Salesforce Marketing Cloud Account Engagement Rest API version you want to use.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) -
  - In Sync mode - Default: empty. Used for Read. It should be in the Spark SQL format.
  - In Async mode - Default : Current `DateTime` value (as per user’s timezone) - 1 year. Used for Read.

- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query.
- `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field.
- `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
- `INSTANCE_URL`(String) - (Required) Used for Read. A valid Salesforce Marketing Cloud Account Engagement instance URL.
- `PARTITION_BY`(String) - (Required) Used for Read. The type of partitioning to be performed. "FIELD" is to be passed in case of field-based partitioning.
- `TRANSFER_MODE`(String) - (Optional), Value to be used for running a job in ASYNC mode , if this option not provided job will run in SYNC mode.
