# Writing to SAP OData

This section describes how to write data to your SAP OData Service using the AWS Glue connector for SAP OData.

**Prerequisites**

- Access to an SAP OData service
- An SAP OData EntitySet Object you would like to write to. You will need the Object name.
- Valid SAP OData credentials and a valid connection
- Appropriate permissions as described in [IAM policies](sap-odata-configuring-iam-permissions.md "sap-odata-configuring-iam-permissions.md")
  The SAP OData connector supports two write operations:

- INSERT
- UPDATE
  While using the UPDATE write operation, ID_FIELD_NAMES must be provided to specify the external ID field for the records.

**Example:**

```
sapodata_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="sapodata",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "WRITE_OPERATION": "INSERT"
    }
```
