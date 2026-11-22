

# Reading from Webex entities

**Prerequisites**

A Webex object you want to read from. For the available entities, see the following supported entities table.

The `messages` entity belongs to a room, and `team-memberships` belongs to a team. Use `messages/{{roomId}}` or `team-memberships/{{teamId}}`. AWS Glue discovers the available room and team IDs for your connection. All other entities are top-level.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| memberships | Yes | Yes | Yes | No | No | 
| messages | Yes | Yes | Yes | No | No | 
| rooms | Yes | Yes | Yes | No | No | 
| team-memberships | No | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 

**Example – Reading from a Webex entity**  
The following example reads from the `memberships` entity. Replace {{connectionName}} with the name of your Webex connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="webex",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "memberships"
    }
)
```