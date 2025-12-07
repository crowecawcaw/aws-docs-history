# Advanced search

capabilities with an Amazon S3 vector engine

Amazon OpenSearch Service offers the ability to use Amazon S3 as a vector engine for vector indexes.
This feature allows you to offload vector data to Amazon S3 while maintaining sub-second
vector search capabilities at low cost.

With this feature, OpenSearch stores vector embeddings in an Amazon S3 vector index
while keeping other document fields in the OpenSearch cluster's storage. This
architecture offers the following benefits:

- **Durability**: Data written to S3 Vectors is
  stored on S3, which is designed for 11 9s of data durability.
- **Scalability**: Offload large vector
  datasets to S3 without consuming cluster storage.
- **Cost-effectiveness**: Optimize storage
  costs for vector-heavy workloads.
  OpenSearch has the following requirements for using S3 vector indexes:

- OpenSearch version 2.19 or later
- OpenSearch Optimized instances
- Latest patch version for your OpenSearch release

## Enabling S3

Vectors

When [creating a new domain](createupdatedomains.md "createupdatedomains.md") or updating an existing domain, you can
choose the **Enable S3 Vectors as an engine option** in the
**Advanced features** section. This setting allows
OpenSearch to create an S3 vector bucket when you leverage S3 Vectors as your
engine. When you enable this option, OpenSearch configures S3 Vectors for your
domain by:

1. Creating two new grants on the AWS KMS key configured with your
   domain:
   - A grant for the S3 Vectors background indexing jobs with
     decrypt privileges
   - A grant for OpenSearch to create S3 vectors buckets with
     `GenerateDataKey` permissions

2. Configuring the KMS key used by your OpenSearch domain as the CMK for
   encryption at rest of all vector index data.

## Creating indexes with S3 vector engine

After you configure a domain, you can create one or more k-NN indexes with
fields using `s3vector` as the backend vector engine in the index
mappings. You can configure different vector fields with different engine types
based on your use case.

###### Important

You can only use the `s3vector` engine in mapping a field
definition during index creation. You can't add or update the mapping with
`s3vector` engine after index creation.

Here are some examples that create S3 vector engine indexes.

**Example: Creating a k-NN index with S3 vector
engine**

```
PUT my-first-s3vector-index
{
  "settings": {
    "index": {
      "knn": true
    }
  },
  "mappings": {
    "properties": {
        "my_vector_1": {
          "type": "knn_vector",
          "dimension": 2,
          "space_type": "l2",
          "method": {
            "engine": "s3vector"
          }
        },
        "price": {
          "type": "float"
        }
    }
  }
}
```

**Example: Creating a k-NN index with both S3 vector and FAISS
engines**

This example highlights the fact you can use multiple vector engines within the
same index.

```
PUT my-vector-index
{
  "settings": {
    "index": {
      "knn": true
    }
  },
  "mappings": {
    "properties": {
        "my_vector_1": {
          "type": "knn_vector",
          "dimension": 2,
          "space_type": "l2",
          "method": {
            "engine": "s3vector"
          }
        },
        "price": {
          "type": "float"
        },
        "my_vector_2": {
            "type": "knn_vector",
            "dimension": 2,
            "space_type": "cosine",
            "method": {
                "name": "hnsw",
                "engine": "faiss",
                "parameters": {
                    "ef_construction": 128,
                    "m": 24
                }
            }
        }
    }
  }
}
```

**Unsupported example: Adding S3 vector engine after index
creation**

The following approach is not supported and will fail.

```
PUT my-first-s3vector-index
{
  "settings": {
    "index": {
      "knn": true
    }
  }
}

PUT my-first-s3vector-index/_mapping
{
  "properties": {
        "my_vector_1": {
          "type": "knn_vector",
          "dimension": 2,
          "space_type": "l2",
          "method": {
            "engine": "s3vector"
          }
        },
        "price": {
          "type": "float"
        }
    }
}
```

## Functional limitations

Consider the following limitations before using `s3vector` engine
in an index:

| Features and behaviors not supported with s3vector engine | Feature                                                                                                                                                                                                                                                                                                                                                                                                 | Behavior |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Split/Shrink/Clone index                                  | These APIs fail when used with an index configured with<br>`s3vector` engine in `knn_vector`<br>field.                                                                                                                                                                                                                                                                                                  |
| Snapshots                                                 | Indices using `s3vector` engine don't support<br>snapshots. For managed domains:<br>• Automated snapshots only include indices not using<br>`s3vector` engine.<br>• Manual snapshot requests for `s3vector`<br>indices fail.<br>NoteWhile snapshots aren't supported for point-in-time<br>recovery, `s3vector` engine, along with<br>OpenSearch Optimized instances, provide 11 nines of<br>durability. |
| UltraWarm tier                                            | Indices configured with `s3vector` engine<br>can't migrate to UltraWarm tier.                                                                                                                                                                                                                                                                                                                           |
| Cross-cluster replication                                 | Indices configured with `s3vector` engine<br>don't support cross-cluster replication.                                                                                                                                                                                                                                                                                                                   |
| Accidental delete protection                              | Because snapshots aren't supported for indices using<br>`s3vector` engine, accidental delete<br>protection isn't available. You can still restore other<br>indices in the domain.                                                                                                                                                                                                                       |
| Radial search                                             | Queries with radial search aren't supported on fields<br>using `s3vector` engine.                                                                                                                                                                                                                                                                                                                       |

## Indexing documents

After creating an index with S3 vector engine, you can ingest documents using
the standard `_bulk` API. OpenSearch automatically offloads vector
data of `knn_vector` fields using the `s3vector` engine to
the S3 vector index in real time. Data belonging to other fields or
`knn_vector` fields using different engines will be persisted by
OpenSearch in its own storage layer.

For all bulk requests that are acknowledged, OpenSearch guarantees that all
data (vector and non-vector) is durable. If a request receives a negative
acknowledgment, there are no guarantees on the durability of the documents in
that bulk request. You should retry such requests preferably after deleting the previous failed request using the document id to avoid duplicate documents in these rare cases.

**Example bulk indexing**

```
POST _bulk
{ "index": { "_index": "my-first-s3vector-index", "_id": "1" } }
{ "my_vector_1": [1.5, 2.5], "price": 12.2 }
{ "index": { "_index": "my-first-s3vector-index", "_id": "2" } }
{ "my_vector_1": [2.5, 3.5], "price": 7.1 }
{ "index": { "_index": "my-first-s3vector-index", "_id": "3" } }
{ "my_vector_1": [3.5, 4.5], "price": 12.9 }
{ "index": { "_index": "my-first-s3vector-index", "_id": "4" } }
{ "my_vector_1": [5.5, 6.5], "price": 1.2 }
{ "index": { "_index": "my-first-s3vector-index", "_id": "5" } }
{ "my_vector_1": [4.5, 5.5], "price": 3.7 }
```

## Searching documents

You can search your index using the standard `_search` API to
execute text, k-NN, or hybrid queries. For queries on `knn_vector`
fields configured with `s3vector` engine, OpenSearch automatically
offloads the query to the corresponding S3 vectors index.

###### Note

With `s3vector` engine, k-NN search queries support a maximum `k` value of 100. This means a maxmium of 100 nearest neighbors can be returned in the search results.

**Example search query**

```
GET my-first-s3vector-index/_search
{
  "size": 2,
  "query": {
    "knn": {
      "my_vector_1": {
        "vector": [2.5, 3.5],
        "k": 2
      }
    }
  }
}
```

You can run filtered vector search on OpenSearch kNN index using s3vector engine. OpenSearch applies the filter as the post filter and uses oversampling mechanism based on certain heuristics to balance recall vs latency.

**Example search query with filter:**

```
GET my-index/_search
{
  "size": 10,
  "query": {
    "knn": {
      "my_vector_field": {
        "vector": [2.5, 3.5, 1.2, 4.8],
        "k": 10,
        "filter": {
          "range": {
            "price": {
              "gte": 10,
              "lte": 100
            }
          }
        }
      }
    }
  }
}
```

## Supported mapping parameters

With `s3vector` engine, the `knn_vector` field supports
the following parameters in the mappings.

| Vector field parameters | Parameter | Required                                                                                              | Description         | Supported values |
| ----------------------- | --------- | ----------------------------------------------------------------------------------------------------- | ------------------- | ---------------- |
| `type`                  | Yes       | The type of field present in the document.                                                            | `knn_vector`        |
| `dimension`             | Yes       | The dimension of each vector that will be ingested into the<br>index.                                 | >0, <=4096          |
| `space_type`            | No        | The vector space used to calculate the distance between<br>vectors.                                   | `l2`, `cosinesimil` |
| `method.engine`         | Yes       | The approximate k-NN engine to use for indexing and<br>search.                                        | `s3vector`          |
| `method.name`           | No        | The nearest neighbor method                                                                           | ""                  |
| `store`                 | N/A       | Enabling or disabling this mapping parameter is no-op as knn_vector data is not stored in OpenSearch. | Not Supported       |
| `doc_values`            | N/A       | Enabling or disabling this mapping parameter is no-op as knn_vector data is not stored in OpenSearch. | Not Supported       |

###### Important

Nested `knn_vector` field types are unsupported using
`s3vector` engine

## Metering and billing

For information about metering and billing for this feature, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").

## Disabling the

s3vector engine

Before you disable the `s3vector` engine, delete
_all_ indexes that are currently using it. If you don't,
any attempt to disable the engine fails.

Also note that enabling or disabling the `s3vector` engine triggers
a [blue/green deployment](managedomains-configuration-changes.md "managedomains-configuration-changes.md") on your domain.

To disable the `s3vector` engine, [edit your
domain configuration](../../../cli/latest/reference/opensearch/update-domain-config.md "../../../cli/latest/reference/opensearch/update-domain-config.md") and set `S3VectorsEngine.Enabled:
 false`.
