

# Reading from Adobe Marketo Engage entities
<a name="adobe-marketo-engage-reading-from-entities"></a>

**Prerequisite**

An Adobe Marketo Engage object you would like to read from. You will need the object name such as leads or activities or customobjects. The following tables shows the supported entities.

**Supported entities for source (synchronous)**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| leads | Yes | Yes | No | Yes | No | 
| activities | Yes | Yes | No | Yes | No | 
| customobjects | Yes | Yes | No | Yes | No | 

**Supported entities for source (asynchronous)**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| leads | Yes | No | No | Yes | Yes | 
| activities | Yes | No | No | Yes | No | 
| customobjects | Yes | No | No | Yes | Yes | 

**Example**:

```
adobe-marketo-engage_read = glueContext.create_dynamic_frame.from_options(
    connection_type="adobe-marketo-engage",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "leads",
        "API_VERSION": "v2",
        "INSTANCE_URL": "https://539-t**-6**.mktorest.com"
    }
```

**Adobe Marketo Engage entity and field details**:

**Entities with static metadata**: 



- **activities**
  - **Field:** sinceDatetime (only supported in synchronous) / **Data type:** DateTime / **Supported operators:** >= (only for synchronous mode)
  - **Field:** createdAt (only supported in asynchronous) / **Data type:** DateTime / **Supported operators:** between (only for asynchronous mode)
  - **Field:** activitiesTypeId / **Data type:** Integer / **Supported operators:** =
  - **Field:** adobe-marketo-engageGUID / **Data type:** Long / **Supported operators:**  = (only for synchronous mode)
  - **Field:** leadId / **Data type:** Long / **Supported operators:** N/A
  - **Field:** activityDate / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** campaignId / **Data type:** Long / **Supported operators:** N/A
  - **Field:** primaryAttributeValueId / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** primaryAttributeValue / **Data type:** String / **Supported operators:** N/A
  - **Field:** attributes / **Data type:** String / **Supported operators:** N/A



**Entities with dynamic metadata**:

For the following entities, Adobe Marketo Engage provides endpoints to fetch metadata dynamically, so that operator support is captured at the datatype level for each entity.



- **leads**
  - **Data type:** Integer / **Supported operators:**  = (only for synchronous mode)
  - **Data type:** DateTime / **Supported operators:** between (only for asynchronous mode)
  - **Data type:** String / **Supported operators:**  = (only for synchronous mode)
  - **Data type:** Long / **Supported operators:** N/A
  - **Data type:** Boolean / **Supported operators:** N/A
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** Float / **Supported operators:** N/A

- **customobjects**
  - **Data type:** Integer / **Supported operators:** N/A
  - **Data type:** DateTime / **Supported operators:** between (only for asynchronous mode)
  - **Data type:** String / **Supported operators:**  = (only for synchronous mode)
  - **Data type:** Date / **Supported operators:** N/A
  - **Data type:** Long / **Supported operators:** N/A
  - **Data type:** Boolean / **Supported operators:** N/A
  - **Data type:** Float / **Supported operators:** N/A



## Partitioning queries
<a name="adobe-marketo-engage-reading-partitioning-queries"></a>

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.
+ `PARTITION_FIELD`: the name of the field to be used to partition the query.
+ `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

  For the DateTime field, we accept the value in ISO format.

  Example of valid value:

  ```
  "2024-07-01T00:00:00.000Z"
  ```
+ `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
+ `NUM_PARTITIONS`: the number of partitions.

The following table describes the entity partitioning field support details:



- **leads**
  - **Partitioning fields:** createdAt / **Data type:** DateTime
  - **Partitioning fields:** updateAt / **Data type:** DateTime

- **customobjects**
  - **Partitioning fields:** updatedAt
  - **Data type:** DateTime



Example:

```
adobe-marketo-engage_read = glueContext.create_dynamic_frame.from_options(
    connection_type="adobe-marketo-engage",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "leads",
        "API_VERSION": "v1",
        "PARTITION_FIELD": "createdAt"
        "LOWER_BOUND": "2024-07-01T00:00:00.000Z"
        "UPPER_BOUND": "2024-07-02T00:00:00.000Z"
        "NUM_PARTITIONS": "10"
    }
```