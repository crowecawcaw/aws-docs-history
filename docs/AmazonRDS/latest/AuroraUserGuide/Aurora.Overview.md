# Amazon Aurora storage

Following, you can learn about the Aurora storage subsystem. Aurora uses a distributed and
shared storage architecture that is an important factor in performance, scalability, and
reliability for Aurora clusters.

###### Topics

- [Overview of Amazon Aurora storage](#Aurora.Overview.Storage "#Aurora.Overview.Storage")
- [What the cluster volume contains](#aurora-storage-contents "#aurora-storage-contents")
- [Storage configurations for Amazon Aurora DB clusters](#aurora-storage-type "#aurora-storage-type")
- [How Aurora storage automatically resizes](#aurora-storage-growth "#aurora-storage-growth")
- [How Aurora data storage is billed](#aurora-storage-data-billing "#aurora-storage-data-billing")

## Overview of Amazon Aurora storage

Aurora data is stored in the _cluster volume_, which is
a single, virtual volume that uses solid state drives (SSDs). A cluster volume consists of
copies of the data across three Availability Zones in a single AWS Region. Because the
data is automatically replicated across Availability Zones, your data is highly durable with
less possibility of data loss. This replication also ensures that your database is more
available during a failover. It does so because the data copies already exist in the other
Availability Zones and continue to serve data requests to the DB instances in your DB
cluster. The amount of replication is independent of the number of DB instances in your
cluster.

Aurora uses separate local storage for nonpersistent, temporary files. This includes
files that are used for such purposes as sorting large data sets during query processing,
and building indexes. For more information, see [Temporary storage limits for Aurora MySQL](AuroraMySQL.Managing.md#AuroraMySQL.Managing.TempStorage "AuroraMySQL.Managing.md#AuroraMySQL.Managing.TempStorage") and [Temporary storage limits for Aurora PostgreSQL](AuroraPostgreSQL.md#AuroraPostgreSQL.Managing.TempStorage "AuroraPostgreSQL.md#AuroraPostgreSQL.Managing.TempStorage").

## What the cluster volume contains

The Aurora cluster volume contains all your user data, schema objects, and internal
metadata such as the system tables and the binary log. For example, Aurora stores all the
tables, indexes, binary large objects (BLOBs), stored procedures, and so on for an Aurora
cluster in the cluster volume.

The Aurora shared storage architecture makes your data independent from the DB instances
in the cluster. For example, you can add a DB instance quickly because Aurora doesn't make a
new copy of the table data. Instead, the DB instance connects to the shared volume that
already contains all your data. You can remove a DB instance from a cluster without removing
any of the underlying data from the cluster. Only when you delete the entire cluster does
Aurora remove the data.

## Storage configurations for Amazon Aurora DB clusters

Amazon Aurora has two DB cluster storage configurations:

- **Aurora I/O-Optimized** – Improved price performance and predictability
  for I/O-intensive applications. You pay only for the usage and storage of your DB
  clusters, with no additional charges for read and write I/O operations.

Aurora I/O-Optimized is the best choice when your I/O spending is 25% or more of your total Aurora
database spending.

You can choose Aurora I/O-Optimized when you create or modify a DB cluster with a DB engine
version that supports the Aurora I/O-Optimized cluster configuration. You can switch from Aurora I/O-Optimized to
Aurora Standard at any time.

- **Aurora Standard** – Cost-effective pricing for many applications
  with moderate I/O usage. In addition to the usage and storage of your DB clusters, you
  also pay a standard rate per 1 million requests for I/O operations.

Aurora Standard is the best choice when your I/O spending is less than 25% of your total
Aurora database spending.

You can switch from Aurora Standard to Aurora I/O-Optimized once every 30 days. When you switch between
Aurora Standard and Aurora I/O-Optimized storage options for non-NVMe-based DB instances, there is no downtime.
However, for NVMe-based DB instances, switching between Aurora I/O-Optimized and Aurora Standard storage options
requires a database engine restart, which may cause a brief period of downtime.

For information on AWS Region and version support, see [Supported Regions and Aurora DB engines for cluster storage configurations](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

For more information on pricing for Amazon Aurora storage configurations, see [Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/").

For information on choosing the storage configuration when creating a DB cluster, see
[Creating a DB cluster](Aurora.md#Aurora.CreateInstance.Creating "Aurora.md#Aurora.CreateInstance.Creating"). For information on modifying the storage
configuration for a DB cluster, see [Settings for Amazon Aurora](Aurora.md#Aurora.Modifying.Settings "Aurora.md#Aurora.Modifying.Settings").

## How Aurora storage automatically resizes

Aurora cluster volumes automatically grow as the amount of data in your database
increases. For information about maximum Aurora cluster volume sizes for each engine version, see [Amazon Aurora size limits](CHAP_Limits.md#RDS_Limits.FileSize.Aurora "CHAP_Limits.md#RDS_Limits.FileSize.Aurora"). This automatic storage scaling is combined
with a high-performance and highly distributed storage subsystem. These make Aurora a good
choice for your important enterprise data when your main objectives are reliability and high
availability.

To display the volume status, see [Displaying volume status for an Aurora MySQL DB cluster](AuroraMySQL.Managing.md "AuroraMySQL.Managing.md") or [Displaying volume status for an Aurora PostgreSQL DB cluster](AuroraPostgreSQL.Managing.md "AuroraPostgreSQL.Managing.md"). For ways to balance storage
costs against other priorities, [Storage scaling](Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling "Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling") describes how to monitor the
Amazon Aurora metrics `AuroraVolumeBytesLeftTotal` and `VolumeBytesUsed`
in CloudWatch.

When Aurora data is removed, the space allocated for that data is freed. Examples of
removing data include dropping or truncating a table. This automatic reduction in storage
usage helps you to minimize storage charges.

###### Note

The storage limits and dynamic resizing behavior discussed here apply to persistent
tables and other data stored in the cluster volume.

For Aurora PostgreSQL, temporary table data is stored in the local DB instance.

For Aurora MySQL version 2, temporary table data is stored by default in the cluster
volume for writer instances and in local storage for reader instances. For more
information, see [Storage engine for on-disk temporary tables](AuroraMySQL.md#AuroraMySQL.StorageEngine57 "AuroraMySQL.md#AuroraMySQL.StorageEngine57").

For Aurora MySQL version 3, temporary table data is stored in the local DB instance or
in the cluster volume. For more information, see [New temporary table behavior in Aurora MySQL version 3](ams3-temptable-behavior.md "ams3-temptable-behavior.md").

The maximum size of temporary tables that reside in local storage is limited by the
maximum local storage size of the DB instance. The local storage size depends on the
instance class that you use. For more information, see [Temporary storage limits for Aurora MySQL](AuroraMySQL.Managing.md#AuroraMySQL.Managing.TempStorage "AuroraMySQL.Managing.md#AuroraMySQL.Managing.TempStorage") and [Temporary storage limits for Aurora PostgreSQL](AuroraPostgreSQL.md#AuroraPostgreSQL.Managing.TempStorage "AuroraPostgreSQL.md#AuroraPostgreSQL.Managing.TempStorage").

Some storage features, such as the maximum size of a cluster volume and automatic
resizing when data is removed, depend on the Aurora version of your cluster. For more
information, see [Storage scaling](Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling "Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling"). You can also learn how to
avoid storage issues and how to monitor the allocated storage and free space in your
cluster.

## How Aurora data storage is billed

Even though an Aurora cluster volume can grow up to 256 tebibytes (TiB) for specific engine versions, you are only
charged for the space that you use in an Aurora cluster volume. In earlier Aurora versions,
the cluster volume could reuse space that was freed up when you removed data, but the
allocated storage space would never decrease. Now when Aurora data is removed, such as by
dropping a table or database, the overall allocated space decreases by a comparable amount.
Thus, you can reduce storage charges by dropping tables, indexes, databases, and so on that
you no longer need.

###### Tip

For earlier versions without the dynamic resizing feature, resetting the storage usage
for a cluster involved doing a logical dump and restoring to a new cluster. That operation
can take a long time for a substantial volume of data. If you encounter this situation,
consider upgrading your cluster to a version that supports dynamic volume resizing.

For information about which Aurora versions support dynamic resizing, and how to minimize
storage charges by monitoring storage usage for your cluster, see [Storage scaling](Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling "Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling"). For information about Aurora
backup storage billing, see [Understanding Amazon Aurora backup storage usage](aurora-storage-backup.md "aurora-storage-backup.md"). For pricing information about Aurora data storage,
see [Amazon RDS for Aurora pricing](https://aws.amazon.com/rds/aurora/pricing "https://aws.amazon.com/rds/aurora/pricing").
