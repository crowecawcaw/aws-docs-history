

# Reading from Klaviyo entities
<a name="klaviyo-reading-from-entities"></a>

**Prerequisites**

A Klaviyo object you want to read from. See the supported entities table below for the available entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| campaigns | No | Yes | Yes | No | No | 
| events | Yes | Yes | Yes | No | Yes | 
| lists | No | Yes | Yes | No | No | 
| metrics | No | Yes | Yes | No | No | 
| profiles | No | Yes | Yes | No | No | 
| segments | No | Yes | Yes | No | No | 

**Example – Reading from a Klaviyo entity**  
The following example reads from the `campaigns` entity. Replace {{connectionName}} with the name of your Klaviyo connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="klaviyo",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "campaigns"
    }
)
```

**Partitioning queries**

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` to read in parallel. The query is split into `NUM_PARTITIONS` sub-queries that Spark runs concurrently. The following entities and fields support partitioning:


| Entity | Partitioning field | 
| --- | --- | 
| events | datetime | 