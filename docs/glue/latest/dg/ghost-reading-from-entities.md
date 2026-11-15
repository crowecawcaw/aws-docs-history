

# Reading from Ghost entities
<a name="ghost-reading-from-entities"></a>

**Prerequisites**

A Ghost object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| authors | No | No | Yes | No | No | 
| pages | No | No | Yes | No | No | 
| posts | No | No | Yes | No | No | 
| tags | No | No | Yes | No | No | 
| tiers | No | No | Yes | No | No | 

**Example – Reading from a Ghost entity**  
The following example reads from the `authors` entity. Replace {{connectionName}} with the name of your Ghost connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="ghost",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "authors"
    }
)
```