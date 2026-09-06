

# Table maintenance
<a name="msk-data-delivery-iceberg-maintenance"></a>

S3 Tables provides optional automated table maintenance jobs — compaction, snapshot expiration, and unreferenced file cleanup. Enabling these jobs is recommended: they optimize query performance by merging small data files, reduce storage costs by removing obsolete snapshots, and prevent metadata bloat over time as the Channel continuously writes to your table.

You can also enable a record expiration job to automatically delete records older than a specified retention period when your table is partitioned by a `timestamptz` column. This helps you manage storage costs and meet data-retention requirements without running manual delete operations against your Iceberg table.

For more details, see [S3 Tables maintenance overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance-overview.html) in the *Amazon S3 User Guide*.