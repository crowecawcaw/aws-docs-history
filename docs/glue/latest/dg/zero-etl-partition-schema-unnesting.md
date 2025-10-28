#

Partition specification and schema unnesting guide

When working with NoSQL data sources like DynamoDB and SaaS applications, data often presents unique challenges for analytics:

1. Records within the same table may have different schema
2. Nested records within the same table can be represented differently
3. Complex nested structures like maps and arrays require transformation for efficient querying
4. Optimal data organization is needed to ensure query performance at scale

AWS Glue Zero-ETL integrations address these challenges through two powerful capabilities:

- **Schema Unnesting:** Automatically flattens complex nested data structures into analytics-friendly formats,
  with configurable levels of unnesting to balance between preserving data structure and optimizing for query simplicity.
- **Data Partitioning:** Organizes data into logical partitions based on specified columns or time-based dimensions,
  improving query performance and reducing costs by enabling partition pruning during query execution.

In order to query such data sources effectively, AWS Glue Zero-ETL provides out-of-the-box schema handling and partitioning schemes for source data
being replicated in the target AWS Glue Database. You can configure schema unnesting and partitioning settings for each table through the
CreateIntegrationTableProperty API, allowing for fine-tuned control over how data is structured and organized for analytics workloads.

## Default unnesting & partitioning behavior

1. AWS Glue Zero-ETL defaults to FULL Unnest when no Unnesting options are provided for target table
2. AWS Glue Zero-ETL defaults to Bucket partitioning when no PartitionSpec are provided for target table
