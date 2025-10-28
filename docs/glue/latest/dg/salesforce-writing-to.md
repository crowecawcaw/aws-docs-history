# Writing to Salesforce

**Prerequisites**

A Salesforce sObject you would like to write to. You will need the object name such as `Account` or `Case` or `Opportunity`.

The Salesforce connector supports four write operations:

- INSERT
- UPSERT
- UPDATE
- DELETE
  When using the `UPSERT` write operation, the `ID_FIELD_NAMES` option must be provided to specify the external ID field for the records.

You can also add connection options:

- `TRANSFER_MODE`: Supports two modes: `SYNC` and `ASYNC`. Default is `SYNC`. When set to
  `ASYNC`, Bulk API 2.0 Ingest will be utilized for processing.
- `FAIL_ON_FIRST_ERROR`: The default value is `FALSE`, which means the AWS Glue job will continue processing all the
  data even if there are some failed write records. When set to `TRUE`, the AWS Glue job will fail if there are any failed write records,
  and it will not continue processing.
  **Example**

```
salesforce_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="salesforce",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Account",
        "API_VERSION": "v60.0",
        "WRITE_OPERATION": "INSERT",
        "TRANSFER_MODE": "ASYNC",
        "FAIL_ON_FIRST_ERROR": "true"
    }
)
```
