

# Reading from Domo entities
<a name="domo-reading-from-entities"></a>

**Prerequisite**

A Domo object you would like to read from. You will need the object name such as Data Set or Data Permission Policies. The following table shows the supported entities.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Data Set | Yes | Yes | Yes | Yes | Yes | 
| Data Permission Policies | No | No | No | Yes | No | 

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
<a name="domo-reading-from-entities-field-details"></a>

Entities with static metadata:



- **Data Permission Policies**
  - **Field:** id / **Data type:** Long / **Supported operators:** N/A
  - **Field:** type / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** filters / **Data type:** List / **Supported operators:** N/A
  - **Field:** users / **Data type:** List / **Supported operators:** N/A
  - **Field:** virtualUsers / **Data type:** List / **Supported operators:** N/A
  - **Field:** groups / **Data type:** List / **Supported operators:** N/A



For the following entity, Domo provides endpoints to fetch metadata dynamically, so that operator support is captured at the datatype level for the entity.



- **Data Set**
  - **Data type:** Integer / **Supported operators:** =, \!=, <, >, >=, <=
  - **Data type:** Long / **Supported operators:** =, \!=, <, >, >=, <=
  - **Data type:** String / **Supported operators:** =, \!=, CONTAINS
  - **Data type:** Date / **Supported operators:**  =, >, >=, <, <=, BETWEEN
  - **Data type:** DateTime / **Supported operators:**  =, >, >=, <, <=, BETWEEN
  - **Data type:** Boolean / **Supported operators:** =, \!=
  - **Data type:** Double / **Supported operators:** =, \!=, <, >, >=, <=
  - **Data type:** List / **Supported operators:** N/A
  - **Data type:** Struct / **Supported operators:** N/A



## Partitioning queries
<a name="domo-reading-from-partitioning"></a>

**Field-based partitioning**

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.
+ `PARTITION_FIELD`: the name of the field to be used to partition the query.
+ `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

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
+ `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.

  Example of valid value:

  ```
  "2023-02-15T11:18:39.205Z"
  ```
+ `NUM_PARTITIONS`: the number of partitions.

Entity-wise partitioning field support details are captured in the following table:



- **Dataset**
  - **Partitioning fields:** Any Date/Time based field [dynamic metadata] / **Data type:** DateTime
  - **Partitioning fields:** Any Date based field [dynamic metadata] / **Data type:** Date



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