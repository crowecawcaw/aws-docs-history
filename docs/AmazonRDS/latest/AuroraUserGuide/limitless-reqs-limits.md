# Aurora PostgreSQL Limitless Database requirements and considerations

Aurora PostgreSQL Limitless Database has the following requirements and considerations.

###### Topics

- [Requirements for Aurora PostgreSQL Limitless Database](#limitless-requirements "#limitless-requirements")
- [Considerations for Aurora PostgreSQL Limitless Database](#limitless-limitations "#limitless-limitations")
- [Features not supported in Aurora PostgreSQL Limitless Database](#limitless-not-supported "#limitless-not-supported")

## Requirements for Aurora PostgreSQL Limitless Database

Make sure to follow these requirements for Aurora PostgreSQL Limitless Database.

- Aurora PostgreSQL Limitless Database is available in all AWS Regions except Asia Pacific (Taipei).

###### Note

If you create your Aurora PostgreSQL Limitless Database DB cluster in US East (N. Virginia), don't include the `us-east-1e` Availability Zone
(AZ) in your DB subnet group. Because of resource limitations, Aurora Serverless v2 (and therefore
Aurora PostgreSQL Limitless Database) isn't supported in the `us-east-1e` AZ.

- Aurora PostgreSQL Limitless Database supports only the Aurora I/O-Optimized DB cluster storage configuration. For more information, see [Storage configurations for Amazon Aurora DB clusters](Aurora.Overview.md#aurora-storage-type "Aurora.Overview.md#aurora-storage-type").
- Aurora PostgreSQL Limitless Database uses special Aurora PostgreSQL DB engine versions for Aurora PostgreSQL Limitless Database:
  - `16.6.8-limitless`
  - `16.6-limitless`
  - `16.4-limitless`

- Your DB cluster can't have any writer or reader DB instances.
- You must use Enhanced Monitoring and Performance Insights. The Performance Insights retention time must be at least 1 month (31 days).
- You must export the PostgreSQL log to Amazon CloudWatch Logs.

###### Note

Some required features, such as Enhanced Monitoring, Performance Insights, and CloudWatch Logs, incur extra charges. For Aurora pricing information, see the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing "https://aws.amazon.com/rds/aurora/pricing").

## Considerations for Aurora PostgreSQL Limitless Database

The following considerations apply to DB shard groups in Aurora PostgreSQL Limitless Database:

- You can have only one DB shard group per DB cluster.
- You can have up to five DB shard groups per AWS Region.

Therefore, you can have up to five Aurora PostgreSQL Limitless Database DB clusters per AWS Region. For more information, see [Quotas in Amazon Aurora](CHAP_Limits.md#RDS_Limits.Limits "CHAP_Limits.md#RDS_Limits.Limits").

- You can set the maximum capacity of a DB shard group to 16–6144 ACUs. For capacity limits higher than 6144 ACUs, contact AWS.

The initial number of routers and shards is determined by the maximum capacity that you set when you create a DB shard
group. For more information, see [Correlating DB shard group maximum capacity with the number of routers and shards created](limitless-cluster.md#limitless-capacity-mapping "limitless-cluster.md#limitless-capacity-mapping").

- The number of routers and shards doesn't change when you modify the maximum capacity of a DB shard group.
- Make sure that the DB subnet where you create the DB shard group has enough free IP addresses for connecting with the DB shard group. You
  need one IP address for each router and up to three IP addresses for each shard in the DB shard group.

For more information on the number of routers created when you create a DB shard group, see [Correlating DB shard group maximum capacity with the number of routers and shards created](limitless-cluster.md#limitless-capacity-mapping "limitless-cluster.md#limitless-capacity-mapping").

- If you make your DB shard group publicly accessible, make sure to set up an internet gateway in your VPC.
- You use SQL functions to [split shards](limitless-shard-split.md "limitless-shard-split.md") and [add routers](limitless-add-router.md "limitless-add-router.md").
- Merging shards isn't supported.
- You can't delete individual shards and routers.
- You can't modify (perform `UPDATE` operations on) shard keys in any way, including changing their values in
  table rows.

To change a shard key, delete and then re-create it.

- The repeatable read, read committed, and read uncommitted isolation levels are supported. You can't set the isolation level to
  serializable.
- Some SQL commands aren't supported. For more information, see [Aurora PostgreSQL Limitless Database reference](limitless-reference.md "limitless-reference.md").
- Not all PostgreSQL extensions are supported. For more information, see [Extensions](limitless-reference.md#limitless-reference.DDL-limitations.Extensions "limitless-reference.md#limitless-reference.DDL-limitations.Extensions").
- When creating a shard group, or when adding new shard group nodes (shards or routers), those nodes are created in one of the Availability
  Zones (AZs) available to the DB cluster. You can't choose a specific AZ for individual nodes.
- If you use a compute redundancy of 2 (two compute standbys for the DB shard group), make sure that your DB subnet group has at least three
  AZs.
- Aurora PostgreSQL Limitless Database supports up to 54 characters for sharded table names.

The following considerations apply to the Aurora PostgreSQL Limitless Database DB cluster:

- We recommend that you use AWS managed policies to limit permissions for your database and applications to those that customers need for
  their use cases. For more information, see [Policy best practices](security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices "security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices").
- When you create your Aurora PostgreSQL Limitless Database DB cluster, you only set scaling parameters for the DB shard group.
- If you need to delete your DB cluster, you must delete the DB shard group first.
- Aurora PostgreSQL Limitless Database can't be a replication source.

## Features not supported in Aurora PostgreSQL Limitless Database

The following Aurora PostgreSQL features aren't supported in Aurora PostgreSQL Limitless Database:

- Active Directory (Kerberos) authentication
- Amazon DevOps Guru
- Amazon ElastiCache
- Amazon RDS Blue/Green Deployments
- Amazon RDS Proxy
- Aurora Auto Scaling (adding reader instances to the DB cluster automatically)
- Aurora Global Database
- Aurora machine learning
- Aurora recommendations
- Aurora Serverless v1
- Aurora zero-ETL integrations
- AWS Backup
- AWS Lambda integration
- AWS Secrets Manager
- Babelfish for Aurora PostgreSQL
- Cloning DB clusters
- Custom endpoints
- Database activity streams
- Read replicas
- RDS Data API
