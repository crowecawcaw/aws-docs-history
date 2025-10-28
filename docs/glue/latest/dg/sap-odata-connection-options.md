# SAP OData connection options

The following are connection options for SAP OData:

- `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in SAP OData.

For example: /sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder

- `API_VERSION`(String) - (Optional) Used for Read. SAP OData Rest API version you want to use. Example: 2.0.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.

For example: SalesOrder

- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.

For example: `SalesOrder = "10"`

- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.

For example: `SELECT * FROM /sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder`

- `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query.

For example: `ValidStartDate`

- `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field.

For example: `"2000-01-01T00:00:00.000Z"`

- `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field.

For example: `"2024-01-01T00:00:00.000Z"`

- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
- `INSTANCE_URL`(String) - The SAP instance application host URL.

For example: `https://example-externaldata.sierra.aws.dev`

- `SERVICE_PATH`(String) - The SAP instance application service path.

For example: `/sap/opu/odata/iwfnd/catalogservice;v=2`

- `CLIENT_NUMBER`(String) - The SAP instance application client number.

For example: 100

- `PORT_NUMBER`(String) - Default: The SAP instance application port number.

For example: 443

- `LOGON_LANGUAGE`(String) - The SAP instance application logon language.

For example: `EN`

- `ENABLE_CDC`(String) - Defines whether to run a job with CDC enabled, that is, with track changes.

For example: `True/False`

- `DELTA_TOKEN`(String) - Runs an incremental data pull based on the valid Delta Token supplied.

For example: `D20241107043437_000463000`

- `PAGE_SIZE`(Integer) - Defines the page size for querying the records. The default page size is 50,000.
  When a page size is specified, SAP returns only the defined number of records per API call, rather than the entire dataset.
  The connector will still provide the total number of records and handle pagination using your specified page size.
  If you require a larger page size, you can choose any value up to 500,000, which is the maximum allowed.
  Any specified page size exceeding 500,000 will be ignored. Instead, the system will use the maximum allowed page size.
  You can specify the page size in the AWS Glue Studio UI by adding a connection option `PAGE_SIZE` with your desired value.

For example: `20000`
