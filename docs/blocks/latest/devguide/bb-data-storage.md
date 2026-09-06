

# Data storage
<a name="bb-data-storage"></a>

This section covers Blocks for persisting and retrieving data.

## Choosing a data Block
<a name="_choosing_a_data_block"></a>


| Block | Best for | Avoid when | 
| --- | --- | --- | 
|  `KVStore`  | Caches, session stores, feature flags, config values | You need queries by multiple attributes or sorting | 
|  `DistributedTable`  | Entities with multiple access patterns, structured data with indexes | You need JOINs, transactions across tables, or complex SQL | 
|  `Database`  | Relational data, complex queries, JOINs, transactions, migrations | Your workload is mostly key-value lookups (higher latency and cost) | 
|  `DistributedDatabase`  | Globally distributed relational data, scale-to-zero workloads | You need strong consistency (uses optimistic concurrency control) | 
|  `FileBucket`  | File uploads, user-generated content, large binary objects | You need structured queries over file metadata (pair with `KVStore` for metadata) | 

## KVStore
<a name="bb-kvstore"></a>

Simple key-value storage. Store and retrieve values by key with optional conditional writes. Supports listing by prefix and scanning all entries. Best for caches, session stores, feature flags, and configuration values where you always know the key.

Locally, KVStore persists data to the filesystem in the `.bb-data/` directory. On AWS, it provisions a DynamoDB table. You can also wrap an existing DynamoDB table with `KVStore.fromExisting(tableName)`.

For more information, see [bb-kv-store on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-kv-store).

## DistributedTable
<a name="bb-distributed-table"></a>

Structured data with schema validation, secondary indexes, and rich queries. Define a schema and key structure, then query by partition key, sort key conditions, or secondary indexes. Supports batch operations for up to 25 items at a time.

Best for entities with multiple access patterns where you need to query data by different attributes. Locally, DistributedTable uses in-memory storage. On AWS, it provisions a DynamoDB table with Global Secondary Indexes.

For more information, see [bb-distributed-table on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-distributed-table).

## Database
<a name="bb-database"></a>

Full PostgreSQL with the Kysely query builder, migrations, transactions, foreign keys, and Row Level Security. Write SQL queries with full TypeScript type inference. Supports parameterized queries, single-row lookups, and ACID transactions.

Locally, Database runs PGlite (a WebAssembly Postgres engine) in-process for zero-latency development. On AWS, it provisions Aurora Serverless v2. Use the `db pull` command to import an existing database schema.

For more information, see [bb-data on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-data).

## DistributedDatabase
<a name="bb-distributed-data"></a>

Serverless SQL with instant provisioning, scale-to-zero, and optional multi-region active-active writes. Same query API as Database (Kysely query builder, transactions, migrations). Transactions use optimistic concurrency control and may fail at commit under contention.

Locally, DistributedDatabase uses PGlite. On AWS, it provisions Amazon Aurora DSQL. Best for globally distributed workloads or applications that need scale-to-zero SQL without managing connection pools.

For more information, see [bb-distributed-data on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-distributed-data).

## FileBucket
<a name="bb-file-bucket"></a>

File storage for uploads and downloads. Store files by path, generate presigned URLs for direct browser uploads and downloads, and list files by prefix. Supports versioning for point-in-time recovery.

Locally, FileBucket stores files in the `.bb-data/` directory on your filesystem, mirroring the S3 API behavior. On AWS, it provisions an S3 bucket. You can also wrap an existing S3 bucket with `FileBucket.fromExisting(bucketName)`.

For more information, see [bb-file-bucket on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-file-bucket).