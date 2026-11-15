

# Reading from Vonage entities
<a name="vonage-reading-from-entities"></a>

**Prerequisites**

A Vonage object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| api\_secrets | No | Yes | Yes | No | No | 
| balance\_transfers | No | Yes | Yes | No | No | 
| subaccounts | No | Yes | Yes | No | No | 

**Example – Reading from a Vonage entity**  
The following example reads from the `api_secrets` entity. Replace {{connectionName}} with the name of your Vonage connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="vonage",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "api_secrets"
    }
)
```