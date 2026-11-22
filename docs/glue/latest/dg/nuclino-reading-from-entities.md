

# Reading from Nuclino entities

**Prerequisites**

A Nuclino object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| items | No | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| workspaces | No | Yes | Yes | No | No | 

**Example – Reading from a Nuclino entity**  
The following example reads from the `items` entity. Replace {{connectionName}} with the name of your Nuclino connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="nuclino",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "items"
    }
)
```