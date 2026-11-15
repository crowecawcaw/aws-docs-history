

# Reading from Postman entities
<a name="postman-reading-from-entities"></a>

**Prerequisites**

A Postman object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| api-operations | No | Yes | Yes | No | No | 
| collection-definitions | No | Yes | Yes | No | No | 
| collection-forks | No | Yes | Yes | No | No | 
| collection-pull-requests | No | Yes | Yes | No | No | 
| collection-user-roles | No | Yes | Yes | No | No | 
| collections | Yes | Yes | Yes | No | No | 
| mock-call-logs | Yes | Yes | Yes | No | No | 
| mock-server-details | No | Yes | Yes | No | No | 
| mock-server-responses | No | Yes | Yes | No | No | 
| mock-servers | Yes | Yes | Yes | No | No | 
| monitors | Yes | Yes | Yes | No | No | 
| specifications | No | Yes | Yes | No | No | 
| team-users | No | Yes | Yes | No | No | 
| workspace-roles | No | Yes | Yes | No | No | 
| workspaces | Yes | Yes | Yes | No | No | 

Some Postman entities are scoped to a parent collection, mock server, or workspace. To read one of these entities, set `ENTITY_NAME` to the entity name, a forward slash (`/`), and the parent identifier, for example `collection-forks/{{collectionUid}}`. The following table lists the parent-scoped entities and where to find the parent identifier.


| Entity | Parent | Parent identifier | 
| --- | --- | --- | 
| collection-definitions | Collection | The uid field of collections | 
| collection-forks | Collection | The uid field of collections | 
| collection-pull-requests | Collection | The uid field of collections | 
| collection-user-roles | Collection | The uid field of collections | 
| mock-call-logs | Mock server | The id field of mock-servers | 
| mock-server-details | Mock server | The id field of mock-servers | 
| mock-server-responses | Mock server | The id field of mock-servers | 
| specifications | Workspace | The id field of workspaces | 
| workspace-roles | Workspace | The id field of workspaces | 

**Example – Reading from a Postman entity**  
The following example reads from the `api-operations` entity. Replace {{connectionName}} with the name of your Postman connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="postman",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "api-operations"
    }
)
```