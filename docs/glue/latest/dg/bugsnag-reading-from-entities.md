

# Reading from BugSnag entities

**Prerequisites**

A BugSnag object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| errors | No | Yes | Yes | No | No | 
| organizations | No | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 

**Example – Reading from a BugSnag entity**  
The following example reads from the `errors` entity. Replace {{connectionName}} with the name of your BugSnag connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="bugsnag",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "errors"
    }
)
```