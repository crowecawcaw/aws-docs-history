# Writing to HubSpot Entities

## Prerequisites

- A HubSpot object you would like to write to. You will need the object name such as contact or ticket.
- The HubSpot connector supports following write operations:
  - INSERT
  - UPDATE

- When using the `UPDATE` write operation, the `ID_FIELD_NAMES` option must be provided to specify the ID field for the records.

## Supported entities for Sync Destination

| Entity              | API Version | Will be supported as Destination Connector | Can be Inserted    | Can be Updated     |
| ------------------- | ----------- | ------------------------------------------ | ------------------ | ------------------ |
| Companies           | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Contacts            | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Deals               | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Products            | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Calls               | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Meetings            | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Notes               | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Emails              | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Tasks               | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Postal Mails        | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Custom Objects      | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Tickets             | v3          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |
| Associations        | v4          | Yes                                        | Yes (Single, Bulk) | No                 |
| Associations Labels | v4          | Yes                                        | Yes (Single, Bulk) | Yes (Single, Bulk) |

**Examples**:

**INSERT Operation**

```

hubspot_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="hubspot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "contact",
        "API_VERSION": "v3",
        "WRITE_OPERATION": "INSERT"
    }
)

```

**UPDATE Operation**

```

hubspot_write = glueContext.write_dynamic_frame.from_options(
    frame=frameToWrite,
    connection_type="hubspot",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "deal",
        "API_VERSION": "v3",
        "WRITE_OPERATION": "UPDATE",
        "ID_FIELD_NAMES": "hs_object_id"
    }
)

```
