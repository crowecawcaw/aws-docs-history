

# Adding full-text searchable content to your vectors

You insert full-text searchable content by writing it as metadata associated with your vectors with the `PutVectors` API operation (using the AWS SDK or AWS CLI). Each vector includes a unique key, the vector values, and metadata as key-value pairs. Write the full-text searchable content as the value of a metadata field whose key matches a `textSearchConfigurations` entry on the index. S3 Vectors then indexes that field for full-text search automatically as the data is written: it breaks the text into tokens using the analyzer configured for that field (the standard analyzer by default, or the language analyzer you set), and makes those tokens searchable.

Before you write data, configure which fields are full-text searchable as described in [Configuring full-text search](s3-vectors-configuring-full-text-search.md). After you write your data, run queries as described in [Querying with full-text and vector search](s3-vectors-querying-full-text-and-vector-search.md). For an overview, see [Hybrid search with Amazon S3 Vectors](s3-vectors-hybrid-search.md).

Writes are strongly consistent, so a query reflects the most recently written data. To optimize cost and throughput, write vectors in large batches, up to the per-request maximum. For the maximum number of vectors and request size, see [Limitations and restrictions](s3-vectors-limitations.md).

## Write vectors with searchable text
<a name="s3-vectors-ingesting-full-text-data-write"></a>

The following examples write a document chunk for a Retrieval Augmented Generation (RAG) index: an embedding plus two metadata fields. The `title` field is both filterable and full-text searchable, so you can filter on it and run full-text search over it. The `passage_body` field holds the larger passage text and is full-text searchable only; because it was declared in `nonFilterableMetadataKeys` at index creation, it isn't filterable.

### Using the AWS CLI
<a name="s3-vectors-ingesting-full-text-data-write-cli"></a>

**Example: Write a vector with searchable text**

```bash
aws s3vectors put-vectors \
    --vector-bucket-name "{{amzn-s3-demo-vector-bucket}}" \
    --index-name "{{documents}}" \
    --vectors '[
        {
            "key": "doc-42-chunk-3",
            "data": { "float32": [0.013, -0.21, 0.04 ...] },
            "metadata": {
                "title": "Quarterly maintenance guide",
                "passage_body": "Reset the controller after error code E1234 ..."
            }
        }
    ]'
```

### Using the AWS SDKs
<a name="s3-vectors-ingesting-full-text-data-write-sdk"></a>

------
#### [ SDK for Python (Boto3) ]

```python
import boto3

client = boto3.client("s3vectors")

embedding = [0.013, -0.21, 0.04 ...]  # embedding from your model

client.put_vectors(
    vectorBucketName="my-vector-bucket",
    indexName="documents",
    vectors=[
        {
            "key": "doc-42-chunk-3",
            "data": {"float32": embedding},
            "metadata": {
                "title": "Quarterly maintenance guide",
                "passage_body": "Reset the controller after error code E1234 ...",
            },
        },
    ],
)
```

------

## Considerations
<a name="s3-vectors-ingesting-full-text-data-considerations"></a>
+ S3 Vectors indexes string and list of string values for full-text search. Any non-string value written to a full-text searchable field is stored (and can be retrieved) but is excluded from search.
+ A field can be both filterable and full-text searchable. Filterable values have a smaller maximum size than non-filterable, search-only fields, so for a large field that you only want to search, declare it in `nonFilterableMetadataKeys` when you create the index. For more information about non-filterable metadata, see [Non-filterable metadata](s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-non-filterable). For the field size limits, see [Limitations and restrictions](s3-vectors-limitations.md).
+ A word longer than the maximum token length of 255 bytes is excluded from the full-text index and from queries, although it remains stored and retrievable. For long identifiers, consider storing them as filterable metadata and use exact-match filters instead of full-text search.