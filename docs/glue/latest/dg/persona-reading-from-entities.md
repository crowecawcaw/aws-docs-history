

# Reading from Persona entities
<a name="persona-reading-from-entities"></a>

**Prerequisites**

A Persona object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| accounts | No | Yes | Yes | No | No | 
| api-logs | No | Yes | Yes | No | No | 
| inquiries | Yes | Yes | Yes | No | No | 
| lists | No | Yes | Yes | No | No | 

**Example – Reading from a Persona entity**  
The following example reads from the `accounts` entity. Replace {{connectionName}} with the name of your Persona connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="persona",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "accounts"
    }
)
```