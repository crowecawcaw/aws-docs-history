

# Reading from Adyen entities
<a name="adyen-reading-from-entities"></a>

**Prerequisites**

An Adyen object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| api\_credentials | No | Yes | Yes | No | No | 
| companies | No | Yes | Yes | No | No | 
| company\_merchants | No | Yes | Yes | No | No | 
| merchant\_stores | No | Yes | Yes | No | No | 
| merchants | No | Yes | Yes | No | No | 
| payment\_methods | No | Yes | Yes | No | No | 
| stores | No | Yes | Yes | No | No | 
| webhooks | No | Yes | Yes | No | No | 

**Example – Reading from an Adyen entity**  
The following example reads from the `api_credentials` entity. Replace {{connectionName}} with the name of your Adyen connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="adyen",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "api_credentials"
    }
)
```