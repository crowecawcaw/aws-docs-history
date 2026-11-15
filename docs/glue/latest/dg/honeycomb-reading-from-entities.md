

# Reading from Honeycomb entities
<a name="honeycomb-reading-from-entities"></a>

**Prerequisites**

A Honeycomb object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| api\_keys | No | Yes | Yes | No | No | 
| environments | No | Yes | Yes | No | No | 

**Example – Reading from a Honeycomb entity**  
The following example reads from the `api_keys` entity. Replace {{connectionName}} with the name of your Honeycomb connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="honeycomb",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "api_keys"
    }
)
```