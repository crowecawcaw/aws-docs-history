# DB instance billing for Aurora

Amazon RDS provisioned instances in an Amazon Aurora cluster are billed based on the following components:

- DB instance hours (per hour) – Based on the DB instance class of the DB
  instance (for example, db.t2.small or db.m4.large). Pricing is listed on a per-hour
  basis, but bills are calculated down to the second and show times in decimal form.
  RDS usage is billed in 1-second increments, with a minimum of 10 minutes. For more
  information, see [Amazon AuroraDB instance classes](Concepts.md "Concepts.md").
- Storage (per GiB per month) – Storage capacity that you have provisioned to your DB instance. If you scale your provisioned
  storage capacity within the month, your bill is prorated. For more information, see [Amazon Aurora storage](Aurora.Overview.md "Aurora.Overview.md").
- Input/output (I/O) requests (per 1 million requests) – Total number of storage I/O requests that you have made in a billing
  cycle, for the Aurora Standard DB cluster
  configuration only.

For more information on Amazon Aurora I/O billing, see [Storage configurations for Amazon Aurora DB clusters](Aurora.Overview.md#aurora-storage-type "Aurora.Overview.md#aurora-storage-type").

- Backup storage (per GiB per month) – _Backup storage_ is the storage that is associated with automated database backups and any
  active database snapshots that you have taken. Increasing your backup retention
  period or taking additional database snapshots increases the backup storage consumed
  by your database. Per second billing doesn't apply to backup storage (metered
  in GB-month).

For more information, see [Backing up and restoring an Amazon Aurora DB cluster](BackupRestoreAurora.md "BackupRestoreAurora.md").

- Data transfer (per GB) – Data transfer in and out of your DB instance from
  or to the internet and other AWS Regions. For useful examples, see the AWS blog
  post [Exploring Data Transfer Costs for AWS Managed Databases](https://aws.amazon.com/blogs/architecture/exploring-data-transfer-costs-for-aws-managed-databases "https://aws.amazon.com/blogs/architecture/exploring-data-transfer-costs-for-aws-managed-databases").
  Amazon RDS provides the following purchasing options to enable you to optimize your costs based on your needs:

- **On-Demand instances** – Pay by the hour for the DB
  instance hours that you use. Pricing is listed on a per-hour basis, but bills are
  calculated down to the second and show times in decimal form. RDS usage is now
  billed in 1-second increments, with a minimum of 10 minutes.
- **Reserved instances** – Reserve a DB instance for a
  one-year or three-year term and get a significant discount compared to the on-demand
  DB instance pricing. With Reserved Instance usage, you can launch, delete, start, or
  stop multiple instances within an hour and get the Reserved Instance benefit for all
  of the instances.
- **Aurora Serverless v2** – Aurora Serverless v2 provides
  on-demand capacity where the billing unit is Aurora capacity unit (ACU) hours instead
  of DB instance hours. Aurora Serverless v2 capacity increases and decreases, within a
  range that you specify, depending on the load on your database. You can configure a
  cluster where all the capacity is Aurora Serverless v2. Or you can configure a
  combination of Aurora Serverless v2 and on-demand or reserved provisioned instances.
  For information about how Aurora Serverless v2 ACUs work, see [How Aurora Serverless v2 works](aurora-serverless-v2.md "aurora-serverless-v2.md").
- **Aurora PostgreSQL Limitless Database** – Aurora PostgreSQL Limitless Database is an automated, horizontal scaling capability that scales beyond the write throughput and
  storage limits of a single DB instance. Limitless Database distributes the workload over multiple Aurora writer instances, while maintaining the ease of
  operating as a single database. Limitless Database provides on-demand capacity where the billing unit is Aurora capacity unit (ACU) hours in a DB
  shard group. For information about how Limitless Database ACUs work, see [Creating a DB cluster that uses Aurora PostgreSQL Limitless Database](limitless-cluster.md "limitless-cluster.md").
  For Aurora pricing information, see the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing "https://aws.amazon.com/rds/aurora/pricing").

###### Topics

- [On-Demand DB instances for Aurora](USER_OnDemandDBInstances.md "USER_OnDemandDBInstances.md")
- [Reserved DB instances for Amazon Aurora](USER_WorkingWithReservedDBInstances.md "USER_WorkingWithReservedDBInstances.md")
