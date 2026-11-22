

# Reading from Vercel entities

**Prerequisites**

A Vercel object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| aliases | Yes | Yes | Yes | No | No | 
| deployments | Yes | Yes | Yes | No | No | 
| domains | Yes | Yes | Yes | No | No | 
| events | Yes | Yes | Yes | No | No | 
| global-config | No | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 
| projects-checks | Yes | Yes | Yes | No | No | 
| projects-domains | Yes | Yes | Yes | No | No | 
| projects-env | No | Yes | Yes | No | No | 
| teams | Yes | Yes | Yes | No | No | 
| teams-members | Yes | Yes | Yes | No | No | 

Some Vercel entities are scoped to a parent project or team. To read one of these entities, set `ENTITY_NAME` to the entity name, a forward slash (`/`), and the parent identifier, for example `projects-env/{{projectId}}`. The following table lists the parent-scoped entities and where to find the parent identifier.


| Entities | Parent identifier | 
| --- | --- | 
| projects-checks, projects-domains, projects-env | Project ID. Use the id column of the projects entity. | 
| teams-members | Team ID. Use the id column of the teams entity. | 

**Example – Reading from a Vercel entity**  
The following example reads from the `aliases` entity. Replace {{connectionName}} with the name of your Vercel connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="vercel",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "aliases"
    }
)
```