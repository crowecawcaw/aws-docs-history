# Delta Token based Incremental Transfers

To enable Incremental Transfer using Change Data Capture (CDC) for ODP-enabled entities that support it, follow these steps:

1. Create the Incremental Transfer job in script mode.
2. When creating the DataFrame or Glue DynamicFrame, you need to pass the option `"ENABLE_CDC": "True"`. This option ensures that you will receive a Delta Token from SAP, which can be used for subsequent retrieval of changed data.
   The delta token will be present in the last row of the dataframe, in the DELTA_TOKEN column. This token can be used as a connector option in subsequent calls to incrementally retrieve the next set of data.

**Example**

- We set the `ENABLE_CDC` flag to `true`, when creating the DynamicFrame. Note: `ENABLE_CDC` is `false` by default, if you don’t want to initialize the delta queue, you don’t need to send this flag or set it to true. Not setting this flag to true will result in a full load extraction.

```
sapodata_df = glueContext.create_dynamic_frame.from_options(
    connection_type="SAPOData",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "ENABLE_CDC": "true"
    }, transformation_ctx=key)

# Extract the delta token from the last row of the DELTA_TOKEN column
delta_token_1 = your_logic_to_extract_delta_token(sapodata_df) # e.g., D20241029164449_000370000
```

- The extracted delta token can be passed as a an option to retrieve new events.

```
sapodata_df_2 = glueContext.create_dynamic_frame.from_options(
    connection_type="SAPOData",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        // passing the delta token retrieved in the last run
        "DELTA_TOKEN": delta_token_1
    } , transformation_ctx=key)

# Extract the new delta token for the next run
delta_token_2 = your_logic_to_extract_delta_token(sapodata_df_2)
```

Note that the last record, in which the `DELTA_TOKEN` is present, is not a transactional record from source, and is only there for the purpose of passing the delta token value.

Apart from the `DELTA_TOKEN`, the following fields are returned in each row of the dataframe.

- **GLUE_FETCH_SQ**: This is a sequence field, generated from the EPOC timestamp in the order the record was received, and is unique for each record. This can be used if you need to know or establish the order of changes in the source system. This field will be present only for ODP enabled entities.
- **DML_STATUS**: This will show `UPDATED` for all newly inserted and updated records from the source, and `DELETED` for records that have been deleted from source.
  For more details about how to manage state and reuse the delta token to retrieve changed records through an example refer to the [Using the SAP OData state management script](sap-odata-state-management-script.md "sap-odata-state-management-script.md") section.

## Delta Token Invalidation

A delta token is associated with the service collection and a user. If a new initial pull with `“ENABLE_CDC” : “true”` is initiated for the same service collection and the user, all previous delta tokens issued as a result of a previous initialization will be invalidated by SAP OData service. Invoking the connector with an expired delta token will lead to an exception:

`Could not open data access via extraction API RODPS_REPL_ODP_OPEN`
