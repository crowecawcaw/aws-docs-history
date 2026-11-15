

# Reading from Todoist entities
<a name="todoist-reading-from-entities"></a>

**Prerequisites**

A Todoist object you want to read from. For the available entities, see the following supported entities table.

Some entities require a parent identifier in `ENTITY_NAME`. Use `collaborators/{{projectId}}`, `comments/{{taskId}}`, `folders/{{workspaceId}}`, or `workspace_invitations/{{workspaceId}}`. AWS Glue discovers the available project, task, and workspace IDs for your connection.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| activities | No | Yes | Yes | No | No | 
| archived\_projects | No | Yes | Yes | No | No | 
| collaborators | No | Yes | Yes | No | No | 
| comments | No | Yes | Yes | No | No | 
| folders | No | Yes | Yes | No | No | 
| labels | No | Yes | Yes | No | No | 
| projects | Yes | Yes | Yes | No | No | 
| sections | Yes | Yes | Yes | No | No | 
| tasks | Yes | Yes | Yes | No | No | 
| workspace\_invitations | No | Yes | Yes | No | No | 
| workspaces | No | Yes | Yes | No | No | 

**Example – Reading from a Todoist entity**  
The following example reads from the `activities` entity. Replace {{connectionName}} with the name of your Todoist connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="todoist",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "activities"
    }
)
```