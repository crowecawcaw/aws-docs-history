

# Reading from Smartlook entities
<a name="smartlook-reading-from-entities"></a>

**Prerequisites**

A Smartlook object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| events | No | Yes | Yes | No | No | 
| funnels | No | Yes | Yes | No | No | 

**Example – Reading from a Smartlook entity**  
The following example reads from the `events` entity. Replace {{connectionName}} with the name of your Smartlook connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="smartlook",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "events"
    }
)
```