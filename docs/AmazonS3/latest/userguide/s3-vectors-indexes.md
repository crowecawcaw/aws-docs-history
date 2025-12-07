# Vector indexes

###### Note

Choose your vector index configuration parameters carefully. After you create a vector index, you can't update the vector index name, dimension, distance metric, or non-filterable metadata keys. To change any of these values, you must create a new vector index.

Vector indexes are resources within vector buckets that store and organize vector data
for efficient similarity search operations. When you create a vector index, you specify the
distance metric (`Cosine` or `Euclidean`), the number of dimensions
that a vector should have, and optionally a list of metadata fields that you want to exclude
from filtering during similarity queries.

For more information about vector index limits per bucket, vector limits per index, and
dimension limits per vector, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md").

Each vector index has a unique Amazon Resource Name (ARN). The ARNs of vector indexes
follow the following format:

```
arn:aws:s3vectors:`region`:`account-id`:bucket/`bucket-name`/index/`index-name`
```

## Vector index naming requirements

- Vector index names must be unique within the vector bucket.
- Vector index names must be between 3 and 63 characters long.
- Valid characters are lowercase letters (a-z), numbers (0-9), hyphens (-), and
  dots (.).
- Vector index names must begin and end with a letter or number.

## Dimension requirements

A dimension is the number of values in a vector. All vectors added to the index must
have exactly this number of values.

- A dimension must be an integer between 1 and 4096.
- A larger dimension requires more storage space.

## Distance metric options

Distance metric specifies how similarity between vectors is calculated. When creating
vector embeddings, choose your embedding model's recommended distance metric for more
accurate results.

- **Cosine** – Measures the cosine of the angle
  between vectors. Best for normalized vectors and when direction matters more
  than magnitude.
- **Euclidean** – Measures the straight-line
  distance between vectors. Best when both direction and magnitude are
  important.

## Non-filterable metadata keys

Metadata keys allow you to attach additional information to your vectors as key-value
pairs during storage and retrieval. By default, all metadata is filterable, so you can
use it to filter query results. However, you can designate specific metadata keys as
non-filterable when you want to store information with vectors without using it for
filtering.

Unlike default metadata keys, these keys can't be used as query filters.
Non-filterable metadata keys can be retrieved but can't be searched, queried, or
filtered. You can only access it after finding the index.

Non-filterable metadata keys allow you to enrich vectors with additional context that
you want to retrieve with search results but don't need for filtering. A common example
of a non-filterable metadata key is when you embed text into vectors and want to include
the original text itself as non-filterable metadata. This allows you to return the
source text alongside vector search results without increasing your filterable metadata
size limits. Other examples include storing creation timestamps, source URLs, or
descriptive information purely for reference. Non-filterable metadata keys can be
accessed when retrieving vectors but, unlike default metadata keys, these keys can't be
used as query filters.

Requirements for non-filterable metadata keys are as follows.

- Non-filterable metadata keys must be unique within the vector index.
- Non-filterable metadata keys must be 1 to 63 characters long.
- Non-filterable metadata keys can't be modified after the vector index is created.
- S3 Vectors support up to 10 non-filterable metadata keys per index.

For more information about non-filterable metadata keys, see [Non-filterable
metadata](s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-non-filterable "s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-non-filterable").

###### Topics

- [Creating a vector index in a vector bucket](s3-vectors-create-index.md "s3-vectors-create-index.md")
- [Listing vector indexes](s3-vectors-index-list.md "s3-vectors-index-list.md")
- [Deleting a vector index](s3-vectors-index-delete.md "s3-vectors-index-delete.md")
- [Using tags with S3 vector indexes](vector-index-tagging.md "vector-index-tagging.md")
