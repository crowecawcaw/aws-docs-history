

# Reading from Teamwork entities

**Prerequisites**

A Teamwork object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| companies | No | No | Yes | No | No | 
| milestones | No | No | Yes | No | No | 
| people | No | No | Yes | No | No | 
| projects | No | No | Yes | No | No | 
| tags | No | No | Yes | No | No | 
| tasklists | No | No | Yes | No | No | 
| tasks | No | No | Yes | No | No | 
| time | No | No | Yes | No | No | 

**Example – Reading from a Teamwork entity**  
The following example reads from the `companies` entity. Replace {{connectionName}} with the name of your Teamwork connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="teamwork",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "companies"
    }
)
```