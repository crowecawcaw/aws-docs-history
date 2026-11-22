

# Reading from Webflow entities

**Prerequisites**

A Webflow object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| asset\_folders | No | Yes | Yes | No | No | 
| assets | No | Yes | Yes | No | No | 
| collection\_items | Yes | Yes | Yes | No | No | 
| collections | No | No | Yes | No | No | 
| custom\_fonts | No | Yes | Yes | No | No | 
| pages | No | Yes | Yes | No | No | 
| sites | No | No | Yes | No | No | 
| webhooks | No | No | Yes | No | No | 

**Example – Reading from a Webflow entity**  
The following example reads from the `asset_folders` entity. Replace {{connectionName}} with the name of your Webflow connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="webflow",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "asset_folders"
    }
)
```