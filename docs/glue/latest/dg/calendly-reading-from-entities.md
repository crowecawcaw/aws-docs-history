

# Reading from Calendly entities
<a name="calendly-reading-from-entities"></a>

**Prerequisites**

A Calendly object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| event\_types | No | Yes | Yes | No | No | 
| groups | No | Yes | Yes | No | No | 
| organization\_memberships | No | Yes | Yes | No | No | 
| routing\_forms | No | Yes | Yes | No | No | 
| scheduled\_events | Yes | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| user\_availability\_schedules | No | Yes | Yes | No | No | 
| webhook\_subscriptions | No | Yes | Yes | No | No | 

**Example – Reading from a Calendly entity**  
The following example reads from the `event_types` entity. Replace {{connectionName}} with the name of your Calendly connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="calendly",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "event_types"
    }
)
```