

# Reading from Copper entities

**Prerequisites**

A Copper object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| contact\_types | No | No | Yes | No | No | 
| custom\_field\_definitions | No | No | Yes | No | No | 
| customer\_sources | No | No | Yes | No | No | 
| loss\_reasons | No | No | Yes | No | No | 
| pipelines | No | No | Yes | No | No | 
| users | No | No | Yes | No | No | 

**Example – Reading from a Copper entity**  
The following example reads from the `contact_types` entity. Replace {{connectionName}} with the name of your Copper connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="copper",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "contact_types"
    }
)
```