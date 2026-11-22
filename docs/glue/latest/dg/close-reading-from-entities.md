

# Reading from Close CRM entities

**Prerequisites**

A Close CRM object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| activity | Yes | Yes | Yes | No | No | 
| contact | No | Yes | Yes | No | No | 
| lead | No | Yes | Yes | No | No | 
| lead-status | No | Yes | Yes | No | No | 
| opportunity | Yes | Yes | Yes | No | No | 
| opportunity-status | No | Yes | Yes | No | No | 
| pipeline | No | Yes | Yes | No | No | 
| task | Yes | Yes | Yes | No | No | 
| user | No | Yes | Yes | No | No | 

**Example – Reading from a Close CRM entity**  
The following example reads from the `activity` entity. Replace {{connectionName}} with the name of your Close CRM connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="close",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "activity"
    }
)
```