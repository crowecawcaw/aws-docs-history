

# Reading from Folk entities

**Prerequisites**

A Folk object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| companies | No | Yes | Yes | No | No | 
| groups | No | Yes | Yes | No | No | 
| notes | No | Yes | Yes | No | No | 
| people | No | Yes | Yes | No | No | 
| tasks | No | Yes | Yes | No | No | 

**Example – Reading from a Folk entity**  
The following example reads from the `companies` entity. Replace {{connectionName}} with the name of your Folk connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="folk",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "companies"
    }
)
```