

# Reading from Weaviate entities

**Prerequisites**

A Weaviate object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| classes | No | Yes | Yes | No | No | 
| objects | Yes | Yes | Yes | No | No | 

The `objects` entity is scoped to a collection. To read the objects in a collection, set `ENTITY_NAME` to `objects/{{CollectionName}}`, for example `objects/Article`. The connector discovers the collections in your cluster. Use the `class` column of the `classes` entity for the collection name. The name is case sensitive.

**Example – Reading from a Weaviate entity**  
The following example reads from the `classes` entity. Replace {{connectionName}} with the name of your Weaviate connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="weaviate",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "classes"
    }
)
```