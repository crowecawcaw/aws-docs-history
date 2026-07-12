# Availability and durability

###### Topics

- [Instance monitoring and repair](#aurora-features-instance-monitoring "#aurora-features-instance-monitoring")
- [Multi-AZ failover](#aurora-features-multi-az "#aurora-features-multi-az")
- [Amazon Aurora Global Database](#aurora-features-global-database "#aurora-features-global-database")
- [Fault-tolerant and self-healing storage](#aurora-features-fault-tolerant "#aurora-features-fault-tolerant")
- [Automatic, continuous, incremental backups and point-in-time restore](#aurora-features-backups "#aurora-features-backups")
- [Database snapshots](#aurora-features-snapshots "#aurora-features-snapshots")

## Instance monitoring and repair

Aurora continuously monitors the health of your databases. In the rare event of a failure, Aurora
automatically restarts your database and associated processes. Unlike other databases, Aurora does not require
crash recovery replay of database redo logs, which greatly reduces restart times. Aurora also isolates the
database buffer cache from database processes, which allows the cache to survive a database restart without
brownouts.

## Multi-AZ failover

On instance failure, Aurora uses [RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/ "https://aws.amazon.com/rds/features/multi-az/") technology to automate failover to one of up to 15 Aurora
read replicas you created in any three Availability Zones (AZs). If no read replicas were provisioned, Aurora
will automatically attempt to create a new Aurora DB instance for you. You can reduce failover times further by
using open source and drop-in compatible [AWS JDBC Driver for PostgreSQL](https://awslabs.github.io/aws-postgresql-jdbc/ "https://awslabs.github.io/aws-postgresql-jdbc/") and [AWS JDBC Driver for MySQL](https://awslabs.github.io/aws-mysql-jdbc/ "https://awslabs.github.io/aws-mysql-jdbc/"), or
utilize [RDS Proxy](https://aws.amazon.com/rds/proxy/ "https://aws.amazon.com/rds/proxy/") to decrease failover times by up to 66% while preserving application connections.

## Amazon Aurora Global Database

[Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/ "https://aws.amazon.com/rds/aurora/global-database/") allows a single Aurora database to span multiple AWS Regions to enable fast local
reads and improve disaster recovery posture. It uses storage-based replication to replicate a database across
multiple Regions with typical latency of less than one second. In the rare event of a Regional degradation or
outage, a [database in a secondary Region can be promoted to full read and write capabilities in less than 1
minute](../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database.md").

## Fault-tolerant and self-healing storage

Aurora makes your data durable across 3 AZs, and its storage is fault-tolerant transparently handling the
loss of up to two copies of data without affecting database write availability and up to three copies without
affecting read availability. Aurora storage is also self-healing, and data blocks and disks are continuously
scanned for errors and replaced automatically.

## Automatic, continuous, incremental backups and point-in-time restore

Aurora backups are automatic, incremental, and continuous and have no impact on database performance. The
backup capability of Aurora enables point-in-time recovery for your instance, and you can restore your database
to any second during your retention period, up to the last 5 minutes. Your automatic backup retention period
can be configured up to 35 days. Automated backups are stored in [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"), which is designed for
99.999999999% durability.

## Database snapshots

You can create user-initiated backups of your Aurora instance at any time, and snapshots are stored in
Amazon S3 and retained until you explicitly delete them. Aurora uses automated incremental snapshots to reduce
the time and storage required. You can create a new instance from a DB snapshot whenever you desire.
