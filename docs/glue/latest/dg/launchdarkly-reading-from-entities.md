

# Reading from LaunchDarkly entities
<a name="launchdarkly-reading-from-entities"></a>

**Prerequisites**

A LaunchDarkly object you want to read from. See the supported entities table below for the available entities.

Some LaunchDarkly entities are scoped to a project or to an environment in a project. Use `feature_flags/{{projectKey}}`, `environments/{{projectKey}}`, `metrics/{{projectKey}}`, `metric_groups/{{projectKey}}`, or `context_kinds/{{projectKey}}` for project-scoped entities. Use `segments/{{projectKey}}/{{environmentKey}}` or `flag_statuses/{{projectKey}}/{{environmentKey}}` for environment-scoped entities. AWS Glue discovers the available project and environment keys for your connection.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| projects | No | Yes | Yes | No | No | 
| members | No | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| roles | No | Yes | Yes | No | No | 
| tokens | No | Yes | Yes | No | No | 
| destinations | No | No | Yes | No | No | 
| feature\_flags | No | Yes | Yes | No | No | 
| environments | No | Yes | Yes | No | No | 
| metrics | No | Yes | Yes | No | No | 
| segments | No | Yes | Yes | No | No | 
| webhooks | No | No | Yes | No | No | 
| code\_ref\_repositories | No | No | Yes | No | No | 
| metric\_groups | No | Yes | Yes | No | No | 
| context\_kinds | No | No | Yes | No | No | 
| flag\_statuses | No | No | Yes | No | No | 

**Example – Reading from a LaunchDarkly entity**  
The following example reads from the `projects` entity. Replace {{connectionName}} with the name of your LaunchDarkly connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="launchdarkly",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "projects"
    }
)
```