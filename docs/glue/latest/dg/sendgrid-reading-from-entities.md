# Reading from SendGrid entities

**Prerequisite**

A SendGrid object you would like to read from. You will need the object name such as `lists`, `singlesends` or `segments`.

**Supported entities for source**:

| Entity                                | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ------------------------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Lists                                 | No              | Yes            | No                | Yes                | No                    |
| Single Sends                          | Yes             | Yes            | No                | Yes                | No                    |
| Marketing Campaign Stats-Automations  | Yes             | Yes            | No                | Yes                | No                    |
| Marketing Campaign Stats-Single Sends | Yes             | Yes            | No                | Yes                | No                    |
| Segments                              | Yes             | No             | No                | Yes                | No                    |
| Contacts                              | Yes             | No             | No                | Yes                | No                    |
| Category                              | No              | No             | No                | Yes                | No                    |
| Stats                                 | Yes             | No             | No                | Yes                | No                    |
| Unsubscribe Groups                    | Yes             | No             | No                | Yes                | No                    |

**Example**:

```
sendgrid_read = glueContext.create_dynamic_frame.from_options(
    connection_type="sendgrid",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "lists",
        "API_VERSION": "v3",
        "INSTANCE_URL": "instanceUrl"
    }
```

**SendGrid entity and field details**:

Entities with static metadata:

| Entity                               | Field      | Data type          | Supported operators |
| ------------------------------------ | ---------- | ------------------ | ------------------- |
| Lists                                | id         | String             | N/A                 |
| name                                 | String     | N/A                |
| contact\_count                       | Integer    | N/A                |
| \_metadata                           | Struct     | N/A                |
| Single Sends                         | id         | String             | N/A                 |
| name                                 | String     | EQUAL\_TO          |
| abtest                               | Struct     | N/A                |
| status                               | String     | EQUAL\_TO          |
| categories                           | List       | EQUAL\_TO          |
| send\_at                             | String     | N/A                |
| is\_abtest                           | Boolean    | N/A                |
| updated\_at                          | String     | N/A                |
| created\_at                          | String     | N/A                |
| channels                             | List       | N/A                |
| Marketing Campaign Stats-Automations | id         | String             | N/A                 |
| aggregation                          | String     | N/A                |
| step\_id                             | String     | N/A                |
| stats                                | Struct     | N/A                |
| automation\_ids                      | List       | EQUAL\_TO          |
| Marketing Campaign Stats-Singlesends | id         | String             | N/A                 |
| ab\_variation                        | String     | N/A                |
| ab\_phase                            | String     | N/A                |
| aggregation                          | String     | N/A                |
| stats                                | Struct     | N/A                |
| singlesend\_ids                      | List       | EQUAL\_TO          |
| Segments                             | id         | String             | N/A                 |
| name                                 | String     | N/A                |
| query\_version                       | String     | N/A                |
| contacts\_count                      | Integer    | N/A                |
| sample\_updated\_at                  | String     | N/A                |
| next\_sample\_update                 | String     | N/A                |
| created\_at                          | String     | N/A                |
| updated\_at                          | String     | N/A                |
| parent\_list\_id                     | String     | N/A                |
| status                               | Struct     | N/A                |
| parent\_list\_ids                    | String     | EQUAL\_TO          |
| no\_parent\_list\_id                 | Boolean    | EQUAL\_TO          |
| Contacts                             | id         | String             | N/A                 |
| first\_name                          | String     | N/A                |
| last\_name                           | String     | N/A                |
| unique\_name                         | String     | N/A                |
| email                                | String     | N/A                |
| alternate\_emails                    | List       | N/A                |
| address\_line\_1                     | String     | N/A                |
| address\_line\_2                     | String     | N/A                |
| city                                 | String     | N/A                |
| state\_province\_region              | String     | N/A                |
| country                              | String     | N/A                |
| postal\_code                         | String     | N/A                |
| phone\_number                        | String     | N/A                |
| whatsapp                             | String     | N/A                |
| line                                 | String     | N/A                |
| facebook                             | String     | N/A                |
| list\_ids                            | List       | N/A                |
| custom\_fields                       | Struct     | N/A                |
| created\_at                          | String     | N/A                |
| updated\_at                          | String     | N/A                |
| \_metadata                           | Struct     | N/A                |
| event\_timestamp                     | DateTime   | BETWEEN            |
| Category                             | categories | List               | N/A                 |
| Stats                                | date       | String             | N/A                 |
| stats                                | List       | N/A                |
| start\_date                          | DateTime   | EQUAL\_TO, BETWEEN |
| aggregated\_by                       | String     | EQUAL\_TO          |
| Unsubscribe Groups                   | id         | Integer            | EQUAL\_TO           |
| name                                 | String     | N/A                |
| description                          | String     | N/A                |
| last\_email\_sent\_at                | Integer    | N/A                |
| is\_default                          | Boolean    | N/A                |
| unsubscribes                         | Integer    | N/A                |

###### Note

Struct and List data types are converted to String data type, and DateTime data type is converted to Timestamp in the response of the connectors.

## Partitioning queries

SendGrid doesn't support filter-based partitioning or record-based partitioning.
