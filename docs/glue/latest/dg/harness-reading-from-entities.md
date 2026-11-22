

# Reading from Harness entities

**Prerequisites**

A Harness object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| connectors | Yes | Yes | Yes | No | No | 
| organizations | Yes | Yes | Yes | No | No | 
| projects | Yes | Yes | Yes | No | No | 
| user-groups | Yes | Yes | Yes | No | No | 

**Example – Reading from a Harness entity**  
The following example reads from the `connectors` entity. Replace {{connectionName}} with the name of your Harness connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="harness",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "connectors"
    }
)
```