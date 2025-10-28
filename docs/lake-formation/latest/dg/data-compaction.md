# Optimizing Iceberg tables

Lake Formation supports multiple table optimization options to enhance the management and
performance of Apache Iceberg tables used by the AWS analytical engines and ETL jobs.
These optimizers provide efficient storage utilization, improved query performance, and
effective data management. There are three types of table optimizers available in Lake Formation:

- **Compaction** – Data compaction compacts small data files
  to reduce storage usage and improve read performance. Data files are merged and rewritten to
  remove obsolete data and consolidate fragmented data into larger, more efficient files.
  Compaction can be configured to run automatically or manually triggered as needed.
- **Snapshot retention** – Snapshots are timestamped versions
  of an Iceberg table. Snapshot retention configurations allow customers to enforce how long
  to retain snapshots and how many snapshots to retain. Configuring a snapshot retention
  optimizer can help manage storage overhead by removing older, unnecessary snapshots and
  their associated underlying files.
- **Orphan file deletion** – Orphan files are files that are no longer referenced by the Iceberg table metadata. These files can
  accumulate over time, especially after operations like table deletions or failed ETL jobs.
  Enabling orphan file deletion allows AWS Glue to periodically identify and remove these
  unnecessary files, freeing up storage.
  You can enable or disable compaction, snapshot retention, and orphan file deletion
  optimizers for individual Iceberg tables in the Data Catalog using the AWS Glue console, AWS CLI, or
  AWS Glue API operations.

For more information, see [Optimizing Iceberg tables](../../../glue/latest/dg/table-optimizers.md "../../../glue/latest/dg/table-optimizers.md") in the AWS Glue Developer Guide.
