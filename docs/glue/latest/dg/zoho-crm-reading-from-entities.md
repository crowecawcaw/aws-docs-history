# Reading from Zoho CRM entities

**Prerequisite**

Zoho CRM objects you would like to read from. You will need the object name.

**Supported entities for Sync source**:

| Entity         | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| -------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Product        | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Quote          | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Purchase Order | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Solution       | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Call           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Task           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Event          | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Invoice        | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Account        | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Contact        | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Vendor         | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Campaign       | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Deal           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Lead           | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Custom Module  | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Sales Order    | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Price Books    | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Case           | Yes             | Yes            | Yes               | Yes                | Yes                   |

**Example**:

```
zoho_read = glueContext.create_dynamic_frame.from_options(
    connection_type="ZOHO",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v7",
        "INSTANCE_URL": "https://www.zohoapis.in/"
    }
```

**Supported entities for Async source**:

| Entity         | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| -------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Product        | Yes             | No             | No                | Yes                | No                    |
| Quote          | Yes             | No             | No                | Yes                | No                    |
| Purchase Order | Yes             | No             | No                | Yes                | No                    |
| Solution       | Yes             | No             | No                | Yes                | No                    |
| Call           | Yes             | No             | No                | Yes                | No                    |
| Task           | Yes             | No             | No                | Yes                | No                    |
| Event          | Yes             | No             | No                | Yes                | No                    |
| Invoice        | Yes             | No             | No                | Yes                | No                    |
| Account        | Yes             | No             | No                | Yes                | No                    |
| Contact        | Yes             | No             | No                | Yes                | No                    |
| Vendor         | Yes             | No             | No                | Yes                | No                    |
| Campaign       | Yes             | No             | No                | Yes                | No                    |
| Deal           | Yes             | No             | No                | Yes                | No                    |
| Lead           | Yes             | No             | No                | Yes                | No                    |
| Custom Module  | Yes             | No             | No                | Yes                | No                    |
| Sales Order    | Yes             | No             | No                | Yes                | No                    |
| Price Books    | Yes             | No             | No                | Yes                | No                    |
| Case           | Yes             | No             | No                | Yes                | No                    |

**Example**:

```
zoho_read = glueContext.create_dynamic_frame.from_options(
    connection_type="ZOHO",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v7",
        "INSTANCE_URL": "https://www.zohoapis.in/",
        "TRANSFER_MODE": "ASYNC"
    }
```

**Zoho CRM field details**:

Zoho CRM provides endpoints to fetch metadata dynamically for supported entities. Therefore, operator support is captured at the datatype level.

| Entity                       | Data type                    | Supported operators          |
| ---------------------------- | ---------------------------- | ---------------------------- |
| Zoho entities (all entities) | Integer                      | !=, =, <, <=, >, >=, BETWEEN |
| String                       | Like, =, !=                  |
| BigInteger                   | !=, =, <, <=, >, >=, BETWEEN |
| Boolean                      | =                            |
| Double                       | !=, =, <, <=, >, >=, BETWEEN |
| BigDecimal                   | !=, =, <, <=, >, >=, BETWEEN |
| Date                         | !=, =, <, <=, >, >=, BETWEEN |
| DateTime                     | !=, =, <, <=, >, >=, BETWEEN |
| Struct                       | N/A                          |
| List                         | N/A                          |

## Partitioning queries

Partitioning is not supported in Async mode.

**Filter-based partitioning (Sync mode)**:

You can provide the additional Spark options `PARTITION_FIELD`,
`LOWER_BOUND`, `UPPER_BOUND`, and
`NUM_PARTITIONS` if you want to utilize concurrency in Spark. With
these parameters, the original query would be split into `NUM_PARTITIONS`
number of sub-queries that can be executed by Spark tasks
concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the Datetime field, we accept the Spark timestamp format used in Spark SQL queries.

Examples of valid value:

```
"2024-09-30T01:01:01.000Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

Example:

```
zoho_read = glueContext.create_dynamic_frame.from_options(
    connection_type="zohocrm",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v7",
        "PARTITION_FIELD": "Created_Time"
        "LOWER_BOUND": "2022-01-01T01:01:01.000Z"
        "UPPER_BOUND": "2024-01-01T01:01:01.000Z"
        "NUM_PARTITIONS": "10"
    }
```
