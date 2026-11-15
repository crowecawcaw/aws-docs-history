

# Reading from Rootly entities
<a name="rootly-reading-from-entities"></a>

**Prerequisites**

A Rootly object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| alerts | No | Yes | Yes | No | No | 
| environments | No | Yes | Yes | No | No | 
| functionalities | No | Yes | Yes | No | No | 
| incidents | No | Yes | Yes | No | No | 
| services | No | Yes | Yes | No | No | 
| severities | No | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 

**Example – Reading from a Rootly entity**  
The following example reads from the `alerts` entity. Replace {{connectionName}} with the name of your Rootly connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="rootly",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "alerts"
    }
)
```