

# Reading from Bitbucket entities

**Prerequisites**

A Bitbucket object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| branches | No | Yes | Yes | No | No | 
| commits | No | Yes | Yes | No | No | 
| default-reviewers | No | Yes | Yes | No | No | 
| deployments | No | Yes | Yes | No | No | 
| environments | No | Yes | Yes | No | No | 
| members | No | Yes | Yes | No | No | 
| pipelines | No | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 
| pull-request-activity | No | Yes | Yes | No | No | 
| pull-requests | Yes | Yes | Yes | No | No | 
| repositories | Yes | Yes | Yes | No | No | 
| tags | No | Yes | Yes | No | No | 
| user-workspaces | No | Yes | Yes | No | No | 
| watchers | No | Yes | Yes | No | No | 
| workspace-permissions | No | Yes | Yes | No | No | 

**Example – Reading from a Bitbucket entity**  
The following Python example reads the `branches` entity of one repository. Replace {{connectionName}} with the name of your Bitbucket connection, {{workspace}} with the workspace slug, and {{repoSlug}} with the repository slug:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="bitbucket",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "branches/{{workspace}}/{{repoSlug}}"
    }
)
```