# Optimizing query performance for Iceberg tables

Apache Iceberg is a high-performance open table format for huge analytic datasets. AWS Glue
supports calculating and updating number of distinct values (NDVs) for each column in
Iceberg tables. These statistics can facilitate better query optimization, data management,
and performance efficiency for data engineers and scientists working with large-scale
datasets.

AWS Glue estimates the number of distinct values in each column of the Iceberg table and and
store them in [Puffin](https://iceberg.apache.org/puffin-spec/ "https://iceberg.apache.org/puffin-spec/") files on Amazon S3
associated with Iceberg table snapshots. Puffin is an Iceberg file format designed to store
metadata like indexes, statistics, and sketches. Storing sketches in Puffin files tied to
snapshots ensures transactional consistency and freshness of the NDV statistics.

You can configure to run column statistics generation task using AWS Glue console or AWS CLI.
When you initiate the process, AWS Glue starts a Spark job in the background and updates the
AWS Glue table metadata in the Data Catalog. You can view column statistics using AWS Glue console or
AWS CLI or by calling the [GetColumnStatisticsForTable](../webapi/API_GetColumnStatisticsForTable.md "../webapi/API_GetColumnStatisticsForTable.md") API operation.

###### Note

If you're using AWS Lake Formation permissions to control access to the table, the role assumed by the column statistics task requires full table access to generate statistics.

###### Topics

- [Prerequisites for generating column
  statistics](iceberg-column-stats-prereqs.md "iceberg-column-stats-prereqs.md")
- [Generating column statistics for Iceberg tables](iceberg-generate-column-stats.md "iceberg-generate-column-stats.md")
- [See also](#see-also-iceberg-stats "#see-also-iceberg-stats")

## See also

- [Viewing column statistics](view-column-stats.md "view-column-stats.md")
- [Viewing column statistics task runs](view-stats-run.md "view-stats-run.md")
- [Stopping column statistics task run](stop-stats-run.md "stop-stats-run.md")
- [Deleting column statistics](delete-column-stats.md "delete-column-stats.md")
