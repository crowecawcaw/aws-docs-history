

# Reading from Miro entities

**Prerequisites**

A Miro object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| boards | Yes | Yes | Yes | No | No | 

**Example – Reading from a Miro entity**  
The following example reads from the `boards` entity. Replace {{connectionName}} with the name of your Miro connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="miro",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "boards"
    }
)
```