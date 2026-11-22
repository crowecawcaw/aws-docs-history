

# Reading from Kameleoon entities

**Prerequisites**

A Kameleoon object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| accounts | No | Yes | Yes | No | No | 
| custom-datas | No | Yes | Yes | No | No | 
| experiments | No | Yes | Yes | No | No | 
| goals | Yes | Yes | Yes | No | No | 
| images | No | Yes | Yes | No | No | 
| key-moments | Yes | Yes | Yes | No | No | 
| key-pages | No | Yes | Yes | No | No | 
| referrers | No | Yes | Yes | No | No | 
| segments | Yes | Yes | Yes | No | No | 
| sites | Yes | Yes | Yes | No | No | 
| studio-recommender-blocks | Yes | Yes | Yes | No | No | 
| takeaways | No | Yes | Yes | No | No | 
| targeting-rules | No | Yes | Yes | No | No | 
| templates | No | Yes | Yes | No | No | 
| variations | No | Yes | Yes | No | No | 
| widget-studio | No | Yes | Yes | No | No | 
| widget-studio-templates | No | Yes | Yes | No | No | 

**Example – Reading from a Kameleoon entity**  
The following example reads from the `accounts` entity. Replace {{connectionName}} with the name of your Kameleoon connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="kameleoon",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "accounts"
    }
)
```