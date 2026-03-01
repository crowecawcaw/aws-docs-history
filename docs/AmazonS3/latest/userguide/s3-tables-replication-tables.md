# Replicating S3 tables

Amazon S3 Tables support automatic replication of Apache Iceberg tables stored in Amazon S3 table buckets. Replication destinations can be within the same AWS Region,
across multiple AWS Regions, the same account, or to other AWS accounts. By configuring replication for your tables, you can maintain read-only replicas of your
data across multiple locations. You can use replicas to enhance data availability, meet compliance requirements and increase access performance for distributed applications.

S3 Tables replication maintains data consistency by committing all table updates, including snapshots, metadata, and data files, to the destination table in the same order as the source table.

## When to use S3 Tables replication

You can use S3 Tables replication for the following purposes:

- Minimize latency – If your customers are in two geographic locations, you can minimize latency when accessing tables by
  maintaining read replicas in AWS Regions that are geographically closer to your users.
- Regulatory compliance – You can maintain read replicas in specific geographic locations or AWS accounts, which might help
  you meet certain regulatory or compliance requirements. You can configure the replication destination table bucket to encrypt tables with different AWS KMS keys than the source.
- Centralized analytics – If you have data distributed across
  multiple AWS Regions, you can replicate Region-specific datasets to a centralized Region for
  unified reporting, cross-Region analysis, and machine learning model training. This eliminates
  the need to query across Regions or build custom data aggregation pipelines.
- Testing and development environments – You can create read replicas of production tables in separate AWS accounts or table buckets to provide realistic test data for development and QA teams. This isolates testing workloads from production systems while ensuring test environments have current, production-like data without manual exports or data synchronization processes.

## Features

S3 Tables replication offers the following features.

###### Read-only replicas for S3 Tables

S3 Tables replication creates read-only replicas of your Apache Iceberg tables across table buckets. You can query replicas independently using any Iceberg-compatible engine.

###### Automatically maintained replicas

The S3 Tables replication service automatically maintains replica tables. Replication
typically updates replicas within minutes of updates to the source. S3 Tables commits all
updates in the same order as the source table to maintain consistency.

###### Replication to multiple destinations

You can replicate the same table to multiple destination table buckets. Replication
destinations can be within the same AWS Region, across multiple AWS Regions, in the same AWS account, or in other AWS accounts.

###### Independent snapshot retention

Snapshot expiration for replica tables is independent of the source table, allowing you to set different retention periods on replica tables if needed. For example, you can
configure your source table to retain snapshots for 30 days while setting a 90-day retention period for replica tables. If you configure a longer retention period on replicas,
snapshots that expire at the source remain available and queryable in replicas. This configuration provides extended time-travel capabilities for historical analysis.

###### Maintain replica tables in lower-cost storage tiers

You can configure destination table buckets to use the S3 Intelligent-Tiering storage
class, which automatically optimizes storage costs based on access patterns without performance
impact or operational overhead. S3 Intelligent-Tiering is well-suited for replica tables that
may be accessed less frequently.

For more information about S3 Tables replication, see the following topics.

###### Topics

- [How S3 Tables replication works](s3-tables-replication-how-replication-works.md "s3-tables-replication-how-replication-works.md")
- [Setting up S3 Tables replication](s3-tables-replication-setting-up.md "s3-tables-replication-setting-up.md")
- [Managing S3 Tables replication](s3-tables-replication-managing.md "s3-tables-replication-managing.md")
