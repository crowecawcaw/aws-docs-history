

# Reading from Anthropic entities
<a name="anthropic-reading-from-entities"></a>

**Prerequisites**

An Anthropic object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| api\_keys | Yes | Yes | Yes | No | No | 
| cost\_report | Yes | Yes | Yes | No | No | 
| files | No | Yes | Yes | No | No | 
| invites | Yes | Yes | Yes | No | No | 
| message\_batches | No | Yes | Yes | No | No | 
| models | Yes | Yes | Yes | No | No | 
| skill\_versions | No | Yes | Yes | No | No | 
| skills | Yes | Yes | Yes | No | No | 
| usage\_report | Yes | Yes | Yes | No | No | 
| users | Yes | Yes | Yes | No | No | 
| workspace\_members | No | Yes | Yes | No | No | 
| workspaces | No | Yes | Yes | No | No | 

**Example – Reading from an Anthropic entity**  
The following example reads from the `api_keys` entity. Replace {{connectionName}} with the name of your Anthropic connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="anthropic",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "api_keys"
    }
)
```