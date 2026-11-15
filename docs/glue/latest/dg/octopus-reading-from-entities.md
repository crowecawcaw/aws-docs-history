

# Reading from Octopus Deploy entities
<a name="octopus-reading-from-entities"></a>

**Prerequisites**

An Octopus Deploy object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| actiontemplates-categories | No | Yes | Yes | No | No | 
| artifacts | No | Yes | Yes | No | No | 
| channels | No | Yes | Yes | No | No | 
| communityactiontemplates | No | Yes | Yes | No | No | 
| deploymentprocesses | No | Yes | Yes | No | No | 
| deployments | No | Yes | Yes | No | No | 
| environments | No | Yes | Yes | No | No | 
| events | No | Yes | Yes | No | No | 
| events-agents | No | Yes | Yes | No | No | 
| events-categories | No | Yes | Yes | No | No | 
| events-documenttypes | No | Yes | Yes | No | No | 
| events-groups | No | Yes | Yes | No | No | 
| feeds | Yes | Yes | Yes | No | No | 
| interruptions | No | Yes | Yes | No | No | 
| libraryvariablesets | No | Yes | Yes | No | No | 
| lifecycles | No | Yes | Yes | No | No | 
| machinepolicies | No | Yes | Yes | No | No | 
| machines | No | Yes | Yes | No | No | 
| project-groups | Yes | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 
| projecttriggers | No | Yes | Yes | No | No | 
| releases | No | Yes | Yes | No | No | 
| runbookprocesses | No | Yes | Yes | No | No | 
| runbookruns | No | Yes | Yes | No | No | 
| runbooks | No | Yes | Yes | No | No | 
| runbooksnapshots | No | Yes | Yes | No | No | 
| spaces | Yes | Yes | Yes | No | No | 
| tagsets | No | Yes | Yes | No | No | 
| tasks | No | Yes | Yes | No | No | 
| tasks-tasktypes | No | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| tenants | No | Yes | Yes | No | No | 
| users | No | Yes | Yes | No | No | 
| worker-pools | No | Yes | Yes | No | No | 

**Space-scoped and project-scoped entities**  
Most Octopus Deploy entities belong to a space, and some belong to a project in a space. For these entities, include the space ID, and the project ID when required, in `ENTITY_NAME`, separated by `/`. AWS Glue discovers the available spaces and projects when you browse entities. The following table lists the `ENTITY_NAME` format for each scope.


| Scope | `ENTITY_NAME` format | Entities | 
| --- | --- | --- | 
| Instance | {{entity}} | actiontemplates-categories, communityactiontemplates, events, events-agents, events-categories, events-documenttypes, events-groups, spaces, tasks-tasktypes, teams, users | 
| Space | {{entity}}/{{spaceId}}, for example deployments/Spaces-1 | artifacts, channels, deploymentprocesses, deployments, environments, feeds, interruptions, libraryvariablesets, lifecycles, machinepolicies, machines, project-groups, projects, releases, tagsets, tasks, tenants, worker-pools | 
| Project | {{entity}}/{{spaceId}}/{{projectId}}, for example runbooks/Spaces-1/Projects-1 | projecttriggers, runbookprocesses, runbookruns, runbooks, runbooksnapshots | 

**Example – Reading from an Octopus Deploy entity**  
The following example reads from the `actiontemplates-categories` entity. Replace {{connectionName}} with the name of your Octopus Deploy connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="octopus",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "actiontemplates-categories"
    }
)
```