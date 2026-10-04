

# Metadata filtering
<a name="s3-vectors-metadata-filtering"></a>

Metadata filtering allows you to filter query results based on specific attributes attached to your vectors. You can use metadata filters with query operations to find vectors that match both similarity criteria and specific metadata conditions. 

S3 Vectors supports two types of metadata: filterable metadata and non-filterable metadata. The key difference is that filterable metadata can be used in query filters but has stricter size limitations, while non-filterable metadata can't be used in filters but can store larger amounts of data within its size limits. For more information about metadata limits, including size limits per vector and maximum metadata keys per vector, see [Limitations and restrictions](s3-vectors-limitations.md).

S3 Vectors evaluates your metadata filter before it runs vector search, a technique known as pre-filtering. S3 Vectors first identifies the vectors that match your filter, then only searches those vectors for the most similar ones, ensuring high recall even when filters match a small fraction of vectors. For example, if you search for similar movie embeddings and you filter by genre='mystery', S3 Vectors first identifies the vectors where the genre metadata is 'mystery', then only searches those for the closest matches to your query vector.

Pre-filtering applies to vector indexes whose index mode is `ENHANCED`. Vector buckets created on or after September 30, 2026 create `ENHANCED` indexes. In a vector bucket created before that date, indexes have the index mode `CLASSIC`.

S3 Vectors performs vector search and filter evaluation in tandem on a vector index whose index mode is `CLASSIC`. S3 Vectors searches through candidate vectors in the index to find the top K similar vectors while simultaneously validating if each candidate vector matches your metadata filter conditions. On a `CLASSIC` index, queries with filters may return fewer than top K results when the vector index contains very few matching results.

To move an existing index to `ENHANCED`, see [Changing a vector index's mode](s3-vectors-index-mode.md).

**Topics**
+ [Filterable metadata](#s3-vectors-metadata-filtering-filterable)
+ [Filter constraints per query](#s3-vectors-metadata-filtering-constraints)
+ [Examples of valid filterable metadata](#s3-vectors-metadata-filtering-examples)
+ [Non-filterable metadata](#s3-vectors-metadata-filtering-non-filterable)
+ [Query performance with filters](#s3-vectors-metadata-filtering-performance)

## Filterable metadata
<a name="s3-vectors-metadata-filtering-filterable"></a>

Filterable metadata allows you to filter query results based on specific metadata values. By default, all metadata fields are filterable in a similarity query unless explicitly specified as non-filterable during vector index creation. S3 Vectors supports string, number, boolean, and list types of metadata with a size limit per vector. The metadata type is ideal for attributes that you want to filter on, such as categories, timestamps, or status values.

If the metadata size exceeds the supported limits, the [PutVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectors.html) API operation will return a `400 Bad Request` error. For more information about the filterable metadata size limit per vector, see [Limitations and restrictions](s3-vectors-limitations.md). 

The following operations can be used with filterable metadata.


| Operator | Valid Input Types | Description | 
| --- | --- | --- | 
| $eq | String, Number, Boolean | Exact match comparison for single values.<br />When comparing with an array metadata value, returns true if the input value matches any element in the array. For example, `{"category": {"$eq": "documentary"}}` would match a vector with metadata `"category": ["documentary", "romance"]`. | 
| $ne | String, Number, Boolean | Not equal comparison | 
| $gt | Number | Greater than comparison | 
| $gte | Number | Greater than or equal comparison | 
| $lt | Number | Less than comparison | 
| $lte | Number | Less than or equal comparison | 
| $startsWith | String | Prefix match. Matches values that begin with the specified string. | 
| $in | Non-empty array of primitives | Match any value in array | 
| $nin | Non-empty array of primitives | Match none of the values in array | 
| $exists | Boolean | Check if field exists | 
| $and | Non-empty array of filters | Logical AND of multiple conditions | 
| $or | Non-empty array of filters | Logical OR of multiple conditions | 

`$startsWith` requires `ENHANCED` query behavior. It is available on a vector index whose index mode is `ENHANCED`, and on a `CLASSIC` index when the request sets `queryMode` to `ENHANCED`.

## Filter constraints per query
<a name="s3-vectors-metadata-filtering-constraints"></a>

On a vector index whose index mode is `ENHANCED`, a single query filter can use up to 100 filter constraints. Each value the filter evaluates counts as one constraint: `{"category": "electronics"}` is one, `{"region": {"$in": ["us-east-1", "us-west-2", "eu-west-1"]}}` is three, and `{"$and": [{"category": "electronics"}, {"price": {"$lte": 500}}]}` is two. This limit only applies to `ENHANCED` indexes.

Typical filtered queries are well within 100 constraints. For guidance on writing filters that stay within the limit, see [S3 Vectors best practices](s3-vectors-best-practices.md).

## Examples of valid filterable metadata
<a name="s3-vectors-metadata-filtering-examples"></a>

**Simple equality**  

```
{"genre": "documentary"}
```
This filter matches vectors where the genre metadata key equals "documentary". When you don't specify an operator, S3 Vectors automatically uses the $eq operator.

**Explicit equality**  

```
// Example: Exact match
{"genre": {"$eq": "documentary"}}
```

```
// Example: Not equal to
{"genre": {"$ne": "drama"}}
```

**Numeric comparison**  

```
{"year": {"$gt": 2019}}
```

```
{"year": {"$gte": 2020}}
```

```
{"year": {"$lt": 2020}}
```

```
{"year": {"$lte": 2020}}
```

**Prefix match**  

```
{"s3_path": {"$startsWith": "/marketing/"}}
```
This filter matches vectors whose s3\_path metadata begins with "/marketing/". Useful for hierarchical paths and URL prefixes.

**Array operations**  

```
{"genre": {"$in": ["comedy", "documentary"]}}
```

```
{"genre": {"$nin": ["comedy", "documentary"]}}
```

**Existence check**  

```
{"genre": {"$exists": true}}
```
The `$exists` filter matches vectors that have a "genre" metadata key, regardless of the value that's stored for that metadata key.

**Logical operations**  

```
{"$and": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}
```

```
{"$or": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}
```

**Price range (Multiple conditions on the same field)**  

```
{"price": {"$gte": 10, "$lte": 50}}
```

For more information about how to query vectors with metadata filtering, see [Metadata filtering](s3-vectors.md#s3-vectors-filtering-metadata).

## Non-filterable metadata
<a name="s3-vectors-metadata-filtering-non-filterable"></a>

Non-filterable metadata can't be used in query filters but can store larger amounts of contextual data than filterable metadata. It's ideal for storing large text chunks, detailed descriptions, or other contextual information that doesn't need to be searchable but can be returned with query results. For example, you might store full document text, image descriptions, or detailed product specifications as non-filterable metadata.

Non-filterable metadata keys must be explicitly configured during vector index creation. Once a metadata key is designated as non-filterable during index creation, it can't be changed to filterable later. You can configure multiple metadata keys as non-filterable per vector index, with each metadata key name limited to 63 characters. For more information about the maximum number of non-filterable metadata keys that's allowed per vector index, see [Limitations and restrictions](s3-vectors-limitations.md).

While you can't filter on non-filterable metadata, you can retrieve it alongside query results using the `return-metadata` parameter. You can use non-filterable metadata for some use cases as follows.
+ Use it to provide context for your application without parsing separate data sources.
+ Store larger text chunks that would exceed the filterable metadata size limits.
+ Include it in vector exports by using the [ListVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListVectors.html) API operation.

For more information about configuring non-filterable metadata, see [Creating a vector index in a vector bucket](s3-vectors-create-index.md).

## Query performance with filters
<a name="s3-vectors-metadata-filtering-performance"></a>

Because an `ENHANCED` index evaluates your filter before it searches, the work a filtered query does depends on the filter you send. Three things increase that work, and with it the query's latency: a larger vector index, a filter that matches a larger share of the vectors in the index, and a filter with more constraints.

Because actual performance varies with your dataset size, dimensions, and filters, we recommend testing with representative data and queries. For guidance on writing filters, see [S3 Vectors best practices](s3-vectors-best-practices.md).