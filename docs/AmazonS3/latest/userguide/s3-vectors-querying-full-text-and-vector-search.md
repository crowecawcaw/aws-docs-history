

# Querying with full-text and vector search

You run full-text, vector, and hybrid queries with the `QueryVectors` API operation (using the AWS SDK or AWS CLI). Specify `topK`, and then provide the query vector, query text strings, or both. S3 Vectors selects the behavior from the inputs you provide:
+ A `queryVector` and no `queryTexts` runs a vector-only search.
+ `queryTexts` and no `queryVector` runs a full-text-only search that ranks results with BM25 (Best Matching 25) scoring. BM25 is a ranking function that scores each record by how often your query terms appear in the searched field. It gives more weight to rarer terms and less to very common ones, so the records whose text best matches your terms rank highest.
+ Both present runs a hybrid search. S3 Vectors runs a full-text search for each query text field and a vector search, fuses the rankings with Reciprocal Rank Fusion (RRF), and returns one ranked list of your top K results.

Before you query, configure which fields are full-text searchable as described in [Configuring full-text search](s3-vectors-configuring-full-text-search.md), and write your data as described in [Adding full-text searchable content to your vectors](s3-vectors-ingesting-full-text-data.md). For an overview, see [Hybrid search with Amazon S3 Vectors](s3-vectors-hybrid-search.md).

Each `queryTexts` entry contains the text to search for and the metadata field to search it against. S3 Vectors analyzes your query text with the same analyzer that the field uses in its text search configuration, so the query terms match the indexed terms. By default, the response returns the result keys. Set `returnMetadata`, `returnDistance`, and `returnScores` to also return the metadata, the vector distance, and the scores. With `returnScores`, a hybrid query returns the fused score and the BM25 score. For the maximum query text size and the number of fields you can search per request, see [Limitations and restrictions](s3-vectors-limitations.md).

S3 Vectors delivers sub-second response times for cold queries, using Amazon S3 elastic throughput to efficiently search across billions of vectors and text data. This makes it cost-effective for workloads with infrequent queries. For warm queries, S3 Vectors can deliver response times as low as 100 ms, which benefits workloads with repeated or frequent query patterns. When query results are returned across multiple pages, subsequent pages can be accessed immediately. On a full-text or hybrid query, response time also varies with the work your query does; for guidance on writing full-text and hybrid queries, see [S3 Vectors best practices](s3-vectors-best-practices.md).

Vector search with S3 Vectors delivers 90%\+ average recall for most datasets, meaning that the query response contains 90% of the true nearest stored vectors to your query vector. Full-text search with BM25 scoring instead matches on the exact terms in your text. It uses the lexical signal of specific terms such as identifiers, product codes, citations, and proper nouns to find the records that contain them. When result relevance is driven by the presence of specific text terms, BM25 scoring can produce more relevant results than vector search. Hybrid queries can provide recall gains over both full-text alone and vector alone, because they capture both signals at once. They use the exact-term (lexical) signal that full-text search relies on and the semantic meaning that vector search captures, so results that either approach would miss on its own are still retrieved and fused into a single ranking. This helps most when your query set is heterogeneous, with a mix of term-driven and conceptual queries. Since actual performance might vary depending on your specific use cases, we recommend conducting your own tests with representative data and queries to validate that S3 Vectors meets your recall requirements.

**Topics**
+ [Run a hybrid query](#s3-vectors-querying-full-text-and-vector-search-hybrid)
+ [Run a full-text-only query](#s3-vectors-querying-full-text-and-vector-search-full-text-only)
+ [Search multiple text fields with a single query request](#s3-vectors-querying-full-text-and-vector-search-multiple-fields)

## Run a hybrid query
<a name="s3-vectors-querying-full-text-and-vector-search-hybrid"></a>

The following example runs a hybrid query over the `documents` index. It combines a vector search with a full-text search on `passage_body`, restricts results to documents whose `title` matches a metadata filter, and returns the top 10 fused results with their metadata, vector distance, and scores.

**Example: Run a hybrid query**

```python
response = client.query_vectors(
    vectorBucketName="my-vector-bucket",
    indexName="documents",
    topK=10,
    queryVector={"float32": query_embedding},
    queryTexts=[
        {"text": "controller error code E1234", "metadataKey": "passage_body"},
    ],
    filter={"title": {"$eq": "Quarterly maintenance guide"}},
    returnMetadata=True,
    returnDistance=True,
    returnScores=True,
)
```

## Run a full-text-only query
<a name="s3-vectors-querying-full-text-and-vector-search-full-text-only"></a>

Omit the query vector to run a BM25-only search.

**Example: Run a full-text-only query**

```python
response = client.query_vectors(
    vectorBucketName="my-vector-bucket",
    indexName="documents",
    topK=10,
    queryTexts=[
        {"text": "controller error code E1234", "metadataKey": "passage_body"},
    ],
    returnScores=True,
)
```

## Search multiple text fields with a single query request
<a name="s3-vectors-querying-full-text-and-vector-search-multiple-fields"></a>

You can pass multiple query text and field pairs in one request, up to the per-request maximum. For the number of fields you can search per request, see [Limitations and restrictions](s3-vectors-limitations.md). S3 Vectors runs a BM25 search for each metadata field, sums the per-field scores into a single full-text score, and then fuses that ranking with the vector ranking using RRF to return one ranked list.

**Example: Search multiple text fields**

```python
response = client.query_vectors(
    vectorBucketName="my-vector-bucket",
    indexName="documents",
    topK=10,
    queryVector={"float32": query_embedding},
    queryTexts=[
        {"text": "error code E1234", "metadataKey": "passage_body"},
        {"text": "maintenance guide", "metadataKey": "title"},
    ],
    returnMetadata=True,
    returnScores=True,
)
```

If you have your own re-ranking or score-normalization step, run a full-text-only query and a vector-only query as separate `QueryVectors` calls with `returnScores` enabled. Each call returns a ranked list with its own scores, and you combine the results in your application.

**Example: Run separate full-text and vector queries for custom fusion**

```python
# 1. Full-text-only ranking, with BM25 scores
text_results = client.query_vectors(
    vectorBucketName="my-vector-bucket",
    indexName="documents",
    topK=50,
    queryTexts=[{"text": "controller error code E1234", "metadataKey": "passage_body"}],
    returnScores=True,
)

# 2. Vector-only ranking, with distances
vector_results = client.query_vectors(
    vectorBucketName="my-vector-bucket",
    indexName="documents",
    topK=50,
    queryVector={"float32": query_embedding},
    returnDistance=True,
)

# 3. Fuse text_results and vector_results with your own scoring logic.
```