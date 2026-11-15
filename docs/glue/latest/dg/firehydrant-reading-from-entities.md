

# Reading from FireHydrant entities
<a name="firehydrant-reading-from-entities"></a>

**Prerequisites**

A FireHydrant object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| alerts | Yes | Yes | Yes | No | No | 
| changes | No | Yes | Yes | No | No | 
| environments | No | Yes | Yes | No | No | 
| functionalities | No | Yes | Yes | No | No | 
| incident\_events | Yes | Yes | Yes | No | No | 
| incident\_milestones | No | Yes | Yes | No | No | 
| incident\_role\_assignments | Yes | Yes | Yes | No | No | 
| incidents | Yes | Yes | Yes | No | No | 
| on\_call\_schedules | No | Yes | Yes | No | No | 
| priorities | No | Yes | Yes | No | No | 
| retrospectives | No | Yes | Yes | No | No | 
| runbooks | No | Yes | Yes | No | No | 
| services | No | Yes | Yes | No | No | 
| severities | No | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| users | No | Yes | Yes | No | No | 

**Example – Reading from a FireHydrant entity**  
The following example reads from the `alerts` entity. Replace {{connectionName}} with the name of your FireHydrant connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="firehydrant",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "alerts"
    }
)
```