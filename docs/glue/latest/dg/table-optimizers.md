# Optimizing Iceberg tables

AWS Glue supports mutiple table optimization options to enhance the management and
performance of Apache Iceberg tables used by the AWS analytical engines and ETL jobs. These
optimizers provide efficient storage utilization, improved query performance, and effective data
management. There are three types of table optimizers available in AWS Glue:

- **Compaction** – Data compaction compacts small data files
  to reduce storage usage and improve read performance. Data files are merged and rewritten to
  remove obsolete data and consolidate fragmented data into larger, more efficient files. You
  can configure compaction to run automatically.

Binpack is the default compaction strategy in Apache Iceberg. It combines smaller data
files into larger ones for optimal performance. Compaction also supports sort and Z-order
strategies that cluster similar data together. Sort organizes data based on specified
columns, improving query performance for filtered operations. Z-order creates sorted
datasets that enhance query performance when multiple columns are queried simultaneously.
All three compaction strategies - bincpak, sort, and Z-order - reduce the amount of data
scanned by query engines, thereby lowering query processing costs.

- **Snapshot retention** – Snapshots are timestamped versions
  of an Iceberg table. Snapshot retention configurations allow customers to enforce how long
  to retain snapshots and how many snapshots to retain. Configuring a snapshot retention
  optimizer can help manage storage overhead by removing older, unnecessary snapshots and
  their associated underlying files.
- **Orphan file deletion** – Orphan files are files that are no longer referenced by the Iceberg table metadata. These files can
  accumulate over time, especially after operations like table deletions or failed ETL jobs.
  Enabling orphan file deletion allows AWS Glue to periodically identify and remove these
  unnecessary files, freeing up storage.
  Catalog-level optimization configuration is available through the Lake Formation console and using
  the AWS Glue `UpdateCatalog` API operation. You can enable or disable compaction,
  snapshot retention, and orphan file deletion optimizers for individual Iceberg tables in the
  Data Catalog using the AWS Glue console, AWS CLI, or AWS Glue API operations.

The following video demonstrates how to configure optimizers for Iceberg tables in the Data Catalog.

###### Topics

- [Table optimization prerequisites](optimization-prerequisites.md "optimization-prerequisites.md")
- [Catalog-level table optimizers](catalog-level-optimizers.md "catalog-level-optimizers.md")
- [Compaction optimization](compaction-management.md "compaction-management.md")
- [Snapshot retention optimization](snapshot-retention-management.md "snapshot-retention-management.md")
- [Deleting orphan files](orphan-file-deletion.md "orphan-file-deletion.md")
- [Viewing optimization details](view-optimization-status.md "view-optimization-status.md")
- [Viewing Amazon CloudWatch metrics](view-optimization-metrics.md "view-optimization-metrics.md")
- [Deleting an optimizer](delete-optimizer.md "delete-optimizer.md")
- [Considerations and limitations](optimizer-notes.md "optimizer-notes.md")
- [Supported Regions for table optimizers](regions-optimizers.md "regions-optimizers.md")
