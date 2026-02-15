# Storing temporary data in an RDS for Oracle instance store

Use an instance store for the temporary tablespaces and the Database Smart Flash Cache
(the flash cache) on supported RDS for Oracle DB instance classes.

###### Topics

- [Overview of the RDS for Oracle instance store](#CHAP_Oracle.advanced-features.instance-store.overview "#CHAP_Oracle.advanced-features.instance-store.overview")
- [Turning on an RDS for Oracle instance store](#CHAP_Oracle.advanced-features.instance-store.Enable "#CHAP_Oracle.advanced-features.instance-store.Enable")
- [Configuring an RDS for Oracle instance store](CHAP_Oracle.advanced-features.instance-store.md "CHAP_Oracle.advanced-features.instance-store.md")
- [Working with an instance store on an Oracle read replica](CHAP_Oracle.advanced-features.instance-store.md "CHAP_Oracle.advanced-features.instance-store.md")
- [Configuring a temporary tablespace group on an instance store and
  Amazon EBS](CHAP_Oracle.advanced-features.instance-store.md "CHAP_Oracle.advanced-features.instance-store.md")
- [Removing an RDS for Oracle instance store](#CHAP_Oracle.advanced-features.instance-store.Disable "#CHAP_Oracle.advanced-features.instance-store.Disable")

## Overview of the RDS for Oracle instance store

An _instance store_ provides temporary block-level storage for an RDS for Oracle DB instance. You can use an
instance store for temporary storage of information that changes frequently.

An instance store is based on Non-Volatile Memory Express (NVMe) devices that are physically attached to the host computer. The storage
is optimized for low latency, random I/O performance, and sequential read throughput.

The size of the instance store varies by DB instance type. For more information about the instance store, see [Amazon EC2 instance store](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md") in the _Amazon Elastic
Compute Cloud User Guide for Linux Instances_.

###### Topics

- [Types of data in the RDS for Oracle instance store](#CHAP_Oracle.advanced-features.instance-store.overview.uses "#CHAP_Oracle.advanced-features.instance-store.overview.uses")
- [Benefits of the RDS for Oracle instance store](#CHAP_Oracle.advanced-features.instance-store.overview.benefits "#CHAP_Oracle.advanced-features.instance-store.overview.benefits")
- [Supported instance classes for the RDS for Oracle
  instance store](#CHAP_Oracle.advanced-features.instance-store.overview.instance-classes "#CHAP_Oracle.advanced-features.instance-store.overview.instance-classes")
- [Supported engine versions for the RDS for Oracle
  instance store](#CHAP_Oracle.advanced-features.instance-store.overview.db-versions "#CHAP_Oracle.advanced-features.instance-store.overview.db-versions")
- [Supported AWS Regions for the RDS for Oracle instance
  store](#CHAP_Oracle.advanced-features.instance-store.overview.regions "#CHAP_Oracle.advanced-features.instance-store.overview.regions")
- [Cost of the RDS for Oracle instance store](#CHAP_Oracle.advanced-features.instance-store.overview.cost "#CHAP_Oracle.advanced-features.instance-store.overview.cost")

### Types of data in the RDS for Oracle instance store

You can place the following types of RDS for Oracle temporary data in an instance store:

A temporary tablespace

Oracle Database uses temporary tablespaces to store intermediate query results that don't fit in memory. Larger queries
can generate large amounts of intermediate data that needs to be cached temporarily, but doesn't need to persist. In
particular, a temporary tablespace is useful for sorts, hash aggregations, and joins. If your RDS for Oracle DB instance uses
the Enterprise Edition or Standard Edition 2, you can place a temporary tablespace in an instance store.

The flash cache

The flash cache improves the performance of single-block random reads in the conventional path. A best practice is to
size the cache to accommodate most of your active data set. If your RDS for Oracle DB instance uses the Enterprise Edition, you
can place the flash cache in an instance store.

By default, an instance store is configured for a temporary tablespace but not for the flash cache. You can't place Oracle data
files and database log files in an instance store.

### Benefits of the RDS for Oracle instance store

You might consider using an instance store to store temporary files and caches that you can afford to lose. If you want to improve
DB performance, or if an increasing workload is causing performance problems for your Amazon EBS storage, consider scaling to an instance
class that supports an instance store.

By placing your temporary tablespace and flash cache on an instance store, you get the following benefits:

- Lower read latencies
- Higher throughput
- Reduced load on your Amazon EBS volumes
- Lower storage and snapshot costs because of reduced Amazon EBS load
- Less need to provision high IOPS, possibly lowering your overall cost

By placing your temporary tablespace on the instance store, you deliver an immediate performance boost to queries that use
temporary space. When you place the flash cache on the instance store, cached block reads typically have much lower latency than Amazon EBS
reads. The flash cache needs to be "warmed up" before it delivers performance benefits. The cache warms up by itself because the
database writes blocks to the flash cache as they age out of the database buffer cache.

###### Note

In some cases, the flash cache causes performance overhead because of cache management. Before you turn on the flash cache in a
production environment, we recommend that you analyze your workload and test the cache in a test environment.

### Supported instance classes for the RDS for Oracle

instance store

Amazon RDS supports the instance store for the following DB instance classes:

- db.m5d
- db.m6id
- db.r5d
- db.r6id
- db.x2idn
- db.x2iedn

RDS for Oracle supports the preceding DB instance classes for the BYOL licensing model only.
For more information, see [Supported RDS for Oracle DB instance
classes](Oracle.Concepts.md#Oracle.Concepts.InstanceClasses.Supported "Oracle.Concepts.md#Oracle.Concepts.InstanceClasses.Supported") and [Bring Your Own License (BYOL) for EE
and SE2](Oracle.Concepts.md#Oracle.Concepts.Licensing.BYOL "Oracle.Concepts.md#Oracle.Concepts.Licensing.BYOL").

To see the total instance storage for the supported DB instance types, run the following
command in the AWS CLI.

###### Example

```
aws ec2 describe-instance-types \
  --filters "Name=instance-type,Values=*5d.*large*,*6id.*large*" \
  --query "InstanceTypes[?contains(InstanceType,'m5d')||contains(InstanceType,'r5d')||contains(InstanceType,'m6id')||contains(InstanceType,'r6id')][InstanceType, InstanceStorageInfo.TotalSizeInGB]" \
  --output table
```

The preceding command returns the raw device size for the instance store. RDS for Oracle uses a small portion of this space for
configuration. The space in the instance store that is available for temporary tablespaces or the flash cache is slightly
smaller.

### Supported engine versions for the RDS for Oracle

instance store

The instance store is supported for the following RDS for Oracle engine versions:

- 21.0.0.0.ru-2022-01.rur-2022-01.r1 or higher Oracle Database 21c versions
- 19.0.0.0.ru-2021-10.rur-2021-10.r1 or higher Oracle Database 19c versions

### Supported AWS Regions for the RDS for Oracle instance

store

The instance store is available in all AWS Regions where one or more of these instance types are supported. For more information
on the db.m5d and db.r5d instance classes, see [DB instance classes](Concepts.md "Concepts.md").
For more information on the instance classes supported by Amazon RDS for Oracle, see [RDS for Oracle DB instance classes](Oracle.Concepts.md "Oracle.Concepts.md").

### Cost of the RDS for Oracle instance store

The cost of the instance store is built into the cost of the instance-store turned on instances. You don't incur additional costs by
enabling an instance store on an RDS for Oracle DB instance. For more information about instance-store turned on instances, see [Supported instance classes for the RDS for Oracle
instance store](#CHAP_Oracle.advanced-features.instance-store.overview.instance-classes "#CHAP_Oracle.advanced-features.instance-store.overview.instance-classes").

## Turning on an RDS for Oracle instance store

To turn on the instance store for RDS for Oracle temporary data, do one of the following:

- Create an RDS for Oracle DB instance using a supported instance class. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
- Modify an existing RDS for Oracle DB instance to use a supported instance class. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Removing an RDS for Oracle instance store

To remove the instance store, modify your RDS for Oracle DB instance to use an instance type that doesn't support instance store, such as
db.m5 or db.r5.
