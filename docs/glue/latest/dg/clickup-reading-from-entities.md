

# Reading from ClickUp entities

**Prerequisites**

A ClickUp object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| groups | No | Yes | Yes | No | No | 
| space-folder | No | Yes | Yes | No | No | 
| space-tag | No | Yes | Yes | No | No | 
| team-custom\_item | No | Yes | Yes | No | No | 
| team-customroles | No | Yes | Yes | No | No | 
| team-goal | No | Yes | Yes | No | No | 
| team-space | No | Yes | Yes | No | No | 
| team-time\_entries | Yes | Yes | Yes | No | No | 
| team-view | No | Yes | Yes | No | No | 
| workspaces | No | Yes | Yes | No | No | 

**Example – Reading from a ClickUp entity**  
The following Python example reads the `groups` entity of one workspace. Replace {{connectionName}} with the name of your ClickUp connection and {{teamId}} with the workspace (team) ID:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="clickup",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "groups/{{teamId}}"
    }
)
```