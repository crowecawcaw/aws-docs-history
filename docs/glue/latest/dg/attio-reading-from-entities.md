

# Reading from Attio entities

**Prerequisites**

An Attio object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| lists | No | Yes | Yes | No | No | 
| meetings | No | Yes | Yes | No | No | 
| notes | No | Yes | Yes | No | No | 
| objects | No | Yes | Yes | No | No | 
| tasks | No | Yes | Yes | No | No | 
| webhooks | No | Yes | Yes | No | No | 
| workspace\_members | No | Yes | Yes | No | No | 

**Example – Reading from an Attio entity**  
The following example reads from the `lists` entity. Replace {{connectionName}} with the name of your Attio connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="attio",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "lists"
    }
)
```