

# Reading from Fivetran entities

**Prerequisites**

A Fivetran object you want to read from. For the available entities, see the following supported entities table.

The `group-users` entity belongs to a group. The `team-groups` and `team-users` entities belong to a team. For a nested entity, set `ENTITY_NAME` to the full entity path that AWS Glue returns when it lists the entities for your connection, for example `group-users/{{groupId}}`. All other entities are top-level entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| connections | Yes | Yes | Yes | No | No | 
| connector-types | No | Yes | Yes | No | No | 
| destinations | No | Yes | Yes | No | No | 
| group-users | Yes | Yes | Yes | No | No | 
| groups | No | Yes | Yes | No | No | 
| roles | No | Yes | Yes | No | No | 
| team-groups | No | Yes | Yes | No | No | 
| team-users | Yes | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| transformation-projects | No | Yes | Yes | No | No | 
| transformations | Yes | Yes | Yes | No | No | 
| users | Yes | Yes | Yes | No | No | 

**Example – Reading from a Fivetran entity**  
The following example reads from the `connections` entity. Replace {{connectionName}} with the name of your Fivetran connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="fivetran",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "connections"
    }
)
```