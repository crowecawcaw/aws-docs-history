

# Reading from Statuspage entities
<a name="statuspage-reading-from-entities"></a>

**Prerequisites**

A Statuspage object you want to read from. For the available entities, see the following supported entities table.

The `pages` entity is a top-level entity. All other Statuspage entities belong to a status page. For these entities, set `ENTITY_NAME` to the full entity path that AWS Glue returns when it lists the entities for your connection, for example `incidents/{{pageId}}`.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| component-groups | No | Yes | Yes | No | No | 
| components | No | Yes | Yes | No | No | 
| incident-templates | No | Yes | Yes | No | No | 
| incidents | No | Yes | Yes | No | No | 
| metrics | No | Yes | Yes | No | No | 
| metrics-providers | No | Yes | Yes | No | No | 
| pages | No | Yes | Yes | No | No | 

**Example – Reading from a Statuspage entity**  
The following example reads from the `pages` entity. Replace {{connectionName}} with the name of your Statuspage connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="statuspage",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "pages"
    }
)
```