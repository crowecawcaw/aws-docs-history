

# Retryable writes in Amazon DocumentDB
<a name="retryable-writes"></a>

Starting with engine version 8.0.2, Amazon DocumentDB supports retryable writes. When a write operation fails due to a transient network error or primary election, the driver can automatically retry the operation exactly once. Amazon DocumentDB deduplicates the retried write so that the operation is applied at most once, preserving idempotency.

Retryable writes require a MongoDB-compatible driver that supports the retryable writes protocol. Most current MongoDB-compatible drivers enable retryable writes by default (`retryWrites=true` in the connection string). If you are upgrading to engine 8.0.2 from an earlier version, you can remove `retryWrites=false` from your connection string to enable this feature.

## Requirements
<a name="retryable-writes-requirements"></a>

To use retryable writes, you must meet the following requirements:
+ Amazon DocumentDB engine version 8.0.2 or later.
+ A MongoDB-compatible driver that supports retryable writes. For the minimum version, see the documentation for your driver.
+ The connection string must include `retryWrites=true`, or the driver must default to retryable writes (most current drivers do).

## Supported operations
<a name="retryable-writes-supported-operations"></a>

Retryable writes apply to write operations in which each individual write affects at most one document. Batch operations qualify, because each write within the batch is deduplicated separately.

The following write operations are retryable:
+ `insertOne`
+ `insertMany`
+ `updateOne`
+ `deleteOne`
+ `findOneAndUpdate`
+ `findOneAndDelete`
+ `findOneAndReplace`
+ `bulkWrite` (when composed of `insertOne`, `updateOne`, `deleteOne`, or `replaceOne` operations)

For `insertMany` and `bulkWrite`, each document in the batch is deduplicated individually. If a retry is needed, only the documents that were not yet applied are inserted.

**Note**  
`commitTransaction` and `abortTransaction` are also retryable, as transaction-control commands rather than as writes. The individual writes inside a transaction are not retryable. For more information, see [Limitations](#retryable-writes-limitations).

## Limitations
<a name="retryable-writes-limitations"></a>

The following limitations apply to retryable writes in Amazon DocumentDB:
+ `updateMany` and `deleteMany` are not retryable.
+ Writes inside multi-statement transactions are not retryable. Transaction commit and abort operations are retryable separately.
+ Documents must include an `_id` field for retryable inserts.
+ Retryable writes are available only on engine version 8.0.2 and later. On earlier engine versions, set `retryWrites=false` in your connection string to avoid errors.
+ Write operations are not retryable on clusters that use query planner version 1.0.
+ For `findOneAndUpdate`, `findOneAndDelete`, and `findOneAndReplace` operations that return large documents, retryable writes may increase write latency because the full result document is cached for deduplication. If write performance is critical and the returned documents are large, consider setting `retryWrites=false` for those workloads.

## Enabling retryable writes
<a name="retryable-writes-enabling"></a>

To enable retryable writes, include `retryWrites=true` in your connection string:

```
mongodb://{{<username>}}:{{<password>}}@{{<cluster-endpoint>}}:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=true
```

If your driver defaults to `retryWrites=true`, you can remove any explicit `retryWrites=false` from your connection string.

For the full connection string walkthrough, see [Connecting programmatically to Amazon DocumentDB](connect_programmatically.md).

## How retryable writes work
<a name="retryable-writes-how-it-works"></a>

When your application sends a write with `retryWrites=true`, the driver attaches a logical session ID (`lsid`) and a transaction number (`txnNumber`) to the write command. Amazon DocumentDB uses these identifiers to deduplicate writes:
+ On the first attempt, Amazon DocumentDB executes the write and caches the result.
+ If the driver retries the same write (same `lsid` and `txnNumber`), Amazon DocumentDB returns the cached result without re-executing the write.
+ Amazon DocumentDB honors retries for 60 minutes after the original write. Drivers retry immediately, so this window is far longer than a driver needs.

If a retry arrives more than 60 minutes after the original write, Amazon DocumentDB no longer has a cached result for it and runs the write as a new operation.

## Error handling
<a name="retryable-writes-errors"></a>

The following errors are specific to retryable writes in Amazon DocumentDB:


| Error code | Name | Description | 
| --- | --- | --- | 
| 225 | TransactionTooOld | A newer transaction number for the same session and statement was already committed, so this retry is too old to apply. | 
| 301 | Retryable writes not supported | The write included retryable write fields, but the engine version does not support retryable writes, or the operation is not retryable. Set retryWrites=false when connecting to engine versions earlier than 8.0.2. | 

## Migrating from retryWrites=false
<a name="retryable-writes-migration"></a>

If you are upgrading to engine version 8.0.2 and currently use `retryWrites=false` in your connection strings:

1. Upgrade your cluster to engine version 8.0.2 or later.

1. Remove `retryWrites=false` from your application's connection strings, or change it to `retryWrites=true`.

1. No application code changes are required. The driver handles retries automatically.