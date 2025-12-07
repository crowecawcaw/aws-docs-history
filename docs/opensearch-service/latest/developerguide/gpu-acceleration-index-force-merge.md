# Indexing vector data and

force-merging

Once you've created a GPU-accelerated vector index on your domain or collection, you can add
vector data and optimize your index using standard OpenSearch operations. GPU-acceleration automatically
enhances both indexing performance and force-merge operations, making it faster to build and
maintain large-scale vector search applications without requiring changes to your existing
workflows.

## Indexing vector data

Index vector data as you normally would. The GPU-acceleration automatically applies to
indexing and force-merge operations. The following example demonstrates how to add
vector documents to your index using the [bulk](https://docs.opensearch.org/latest/api-reference/document-apis/bulk/#index "https://docs.opensearch.org/latest/api-reference/document-apis/bulk/#index") API. Each document contains a vector field with numerical values
and associated text content:

```
POST _bulk
{"index": {"_index": "my-vector-index"}}
{"vector_field": [0.1, 0.2, 0.3, ...], "text": "Sample document 1"}
{"index": {"_index": "my-vector-index"}}
{"vector_field": [0.4, 0.5, 0.6, ...], "text": "Sample document 2"}
```

### Force-merge operations

GPU-acceleration also applies to [force-merge](https://docs.opensearch.org/latest/api-reference/index-apis/force-merge/ "https://docs.opensearch.org/latest/api-reference/index-apis/force-merge/") operations, which can significantly reduce the time
required to optimize vector indexes. Note that force-merge operations aren't supported on collections. The following example demonstrates how to
optimize your vector index by consolidating all segments into a single
segment:

```
POST my-vector-index/_forcemerge?max_num_segments=1
```
