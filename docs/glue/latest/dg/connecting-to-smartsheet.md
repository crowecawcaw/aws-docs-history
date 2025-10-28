# Connecting to Smartsheet

Smartsheet is a work management and collaboration SaaS product. Fundamentally, Smartsheet
allows users to use spreadsheet-like objects to create, store, and utilize business
data.

###### Topics

- [AWS Glue support for Smartsheet](smartsheet-support.md "smartsheet-support.md")
- [Policies containing the API operations for creating and using connections](smartsheet-configuring-iam-permissions.md "smartsheet-configuring-iam-permissions.md")
- [Configuring Smartsheet](smartsheet-configuring.md "smartsheet-configuring.md")
- [Configuring Smartsheet connections](smartsheet-configuring-connections.md "smartsheet-configuring-connections.md")
- [Reading from Smartsheet
  entities](smartsheet-reading-from-entities.md "smartsheet-reading-from-entities.md")
- [Smartsheet connection options](smartsheet-connection-options.md "smartsheet-connection-options.md")
- [Creating an Smartsheet account](smartsheet-create-account.md "smartsheet-create-account.md")
- [Limitations](smartsheet-connector-limitations.md "smartsheet-connector-limitations.md")
  **Entities with dynamic metadata:**

For the following entity, Smartsheet provides an endpoint to fetch metadata dynamically,
allowing operator support to be captured at the datatype level.

| Entity     | Data Type | Supported Operators |
| ---------- | --------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Sheet Data | String    | NA                  |
| Sheet Data | Long      | "="                 |
| Sheet Data | Integer   | NA                  |
| Sheet Data | DateTime  | >                   | **Example** `Smartsheet_read = glueContext.create_dynamic_frame.from_options( connection_type="smartsheet", connection_options={ "connectionName": "connectionName", "ENTITY_NAME": "list-sheets", "API_VERSION": "2.0", "INSTANCE_URL": "https://api.smartsheet.com" }` |
