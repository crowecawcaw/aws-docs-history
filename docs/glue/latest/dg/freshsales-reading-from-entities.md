# Reading from Freshsales entities

**Prerequisite**

A Freshsales object you would like to read from. You will need the object name.

**Supported entities for source**:

| Entity   | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| -------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Accounts | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Contacts | Yes             | Yes            | Yes               | Yes                | Yes                   |

**Example**:

```
freshSales_read = glueContext.create_dynamic_frame.from_options(
     connection_type="freshsales",
     connection_options={
         "connectionName": "connectionName",
         "ENTITY_NAME": "entityName",
         "API_VERSION": "v1.0"
     }
```

**Freshsales entity and field details**:

Freshsales provides endpoints to fetch metadata dynamically for supported entities. Accordingly, operator support is captured at the datatype level.

| Entity                   | Data type              | Supported operators    |
| ------------------------ | ---------------------- | ---------------------- |
| Freshsale entities (all) | Integer                | !=,=,<,<=,>,>=,BETWEEN |
| String                   | Like, =, !=            |
| BigInteger               | !=,=,<,<=,>,>=,BETWEEN |
| Boolean                  | =                      |
| Double                   | !=,=,<,<=,>,>=,BETWEEN |
| BigDecimal               | !=,=,<,<=,>,>=,BETWEEN |
| Date                     | !=,=,<,<=,>,>=,BETWEEN |
| DateTime                 | !=,=,<,<=,>,>=,BETWEEN |
| Struct                   | N/A                    |
| List                     | N/A                    |

## Partitioning queries

**Filter-based partitioning**:

You can provide the additional Spark options `PARTITION_FIELD`,
`LOWER_BOUND`, `UPPER_BOUND`, and
`NUM_PARTITIONS` if you want to utilize concurrency in Spark. With
these parameters, the original query would be split into `NUM_PARTITIONS`
number of sub-queries that can be executed by Spark tasks
concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the Datetime field, we accept the value in ISO format.

Examples of valid value:

```
"2024-09-30T01:01:01.000Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

Example:

```
freshSales_read = glueContext.create_dynamic_frame.from_options(
     connection_type="freshsales",
     connection_options={
         "connectionName": "connectionName",
         "ENTITY_NAME": "entityName",
         "API_VERSION": "v1",
         "PARTITION_FIELD": "Created_Time"
         "LOWER_BOUND": " 2024-10-15T21:16:25Z"
         "UPPER_BOUND": " 2024-10-20T21:25:50Z"
         "NUM_PARTITIONS": "10"
     }
```
