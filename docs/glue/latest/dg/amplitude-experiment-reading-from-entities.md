

# Reading from Amplitude Experiment entities
<a name="amplitude-experiment-reading-from-entities"></a>

**Prerequisites**

An Amplitude Experiment object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| deployments | No | Yes | Yes | No | No | 
| experiment-deployments | No | Yes | Yes | No | No | 
| experiment-variants | No | Yes | Yes | No | No | 
| experiment-versions | No | Yes | Yes | No | No | 
| experiments | No | Yes | Yes | No | No | 
| flag-deployments | No | Yes | Yes | No | No | 
| flag-variants | No | Yes | Yes | No | No | 
| flag-versions | No | Yes | Yes | No | No | 
| flags | No | Yes | Yes | No | No | 

**Example – Reading from an Amplitude Experiment entity**  
The following example reads from the `deployments` entity. Replace {{connectionName}} with the name of your Amplitude Experiment connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="amplitude-experiment",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "deployments"
    }
)
```