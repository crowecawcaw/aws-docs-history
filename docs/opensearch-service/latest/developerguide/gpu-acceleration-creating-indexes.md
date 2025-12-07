# Creating GPU-accelerated vector

indexes

After enabling GPU-acceleration on your domain or collection, create vector indexes that can take
advantage of GPU processing.

###### Note

When you create a domain with GPU-acceleration enabled, the `index.knn.remote_index_build.enabled` setting is `true` by default. You don't need to explicitly set this setting when creating indexes. For collections, you must explicitly specify a value for this setting.

Creating index with GPU-acceleration
The following example creates a vector index optimized for GPU processing.
This index stores 768-dimensional vectors (common for text embeddings).

```
PUT my-vector-index
{
  "settings": {
    "index.knn": true,
    "index.knn.remote_index_build.enabled": true
  },
  "mappings": {
    "properties": {
      "vector_field": {
        "type": "knn_vector",
        "dimension": 768
      },
      "text": {
        "type": "text"
      }
    }
  }
}
```

Key configuration elements:

- `"index.knn": true` - Enables k-nearest neighbor
  functionality
- `"index.knn.remote_index_build.enabled": true` -
  Enables GPU processing for this index. When the domain has GPU-acceleration enabled, not specifying this setting defaults to `true`. For collections, you must explicitly specify a value for this setting.
- `"dimension": 768` - Specifies vector size (adjust
  based on your embedding model)

Creating index without GPU-acceleration
The following example creates a vector index where GPU processing is
disabled. This index stores 768-dimensional vectors (common for text
embeddings).

```
PUT my-vector-index
{
  "settings": {
    "index.knn": true,
    "index.knn.remote_index_build.enabled": false
  },
  "mappings": {
    "properties": {
      "vector_field": {
        "type": "knn_vector",
        "dimension": 768
      },
      "text": {
        "type": "text"
      }
    }
  }
}
```
