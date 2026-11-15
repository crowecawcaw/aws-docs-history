

# Reading from Coda entities
<a name="coda-reading-from-entities"></a>

**Prerequisites**

A Coda object you want to read from. For the available entities, see the following supported entities table.

The `docs`, `folders`, and `doc-analytics` entities are top-level entities. The `controls`, `doc-permissions`, `pages`, and `tables` entities belong to a doc. The `columns` and `rows` entities belong to a table in a doc. For a nested entity, set `ENTITY_NAME` to the full entity path that AWS Glue returns when it lists the entities for your connection, for example `rows/{{docId}}/{{tableId}}`.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| columns | No | Yes | Yes | No | No | 
| controls | No | Yes | Yes | No | No | 
| doc-analytics | Yes | Yes | Yes | No | No | 
| doc-permissions | No | Yes | Yes | No | No | 
| docs | Yes | Yes | Yes | No | No | 
| folders | Yes | Yes | Yes | No | No | 
| pages | No | Yes | Yes | No | No | 
| rows | Yes | Yes | Yes | No | No | 
| tables | Yes | Yes | Yes | No | No | 

**Example – Reading from a Coda entity**  
The following Python example reads from the `docs` entity. Replace {{connectionName}} with the name of your Coda connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="coda",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "docs"
    }
)
```