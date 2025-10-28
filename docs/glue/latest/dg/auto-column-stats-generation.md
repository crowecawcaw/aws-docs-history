# Automatic column statistics generation

Automatic generation of column statistics allows you to schedule and automatically
compute statistics on new tables in the AWS Glue Data Catalog. When you enable automatic
statistics generation, the Data Catalog discovers new tables with specific data formats such
as Parquet, JSON, CSV, XML, ORC, ION, and Apache Iceberg, along with their individual
bucket paths. With a one-time catalog configuration, the Data Catalog generates statistics
for these tables.

Data lake administrators can configure the statistics generation by selecting the
default catalog in the Lake Formation console, and enabling table statistics using the
`Optimization configuration` option. When you create new tables or update
existing tables in the Data Catalog, the Data Catalog collects the number of distinct values
(NDVs) for Apache Iceberg tables, and additional statistics such as the number of nulls,
maximum, minimum, and average length for other supported file formats on a weekly basis.

If you have configured statistics generation at the table-level or if you have
previously deleted the statistics generation settings for a table, those table-specific
settings take precedence over the default catalog settings for automatic column
statistics generation.

Automatic statistics generation task analyzes 50% of records in the tables to
calculate statistics. Automatic column statistics generation ensures that the Data Catalog
maintains weekly metrics that can be used by query engines like Amazon Athena and Amazon Redshift Spectrum
for improved query performance and potential cost savings. It allows scheduling
statistics generation using AWS Glue APIs or the console, providing an automated process
without manual intervention.

###### Topics

- [Enabling catalog-level automatic statistics generation](enable-auto-column-stats-generation.md "enable-auto-column-stats-generation.md")
- [Viewing automated table-level settings](view-auto-column-stats-settings.md "view-auto-column-stats-settings.md")
- [Disabling catalog-level column statistics generation](disable-auto-column-stats-generation.md "disable-auto-column-stats-generation.md")
