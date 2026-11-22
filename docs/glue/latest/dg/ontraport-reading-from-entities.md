

# Reading from Ontraport entities

**Prerequisites**

An Ontraport object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Contacts | No | Yes | Yes | No | No | 
| Products | No | Yes | Yes | No | No | 

**Example – Reading from an Ontraport entity**  
The following example reads from the `Contacts` entity. Replace {{connectionName}} with the name of your Ontraport connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="ontraport",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "Contacts"
    }
)
```