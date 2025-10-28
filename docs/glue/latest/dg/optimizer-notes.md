# Considerations and limitations

This section includes things to consider when using table optimizers within the AWS Glue Data Catalog.

## Supported formats and limitations for managed data

compaction

Data compaction supports a variety of data types and compression formats for reading and writing data, including reading data from encrypted tables.

**Data compaction supports:**

- Encryption – Data compaction only supports default Amazon S3 encryption (SSE-S3) and server-side KMS encryption (SSE-KMS).
- Compaction strategies –- Binpack, sort, and Z-order
  sorting
- You can run compaction from the account where Data Catalog resides when the Amazon S3
  bucket that stores the underlying data is in another account. To do this, the
  compaction role requires access to the Amazon S3 bucket.

**Data compaction currently doesn’t support:**

- Compaction on cross-account tables – You can't run compaction on cross-account tables.
- Compaction on cross-Region tables – You can't run
  compaction on cross-Region tables.
- Enabling compaction on resource links
- Tables in Amazon S3 Express One Zone storage class –
  You can't run compaction on S3 Express One Zone Iceberg Tables.
- Z-order compaction strategy doesn't support the following data types
  :
  - Decimal
  - TimestampWithoutZone

## Considerations for snapshot retention and orphan file

deletion optimizers

The following considerations apply to the snapshot retention and the orphan file
deletion optimizers.

- The snapshot retention and orphan file deletion processes have a maximum limit of deleting
  1,000,000 files per run. When deleting expired snapshots, if the number of eligible
  files for deletion surpasses 1,000,000, any remaining files beyond that threshold will
  continue to exist in the table storage as orphan files.
- Snapshots will be preserved by the snapshot retention optimizer only when both
  criteria are satisfied: the minimum number of snapshots to keep and the specified
  retention period.
- The snapshot retention optimizer deletes expired snapshot metadata from Apache
  Iceberg, preventing time travel queries for expired snapshots and optionally deleting
  associated data files.
- Orphan file deletion optimizer deletes orphaned data and metadata files that are no
  longer referenced by Iceberg metadata if their creation time is before the orphan file
  deletion retention period from the time of optimizer run.
- Apache Iceberg facilitates version control through branches and tags, which are
  named pointers to specific snapshot states. Each branch and tag follows its own
  independent life-cycle, governed by retention policies defined at their respective levels.
  The AWS Glue Data Catalog optimizers take these life cycle policies into account, ensuring adherence
  to the specified retention rules. Branch and tag-level retention policies take precedence
  over the optimizer configurations.

For more information, see [Branching and Tagging](https://iceberg.apache.org/docs/1.6.0/branching/?h=branch "https://iceberg.apache.org/docs/1.6.0/branching/?h=branch") in Apache Iceberg documentation.

- Snapshot retention and orphan file deletion optimizers will delete files eligible
  for clean-up as per configured parameters. Enhance your control over file deletion by
  implementing S3 versioning and life-cycle policies on the appropriate buckets.

For detailed instructions on setting up versioning and creating life cycle rules, see
[https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md").

- For proper orphan file determination, ensure that the provided table location and any sub-paths don't overlap with or contain data from any other tables or data sources.
  If paths overlap, you risk unrecoverable data loss from unintended deletion of files.

## Debugging `OversizedAllocationException` exception

To resolve an `OversizedAllocationException` exception:

- Reduce the batch size of the vectorized reader and check. The default batch size is 5000. This is controlled in the `read.parquet.vectorization.batch-size`.
  - If this doesn’t work even after multiple variations, turn off vectorization. This is controlled in the `read.parquet.vectorization.enabled`.
  - If this doesn't work even after multiple variations, turn off vectorization. This is controlled in the `read.parquet.vectorization.enabled`.
