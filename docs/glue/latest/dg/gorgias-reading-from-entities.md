

# Reading from Gorgias entities

**Prerequisites**

A Gorgias object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| customers | Yes | Yes | Yes | No | No | 
| events | Yes | Yes | Yes | No | No | 
| integrations | No | Yes | Yes | No | No | 
| jobs | No | Yes | Yes | No | No | 
| macros | No | Yes | Yes | No | No | 
| rules | No | Yes | Yes | No | No | 
| satisfaction-surveys | Yes | Yes | Yes | No | No | 
| tags | No | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| ticket-messages | Yes | Yes | Yes | No | No | 
| tickets | Yes | Yes | Yes | No | No | 
| users | Yes | Yes | Yes | No | No | 
| views | No | Yes | Yes | No | No | 
| widgets | No | Yes | Yes | No | No | 

**Example – Reading from a Gorgias entity**  
The following example reads from the `customers` entity. Replace {{connectionName}} with the name of your Gorgias connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="gorgias",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "customers"
    }
)
```