

# Reading from Apollo entities
<a name="apollo-reading-from-entities"></a>

**Prerequisites**

An Apollo object you want to read from. See the supported entities table below for the available entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| people | Yes | No | Yes | No | No | 
| organizations | Yes | No | Yes | No | No | 
| contacts | No | No | Yes | No | No | 
| accounts | No | No | Yes | No | No | 
| opportunities | No | No | Yes | No | No | 
| job\_postings | No | No | Yes | No | No | 
| contact\_opportunities | No | No | Yes | No | No | 
| tasks | No | No | Yes | No | No | 
| sequences | No | No | Yes | No | No | 
| users | No | No | Yes | No | No | 
| email\_accounts | No | No | Yes | No | No | 

**Example – Reading from an Apollo entity**  
The following example reads from the `people` entity. Replace {{connectionName}} with the name of your Apollo connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="apollo",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "people", "API_VERSION": "v1"
    }
)
```