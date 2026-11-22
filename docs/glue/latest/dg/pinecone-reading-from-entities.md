

# Reading from Pinecone entities

**Prerequisites**

A Pinecone object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| backups | No | Yes | Yes | No | No | 
| collections | No | Yes | Yes | No | No | 
| indexes | No | Yes | Yes | No | No | 

**Example – Reading from a Pinecone entity**  
The following example reads from the `backups` entity. Replace {{connectionName}} with the name of your Pinecone connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="pinecone",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "backups"
    }
)
```