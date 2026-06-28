# Reading from PayPal entities

**Prerequisite**

A PayPal object you would like to read from. You will need the object name, `transaction`.

**Supported entities for source**:

| Entity      | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ----------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| transaction | Yes             | Yes            | No                | Yes                | Yes                   |

**Example**:

```
paypal_read = glueContext.create_dynamic_frame.from_options(
    connection_type="paypal",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "transaction",
        "API_VERSION": "v1",
        "INSTANCE_URL": "https://api-m.paypal.com"
    }
```

**PayPal entity and field details**:

Entities with static metadata:

| Entity                            | Field                         | Data type | Supported operators |
| --------------------------------- | ----------------------------- | --------- | ------------------- |
| transaction                       | transaction\_initiation\_date | DateTime  | Between             |
| last\_refreshed\_datetime         | String                        | N/A       |
| payment\_instrument\_type         | String                        | =         |
| balance\_affecting\_records\_only | String                        | =         |
| store\_id                         | String                        | =         |
| terminal\_id                      | String                        | =         |
| transaction\_currency             | String                        | =         |
| transaction\_id                   | String                        | N/A       |
| transaction\_status               | String                        | N/A       |
| transaction\_type                 | String                        | N/A       |
| transaction\_info                 | Struct                        | N/A       |
| payer\_info                       | Struct                        | N/A       |
| shipping\_info                    | Struct                        | N/A       |
| cart\_info                        | Struct                        | N/A       |
| store\_info                       | Struct                        | N/A       |
| auction\_info                     | Struct                        | N/A       |
| incentive\_info                   | Struct                        | N/A       |

## Partitioning queries

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
"2024-07-01T00:00:00.000Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

The following field is supported for entity-wise partitioning:

| Entity name | Partitioning fields           | Data type |
| ----------- | ----------------------------- | --------- |
| transaction | transaction\_initiation\_date | DateTime  |

Example:

```
paypal_read = glueContext.create_dynamic_frame.from_options(
    connection_type="paypal",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "transaction",
        "API_VERSION": "v1",
        "PARTITION_FIELD": "transaction_initiation_date"
        "LOWER_BOUND": "2024-07-01T00:00:00.000Z"
        "UPPER_BOUND": "2024-07-02T00:00:00.000Z"
        "NUM_PARTITIONS": "10"
    }
```
