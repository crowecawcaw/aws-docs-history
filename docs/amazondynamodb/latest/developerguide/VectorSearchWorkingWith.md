# Creating and searching vector indexes

This section describes how to create and manage vector indexes, write items with vector
data, and perform similarity searches using the `SearchVectors` API.

###### Topics

- [Before you begin](#VectorSearchWorkingWith.Prerequisites "#VectorSearchWorkingWith.Prerequisites")
- [SearchVectors endpoints](#VectorSearchWorkingWith.Endpoints "#VectorSearchWorkingWith.Endpoints")
- [Generating vector embeddings](#VectorSearchWorkingWith.Embeddings "#VectorSearchWorkingWith.Embeddings")
- [Creating a vector index](#VectorSearchWorkingWith.Create "#VectorSearchWorkingWith.Create")
- [Writing items with vector data](#VectorSearchWorkingWith.Write "#VectorSearchWorkingWith.Write")
- [Searching with SearchVectors](#VectorSearchWorkingWith.Search "#VectorSearchWorkingWith.Search")
- [Deleting a vector index](#VectorSearchWorkingWith.Delete "#VectorSearchWorkingWith.Delete")

## Before you begin

Before you work with vector indexes, verify the following:

- Your table uses on-demand capacity mode (`PAY_PER_REQUEST`).
  Vector indexes use on-demand capacity mode only and require a table that also
  uses on-demand capacity mode, so you cannot mix the two capacity modes.
- Your AWS Identity and Access Management (IAM) identity has `dynamodb:CreateTable` or
  `dynamodb:UpdateTable` permissions to create vector indexes.
- Your IAM identity has `dynamodb:SearchVectors` permission on
  the vector index resource to perform searches. The resource ARN format is
  `arn:aws:dynamodb:`region`:`account-id`:table/`table-name`/index/`index-name``.

## SearchVectors endpoints

`SearchVectors` requests use dedicated vector-search endpoints, which are
distinct from the standard DynamoDB endpoints that you use to create and manage vector
indexes (for example, with `CreateTable`, `UpdateTable`, and
`DescribeTable`). The AWS SDKs and AWS CLI route
`SearchVectors` requests to the correct endpoint automatically. You do
not need to configure or override the endpoint in your application code.

If you are building a custom HTTP client that calls the DynamoDB API directly
without an AWS SDK, use one of the following vector-search endpoints, replacing
`account-id` and `region` as
appropriate:

- ``account-id`.search-ddb.`region`.amazonaws.com`
  — Account-based endpoint.
- `search-dynamodb.`region`.api.aws`
  — Dual-stack endpoint, compatible with both IPv4 and IPv6.

## Generating vector embeddings

DynamoDB stores and searches vector embeddings, but it does not generate them. You
produce embeddings with an embedding model, such as the Amazon Bedrock Titan Text Embeddings or
Cohere Embed models, or any embedding model you operate. You then store the resulting
vector in a DynamoDB item and pass a query vector to `SearchVectors`.

###### Query vector and stored vectors must use the same model

The query vector you pass to `SearchVectors` and the vectors stored
in your items must be produced by the same embedding model and must have the same
number of dimensions as the vector index. Mixing models, or querying with a
different number of dimensions than the index was created with, produces meaningless
results or a validation error.

The typical flow is:

1. Send your source content (for example, a product description) to an
   embedding model and receive a vector.
2. Store that vector in a DynamoDB item, in the attribute named by the vector
   index (`VectorAttribute`), as a list (`L`) of numbers
   (`N`).
3. At query time, generate a vector from the search text using the same model,
   and pass it as the `SearchVector`.

###### Choose your embedding model before creating the index

Choose your embedding model before you create the vector index, because the
model determines the number of dimensions. Common embedding models produce 384,
768, 1024, 1536, or 3072 dimensions. DynamoDB supports up to 4,096 dimensions. See
[Requirements and limitations](VectorSearch.Requirements.md "VectorSearch.Requirements.md").

The distance function you choose interacts with how your model produces embeddings.
`COSINE` compares direction and ignores magnitude, so it works with
embeddings whether or not they are normalized. `DOT_PRODUCT` is sensitive to
magnitude: if your embeddings are not normalized to unit length, larger vectors receive
higher scores regardless of direction. If you use `DOT_PRODUCT` and want
direction-based similarity, normalize your embeddings to unit length before you store
them. See [How distance functions rank results](VectorSearch.md#VectorSearchWorkingWith.Ranking "VectorSearch.md#VectorSearchWorkingWith.Ranking").

## Creating a vector index

You can create a vector index when you create a new table or add one to an existing
table.

### Creating a table with a vector index

Use the `CreateTable` API with the `VectorIndexes`
parameter to create a table with a vector index. The following AWS CLI example creates a
`Products` table with a vector index named
`ProductEmbeddingIndex`.

```
aws dynamodb create-table \
    --table-name Products \
    --attribute-definitions AttributeName=ProductId,AttributeType=S \
                            AttributeName=Category,AttributeType=S \
                            AttributeName=Brand,AttributeType=S \
    --key-schema AttributeName=ProductId,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --vector-indexes \
        "[
            {
                \"IndexName\": \"ProductEmbeddingIndex\",
                \"VectorAttribute\": {\"AttributeName\": \"Embedding\"},
                \"SearchSchema\": [{\"AttributeName\":\"Category\",\"SearchSchemaElementType\":\"HASH\"},
                                  {\"AttributeName\":\"Brand\",\"SearchSchemaElementType\":\"INLINE_FILTER\"}],
                \"Projection\": {\"ProjectionType\": \"ALL\"},
                \"Dimensions\": 1536,
                \"DistanceFunction\": \"COSINE\"
            }
        ]"
```

In this example:

- `VectorAttribute` specifies `Embedding` as the
  attribute that contains vector data.
- `SearchSchema` defines `Category` as a vector
  index partition key (`HASH`), which partitions the index by
  category for scaling. It also defines `Brand` as an
  `INLINE_FILTER`, which lets you filter search results by
  brand at the storage layer. Because both `Category` and
  `Brand` are referenced in the
  SearchSchema,
  they must also be declared in `AttributeDefinitions`, the same way
  key attributes are declared for a global secondary index.
- `Dimensions` is set to 1536, matching the output of common
  embedding models.
- `DistanceFunction` is set to `COSINE`, where
  lower scores indicate greater similarity.

### Adding a vector index to an existing table

Use the `UpdateTable` API with the `VectorIndexUpdates`
parameter to add a vector index to an existing table. This example adds a second,
independent index named `ProductEmbeddingIndexV2` to the same
`Products` table.

```
aws dynamodb update-table \
    --table-name Products \
    --vector-index-updates \
        "[
            {
                \"Create\": {
                    \"IndexName\": \"ProductEmbeddingIndexV2\",
                    \"VectorAttribute\": {\"AttributeName\": \"Embedding\"},
                    \"Projection\": {\"ProjectionType\": \"ALL\"},
                    \"Dimensions\": 1536,
                    \"DistanceFunction\": \"EUCLIDEAN\"
                }
            }
        ]"
```

When you add a vector index to an existing table, DynamoDB reports index progress
through two fields in the `DescribeTable` response: an
`IndexStatus` value and a separate `Backfilling` boolean.

1. `IndexStatus` is `CREATING` and
   `Backfilling` is absent or `false`. DynamoDB is
   provisioning the index infrastructure.
2. `IndexStatus` is `CREATING` and
   `Backfilling` is `true`. DynamoDB is populating the
   index from existing base table data. New writes to the base table are
   replicated to the index during this phase.
   `SearchVectors` returns a
   `ValidationException`. This phase can take a substantial
   amount of time even when the base table holds very few items.
3. `IndexStatus` is `ACTIVE` and
   `Backfilling` is no longer reported. The index is ready for
   search.

###### You can't search while the index is backfilling

`SearchVectors` returns a
`ValidationException` while a vector index is backfilling. Use
`DescribeTable` to check both the `IndexStatus` and
the `Backfilling` flag, and wait until `IndexStatus`
is `ACTIVE` and `Backfilling` is not
`true` before you search. There is no
`BACKFILLING` index status value; an index that is backfilling
reports `IndexStatus` `CREATING` with
`Backfilling` set to `true`.

###### A newly ready index is not immediately searchable

`SearchVectors` requests are served by a dedicated search
endpoint, separate from the endpoint that serves
`DescribeTable`. After `DescribeTable` first reports
`IndexStatus` `ACTIVE`, the search endpoint can
require additional time before it begins serving the index. During that
interval `SearchVectors` returns a
`ValidationException`, typically `The table does not have
 the specified index`.

Treat a `ValidationException` on the first searches after
index creation as retryable rather than as a failure. Code that searches
immediately after observing `ACTIVE` might appear to work in
one environment and fail in another. The interval is brief and
varies.

For a readiness check that does not depend on either status field, issue
a real `SearchVectors` request in a retry loop. Treat the
first successful response as the signal that the index is ready.

You can create or delete only one vector index per table at a time. This
limit is shared with global secondary index creation on the same table. A second
`UpdateTable` request that creates or deletes an index while another
index operation is in progress fails with
`LimitExceededException: Subscriber limit exceeded: Only 1 online index
 can be created or deleted simultaneously per table`.

This applies to a single request as well: an `UpdateTable` call
containing two `Create` actions in its
`VectorIndexUpdates` parameter fails with the same error. Create
vector indexes one at a time, waiting for each to reach `ACTIVE`
before starting the next. Because each index must finish backfilling before the
next can start, building several vector indexes on one table takes considerably
longer than building one.

A `CreateTable` request can define multiple vector indexes at
once, up to the per-table limit of five. Exceeding that limit fails with
`ValidationException: One or more parameter values were invalid:
 VectorIndex count exceeds the per-table limit of 5`.

## Writing items with vector data

You write items with vector data using the standard DynamoDB write APIs
(`PutItem`, `UpdateItem`, `BatchWriteItem`,
`TransactWriteItems`). Store the vector embedding as a list of numbers
(`L` type containing `N` elements).

Because a vector contains many values, save the item to a file such as
`item.json`, then pass the file to the AWS CLI.

```
{
    "ProductId": { "S": "prod-123" },
    "Category": { "S": "Electronics" },
    "Title": { "S": "Wireless Headphones" },
    "Embedding": {
        "L": [
            { "N": "0.1234" },
            { "N": "-0.5678" },
            { "N": "0.9012" },
            ...
        ]
    }
}
```

```
aws dynamodb put-item \
    --table-name Products \
    --item file://item.json
```

###### Vector length must match the index dimensions

The `Embedding` vector shown here is abbreviated. In
`item.json`, it must contain 1,536 values to match the
`Dimensions` you set on `ProductEmbeddingIndex`. Writing a
vector with the wrong number of dimensions is rejected.

DynamoDB validates vector data when you write items to a table that has a vector
index. The following table describes the validation behavior.

| Condition                                                            | Behavior                                                                                                             |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Vector attribute has wrong number of dimensions                      | Write is rejected.                                                                                                   |
| Vector index partition key attribute is missing                      | Write succeeds on the base table, but the item is not replicated<br>to the vector index.                             |
| Vector index partition key attribute type doesn't match index schema | Write is rejected.                                                                                                   |
| Inline filter attribute is missing                                   | Write succeeds and the item is replicated to the vector<br>index.                                                    |
| Vector values have higher precision than 32-bit floating point (f32) | Write succeeds. Values are stored as-is in the base table but<br>lose precision when replicated to the vector index. |
| Vector attribute is deleted from an item                             | The corresponding entry in the vector index is deleted.                                                              |

###### Missing partition key causes silent de-indexing

If your vector index defines a partition key in the SearchSchema and you
write an item without that attribute (or remove it with
`UpdateItem`), the write succeeds on the base table but the item
is silently excluded from the vector index. It will not appear in
`SearchVectors` results even though the base table item and its
vector embedding still exist. Make sure that every item you want to be
searchable contains the vector index partition key attribute.

###### Stale embeddings produce incorrect results

DynamoDB does not recompute embeddings for you. If you change the source content
that produced an embedding (for example, you edit a product description),
the stored vector does not update automatically. You must regenerate the embedding
with your embedding model and write the new vector back to the item. Otherwise the
vector index continues to return results based on the old, stale vector, which can
silently produce incorrect matches.

## Searching with SearchVectors

Use the `SearchVectors` API to find items in a vector index that are
most similar to a query vector. Results are sorted by relevance, with the most similar
item first. Search results are eventually consistent: there might be a brief delay
between writing or updating a vector and it appearing in search results. For more
information, see [Ongoing write synchronization](VectorSearchDataSync.md#VectorSearchDataSync.OngoingWrites "VectorSearchDataSync.md#VectorSearchDataSync.OngoingWrites").

### Basic search

The following example searches for the 10 most similar items in the
`ProductEmbeddingIndex` index. Because this index has a vector index partition key
(`Category`) defined in its SearchSchema, the
`SearchConditionExpression` must include the vector index partition key value.

Save the query vector to a file such as `query-vector.json`, as a
plain JSON array of number values.

```
[
    { "N": "0.1234" },
    { "N": "-0.5678" },
    { "N": "0.9012" },
    ...
]

```

```
aws dynamodb search-vectors \
    --table-name Products \
    --index-name ProductEmbeddingIndex \
    --search-vector file://query-vector.json \
    --top-k 10 \
    --search-condition-expression "Category = :cat" \
    --expression-attribute-values "{\":cat\": {\"S\": \"Electronics\"}}"
```

The response includes a `SearchResults` array. Each element contains
the matching `Item` and a `Score` that indicates how similar
the item is to the query vector.

```
{
    "SearchResults": [
        {
            "Item": {
                "ProductId": { "S": "prod-456" },
                "Category": { "S": "Electronics" },
                "Title": { "S": "Bluetooth Speaker" }
            },
            "Score": 0.0023
        },
        {
            "Item": {
                "ProductId": { "S": "prod-789" },
                "Category": { "S": "Electronics" },
                "Title": { "S": "Noise Cancelling Earbuds" }
            },
            "Score": 0.0145
        }
    ]
}
```

###### Vector attributes are excluded from results by default

By default, the results from `SearchVectors` don't include the
vector attribute (the embedding). Vector data is large, and you typically
don't need it in the response. The results include the other projected
attributes and the `Score` value. To include the vector
attribute, request it with a `ProjectionExpression`. For more
information, see [Using ProjectionExpression](#VectorSearchWorkingWith.Search.Projection "#VectorSearchWorkingWith.Search.Projection").

###### SearchVector is a plain list, not a DynamoDB L type

The `SearchVector` request parameter is a plain JSON array of
number objects (`[{"N": "0.1234"}, ...]`). Do not wrap it
in a DynamoDB `L` type as you would when storing a vector in an
item attribute. The `L` wrapper is only used when writing or
reading vector data in item attributes.

The meaning of the `Score` depends on the distance function you
chose when you created the index. For `COSINE` and
`EUCLIDEAN`, lower scores indicate greater similarity. For
`DOT_PRODUCT`, higher scores indicate greater similarity.

### Filtering with SearchConditionExpression

Use `SearchConditionExpression` to filter search results based on
vector index partition key and inline filter attributes defined in the SearchSchema. This
expression uses the same syntax as other DynamoDB expression parameters.

The following example searches for items in the `Electronics`
category (vector index partition key) with a `Brand` inline filter.

```
aws dynamodb search-vectors \
    --table-name Products \
    --index-name ProductEmbeddingIndex \
    --search-vector file://query-vector.json \
    --top-k 10 \
    --search-condition-expression "Category = :cat AND Brand = :brand" \
    --expression-attribute-values "{\":cat\": {\"S\": \"Electronics\"}, \":brand\": {\"S\": \"Acme\"}}"
```

If your vector index has a partition key defined in the SearchSchema, you must
include it in the `SearchConditionExpression`. Inline filter attributes
are optional.

The equality operator (`=`) is supported in
`SearchConditionExpression` for both vector index partition key and inline filter
attributes. Comparison, range, and set-membership operators
(`<>`, `<`, `<=`, `>`,
`>=`, `IN`) are not yet available.

This filtering is how you scope a similarity search to a subset of your data, a
common requirement in multi-tenant and Retrieval Augmented Generation (RAG)
applications. For example, to find documents similar to a query but only within one
tenant, define the tenant attribute as a vector index partition key (`HASH`) in the
SearchSchema and pass its value in every search. This isolates results to that
tenant. It also improves performance, because the search examines only the
relevant data. Use inline filter attributes for additional
equality constraints, such as a document type or status, that you want to apply
within the routed partition.

###### Partition key scoping is not a security boundary

Using a partition key to scope searches to a single tenant is a
data-locality and performance optimization, not an access-control
mechanism. Any principal that holds `dynamodb:SearchVectors`
permission on the index can search any partition key value. Because
fine-grained access control (FGAC) condition keys such as
`dynamodb:LeadingKeys` do not apply to
`SearchVectors`, you cannot restrict access to individual
partition key values at the IAM policy level. If your workload requires
strict tenant isolation at the data layer, use separate tables or indexes
with distinct IAM grants for each tenant.

### Using ProjectionExpression

Use `ProjectionExpression` to return only specific attributes in the
search results. This can reduce the response size when you don't need all projected
attributes. Because `ProductEmbeddingIndex` defines a vector index partition key
(`Category`) in its SearchSchema, this example still includes the
vector index partition key value in `SearchConditionExpression`.

```
aws dynamodb search-vectors \
    --table-name Products \
    --index-name ProductEmbeddingIndex \
    --search-vector file://query-vector.json \
    --top-k 5 \
    --search-condition-expression "Category = :cat" \
    --expression-attribute-values "{\":cat\": {\"S\": \"Electronics\"}}" \
    --projection-expression "ProductId, Title"
```

###### Only projected attributes can be returned

You can only return attributes that are projected into the vector index.
Attributes that are not in the index projection cannot be returned by
`SearchVectors`.

## Deleting a vector index

Use the `UpdateTable` API with the `VectorIndexUpdates`
parameter to delete a vector index.

```
aws dynamodb update-table \
    --table-name Products \
    --vector-index-updates \
        "[
            {\"Delete\": {\"IndexName\": \"ProductEmbeddingIndex\"}}
        ]"
```

When you delete a vector index, DynamoDB removes the index and all of its data. This
operation does not affect the base table or its items.
