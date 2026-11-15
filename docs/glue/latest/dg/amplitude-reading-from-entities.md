

# Reading from Amplitude entities
<a name="amplitude-reading-from-entities"></a>

**Prerequisites**

An Amplitude object you want to read from. See the supported entities table below for the available entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| cohorts | No | No | Yes | No | No | 
| event-types | No | No | Yes | No | No | 
| event-categories | No | No | Yes | No | No | 
| user-properties | No | No | Yes | No | No | 
| event-properties | No | No | Yes | No | No | 
| events-list | No | No | Yes | No | No | 

**Example – Reading from an Amplitude entity**  
The following example reads from the `cohorts` entity. Replace {{connectionName}} with the name of your Amplitude connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="amplitude",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "cohorts"
    }
)
```