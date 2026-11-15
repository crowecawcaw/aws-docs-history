

# Reading from Trello entities
<a name="trello-reading-from-entities"></a>

**Prerequisites**

A Trello object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| board-members | No | Yes | Yes | No | No | 
| boards | No | Yes | Yes | No | No | 
| boards-actions | No | Yes | Yes | No | No | 
| boards-checklists | No | Yes | Yes | No | No | 
| boards-customfields | No | Yes | Yes | No | No | 
| boards-memberships | No | Yes | Yes | No | No | 
| cards | No | Yes | Yes | No | No | 
| lists | No | Yes | Yes | No | No | 
| members-me-organizations | No | Yes | Yes | No | No | 
| organizations-actions | No | Yes | Yes | No | No | 
| organizations-members | No | Yes | Yes | No | No | 
| organizations-memberships | No | Yes | Yes | No | No | 

Most Trello entities are scoped to a parent board or Workspace. To read one of these entities, set `ENTITY_NAME` to the entity name, a forward slash (`/`), and the parent identifier, for example `cards/{{boardId}}`. The connector discovers the parent identifiers that your token can access. The following table lists the parent-scoped entities and where to find the parent identifier.


| Entities | Parent identifier | 
| --- | --- | 
| board-members, boards-actions, boards-checklists, boards-customfields, boards-memberships, cards, lists | Board ID. Use the id column of the boards entity. | 
| organizations-actions, organizations-members, organizations-memberships | Workspace ID. Use the id column of the members-me-organizations entity, which lists your Trello Workspaces. | 

**Example – Reading from a Trello entity**  
The following example reads the cards on one board. Replace {{connectionName}} with the name of your Trello connection and {{boardId}} with a board ID from the `boards` entity:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="trello",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "cards/{{boardId}}"
    }
)
```