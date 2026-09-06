

# Availability and Durability
<a name="aurora-faq-availability-and-durability"></a>

**Topics**
+ [How does Amazon Aurora store data for high availability?](#aurora-faq-how-does-amazon-aurora-store-data-for-high-availability)
+ [How does Amazon Aurora recover after a database crash?](#aurora-faq-how-does-amazon-aurora-recover-after-a-database-crash)
+ [Are automated backups enabled on Amazon Aurora?](#aurora-faq-are-automated-backups-enabled-on-amazon-aurora)
+ [What happens to my data if I delete my Aurora DB instance?](#aurora-faq-what-happens-to-my-data-if-i-delete-my-aurora-db-instance)
+ [Can I control which replica gets promoted during failover?](#aurora-faq-can-i-control-which-replica-gets-promoted-during-failover)
+ [Can I prevent a specific replica from being promoted?](#aurora-faq-can-i-prevent-a-specific-replica-from-being-promoted)
+ [How can I increase database availability?](#aurora-faq-how-can-i-increase-database-availability)
+ [What is Amazon Aurora Global Database?](#aurora-faq-what-is-amazon-aurora-global-database)
+ [Can I use database activity streams with Aurora Global Database?](#aurora-faq-can-i-use-database-activity-streams-with-aurora-global-datab)
+ [Do I need to update my application code if my primary Region becomes unavailable?](#aurora-faq-do-i-need-to-update-my-application-code-if-my-primary-region)
+ [Can I set up cross-Region replicas?](#aurora-faq-can-i-set-up-cross-region-replicas)
+ [Can I add replicas to a cross-Region Aurora cluster?](#aurora-faq-can-i-add-replicas-to-a-cross-region-aurora-cluster)
+ [Can I promote a cross-Region replica to primary?](#aurora-faq-can-i-promote-a-cross-region-replica-to-primary)
+ [What is the replication lag for replicas in Aurora?](#aurora-faq-what-is-the-replication-lag-for-replicas-in-aurora)

## How does Amazon Aurora store data for high availability?
<a name="aurora-faq-how-does-amazon-aurora-store-data-for-high-availability"></a>

Amazon Aurora automatically divides your database volume into 10 GiB segments spread across many disks. Each segment is replicated six ways across three Availability Zones (AZs). Aurora is designed to transparently handle:
+ Loss of up to two copies of data without affecting database write availability
+ Loss of up to three copies without affecting read availability

[Aurora storage is also self-healing](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability) — data blocks and disks are continuously scanned for errors and repaired automatically.

## How does Amazon Aurora recover after a database crash?
<a name="aurora-faq-how-does-amazon-aurora-recover-after-a-database-crash"></a>

Unlike other databases, Aurora does not need to replay the redo log from the last checkpoint after a crash. This reduces database restart times to less than 60 seconds in most cases. Aurora also moves the buffer cache out of the database process and makes it available immediately at restart, preventing brownouts while the cache repopulates.

## Are automated backups enabled on Amazon Aurora?
<a name="aurora-faq-are-automated-backups-enabled-on-amazon-aurora"></a>

Yes, automated continuous [backups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups) are always enabled on Amazon Aurora DB Instances with no database performance impact. Aurora automatically makes your data durable across three AZs and will attempt to recover your database in a healthy AZ with no data loss. You can also perform point-in-time restore operations (up to five minutes in the past) or restore from DB snapshots. Can I take manual snapshotsof my Aurora database?

Yes, and there is no performance impact when taking[ snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CreateSnapshotCluster). Note that restoring data from  snapshots requires the creation of a new DB Instance.

If my database fails, what is my recovery path?

Amazon Aurora automatically makes your data durable across three AZs in a Region and will automatically attempt to recover your database in a healthy AZ with no data loss. In the unlikely event your data is unavailable within Amazon Aurora storage, you can restore from a DB snapshot or perform a point-in-time restore operation to a new instance. Note that the latest restorable time for a point-in-time restore operation can be up to five minutes in the past.

## What happens to my data if I delete my Aurora DB instance?
<a name="aurora-faq-what-happens-to-my-data-if-i-delete-my-aurora-db-instance"></a>

You can choose to create a final DB snapshot when deleting your DB Instance. You can use this snapshot to restore the deleted DB Instance at a later date. Amazon Aurora retains this final user-created DB Snapshot along with all other manually created DB Snapshots after the DB Instance is deleted. Automated backups created for point-in-time restore are not kept after deletion.

Can I share my snapshots with another AWS account?

Yes. You can share a snapshot with up to 20 AWS account IDs or make them public. Shared snapshots are accessible only within the same AWS Region. Encrypted Aurora snapshots can also be shared.

You can use this feature to share data between your various environments (production, dev/test, staging, etc.) that have different AWS accounts, as well as keep backups of all your data secure in a separate account in case your main AWS account is ever compromised.

Can I automatically share snapshots?

No. Automatic sharing of DB snapshots is not supported. To share a snapshot, you must manually create a copy of the snapshot and then share the copy.

Will I be billed for shared snapshots?

There is no charge for sharing snapshots between accounts. However, you may be charged for the snapshots themselves and any databases restored from them. Learn more about [Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/).

How does failover work in Amazon Aurora?

Failover is handled automatically. The process depends on your configuration.

With replicas, Aurora flips the canonical name record (CNAME) to point at the healthy replica, which is promoted to new primary. Failover typically completes within 30 seconds. For faster failovers,  use [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/) which automatically connect to the failover instance while preserving application connections – reducing failover times by up to 66%.

Aurora serverless works like provisioned for failover and high availability.

For single instance (no replicas, Aurora attempts to create a new DB Instance in the same AZ as the original instance on a best-effort basis. For example, it may not succeed if there is an issue that is broadly affecting the AZ.

Your application should retry database connections in the event of connection loss. Disaster recovery across Regions is a manual process, where you promote a secondary Region to take read/write workloads.

You can assign priority tiers to replicas to control which one gets promoted first. To increase availability, create 1–15 replicas across any of three AZs.

If I have a primary database and a replica actively taking read traffic in Aurora and a failover occurs, what happens?

Amazon Aurora will automatically detect a problem with your primary instance and trigger a failover. If you are using the Cluster Endpoint, your replica will be promoted to the primary. Read traffic that your replicas were serving will be briefly interrupted and directed to the newly promoted Aurora Replica until the old primary node is recovered as a replica.

## Can I control which replica gets promoted during failover?
<a name="aurora-faq-can-i-control-which-replica-gets-promoted-during-failover"></a>

Yes. You can assign a promotion priority tier to each instance on your cluster. When the primary instance fails, Amazon RDS promotes the replica with the highest priority. If two or more replicas share the same priority, Amazon RDS promotes the largest one. You can modify priority tiers at any time without triggering a failover. For more information, read the [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview).

## Can I prevent a specific replica from being promoted?
<a name="aurora-faq-can-i-prevent-a-specific-replica-from-being-promoted"></a>

You can assign lower priority tiers to replicas you don't want promoted to primary. However, if the higher priority replicas on the cluster are unhealthy or unavailable, Amazon RDS will promote the lower priority replica.

## How can I increase database availability?
<a name="aurora-faq-how-can-i-increase-database-availability"></a>

You can add replicas. Any replica can be promoted to primary without any data loss, enhancing fault tolerance. Simply create 1 to 15 replicas in any of three AZs, and Amazon Aurora will automatically include them in failover primary selection. You can use [Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/) if you want your database to span multiple AWS Regions for disaster recovery from region-wide outages.

## What is Amazon Aurora Global Database?
<a name="aurora-faq-what-is-amazon-aurora-global-database"></a>

[Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/) allows a single Aurora database to span multiple AWS Regions. It replicates your data with no impact on database performance, enables fast local reads with typical latency of under one second, and provides disaster recovery from region-wide outages.

Key capabilities:
+ Promote a secondary region to full read/write in under one minute
+ Create up to 10 secondary Regions
+ Supports mixed provisioned/serverless instance types between regions
+ Available for both Aurora MySQL and Aurora PostgreSQL

How do I create an Amazon Aurora Global Database?

To get started, you can use the Amazon RDS console, AWS SDK, or AWS CLI to create an Aurora Global Database. You can use a mixed configuration of provisioned or serverless instance class types between your primary and secondary Regions. You can also configure your primary Region as the Aurora I/O-Optimized cluster configuration and your secondary Regions as Aurora Standard or the reverse. To learn more, visit [Creating an Amazon Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-creating.html).

## Can I use database activity streams with Aurora Global Database?
<a name="aurora-faq-can-i-use-database-activity-streams-with-aurora-global-datab"></a>

Yes. If your goal is to analyze database activity, consider using Aurora advanced auditing, general logs, and slow query logs instead, to avoid impacting the performance of your database.

## Do I need to update my application code if my primary Region becomes unavailable?
<a name="aurora-faq-do-i-need-to-update-my-application-code-if-my-primary-region"></a>

No. If your primary Region becomes unavailable, you can use the managed cross-Region Aurora Global Database failover operation to promote a secondary Region. You can also use the Aurora Global Database writer endpoint to avoid the need to make application code changes. To learn more, visit [Connecting to an Amazon Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-connecting.html).

What types of replicas does Aurora support?

Aurora supports multiple replication options:

For cross-Region replication, use Aurora Global Database for physical replication with sub-second latency, or native logical replication (binlog for MySQL, replication slots for PostgreSQL).

## Can I set up cross-Region replicas?
<a name="aurora-faq-can-i-set-up-cross-region-replicas"></a>

Yes, you can set up cross-Region replicas using either physical or logical replication. Physical replication, called [Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/), uses dedicated infrastructure and can replicate up to five secondary Regions with typical latency of under a second. It is available for both Aurora MySQL and Aurora PostgreSQL. For low-latency global reads and disaster recovery, we recommend using Amazon Aurora Global Database.

## Can I add replicas to a cross-Region Aurora cluster?
<a name="aurora-faq-can-i-add-replicas-to-a-cross-region-aurora-cluster"></a>

Yes, you can add up to 15 replicas on each cross-Region Aurora cluster. They share the same underlying storage as the cross-Region replica and typically lag behind the primary by tens of milliseconds.

## Can I promote a cross-Region replica to primary?
<a name="aurora-faq-can-i-promote-a-cross-region-replica-to-primary"></a>

Yes. For logical (binlog) replication, the promotion process typically takes a few minutes depending on your workload. With Amazon Aurora Global Database, you can promote a secondary Region to take full read/write workloads in under a minute.

## What is the replication lag for replicas in Aurora?
<a name="aurora-faq-what-is-the-replication-lag-for-replicas-in-aurora"></a>

Since replicas share the same data volume as the primary instance in the same AWS Region, there is virtually no replication lag. We typically observe lag times in the tens of milliseconds. For cross-Region replication, binlog-based logical replication lag can grow indefinitely based on change/apply rate and network delays, but under typical conditions, under a minute of replication lag is common. Cross-Region replicas using Aurora Global Database's physical replication will have a typical lag of under a second.

Can I set up binlog replication with an external MySQL database?

Yes, you can set up binlog replication between an Aurora MySQL instance and an external MySQL database. The other database can run on Amazon RDS, as a self-managed database on AWS, or completely outside of AWS. If you're running Aurora MySQL 5.7, consider setting up GTID-based binlog replication for complete consistency.