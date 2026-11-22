

# Reading from mabl entities

**Prerequisites**

A mabl object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| applications | No | Yes | Yes | No | No | 
| environments | No | Yes | Yes | No | No | 

**Example – Reading from a mabl entity**  
The following example reads from the `applications` entity. Replace {{connectionName}} with the name of your mabl connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="mabl",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "applications"
    }
)
```