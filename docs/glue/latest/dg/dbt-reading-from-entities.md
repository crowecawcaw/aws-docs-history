

# Reading from dbt Cloud entities

**Prerequisites**

A dbt Cloud object you want to read from. For the available entities, see the following supported entities table.

Every dbt Cloud entity belongs to a dbt Cloud account. Set `ENTITY_NAME` to the full entity path that AWS Glue returns when it lists the entities for your connection, for example `accounts-runs/{{accountId}}`.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| accounts-connections | No | Yes | Yes | No | No | 
| accounts-environments | No | Yes | Yes | No | No | 
| accounts-jobs | No | Yes | Yes | No | No | 
| accounts-projects | No | Yes | Yes | No | No | 
| accounts-repositories | No | Yes | Yes | No | No | 
| accounts-runs | No | Yes | Yes | No | No | 
| groups | Yes | Yes | Yes | No | No | 
| notifications | No | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 
| service-tokens | No | Yes | Yes | No | No | 
| users | No | Yes | Yes | No | No | 
| webhooks-subscriptions | No | Yes | Yes | No | No | 

**Example – Reading from a dbt Cloud entity**  
The following Python example reads from the `accounts-connections` entity. Replace {{connectionName}} with the name of your dbt Cloud connection and {{accountId}} with your dbt Cloud account ID:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="dbt",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "accounts-connections/{{accountId}}"
    }
)
```