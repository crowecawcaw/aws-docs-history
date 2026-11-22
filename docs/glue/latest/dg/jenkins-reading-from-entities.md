

# Reading from Jenkins entities

**Prerequisites**

A Jenkins object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| builds | No | Yes | Yes | No | No | 
| jobs | No | Yes | Yes | No | No | 
| nodes | No | Yes | Yes | No | No | 
| queue | No | Yes | Yes | No | No | 
| views | No | Yes | Yes | No | No | 

**Example – Reading from a Jenkins entity**  
The following example reads from the `builds` entity. Replace {{connectionName}} with the name of your Jenkins connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="jenkins",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "builds"
    }
)
```