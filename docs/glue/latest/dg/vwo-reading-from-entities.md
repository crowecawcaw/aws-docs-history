

# Reading from VWO entities
<a name="vwo-reading-from-entities"></a>

**Prerequisites**

A VWO object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| attributes | No | No | Yes | No | No | 
| events | No | No | Yes | No | No | 

**Example – Reading from a VWO entity**  
The following example reads from the `attributes` entity. Replace {{connectionName}} with the name of your VWO connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="vwo",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "attributes"
    }
)
```