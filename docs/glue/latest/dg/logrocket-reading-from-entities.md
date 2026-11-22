

# Reading from LogRocket entities

**Prerequisites**

A LogRocket object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| logs | No | Yes | Yes | No | No | 

**Example – Reading from a LogRocket entity**  
The following example reads from the `logs` entity. Replace {{connectionName}} with the name of your LogRocket connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="logrocket",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "logs"
    }
)
```