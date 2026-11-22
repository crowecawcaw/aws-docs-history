

# Reading from Finch entities

**Prerequisites**

A Finch object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| automated\_job | No | Yes | Yes | No | No | 
| benefits | No | No | Yes | No | No | 
| company | No | No | Yes | No | No | 
| directory | No | Yes | Yes | No | No | 
| introspect | No | No | Yes | No | No | 
| pay\_group | Yes | No | Yes | No | No | 
| pay\_statement\_item | Yes | No | Yes | No | No | 
| payment | No | No | Yes | No | No | 
| provider | No | No | Yes | No | No | 

**Example – Reading from a Finch entity**  
The following example reads from the `automated_job` entity. Replace {{connectionName}} with the name of your Finch connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="finch",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "automated_job"
    }
)
```