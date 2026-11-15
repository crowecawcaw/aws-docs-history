

# Reading from Sentry entities
<a name="sentry-reading-from-entities"></a>

**Prerequisites**

A Sentry object you want to read from. For the available entities, see the following supported entities table.

The `organizations` entity is a top-level entity. All other Sentry entities belong to an organization. For these entities, set `ENTITY_NAME` to the full entity path that AWS Glue returns when it lists the entities for your connection, for example `projects/{{organizationSlug}}`.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| organizations | No | Yes | Yes | No | No | 
| organizations-dashboards | Yes | Yes | Yes | No | No | 
| organizations-detectors | Yes | Yes | Yes | No | No | 
| organizations-environments | Yes | Yes | Yes | No | No | 
| organizations-issues | Yes | Yes | Yes | No | No | 
| organizations-members | Yes | Yes | Yes | No | No | 
| organizations-monitors | Yes | Yes | Yes | No | No | 
| organizations-releases | Yes | Yes | Yes | No | No | 
| organizations-tags | Yes | Yes | Yes | No | No | 
| organizations-workflows | No | Yes | Yes | No | No | 
| projects | Yes | Yes | Yes | No | No | 
| teams | Yes | Yes | Yes | No | No | 

**Example – Reading from a Sentry entity**  
The following example reads from the `organizations` entity. Replace {{connectionName}} with the name of your Sentry connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="sentry",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "organizations"
    }
)
```