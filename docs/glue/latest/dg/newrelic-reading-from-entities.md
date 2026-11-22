

# Reading from New Relic entities

**Prerequisites**

A New Relic object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| alerts\_policies | Yes | Yes | Yes | No | No | 
| applications | Yes | Yes | Yes | No | No | 
| key\_transactions | No | Yes | Yes | No | No | 

**Example – Reading from a New Relic entity**  
The following example reads from the `alerts_policies` entity. Replace {{connectionName}} with the name of your New Relic connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="newrelic",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "alerts_policies"
    }
)
```