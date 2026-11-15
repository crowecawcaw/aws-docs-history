

# Reading from Kommo entities
<a name="kommo-reading-from-entities"></a>

**Prerequisites**

A Kommo object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| companies | Yes | Yes | Yes | No | No | 
| contacts | Yes | Yes | Yes | No | No | 
| events | Yes | Yes | Yes | No | No | 
| leads | Yes | Yes | Yes | No | No | 
| pipelines | No | Yes | Yes | No | No | 
| tasks | Yes | Yes | Yes | No | No | 
| users | No | Yes | Yes | No | No | 

**Example – Reading from a Kommo entity**  
The following example reads from the `companies` entity. Replace {{connectionName}} with the name of your Kommo connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="kommo",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "companies"
    }
)
```