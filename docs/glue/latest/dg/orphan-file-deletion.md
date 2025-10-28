# Deleting orphan files

AWS Glue Data Catalog allows you to remove orphan files from your Iceberg tables. Orphan files
are unreferenced files that exist in your Amazon S3 data source under the specified table location,
are not tracked by the Iceberg table metadata, and are older than your configured age limit.
These orphan files can accumulate over time due to failure in operations like compaction,
partition drops, or table rewrites, and take up unnecessary storage space.

The orphan file deletion optimizer in AWS Glue scans the table metadata and the actual
data files, identifies the orphan files, and deletes them to reclaim storage space. The
optimizer only removes files created after the optimizer's creation date that also meet the
configured deletion criteria. Files created before or on the optimizer creation date are never
deleted.

**Orphan file deletion logic**

1. Date check – Compares file creation date with optimizer creation date. If file is older
   than or equal to optimizer creation date, the file is skipped.
2. Optimizer configuration check – If file is newer than optimizer creation date, evaluates
   the file against the configured age limit. The optimizer deletes the file if it matches
   the deletion critera. Skips the file, if it doesn't match the criteria.
   You can initiate the orphan file deletion by creating an orphan file deletion
   table optimizer in the Data Catalog.

###### Important

By default, orphan file deletion evaluates files across your AWS Glue table location.
While you can configure a sub-prefix to limit the scope of evaluation by using API
parameter, you must ensure your table location doesn't contain files from other data sources
or tables. If your table location overlaps with other data sources, the service might
identify and delete unrelated files as orphans.

###### Topics

- [Enabling orphan file deletion](enable-orphan-file-deletion.md "enable-orphan-file-deletion.md")
- [Updating orphan file deletion optimizer](update-orphan-file-deletion.md "update-orphan-file-deletion.md")
- [Disabling orphan file deletion](disable-orphan-file-deletion.md "disable-orphan-file-deletion.md")
