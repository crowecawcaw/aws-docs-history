

# Data synchronization between tables and vector indexes
<a name="VectorSearchDataSync"></a>

DynamoDB keeps a vector index synchronized with its base table automatically. Understanding how synchronization works helps you predict when search results are complete and why an item might not appear in results.

## Backfilling an index on an existing table
<a name="VectorSearchDataSync.Backfilling"></a>

When you add a vector index to a table that already contains items, DynamoDB backfills the index with the existing data. The index first transitions to `IndexStatus` `CREATING` while DynamoDB provisions the index infrastructure. It remains `CREATING` while DynamoDB populates the index from existing base table data, and reports `Backfilling` as `true` during that phase. New writes to the base table are replicated to the index while it backfills, but `SearchVectors` returns a `ValidationException` until backfilling finishes. When the index is ready, `IndexStatus` becomes `ACTIVE` and the `Backfilling` field is no longer reported. Use `DescribeTable` and wait until `IndexStatus` is `ACTIVE` and `Backfilling` is not `true` before you search.

Index construction drives backfill duration, not the number of items in the base table. Even a table with very few items can take a substantial amount of time to finish backfilling. Poll `DescribeTable` rather than assuming a small table will be ready quickly.

See [Adding a vector index to an existing table](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Create.ExistingTable).

## Ongoing write synchronization
<a name="VectorSearchDataSync.OngoingWrites"></a>

After the index is active, DynamoDB replicates each write to the base table into the vector index. The following behaviors affect whether and how a write reaches the index:
+ An item is replicated to the index only if it contains a valid vector attribute. If the index defines a partition key, the item must also contain that partition key attribute; otherwise the write succeeds on the base table but the item is not replicated to the index.
+ Vector values are stored in the base table as written, but are stored at 32-bit floating point (f32) precision in the index. Values with higher precision lose that precision when replicated to the index.
+ When you delete the vector attribute from an item, or delete the item, the corresponding entry is removed from the index.

For the complete set of write-validation rules, see [Writing items with vector data](VectorSearchWorkingWith.md#VectorSearchWorkingWith.Write).

## Synchronization across Regions
<a name="VectorSearchDataSync.GlobalTables"></a>

When a table that has a vector index is a global table, DynamoDB replicates writes in any replica Region to the other Regions and indexes them there. DynamoDB replicates data to the vector index asynchronously. A vector that you write in one Region might not immediately appear in `SearchVectors` results in another Region—even if the table uses multi-Region strong consistency (MRSC). See [Using vector indexes with global tables](VectorSearchGlobalTables.md).