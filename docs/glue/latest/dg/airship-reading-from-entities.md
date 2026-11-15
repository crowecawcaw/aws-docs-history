

# Reading from Airship entities
<a name="airship-reading-from-entities"></a>

**Prerequisites**

An Airship object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| channels | No | Yes | Yes | No | No | 
| lists | No | Yes | Yes | No | No | 
| named\_users | No | Yes | Yes | No | No | 
| schedules | No | Yes | Yes | No | No | 
| segments | No | Yes | Yes | No | No | 

**Example – Reading from an Airship entity**  
The following example reads from the `channels` entity. Replace {{connectionName}} with the name of your Airship connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="airship",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "channels"
    }
)
```