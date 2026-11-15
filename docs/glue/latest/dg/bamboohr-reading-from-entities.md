

# Reading from BambooHR entities
<a name="bamboohr-reading-from-entities"></a>

**Prerequisites**

A BambooHR object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| benefit\_plans | No | Yes | Yes | No | No | 
| employee\_compensation | No | Yes | Yes | No | No | 
| employee\_employmentstatus | No | Yes | Yes | No | No | 
| employee\_jobinfo | No | Yes | Yes | No | No | 
| employees-directory | No | Yes | Yes | No | No | 
| holidays | No | Yes | Yes | No | No | 
| list\_options | No | Yes | Yes | No | No | 
| meta-fields | No | Yes | Yes | No | No | 
| meta-lists | No | Yes | Yes | No | No | 
| meta-tables | No | Yes | Yes | No | No | 
| meta-users | No | Yes | Yes | No | No | 
| time-off-types | No | Yes | Yes | No | No | 
| whos-out | Yes | Yes | Yes | No | Yes | 

**Example – Reading from a BambooHR entity**  
The following example reads from the `benefit_plans` entity. Replace {{connectionName}} with the name of your BambooHR connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="bamboohr",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "benefit_plans"
    }
)
```