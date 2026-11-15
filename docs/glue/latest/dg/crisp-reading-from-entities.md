

# Reading from Crisp entities
<a name="crisp-reading-from-entities"></a>

**Prerequisites**

A Crisp object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| conversations | No | No | Yes | No | No | 
| people | No | No | Yes | No | No | 

**Example – Reading from a Crisp entity**  
The following example reads from the `conversations` entity. Replace {{connectionName}} with the name of your Crisp connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="crisp",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "conversations"
    }
)
```