

# Reading from Nimble entities
<a name="nimble-reading-from-entities"></a>

**Prerequisites**

A Nimble object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| activities | No | Yes | Yes | No | No | 
| contact\_fields | No | No | Yes | No | No | 
| contact\_pipelines | No | No | Yes | No | No | 
| contact\_proceedings\_providers | No | No | Yes | No | No | 
| contacts | Yes | No | Yes | No | No | 
| deals | No | Yes | Yes | No | No | 
| deals\_pipelines | No | No | Yes | No | No | 
| deals\_tags | No | Yes | Yes | No | No | 
| message\_drafts | No | No | Yes | No | No | 

**Example – Reading from a Nimble entity**  
The following example reads from the `activities` entity. Replace {{connectionName}} with the name of your Nimble connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="nimble",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "activities"
    }
)
```