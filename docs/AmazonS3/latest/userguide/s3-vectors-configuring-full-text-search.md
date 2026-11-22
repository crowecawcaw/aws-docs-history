

# Configuring full-text search

For an S3 vector index in your vector bucket, you can configure a metadata field as full-text searchable by adding its key to the `textSearchConfigurations` list in the index's metadata configuration. Amazon S3 Vectors then indexes the data in that field for BM25 (Best Matching 25) scoring, using a built-in text analyzer. BM25 is a ranking function that scores each record by how often your query terms appear in the searched field. It gives more weight to rarer terms and less to very common ones, so the records whose text best matches your terms rank highest. You can configure full-text search when you create an index, or add it to an existing index using the AWS SDK, AWS CLI, or the Amazon S3 console.

Configuring full-text search is the first step in setting up hybrid search. After you configure full-text search, write your data as described in [Adding full-text searchable content to your vectors](s3-vectors-ingesting-full-text-data.md), and run queries as described in [Querying with full-text and vector search](s3-vectors-querying-full-text-and-vector-search.md). For an overview, see [Hybrid search with Amazon S3 Vectors](s3-vectors-hybrid-search.md).

**Topics**
+ [Text analyzers](#s3-vectors-configuring-full-text-search-analyzers)
+ [Configure full-text search fields for a new index](#s3-vectors-configuring-full-text-search-new-index)
+ [Enable full-text search on an existing index](#s3-vectors-configuring-full-text-search-existing-index)
+ [Track backfill status](#s3-vectors-configuring-full-text-search-backfill-status)
+ [Considerations](#s3-vectors-configuring-full-text-search-considerations)
+ [Remove a full-text search configuration](#s3-vectors-configuring-full-text-search-remove)

## Text analyzers
<a name="s3-vectors-configuring-full-text-search-analyzers"></a>

A text analyzer breaks text into the terms (or tokens) that full-text search matches against for BM25 scoring. S3 Vectors applies the same analyzer as you write your data and your query text as you search.

S3 Vectors provides built-in, managed analyzers, so you don't build or run your own tokenization or analysis pipeline.
+ By default, S3 Vectors uses a standard analyzer. It splits text into terms at Unicode word boundaries, drops most punctuation, and lowercases, so `Fox` matches `fox`. It works across most languages with no configuration.
+ Optionally, set a language for a field to use a language-aware analyzer that applies language-specific normalization, which can provide higher quality results if you know the language of the text data upfront. In addition to the standard normalization, a language analyzer applies stemming (for example, the English analyzer reduces words to their root so that `running` also matches `run`), and removes common stopwords (the very frequent words such as `the` and `of`). Stemming can improve recall by matching different forms of the same word, and stopword removal focuses scoring on the meaningful terms, which can improve full-text relevance for content in that language.

S3 Vectors provides 10 built-in language analyzers, for English, French, Spanish, Portuguese, Italian, German, Dutch, Chinese, Japanese, and Korean.

## Configure full-text search fields for a new index
<a name="s3-vectors-configuring-full-text-search-new-index"></a>

You can create an index with full-text search fields using the AWS SDK, AWS CLI, or the Amazon S3 console. For more information about creating an index, see [Creating a vector index in a vector bucket](s3-vectors-create-index.md).

Add one entry per metadata key to `textSearchConfigurations`. By default, S3 Vectors uses the standard analyzer. To use a language-specific analyzer, optionally specify a language for the field. List any large, search-only fields in `nonFilterableMetadataKeys` if you don't need to filter on them. For more information about non-filterable metadata, see [Non-filterable metadata](s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-non-filterable). For details on the size and number of searchable fields, see [Limitations and restrictions](s3-vectors-limitations.md).

**Note**  
After the index is created, you can add new full-text search fields or remove full-text search fields, but you can't change an existing full-text search configuration (for example, its analyzer). For more information, see [Enable full-text search on an existing index](#s3-vectors-configuring-full-text-search-existing-index) and [Remove a full-text search configuration](#s3-vectors-configuring-full-text-search-remove).

**Note**  
You can't change the `nonFilterableMetadataKeys` list after the index is created.

The following examples create a vector index named `documents` in the `amzn-s3-demo-vector-bucket` vector bucket. In addition to the vector dimension and distance metric, you configure two full-text search fields: one with the default standard analyzer (`title`) and one with a language-specific analyzer (`passage_body`).

### Using the AWS CLI
<a name="s3-vectors-configuring-full-text-search-new-index-cli"></a>

**Example: Create an index with searchable fields**

```bash
aws s3vectors create-index \
    --vector-bucket-name "{{amzn-s3-demo-vector-bucket}}" \
    --index-name "{{documents}}" \
    --data-type "float32" \
    --dimension {{1024}} \
    --distance-metric "{{cosine}}" \
    --metadata-configuration '{
        "nonFilterableMetadataKeys": ["passage_body"],
        "textSearchConfigurations": [
            { "metadataKey": "title" },
            { "metadataKey": "passage_body", "language": "en" }
        ]
    }'
```

### Using the AWS SDKs
<a name="s3-vectors-configuring-full-text-search-new-index-sdk"></a>

------
#### [ SDK for Python (Boto3) ]

```python
import boto3

client = boto3.client("s3vectors")

client.create_index(
    vectorBucketName="amzn-s3-demo-vector-bucket",
    indexName="documents",
    dataType="float32",
    dimension=1024,
    distanceMetric="cosine",
    metadataConfiguration={
        "nonFilterableMetadataKeys": ["passage_body"],
        "textSearchConfigurations": [
            {"metadataKey": "title"},
            {"metadataKey": "passage_body", "language": "en"},
        ],
    },
)
```

------

## Enable full-text search on an existing index
<a name="s3-vectors-configuring-full-text-search-existing-index"></a>

If you already store the text you want to search as a metadata field, call `UpdateMetadataConfiguration` (using the AWS SDK, AWS CLI, or the Amazon S3 console) and add that key under `add.textSearchConfigurations`. This triggers a background backfill operation where S3 Vectors indexes your existing data in that field for BM25 scoring using the configured text analyzer. To add a new searchable field, call `UpdateMetadataConfiguration` the same way with the new key, then write the text with `PutVectors`.

**Note**  
Full-text search is supported only on `ENHANCED` indexes. If you have a `CLASSIC` index, upgrade it to an `ENHANCED` index with `UpdateIndexMode` (using the AWS SDK, AWS CLI, or the Amazon S3 console) before you enable full-text search. For more information, see [Changing a vector index's mode](s3-vectors-index-mode.md).

**Note**  
Once configured, you can't change an existing full-text search configuration for a field (for example, its analyzer). However, you can add new full-text search fields or remove full-text search fields using the `UpdateMetadataConfiguration` operation or the console.

### Using the AWS CLI
<a name="s3-vectors-configuring-full-text-search-existing-index-cli"></a>

**Example: Enable full-text search on existing fields**

```bash
aws s3vectors update-metadata-configuration \
    --vector-bucket-name "{{amzn-s3-demo-vector-bucket}}" \
    --index-name "{{documents}}" \
    --add '{
        "textSearchConfigurations": [
            { "metadataKey": "summary", "language": "en" },
            { "metadataKey": "passage_body", "language": "en" }
        ]
    }'
```

### Using the AWS SDKs
<a name="s3-vectors-configuring-full-text-search-existing-index-sdk"></a>

------
#### [ SDK for Python (Boto3) ]

```python
client.update_metadata_configuration(
    vectorBucketName="amzn-s3-demo-vector-bucket",
    indexName="documents",
    add={
        "textSearchConfigurations": [
            {"metadataKey": "summary", "language": "en"},
            {"metadataKey": "passage_body", "language": "en"},
        ],
    },
)
```

------

## Track backfill status
<a name="s3-vectors-configuring-full-text-search-backfill-status"></a>

When S3 Vectors is indexing existing data for full-text search, the field's status is `BUILDING` until the build finishes, then `ACTIVE`. The build can take from a few minutes to several hours, depending on how much data is in the field. Use the `GetIndex` API operation (using the AWS SDK, AWS CLI, or the Amazon S3 console) to track each field's status in `textSearchConfigurations`.
+ While a field is `BUILDING`, full-text or hybrid queries that target that field are rejected. The field becomes searchable when its status is `ACTIVE`.
+ You can continue to write vectors with `PutVectors` during the build. They are indexed for the field as they arrive.

### Using the AWS CLI
<a name="s3-vectors-configuring-full-text-search-backfill-status-cli"></a>

**Example: Read full-text configuration and status**

```bash
aws s3vectors get-index \
    --vector-bucket-name "{{amzn-s3-demo-vector-bucket}}" \
    --index-name "{{documents}}"
```

### Using the AWS SDKs
<a name="s3-vectors-configuring-full-text-search-backfill-status-sdk"></a>

------
#### [ SDK for Python (Boto3) ]

```python
response = client.get_index(
    vectorBucketName="amzn-s3-demo-vector-bucket",
    indexName="documents",
)

for field in response["index"]["metadataConfiguration"]["textSearchConfigurations"]:
    print(field["metadataKey"], field["status"])  # BUILDING or ACTIVE
```

------

## Considerations
<a name="s3-vectors-configuring-full-text-search-considerations"></a>
+ S3 Vectors indexes string and list of string values for full-text search. Any non-string value written to a full-text searchable field is stored (and can be retrieved) but is excluded from search.
+ A field can be both filterable and full-text searchable. Filterable values have a smaller maximum size than non-filterable and full-text searchable fields, so for a large field that you only want to perform full-text search on, declare it in `nonFilterableMetadataKeys` when you create the index. For more information about non-filterable metadata, see [Non-filterable metadata](s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-non-filterable). For the field size limits, see [Limitations and restrictions](s3-vectors-limitations.md).
+ If you know which fields need to be enabled or backfilled for full-text search, enable all of them in a single `UpdateMetadataConfiguration` request. S3 Vectors runs only one `UpdateMetadataConfiguration` request at a time, and a backfill can take from minutes to hours depending on the size of the data being backfilled. While any field is in the `BUILDING` state, S3 Vectors rejects any other `UpdateMetadataConfiguration` request with a `ConflictException` (for example, a request to add, remove, or backfill another field).
+ You can't cancel a backfill in progress, and you can't remove a searchable field while its build is running. Wait until the field is `ACTIVE`.

## Remove a full-text search configuration
<a name="s3-vectors-configuring-full-text-search-remove"></a>

If you no longer need full-text search capability for a field, call `UpdateMetadataConfiguration` (using the AWS SDK, AWS CLI, or the Amazon S3 console) and remove its key from `textSearchConfigurations`. You can continue to retrieve data for that field, but full-text and hybrid queries that reference that field are rejected with a validation error.

### Using the AWS CLI
<a name="s3-vectors-configuring-full-text-search-remove-cli"></a>

**Example: Remove a searchable field**

```bash
aws s3vectors update-metadata-configuration \
    --vector-bucket-name "{{amzn-s3-demo-vector-bucket}}" \
    --index-name "{{documents}}" \
    --delete '{ "textSearchConfigurations": [ { "metadataKey": "summary" } ] }'
```

### Using the AWS SDKs
<a name="s3-vectors-configuring-full-text-search-remove-sdk"></a>

------
#### [ SDK for Python (Boto3) ]

```python
client.update_metadata_configuration(
    vectorBucketName="amzn-s3-demo-vector-bucket",
    indexName="documents",
    delete={
        "textSearchConfigurations": [
            {"metadataKey": "summary"},
        ],
    },
)
```

------