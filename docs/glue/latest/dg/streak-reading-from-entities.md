

# Reading from Streak entities

**Prerequisites**

A Streak object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| boxes | Yes | No | Yes | No | No | 
| comments | No | No | Yes | No | No | 
| fields | No | No | Yes | No | No | 
| files | No | No | Yes | No | No | 
| meetings | No | No | Yes | No | No | 
| pipelines | No | No | Yes | No | No | 
| snippets | No | No | Yes | No | No | 
| stages | No | No | Yes | No | No | 
| tasks | No | No | Yes | No | No | 
| teams | No | No | Yes | No | No | 
| threads | No | No | Yes | No | No | 

**Example – Reading from a Streak entity**  
The following example reads from the `boxes` entity. Replace {{connectionName}} with the name of your Streak connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="streak",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "boxes"
    }
)
```