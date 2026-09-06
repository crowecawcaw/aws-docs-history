

# Using vector indexes with global tables
<a name="VectorSearchGlobalTables"></a>

You can use vector indexes with global tables to run similarity search in multiple AWS Regions. When you add a replica to a table that has a vector index, DynamoDB replicates the vector index definition to the new replica Region automatically. You do not create the vector index separately in each Region. Items that you write in any replica Region are replicated to the other Regions and indexed there, so `SearchVectors` returns results from the local Region.

You can use vector indexes with every global table configuration:
+ **Multi-Region eventual consistency (MREC)** – The default consistency mode for global tables. For more information, see [Multi-Region eventual consistency (MREC)](V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes.mrec).
+ **Multi-Region strong consistency (MRSC)** – A consistency mode that provides strongly consistent reads across Regions. For more information, see [Multi-Region strong consistency (MRSC)](V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes.mrsc).
+ **Multi-account global tables** – Global tables that replicate across AWS accounts. For more information, see [DynamoDB multi-account global tables](globaltables-MultiAccount.md).

Multi-account global tables always use MREC because MRSC supports same-account configurations only. This is a global tables constraint, not a vector index limitation.

The following example adds a replica in the `us-west-2` Region to a table named `Products` that already has a vector index. The table must use on-demand capacity mode, which vector indexes require.

```
aws dynamodb update-table \
    --table-name Products \
    --region us-east-1 \
    --replica-updates '[{"Create": {"RegionName": "us-west-2"}}]'
```

While the replica is being created, the source table status is `UPDATING` and the replica's `ReplicaStatus` is `CREATING`. Use `DescribeTable` to confirm the replica reaches `ACTIVE` and to verify that the vector index was replicated. The replica Region reports the same vector index name, dimensions, distance function, and projection as the source Region.

```
aws dynamodb describe-table \
    --table-name Products \
    --region us-west-2
```

After the replica is active, you can run `SearchVectors` against the replica Region over the same set of vectors as the source Region. Before you search in the replica Region, use `DescribeTable` in that Region and confirm the vector index has finished backfilling, its `IndexStatus` is `ACTIVE` and `Backfilling` is not `true`. The replica's vector index backfills independently, so it can still be backfilling for a short time after the replica itself becomes active. Because vector search uses approximate nearest neighbor (ANN), the ranking might differ slightly between Regions for the same query, even over identical data.

```
aws dynamodb search-vectors \
    --table-name Products \
    --region us-west-2 \
    --index-name ProductEmbeddingIndex \
    --search-vector '[{"N": "0.1234"}, {"N": "-0.5678"}, {"N": "0.9012"}, ...]' \
    --top-k 10
```

**Replication lag affects cross-Region search results**  
The vector index propagates asynchronously across Regions, even for multi-Region strong consistency (MRSC) global tables. A vector that you write in one Region might not immediately appear in `SearchVectors` results in another Region. To read the most recent writes, send the search to the same Region where the write was made.