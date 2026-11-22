

# Reading from Front entities

**Prerequisites**

A Front object you want to read from. See the supported entities table below for the available entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| contacts | No | Yes | Yes | No | No | 
| conversations | No | Yes | Yes | No | No | 
| inboxes | No | Yes | Yes | No | No | 
| tags | No | Yes | Yes | No | No | 
| teammates | No | Yes | Yes | No | No | 

**Example – Reading from a Front entity**  
The following example reads from the `contacts` entity. Replace {{connectionName}} with the name of your Front connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="front",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "contacts"
    }
)
```