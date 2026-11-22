

# Reading from Hex entities

**Prerequisites**

A Hex object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| projects | No | Yes | Yes | No | No | 

**Example – Reading from a Hex entity**  
The following example reads from the `projects` entity. Replace {{connectionName}} with the name of your Hex connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="hex",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "projects"
    }
)
```