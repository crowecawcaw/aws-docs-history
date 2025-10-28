# ServiceNow connection options

The following are connection options for ServiceNow:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in ServiceNow.
- `API_VERSION`(String) - (Required) Used for Read. ServiceNow Rest API version you want to use. For example: v1,v2,v3,v4.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query.
- `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field. For example: 2024-01-30T06:47:51.000Z.
- `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field. For example: 2024-06-30T06:47:51.000Z.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read. For example: 10.
- `INSTANCE_URL`(String) - (Required) A valid ServiceNow instance URL with format https://<instance-name>.service-now.com.
- `PAGE_SIZE`(Integer) - Defines the page size for querying the records. The default page size is 1,000. When a page size is specified, ServiceNow returns
  only the defined number of records per API call, rather than the entire dataset. The connector will still provide the total number of records and handle pagination using your
  specified page size. If you require a larger page size, you can choose any value up to 10,000, which is the maximum allowed. Any specified page size exceeding 10,000 will
  be ignored. Instead, the system will use the maximum allowed page size. You can specify the page size in the AWS Glue Studio UI by adding a connection option `PAGE_SIZE`
  with your desired value. For example: 5000.
