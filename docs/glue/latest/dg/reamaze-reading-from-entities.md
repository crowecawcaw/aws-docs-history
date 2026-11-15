

# Reading from Re:amaze entities
<a name="reamaze-reading-from-entities"></a>

**Prerequisites**

A Re:amaze object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| articles | No | No | Yes | No | No | 
| channels | No | No | Yes | No | No | 
| contacts | No | No | Yes | No | No | 
| conversations | No | No | Yes | No | No | 
| messages | No | No | Yes | No | No | 
| response\_templates | No | No | Yes | No | No | 
| satisfaction\_ratings | No | No | Yes | No | No | 
| staff | No | No | Yes | No | No | 

**Example – Reading from a Re:amaze entity**  
The following example reads from the `articles` entity. Replace {{connectionName}} with the name of your Re:amaze connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="reamaze",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "articles"
    }
)
```