# OData Services (Non-ODP Sources)

## Full Load

For Non-ODP (Operational Data Provisioning) systems, a **Full Load** involves extracting the entire dataset from the source system and loading it into the target system. Since Non-ODP systems do not inherently support advanced data extraction mechanisms like deltas, the process is straightforward but can be resource-intensive depending on the size of the data.

## Incremental Load

For systems or entities that do not support **ODP (Operational Data Provisioning)**, incremental data transfer can be managed manually by implementing a timestamp based mechanism to track and extract changes.

**Timestamp based Incremental Transfers**

For non-ODP enabled entities(or for ODP enabled entities that don’t use the ENABLE_CDC flag), we can use a `filteringExpression` option in the connector to indicate the `datetime` interval for which we want to retrieve data. This method relies on a timestamp field in you data that represents when each record was last created/modified.

**Example**

Retrieving records that changed after 2024-01-01T00:00:00.000

```
sapodata_df = glueContext.create_dynamic_frame.from_options(
    connection_type="SAPOData",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "filteringExpression": "LastChangeDateTime >= 2024-01-01T00:00:00.000"
    }, transformation_ctx=key)


```

Note: In this example, `LastChangeDateTime` is the field that represents when each record was last modified. The actual field name may vary depending on your specific SAP OData entity.

To get a new subset of data in subsequent runs, you would update the `filteringExpression` with a new timestamp. Typically, this would be the maximum timestamp value from the previously retrieved data.

**Example**

```
max_timestamp = get_max_timestamp(sapodata_df)  # Function to get the max timestamp from the previous run
next_filtering_expression = f"LastChangeDateTime > {max_timestamp}"

# Use this next_filtering_expression in your next run
```

In the next section, we will provide an automated approach to manage these timestamp-based incremental transfers, eliminating the need to manually update the filtering expression between runs.
