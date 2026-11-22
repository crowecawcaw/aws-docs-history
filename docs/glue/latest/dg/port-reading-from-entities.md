

# Reading from Port entities

**Prerequisites**

A Port object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| action\_runs | No | Yes | Yes | No | No | 
| actions | No | Yes | Yes | No | No | 
| blueprints | No | Yes | Yes | No | No | 
| entities | No | Yes | Yes | No | No | 
| scorecards | No | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| users | No | Yes | Yes | No | No | 

**Example – Reading from a Port entity**  
The following example reads from the `action_runs` entity. Replace {{connectionName}} with the name of your Port connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="port",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "action_runs"
    }
)
```