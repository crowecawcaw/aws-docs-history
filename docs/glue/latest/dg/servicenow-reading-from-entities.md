# Reading from ServiceNow entities

**Prerequisite**

A ServiceNow Tables object you would like to read from. You will need the object name such as pa_bucket or incident.

**Example**:

```
servicenow_read = glueContext.create_dynamic_frame.from_options(
    connection_type="servicenow",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "pa_buckets",
        "API_VERSION": "v2"
        "instanceUrl": "https://<instance-name>.service-now.com"
    }
)
```

**ServiceNow entity and field details**:

For the following entities, ServiceNow provides endpoints to fetch metadata dynamically,
so that operator support is captured at the datatype level for each
entity.

| Entity                    | Data type                          | Supported operators          |
| ------------------------- | ---------------------------------- | ---------------------------- |
| Tables (dynamic entities) | Integer                            | =, !=, <, <=, >, >=, BETWEEN |
| BigDecimal                | =, !=, <, <=, >, >=, BETWEEN       |
| Float                     | =, !=, <, <=, >, >=, BETWEEN       |
| Long                      | =, !=, <, <=, >, >=, BETWEEN       |
| Date                      | =, !=, <, <=, >, >=, BETWEEN       |
| DateTime                  | =, !=, <, <=, >, >=, BETWEEN       |
| Boolean                   | =, !=                              |
| String                    | =, !=, <, <=, >, >=, BETWEEN, LIKE |
| Struct                    | N/A                                |

###### Note

The Struct data type is converted to a String data type in the response of the connector.

###### Note

`DML_STATUS` is an additional user-defined attribute used for tracking CREATED/UPDATED records.

## Partitioning queries

**Field base partitioning**:

You can provide the additional Spark options `PARTITION_FIELD`,
`LOWER_BOUND`, `UPPER_BOUND`, and
`NUM_PARTITIONS` if you want to utilize concurrency in Spark. With
these parameters, the original query would be split into `NUM_PARTITIONS`
number of sub-queries that can be executed by Spark tasks
concurrently.

| Entity name                    | Partitioning fields | Data type |
| ------------------------------ | ------------------- | --------- |
| Dynamic Entity                 | sys_mod_count       | Integer   |
| sys_created_on, sys_updated_on | DateTime            |

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the Datetime field, we accept the Spark timestamp format used in SPark SQL queries.

Examples of valid value:

```
"2024-01-30T06:47:51.000Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

The following table describes the entity partitioning field support details:

Example:

```
servicenow_read = glueContext.create_dynamic_frame.from_options(
    connection_type="servicenow",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "pa_buckets",
        "API_VERSION": "v2",
        "instanceUrl": "https://<instance-name>.service-now.com"
        "PARTITION_FIELD": "sys_created_on"
        "LOWER_BOUND": "2024-01-30T06:47:51.000Z"
        "UPPER_BOUND": "2024-06-30T06:47:51.000Z"
        "NUM_PARTITIONS": "10"
    }
```

**Record-based partitioning**:

You can provide the additional Spark option `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With this parameter, the original query is split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

In record-based partitioning, the total number of records present is queried from the ServiceNow API, and it is divided by `NUM_PARTITIONS` number provided. The resulting number of records are then concurrently fetched by each sub-query.

- `NUM_PARTITIONS`: the number of partitions.

Example:

```
servicenow_read = glueContext.create_dynamic_frame.from_options(
    connection_type="servicenow",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "pa_buckets",
        "API_VERSION": "v2",
        "instanceUrl": "https://<instance-name>.service-now.com"
        "NUM_PARTITIONS": "2"
    }
```
