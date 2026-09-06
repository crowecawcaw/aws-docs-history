

# Vector indexes
<a name="indexes-vector"></a>

Vector indexes are a specialized type of index designed to efficiently query and manage vector data stored within a collection of documents. Amazon DocumentDB supports Hierarchical Navigable Small World (HNSW) and Inverted File with Flat Compression (IVFFlat) indexes.

For more information, see [Vector search for Amazon DocumentDB](vector-search.md).

Vector indexes are beneficial for machine learning and generative AI use cases, such as:
+ semantic search
+ product recommendation
+ personalization
+ chatbots
+ fraud detection
+ anomaly detection

## Supported index properties
<a name="indexes-vector-properties"></a>


| Option | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster | 
| --- | --- | --- | --- | --- | --- | 
| [name](index-property-name.md) | No | No | Yes | Yes | No | 

## Creating a vector index
<a name="indexes-vector-creating"></a>

Use the createIndex command with the `runCommand()` method to create a vector index. The syntax is:

```
db.runCommand({
  "createIndexes": "<collection>", 
  "indexes": [{
    "key": {
      "<field>": "vector"
    },
    "name": "<name>",
    "vectorOptions": {
      "type": "<hnsw> | <ivfflat>",
      "dimensions": <number of dimensions>,
      "similarity": "<euclidean>|<cosine>|<dotProduct>",
      "lists": <number_of_lists> [applicable for IVFFlat],
      "m": <max number of connections> [applicable for HNSW],
      "efConstruction": <size of the dynamic list for index build> [applicable for HNSW]
    }
  }] 
})
```

The key parameter is a JSON document that specifies the field and vector index type:

```
{
  "<field>": "vector"
}
```

See [Index properties](index-properties.md) for examples of creating vector indexes.