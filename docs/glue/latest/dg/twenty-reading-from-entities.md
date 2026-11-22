

# Reading from Twenty CRM entities

**Prerequisites**

A Twenty CRM object you want to read from. Twenty CRM discovers the available objects and their fields from your workspace schema at runtime, so you supply the object name – for example `companies`, `people`, or `opportunities`, or one of your custom objects.

**Supported entities for source**

Twenty CRM discovers its objects and their fields from your workspace at runtime, so the connector exposes them as a single dynamic entity rather than a fixed list. You choose which object to read by setting `ENTITY_NAME`.


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Dynamic entity | No | Yes | Yes | No | No | 

**Dynamic entity and field discovery**  
The objects available to read come from your own Twenty CRM workspace, so the exact set depends on your instance and can change over time. The connector discovers them (and their fields) at runtime, so you do not configure a fixed entity list. Objects you can read include Twenty CRM standard objects – for example `companies`, `people`, `opportunities`, `tasks`, and `notes` – and any custom objects you define in your workspace. Set `ENTITY_NAME` to the object you want to read. Because Twenty CRM does not support server-side filtering, operator support is not captured per data type.

**Example – Reading from a Twenty CRM entity**  
The following example reads from the `companies` object. Replace {{connectionName}} with the name of your Twenty CRM connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="twenty",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "companies"
    }
)
```