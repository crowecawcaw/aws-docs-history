

# Reading from GetResponse entities
<a name="getresponse-reading-from-entities"></a>

**Prerequisites**

A GetResponse object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| autoresponders | Yes | Yes | Yes | No | No | 
| campaigns | Yes | Yes | Yes | No | No | 
| contacts | Yes | Yes | Yes | No | No | 
| custom\_fields | Yes | Yes | Yes | No | No | 
| landing\_pages | Yes | Yes | Yes | No | No | 
| newsletters | Yes | Yes | Yes | No | No | 
| shops | Yes | Yes | Yes | No | No | 
| tags | Yes | Yes | Yes | No | No | 
| webinars | Yes | Yes | Yes | No | No | 

**Example – Reading from a GetResponse entity**  
The following example reads from the `autoresponders` entity. Replace {{connectionName}} with the name of your GetResponse connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="getresponse",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "autoresponders"
    }
)
```