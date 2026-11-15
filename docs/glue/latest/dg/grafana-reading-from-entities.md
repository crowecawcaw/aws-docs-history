

# Reading from Grafana entities
<a name="grafana-reading-from-entities"></a>

**Prerequisites**

A Grafana object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| access-control-roles | No | Yes | Yes | No | No | 
| annotations | No | Yes | Yes | No | No | 
| dashboard-snapshots | No | Yes | Yes | No | No | 
| dashboards | Yes | Yes | Yes | No | No | 
| dashboards-tags | No | Yes | Yes | No | No | 
| datasources | No | Yes | Yes | No | No | 
| folders | No | Yes | Yes | No | No | 
| org-users | No | Yes | Yes | No | No | 
| playlists | No | Yes | Yes | No | No | 
| provisioning-alert-rules | No | Yes | Yes | No | No | 
| provisioning-contact-points | Yes | Yes | Yes | No | No | 
| provisioning-mute-timings | No | Yes | Yes | No | No | 
| provisioning-notification-templates | No | Yes | Yes | No | No | 
| team-members | No | Yes | Yes | No | No | 
| teams-search | No | Yes | Yes | No | No | 

The `team-members` entity is scoped to a parent team. To read it, set `ENTITY_NAME` to `team-members/{{teamId}}`, for example `team-members/1`. You can also use the `id` column of the `teams-search` entity.

**Example – Reading from a Grafana entity**  
The following example reads from the `access-control-roles` entity. Replace {{connectionName}} with the name of your Grafana connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="grafana",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "access-control-roles"
    }
)
```