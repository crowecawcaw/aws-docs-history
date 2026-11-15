

# Reading from Insightly entities
<a name="insightly-reading-from-entities"></a>

**Prerequisites**

An Insightly object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Contacts | Yes | Yes | Yes | No | No | 
| Countries | No | No | Yes | No | No | 
| Currencies | No | No | Yes | No | No | 
| Emails | No | Yes | Yes | No | No | 
| Events | Yes | Yes | Yes | No | No | 
| LeadSources | No | No | Yes | No | No | 
| LeadStatuses | No | No | Yes | No | No | 
| Milestones | Yes | Yes | Yes | No | No | 
| Notes | Yes | Yes | Yes | No | No | 
| PipelineStages | No | No | Yes | No | No | 
| Pipelines | No | No | Yes | No | No | 
| Relationships | No | No | Yes | No | No | 
| Tasks | Yes | Yes | Yes | No | No | 
| Users | No | Yes | Yes | No | No | 

**Example – Reading from an Insightly entity**  
The following example reads from the `Contacts` entity. Replace {{connectionName}} with the name of your Insightly connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="insightly",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "Contacts"
    }
)
```