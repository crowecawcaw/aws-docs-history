# Working with Amazon Keyspaces (for Apache Cassandra) features

This chapter provides details about working with Amazon Keyspaces and various database features, for example backup and restore, Time to Live, and multi-Region replication.

- **Time to Live** – Amazon Keyspaces expires data from tables automatically based on the Time to Live value you set. Learn how
  to configure TTL and how to use it in your tables.
- **PITR** – Protect your Amazon Keyspaces tables from accidental write or delete operations by creating
  continuous backups of your table data. Learn how to configure PITR on your tables and how to restore a table to a specific point in time or how
  to restore a table that has been accidentally deleted.
- **Working with multi-Region tables** – Multi-Region tables in Amazon Keyspaces must have write throughput
  capacity configured in either on-demand or provisioned capacity mode with auto scaling. Plan the throughput capacity needs by estimating the required
  write capacity units (WCUs) for each Region, and provision the sum of writes from all Regions to ensure sufficient capacity for
  replicated writes.
- **Amazon Keyspaces change data capture (CDC)** – Amazon Keyspaces CDC streams
  record row-level change events from your table in near-real time. Learn how to use the Kinesis Client Library (KCL) to consume and process data from Amazon Keyspaces CDC streams.
- **Queries and pagination** – Amazon Keyspaces supports advanced querying capabilities like
  using the `IN` operator with `SELECT` statements,
  ordering results with `ORDER BY`, and automatic pagination of large result sets. This section explains how Amazon Keyspaces processes
  these queries and provides examples.
- **Partitioners** – Amazon Keyspaces provides three partitioners: `Murmur3Partitioner` (default),
  `RandomPartitioner`, and `DefaultPartitioner`. You can change the partitioner per Region at the account level using the AWS Management Console or Cassandra Query Language (CQL).
- **Client-side timestamps** – Client-side timestamps are Cassandra-compatible
  timestamps that Amazon Keyspaces persists for each cell in your table. Use client-side timestamps for conflict resolution
  and to let your client application determine the order of writes.
- **User-defined types (UDTs)** – With UDTs you can define data structures in your applications
  that represent real-world data hierarchies.
- **Tagging resources** – You can label Amazon Keyspaces resources like keyspaces and tables using tags.
  Tags help categorize resources, enable cost tracking, and let you configure access control based on tags. This section covers tagging restrictions, operations, and
  best practices for Amazon Keyspaces.
- **CloudFormation templates** – CloudFormation helps you model and set up your Amazon Keyspaces keyspaces and tables so that you can spend less time creating
  and managing your resources and infrastructure.

###### Topics

- [System keyspaces in Amazon Keyspaces](working-with-keyspaces.md "working-with-keyspaces.md")
- [User-defined types (UDTs) in Amazon Keyspaces](udts.md "udts.md")
- [Working with CQL queries in Amazon Keyspaces](working-with-queries.md "working-with-queries.md")
- [Working with change data capture (CDC) streams in Amazon Keyspaces](cdc.md "cdc.md")
- [Working with partitioners in Amazon Keyspaces](working-with-partitioners.md "working-with-partitioners.md")
- [Client-side timestamps in Amazon Keyspaces](client-side-timestamps.md "client-side-timestamps.md")
- [Multi-Region replication for Amazon Keyspaces (for Apache Cassandra)](multiRegion-replication.md "multiRegion-replication.md")
- [Backup and restore data with point-in-time recovery for Amazon Keyspaces](PointInTimeRecovery.md "PointInTimeRecovery.md")
- [Expire data with Time to Live (TTL) for Amazon Keyspaces (for Apache Cassandra)](TTL.md "TTL.md")
- [Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md")
- [Working with tags and labels for Amazon Keyspaces resources](tagging-keyspaces.md "tagging-keyspaces.md")
- [Create Amazon Keyspaces resources with AWS CloudFormation](creating-resources-with-cloudformation.md "creating-resources-with-cloudformation.md")
- [Using NoSQL Workbench with Amazon Keyspaces (for Apache Cassandra)](workbench.md "workbench.md")
