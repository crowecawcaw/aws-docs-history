

# Reading from Coalesce entities

**Prerequisites**

A Coalesce object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| environmentNodes | No | Yes | Yes | No | No | 
| environments | Yes | Yes | Yes | No | No | 
| gitAccounts | No | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 
| runResults | No | Yes | Yes | No | No | 
| runs | Yes | Yes | Yes | No | No | 
| userRoles | No | Yes | Yes | No | No | 
| users | No | Yes | Yes | No | No | 
| workspaceNodes | No | Yes | Yes | No | No | 

**Example – Reading from a Coalesce entity**  
The following example reads from the `environmentNodes` entity. Replace {{connectionName}} with the name of your Coalesce connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="coalesce",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "environmentNodes"
    }
)
```