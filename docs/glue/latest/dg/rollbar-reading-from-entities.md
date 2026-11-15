

# Reading from Rollbar entities
<a name="rollbar-reading-from-entities"></a>

**Prerequisites**

A Rollbar object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| deploys | No | Yes | Yes | No | No | 
| environments | No | Yes | Yes | No | No | 
| items | Yes | Yes | Yes | No | No | 
| occurrences | No | Yes | Yes | No | No | 

**Example – Reading from a Rollbar entity**  
The following example reads from the `deploys` entity. Replace {{connectionName}} with the name of your Rollbar connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="rollbar",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "deploys"
    }
)
```