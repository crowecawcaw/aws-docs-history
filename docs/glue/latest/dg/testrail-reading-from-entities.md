

# Reading from TestRail entities
<a name="testrail-reading-from-entities"></a>

**Prerequisites**

A TestRail object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| cases | Yes | Yes | Yes | No | No | 
| milestones | No | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 
| runs | No | Yes | Yes | No | No | 

**Example – Reading from a TestRail entity**  
The following example reads from the `cases` entity. Replace {{connectionName}} with the name of your TestRail connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="testrail",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "cases"
    }
)
```