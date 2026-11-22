

# Reading from Typeform entities

**Prerequisites**

A Typeform object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| form\_fields | No | Yes | Yes | No | No | 
| forms | Yes | Yes | Yes | No | No | 
| images | No | Yes | Yes | No | No | 
| responses | No | Yes | Yes | No | No | 
| themes | No | Yes | Yes | No | No | 
| webhooks | No | Yes | Yes | No | No | 
| workspaces | Yes | Yes | Yes | No | No | 

**Example – Reading from a Typeform entity**  
The following example reads from the `form_fields` entity. Replace {{connectionName}} with the name of your Typeform connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="typeform",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "form_fields"
    }
)
```