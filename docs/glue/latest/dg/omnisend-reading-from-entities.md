

# Reading from Omnisend entities
<a name="omnisend-reading-from-entities"></a>

**Prerequisites**

An Omnisend object you want to read from. See the supported entities table below for the available entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| automations | No | Yes | Yes | No | No | 
| batches | No | Yes | Yes | No | No | 
| campaigns | Yes | Yes | Yes | No | No | 
| contacts | No | Yes | Yes | No | No | 
| product-categories | No | Yes | Yes | No | No | 
| products | No | Yes | Yes | No | No | 
| segments | No | Yes | Yes | No | No | 

**Example – Reading from an Omnisend entity**  
The following example reads from the `automations` entity. Replace {{connectionName}} with the name of your Omnisend connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="omnisend",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "automations"
    }
)
```