

# Reading from Fullstory entities
<a name="fullstory-reading-from-entities"></a>

**Prerequisites**

A Fullstory object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| segments | No | Yes | Yes | No | No | 
| users | Yes | Yes | Yes | No | No | 

**Example – Reading from a Fullstory entity**  
The following example reads from the `segments` entity. Replace {{connectionName}} with the name of your Fullstory connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="fullstory",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "segments"
    }
)
```