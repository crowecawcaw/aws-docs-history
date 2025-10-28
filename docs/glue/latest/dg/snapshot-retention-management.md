# Snapshot retention optimization

Apache Iceberg snapshot retention feature allows users to query historical data at
specific points in time and revert unwanted modifications to their tables. In the AWS Glue Data Catalog,
snapshot retention configuration controls how long these snapshots (versions of the table
data) are kept before being expired and removed. This helps manage storage costs and metadata
overhead by automatically removing older snapshots based on a configured retention period or
maximum number of snapshots to keep.

You can configure the retention period in days and the maximum number of snapshots to
retain for a table. AWS Glue removes snapshots that are older than the specified retention period
from the table metadata, while keeping the most recent snapshots up to the configured limit.
After removing old snapshots from the metadata, AWS Glue deletes the corresponding data and
metadata files that are no longer referenced and unique to the expired snapshots. This allows
time travel queries only up to the remaining retained snapshots, while reclaiming storage
space used by expired snapshot data.

###### Topics

- [Enabling snapshot retention optimizer](enable-snapshot-retention.md "enable-snapshot-retention.md")
- [Updating snapshot retention optimizer](update-snapshot-retention.md "update-snapshot-retention.md")
- [Disabling snapshot retention optimizer](disable-snapshot-retention.md "disable-snapshot-retention.md")
