

# Reading from Contentful entities
<a name="contentful-reading-from-entities"></a>

**Prerequisites**

A Contentful object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| assets | No | Yes | Yes | No | No | 
| content\_types | No | Yes | Yes | No | No | 
| entries | No | Yes | Yes | No | No | 

**Example – Reading from a Contentful entity**  
The following example reads from the `assets` entity. Replace {{connectionName}} with the name of your Contentful connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="contentful",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "assets"
    }
)
```