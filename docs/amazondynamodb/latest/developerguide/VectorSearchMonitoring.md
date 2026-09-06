

# Monitoring vector index capacity
<a name="VectorSearchMonitoring"></a>

To monitor capacity consumption for vector index operations, set the `ReturnConsumedCapacity` parameter to `INDEXES` or `TOTAL` in your `SearchVectors` requests, or to `INDEXES` in your write API requests.

Vector index operations are metered in two units, separate from the read and write capacity units used by the base table:
+ **Vector Search (VS)** – The unit that meters `SearchVectors` operations. VS consumption is reported as `VectorSearchRequestBytes` and scales with the size of the vector data the search examines and returns.
+ **Vector Write (VWR)** – The unit that meters writes replicated into a vector index. VWR consumption is reported as `VectorWriteRequestBytes` and scales with the size of the data replicated to the index.

The following example shows the `ConsumedCapacity` returned by a `SearchVectors` request.

```
{
    "ConsumedCapacity": {
        "VectorSearchRequestBytes": 41714.0
    }
}
```

For write operations (`PutItem`, `UpdateItem`, `DeleteItem`, `BatchWriteItem`, `TransactWriteItems`), the response includes a `VectorIndexes` map in `ConsumedCapacity`, keyed by index name. Each entry reports `VectorWriteRequestBytes` for the capacity consumed when replicating changes to each vector index.

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

Vector index capacity is metered in bytes processed, reported separately from base table read and write capacity. Use these fields to understand what drives your vector index cost:
+ **Search cost** (`VectorSearchRequestBytes`) scales primarily with the size of the vectors the search must examine, which grows with the number of dimensions in the index and the amount of data returned. Restricting a search to a single partition key value reduces the amount of data examined. Returning the vector attribute in results increases cost further because the response includes the full vector data. Search cost does not rise in proportion to the number of items in the index. If the number of dimensions, the `TopK` value, and the projection stay the same, the data a search examines grows logarithmically as you add items. This happens because an approximate nearest neighbor search traverses a small subset of the index rather than reading every vector. Doubling the number of items in an index adds a small, constant amount to the data each search examines.
+ **Write cost** (`VectorWriteRequestBytes`) is incurred each time you write, update, or delete an item that changes a vector-indexed attribute, and scales with the size of the data replicated to the index. Writes that do not change an indexed attribute do not incur vector write capacity.

Higher-dimensional embeddings increase both search and write cost because each vector carries more data. For current pricing, see the [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/) on the AWS website.

DynamoDB also publishes vector index capacity to CloudWatch as the `VectorSearchRequestBytes` and `VectorWriteRequestBytes` metrics, dimensioned by `TableName` and `VectorIndexName`. Use these metrics to chart and alarm on vector index usage over time. For metric definitions, see [VectorSearchRequestBytes](metrics-dimensions.md#VectorSearchRequestBytes) and [VectorWriteRequestBytes](metrics-dimensions.md#VectorWriteRequestBytes).

## Per-request metering minimum
<a name="VectorSearchMonitoring.MeteringMinimum"></a>

DynamoDB meters vector index capacity at a minimum of 1 KB per request and bills per byte above that minimum. This applies to both request types. A `SearchVectors` request that examines less than 1 KB of vector data is metered at 1 KB. A write request that replicates less than 1 KB into a table's vector indexes is also metered at 1 KB.

The minimum applies per request, not per index. A write that updates vectors in several of a table's vector indexes does not incur a separate 1 KB minimum for each one, even though `ConsumedCapacity` reports `VectorWriteRequestBytes` per index.

As a result, low-dimension vectors do not meter proportionally lower. A vector with a small number of dimensions holds only a few bytes of 32-bit floating point data and is still metered at the 1 KB minimum.

Above the minimum, `VectorSearchRequestBytes` reflects the vector data the search examines within the index, not the size of the query vector you supply. As a result, `VectorSearchRequestBytes` is larger than the query vector alone.

Search cost grows logarithmically, as explained earlier, but that relationship is not a formula for estimating your bill. `VectorSearchRequestBytes` also includes the data the search returns. That data scales with `TopK` and with the attributes you project. The metric is also floored at the 1 KB per-request minimum. At a high `TopK` with a full projection, returned data can exceed examined data.

Do not estimate vector index cost from dimension count. Use the `VectorSearchRequestBytes` and `VectorWriteRequestBytes` values returned by your own workload, or the corresponding CloudWatch metrics. Validate against a representative dataset before you size a workload.