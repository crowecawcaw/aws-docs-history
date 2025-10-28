# S3 Tables maintenance

Amazon S3 automatically performs maintenance to enhance the performance of your
tables in S3 table buckets. Maintenance is performed at the table bucket and individual table level and includes the following:

**Table bucket-level maintenance:**

- **Unreferenced file removal** – Cleans up orphaned files to optimize storage usage and costs

**Table-level maintenance:**

- **File compaction** – Consolidates small files to improve query performance
  and reduce storage costs.
- **Snapshot management** – Controls table version history and prevents
  excessive metadata growth.

These options are enabled by default. You can edit or disable these operations through maintenance configuration files.

###### Topics

- [S3 Tables maintenance job status](s3-tables-maintenance-status.md "s3-tables-maintenance-status.md")
- [Maintenance for table buckets](s3-table-buckets-maintenance.md "s3-table-buckets-maintenance.md")
- [Maintenance for tables](s3-tables-maintenance.md "s3-tables-maintenance.md")
- [Considerations and limitations for maintenance jobs](s3-tables-considerations.md "s3-tables-considerations.md")
