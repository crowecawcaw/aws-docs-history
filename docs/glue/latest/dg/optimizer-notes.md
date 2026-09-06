

# Considerations and limitations
<a name="optimizer-notes"></a>

 This section includes things to consider when using table optimizers within the AWS Glue Data Catalog. 

## Durability and correctness
<a name="durability-correctness"></a>

**S3 Table Locations:**

When multiple AWS Glue Data Catalog tables share the same Amazon S3 location and have optimizers enabled, the snapshot retention or orphan file deletion optimizer for one table may delete files that are still referenced by the other table. Ensure that each table with optimizers enabled has a unique Amazon S3 location that is not shared with any other table, including tables in different databases.

**S3 Lifecycle Expiry:**

Amazon S3 lifecycle expiration rules that apply to Iceberg table storage locations can delete manifest and data files that are still referenced by active snapshots. If your bucket has lifecycle expiration rules, ensure they exclude the Iceberg table storage path.

## Known issues
<a name="known-issues"></a>

The [Catalog-level table optimizers](https://docs.aws.amazon.com/glue/latest/dg/catalog-level-optimizers.html) documentation states that "tables without their own optimizer configurations will inherit the disabled state from the catalog level." There is a known issue where some tables without their own optimizer configuration may not correctly inherit the disabled state from the catalog-level configuration. Use the AWS Glue console and optimizer execution logs to verify which optimizers are currently enabled and running in your account, and disable any that you do not require.

## Supported formats and limitations for managed data compaction
<a name="compaction-notes"></a>

Data compaction supports a variety of data types and compression formats for reading and writing data, including reading data from encrypted tables.

**Concurrency Control:**

 Apache Iceberg supports optimistic concurrency control, allowing multiple writers to perform operations simultaneously. Conflicts are detected and resolved at commit time. When working with streaming pipelines, configure appropriate retry settings through table properties and compaction settings to handle concurrent writes effectively. For detailed guidance, refer to the AWS Big Data Blog on [managing concurrent writes in Iceberg tables](https://aws.amazon.com/blogs/big-data/manage-concurrent-write-conflicts-in-apache-iceberg-on-the-aws-glue-data-catalog/). 

**Compaction Retries:**

 When compaction operations fail four consecutive times, AWS Glue catalog table optimization automatically suspends the optimizer to prevent unnecessary compute resource consumption. First investigate the logs and try to understand why compaction is repeatedly failing. To resume compaction optimization, you can re-enable the optimizer through the AWS Glue console or API. 

 **Data compaction supports:**
+ **Encryption** – Data compaction only supports default Amazon S3 encryption (SSE-S3) and server-side KMS encryption (SSE-KMS).
+ **Compaction strategies** – Binpack, sort, and Z-order sorting
+ You can run compaction from the account where Data Catalog resides when the Amazon S3 bucket that stores the underlying data is in another account. To do this, the compaction role requires access to the Amazon S3 bucket.

 **Data compaction currently doesn’t support:** 
+ **Compaction on cross-account tables** – You can't run compaction on cross-account tables.
+ **Compaction on cross-Region tables** – You can't run compaction on cross-Region tables.
+ **Enabling compaction on resource links**
+ **Tables in Amazon S3 Express One Zone storage class ** – You can't run compaction on Amazon S3 Express One Zone Iceberg Tables. 
+ **Z-order compaction strategy doesn't support the following data types :**
  + Decimal
  + TimestampWithoutZone

## Considerations for snapshot retention and orphan file deletion optimizers
<a name="retention-notes"></a>

The following considerations apply to the snapshot retention and the orphan file deletion optimizers. 
+ The snapshot retention and orphan file deletion processes have a maximum limit of deleting 1,000,000 files per run. When deleting expired snapshots, if the number of eligible files for deletion surpasses 1,000,000, any remaining files beyond that threshold will continue to exist in the table storage as orphan files. 
+ Snapshots will be preserved by the snapshot retention optimizer only when both criteria are satisfied: the minimum number of snapshots to keep and the specified retention period.
+ The snapshot retention optimizer deletes expired snapshot metadata from Apache Iceberg, preventing time travel queries for expired snapshots and optionally deleting associated data files.
+  Orphan file deletion optimizer deletes orphaned data and metadata files that are no longer referenced by Iceberg metadata if their creation time is before the orphan file deletion retention period from the time of optimizer run.
+ Apache Iceberg facilitates version control through branches and tags, which are named pointers to specific snapshot states. Each branch and tag follows its own independent life-cycle, governed by retention policies defined at their respective levels. The AWS Glue Data Catalog optimizers take these life cycle policies into account, ensuring adherence to the specified retention rules. Branch and tag-level retention policies take precedence over the optimizer configurations. 

   For more information, see [Branching and Tagging](https://iceberg.apache.org/docs/nightly/branching/) in Apache Iceberg documentation. 
+ Snapshot retention and orphan file deletion optimizers will delete files eligible for clean-up as per configured parameters. Enhance your control over file deletion by implementing S3 versioning and life-cycle policies on the appropriate buckets.

   For detailed instructions on setting up versioning and creating life cycle rules, see [https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html). 
+  For proper orphan file determination, ensure that the provided table location and any sub-paths don't overlap with or contain data from any other tables or data sources. If paths overlap, you risk unrecoverable data loss from unintended deletion of files. 

## Debugging OversizedAllocationException exception
<a name="debug-exception"></a>

To resolve an `OversizedAllocationException` exception:
+ Reduce the batch size of the vectorized reader and check. The default batch size is 5000. This is controlled in the `read.parquet.vectorization.batch-size`.
  + If this doesn’t work even after multiple variations, turn off vectorization. This is controlled in the `read.parquet.vectorization.enabled`.