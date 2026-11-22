

# Hybrid search with Amazon S3 Vectors

Hybrid search in Amazon S3 Vectors combines full-text search with vector similarity search in a single query. S3 Vectors runs both searches, fuses the two rankings with Reciprocal Rank Fusion (RRF), and returns one ranked list of results. You get matches on both the meaning of a query and the exact terms it contains, using the same S3 Vectors API operations and the elasticity, durability, and pay-per-use economics of Amazon S3.

Vector search captures meaning, but on its own it can return less relevant results for queries that hinge on specific terms. These terms include product codes, SKUs, error codes, acronyms, legal citations, drug names, file names, and proper nouns. Full-text search uses BM25 (Best Matching 25) scoring to rank results by the terms they contain, so it can be more precise for queries where you are looking for specific terms. Hybrid search combines both full-text and vector search, which can help improve retrieval relevance for applications such as:
+ Retrieval Augmented Generation (RAG) and knowledge base search over documents
+ Agent memory, where an agent recalls past interactions by both meaning and exact identifiers
+ Catalog and enterprise document search that depends on exact IDs, citations, and codes
+ Media and content discovery across titles, descriptions, transcripts, and concepts

With hybrid search, your searchable text lives in the same vector index as your vectors, so every query runs against a single index.

To set up and use hybrid search, you configure full-text search on an index, write your searchable data, and run queries. For more information, see [Configuring full-text search](s3-vectors-configuring-full-text-search.md), [Adding full-text searchable content to your vectors](s3-vectors-ingesting-full-text-data.md), and [Querying with full-text and vector search](s3-vectors-querying-full-text-and-vector-search.md).

## Query types
<a name="s3-vectors-hybrid-search-query-types"></a>

You run all three types against the same index with the `QueryVectors` API operation:
+ **Vector-only** – Provide a query vector and no query text strings. Results are ranked by vector distance.
+ **Full-text-only** – Provide query text strings and no query vector. Results are ranked by BM25 score.
+ **Hybrid** – Provide both a query vector and query text strings. S3 Vectors fuses the two rankings with RRF and returns one ranked list.

## Requirements
<a name="s3-vectors-hybrid-search-requirements"></a>

Full-text and hybrid search are supported on `ENHANCED` indexes only, not on `CLASSIC` indexes. If your index is `CLASSIC`, convert it with the `UpdateIndexMode` API operation before you enable full-text search. For more information, see [Changing a vector index's mode](s3-vectors-index-mode.md).

## How to get started
<a name="s3-vectors-hybrid-search-getting-started"></a>

1. Configure which text fields are full-text searchable, on a new or existing index. For more information, see [Configuring full-text search](s3-vectors-configuring-full-text-search.md).

1. Write your vectors and your searchable text as metadata with the `PutVectors` API operation. For more information, see [Adding full-text searchable content to your vectors](s3-vectors-ingesting-full-text-data.md).

1. Run hybrid, full-text-only, or vector-only queries with the `QueryVectors` API operation. For more information, see [Querying with full-text and vector search](s3-vectors-querying-full-text-and-vector-search.md).

**Topics**
+ [Query types](#s3-vectors-hybrid-search-query-types)
+ [Requirements](#s3-vectors-hybrid-search-requirements)
+ [How to get started](#s3-vectors-hybrid-search-getting-started)
+ [Configuring full-text search](s3-vectors-configuring-full-text-search.md)
+ [Adding full-text searchable content to your vectors](s3-vectors-ingesting-full-text-data.md)
+ [Querying with full-text and vector search](s3-vectors-querying-full-text-and-vector-search.md)