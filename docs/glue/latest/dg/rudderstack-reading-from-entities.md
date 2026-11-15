

# Reading from RudderStack entities
<a name="rudderstack-reading-from-entities"></a>

**Prerequisites**

A RudderStack object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| libraries | No | No | Yes | No | No | 
| transformations | No | No | Yes | No | No | 

**Example – Reading from a RudderStack entity**  
The following example reads from the `libraries` entity. Replace {{connectionName}} with the name of your RudderStack connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="rudderstack",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "libraries"
    }
)
```