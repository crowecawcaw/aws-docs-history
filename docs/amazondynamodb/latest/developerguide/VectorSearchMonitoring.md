# Monitoring vector index capacity

To monitor capacity consumption for vector index operations, set the
`ReturnConsumedCapacity` parameter to `INDEXES` or
`TOTAL` in your `SearchVectors` requests, or to
`INDEXES` in your write API requests.

Vector index operations are metered in two units, separate from the read and write
capacity units used by the base table:

- **Vector Search (VS)** – The unit that meters
  `SearchVectors` operations. VS consumption is reported as
  `VectorSearchRequestBytes` and scales with the size of the vector data
  the search examines and returns.
- **Vector Write (VWR)** – The unit that meters
  writes replicated into a vector index. VWR consumption is reported as
  `VectorWriteRequestBytes` and scales with the size of the data
  replicated to the index.
  The following example shows the `ConsumedCapacity` returned by a
  `SearchVectors` request.

```
{
    "ConsumedCapacity": {
        "VectorSearchRequestBytes": 41714.0
    }
}
```

For write operations (`PutItem`, `UpdateItem`,
`DeleteItem`, `BatchWriteItem`,
`TransactWriteItems`), the response includes a `VectorIndexes`
map in `ConsumedCapacity`, keyed by index name. Each entry reports
`VectorWriteRequestBytes` for the capacity consumed when replicating
changes to each vector index.

```
{
    "ConsumedCapacity": {
        "TableName": "Products",
        "CapacityUnits": 5.0,
        "Table": {
            "CapacityUnits": 5.0
        },
        "VectorIndexes": {
            "ProductEmbeddingIndex": {
                "VectorWriteRequestBytes": 4125.0
            }
        }
    }
}
```

Vector index capacity is metered in bytes processed, reported separately from base
table read and write capacity. Use these fields to understand what drives your vector
index cost:

- **Search cost**
  (`VectorSearchRequestBytes`) scales primarily with the size of the
  vectors the search must examine, which grows with the number of dimensions in
  the index and the amount of data returned. Restricting a search to a single
  partition key value reduces the amount of data examined. Returning the vector
  attribute in results increases cost further because the response includes the
  full vector data.
- **Write cost**
  (`VectorWriteRequestBytes`) is incurred each time you write, update,
  or delete an item that changes a vector-indexed attribute, and scales with the
  size of the data replicated to the index. Writes that do not change an
  indexed attribute do not incur vector write capacity.
  Higher-dimensional embeddings increase both search and write cost because each
  vector carries more data. For current pricing, see the [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/ "https://aws.amazon.com/dynamodb/pricing/") on the AWS website.

DynamoDB also publishes vector index capacity to CloudWatch as the
`VectorSearchRequestBytes` and `VectorWriteRequestBytes` metrics,
dimensioned by `TableName` and `VectorIndexName`. Use these metrics
to chart and alarm on vector index usage over time. For metric definitions, see
[VectorSearchRequestBytes](metrics-dimensions.md#VectorSearchRequestBytes "metrics-dimensions.md#VectorSearchRequestBytes") and [VectorWriteRequestBytes](metrics-dimensions.md#VectorWriteRequestBytes "metrics-dimensions.md#VectorWriteRequestBytes").
