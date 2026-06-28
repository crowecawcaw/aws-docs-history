# Reading from Zoom Meetings entities

**Prerequisite**

A Zoom Meetings object you would like to read from. You will need the object namem such as `Group` or `Zoom Rooms`.

**Supported entities for source**:

| Entity         | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| -------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Zoom Rooms     | No              | Yes            | No                | Yes                | No                    |
| Group          | No              | No             | No                | Yes                | No                    |
| Group Member   | Yes             | Yes            | No                | Yes                | No                    |
| Group Admin    | No              | Yes            | No                | Yes                | No                    |
| Report (daily) | Yes             | No             | No                | Yes                | No                    |
| Roles          | No              | No             | No                | Yes                | No                    |
| Users          | Yes             | Yes            | No                | Yes                | No                    |

**Example**:

```
zoom_read = glueContext.create_dynamic_frame.from_options(
    connection_type="zoom",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "organization",
        "API_VERSION": "v2"
    }
)
```

**Zoom Meetings entity and field details**:

Zoom Meetings dynamically loads the available fields under the selected entity. Depending on the data type of the field, it supports the following filter operators.

| Entity                | Field       | Data type | Supported operators |
| --------------------- | ----------- | --------- | ------------------- |
| Zoom Room             | status      | String    | =                   |
| type                  | String      | =         |
| unassigned\_rooms     | Boolean     | =         |
| location\_id          | String      | =         |
| room\_id              | String      | N/A       |
| activation\_code      | String      | N/A       |
| id                    | String      | N/A       |
| name                  | String      | N/A       |
| tag\_ids              | String      | N/A       |
| query\_name           | String      | N/A       |
| Daily Report          | month       | Date      | =                   |
| date                  | Date        | N/A       |
| meeting\_minutes      | Integer     | N/A       |
| meetings              | Integer     | N/A       |
| new\_users            | Integer     | N/A       |
| participants          | Integer     | N/A       |
| group\_id             | String      | N/A       |
| User                  | created\_at | DateTime  | N/A                 |
| dept                  | String      | N/A       |
| email                 | String      | N/A       |
| employee\_unique\_id  | String      | N/A       |
| first\_name           | String      | N/A       |
| group\_ids            | List        | N/A       |
| host\_key             | String      | N/A       |
| id                    | String      | N/A       |
| im\_group\_ids        | String      | N/A       |
| last\_client\_version | String      | N/A       |
| last\_login\_time     | DateTime    | N/A       |
| last\_name            | String      | N/A       |
| plan\_united\_type    | String      | N/A       |
| custom\_attributes    | List        | N/A       |
| pmi                   | BigInteger  | N/A       |
| role\_id              | String      | =         |
| status                | String      | =         |
| timezone              | String      | N/A       |
| type                  | Integer     | N/A       |
| verified              | Integer     | N/A       |
| user\_created\_at     | DateTime    | N/A       |
| display\_name         | String      | N/A       |
| phone\_number         | String      | N/A       |
| language              | String      | N/A       |
| license               | String      | =         |
| Group                 | id          | String    | N/A                 |
| name                  | String      | N/A       |
| total\_members        | Integer     | N/A       |
| Group Member          | email       | String    | N/A                 |
| first\_name           | String      | N/A       |
| id                    | String      | N/A       |
| last\_name            | String      | N/A       |
| type                  | Integer     | N/A       |
| primary\_group        | Boolean     | N/A       |
| member\_id            | String      | N/A       |
| Group Admin           | id          | String    | N/A                 |
| email                 | String      | N/A       |
| name                  | String      | N/A       |
| role                  | description | String    | N/A                 |
| id                    | String      | N/A       |
| name                  | String      | N/A       |
| total\_members        | Integer     | N/A       |
| type                  | String      | =         |

## Partitioning queries

Zoom Meetings doesn't support filter-based partitioning or record-based partitioning.
