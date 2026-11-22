

# Reading from Shortcut entities

**Prerequisites**

A Shortcut object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| categories | No | Yes | Yes | No | No | 
| custom-fields | No | Yes | Yes | No | No | 
| epics | No | Yes | Yes | No | No | 
| files | No | Yes | Yes | No | No | 
| iterations | No | Yes | Yes | No | No | 
| labels | No | Yes | Yes | No | No | 
| linked-files | No | Yes | Yes | No | No | 
| members | No | Yes | Yes | No | No | 
| objectives | No | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 
| repositories | No | Yes | Yes | No | No | 
| workflows | No | Yes | Yes | No | No | 

**Example – Reading from a Shortcut entity**  
The following example reads from the `categories` entity. Replace {{connectionName}} with the name of your Shortcut connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="shortcut",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "categories"
    }
)
```