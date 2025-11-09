# Reading from Domo entities

**Prerequisite**

A Domo object you would like to read from. You will need the object name such as Data Set or Data Permission Policies. The following table shows the supported entities.

**Supported entities for source**:

| Entity                   | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ------------------------ | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Data Set                 | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Data Permission Policies | No              | No             | No                | Yes                | No                    |

**Example**:

```
Domo_read = glueContext.create_dynamic_frame.from_options(
    connection_type="domo",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "dataset",
        "API_VERSION": "v1"
    }
```

## Domo entity and field details

Entities with static metadata:

| Entity                   | Field  | Data type | Supported operators |
| ------------------------ | ------ | --------- | ------------------- |
| Data Permission Policies | id     | Long      | N/A                 |
| type                     | String | N/A       |
| name                     | String | N/A       |
| filters                  | List   | N/A       |
| users                    | List   | N/A       |
| virtualUsers             | List   | N/A       |
| groups                   | List   | N/A       |

For the following entity, Domo provides endpoints to fetch metadata dynamically, so that operator support is captured at the datatype level for the entity.

| Entity   | Data type                | Supported operators |
| -------- | ------------------------ | ------------------- |
| Data Set | Integer                  | =, !=, <, >, >=, <= |
| Long     | =, !=, <, >, >=, <=      |
| String   | =, !=, CONTAINS          |
| Date     | =, >, >=, <, <=, BETWEEN |
| DateTime | =, >, >=, <, <=, BETWEEN |
| Boolean  | =, !=                    |
| Double   | =, !=, <, >, >=, <=      |
| List     | N/A                      |
| Struct   | N/A                      |

## Partitioning queries

**Field-based partitioning**

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the DateTime field, we accept the value in ISO format.

Example of valid value:

```
"2023-01-15T11:18:39.205Z"
```

For the Date field, we accept the value in ISO format.

Example of valid value:

```
"2023-01-15"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.

Example of valid value:

```
"2023-02-15T11:18:39.205Z"
```

- `NUM_PARTITIONS`: the number of partitions.

Entity-wise partitioning field support details are captured in the following table:

| Entity name                             | Partitioning fields                          | Data type |
| --------------------------------------- | -------------------------------------------- | --------- |
| Dataset                                 | Any Date/Time based field [dynamic metadata] | DateTime  |
| Any Date based field [dynamic metadata] | Date                                         |

Example:

```
Domo_read = glueContext.create_dynamic_frame.from_options(
    connection_type="domo",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "dataset",
        "API_VERSION": "v1",
        "PARTITION_FIELD": "permissionTime"
        "LOWER_BOUND": "2023-01-15T11:18:39.205Z"
        "UPPER_BOUND": "2023-02-15T11:18:39.205Z"
        "NUM_PARTITIONS": "2"
    }
```

**Record-based partitioning**

You can provide the additional Spark option `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With this parameter, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

In record based partitioning, the total number of records present is queried from Domo, and it is divided by the `NUM_PARTITIONS` number provided. The resulting number of records are then concurrently fetched by each sub-query.

Example:

```
Domo_read = glueContext.create_dynamic_frame.from_options(
    connection_type="domo",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "dataset",
        "API_VERSION": "v1",
        "NUM_PARTITIONS": "2"
    }
```
