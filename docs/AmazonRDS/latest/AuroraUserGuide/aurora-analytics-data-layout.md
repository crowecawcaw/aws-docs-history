

# Optimizing data layout in Amazon S3
<a name="aurora-analytics-data-layout"></a>

Aurora PostgreSQL scans columnar data in Amazon S3, so your data layout determines how much data each query reads. Follow these practices.
+ **Avoid many small files**: Consolidate data into fewer, larger files. Reading many small files adds per-file metadata and Amazon S3 request overhead.
+ **Use a reasonable row group size**: Row groups let the engine read and skip data in chunks using min/max statistics. Very small row groups add per-group overhead, while very large ones reduce how precisely the engine can skip data that a query does not need.
+ **Partition on your filter columns**: Partitioning splits data into separate paths by column value, so a query that filters on a partition column skips entire partitions without reading them.

For detailed guidance, see [Optimize data](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html) in the *Amazon Athena User Guide*.