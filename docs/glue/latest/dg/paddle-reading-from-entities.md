

# Reading from Paddle entities

**Prerequisites**

A Paddle object you want to read from. See the supported entities table below for the available entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| adjustments | Yes | Yes | Yes | No | No | 
| checkout\_domains | Yes | Yes | Yes | No | No | 
| client\_tokens | No | Yes | Yes | No | No | 
| customers | Yes | Yes | Yes | No | No | 
| addresses | Yes | Yes | Yes | No | No | 
| businesses | Yes | Yes | Yes | No | No | 
| credit\_balances | Yes | Yes | Yes | No | No | 
| customer\_payment\_methods | Yes | Yes | Yes | No | No | 
| discount\_groups | Yes | Yes | Yes | No | No | 
| discounts | Yes | Yes | Yes | No | No | 
| event\_types | No | Yes | Yes | No | No | 
| events | Yes | Yes | Yes | No | No | 
| notification\_settings | Yes | Yes | Yes | No | No | 
| notifications | Yes | Yes | Yes | No | No | 
| notification\_logs | No | Yes | Yes | No | No | 
| prices | Yes | Yes | Yes | No | No | 
| products | Yes | Yes | Yes | No | No | 
| simulation\_types | No | Yes | Yes | No | No | 
| simulation\_run\_events | Yes | Yes | Yes | No | No | 
| subscription\_history | Yes | Yes | Yes | No | No | 
| subscriptions | Yes | Yes | Yes | No | No | 
| transactions | Yes | Yes | Yes | No | Yes | 

**Example – Reading from a Paddle entity**  
The following example reads from the `adjustments` entity. Replace {{connectionName}} with the name of your Paddle connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="paddle",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "adjustments"
    }
)
```

**Partitioning queries**

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` to read in parallel. The query is split into `NUM_PARTITIONS` sub-queries that Spark runs concurrently. The following entities and fields support partitioning:


| Entity | Partitioning field | 
| --- | --- | 
| transactions | created\_at | 
| transactions | billed\_at | 