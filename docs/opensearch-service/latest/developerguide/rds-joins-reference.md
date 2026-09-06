

# Joining data from multiple tables
<a name="rds-joins-reference"></a>

You can configure denormalized joins to automatically merge data from multiple related tables into single OpenSearch documents. This feature supports one-to-one and one-to-many relationships between parent and child tables. The pipeline reads change data capture (CDC) events from all configured tables and merges them into a parent document.

The joins configuration is the same for both Amazon RDS and Aurora sources. For configuration details and examples, see [Joining data from multiple tables to ingest into one document](aurora-denormalized-joins.md).