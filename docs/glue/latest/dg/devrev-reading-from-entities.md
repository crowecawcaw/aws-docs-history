

# Reading from DevRev entities
<a name="devrev-reading-from-entities"></a>

**Prerequisites**

A DevRev object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| commands | Yes | Yes | Yes | No | No | 
| conversations | Yes | Yes | Yes | No | No | 
| dev-users | Yes | Yes | Yes | No | No | 
| groups | Yes | Yes | Yes | No | No | 
| metric-definitions | Yes | Yes | Yes | No | No | 
| parts | Yes | Yes | Yes | No | No | 
| rev-orgs | Yes | Yes | Yes | No | No | 
| stock-schema-fragments | Yes | Yes | Yes | No | No | 
| vistas | Yes | Yes | Yes | No | No | 
| works | Yes | Yes | Yes | No | No | 

**Example – Reading from a DevRev entity**  
The following example reads from the `commands` entity. Replace {{connectionName}} with the name of your DevRev connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="devrev",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "commands"
    }
)
```