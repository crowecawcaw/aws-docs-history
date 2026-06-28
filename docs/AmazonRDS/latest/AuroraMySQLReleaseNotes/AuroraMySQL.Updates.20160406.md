# Aurora MySQL database engine updates: 2016-04-06 (version 1.6) (Deprecated)

**Version:** 1.6

This update includes the following improvements:

## New features

- **Parallel read-ahead** – Parallel
  read-ahead is now enabled by default for all Aurora MySQL DB clusters, and is
  not configurable. Parallel read-ahead was introduced in the December 2015
  update. For more information, see [Aurora MySQL database engine updates: 2015-12-03 (version 1.4) (Deprecated)](AuroraMySQL.Updates.20151203.md "AuroraMySQL.Updates.20151203.md").

In addition to enabling parallel read-ahead by default, this release
includes the following improvements to parallel read-ahead:

    + Improved logic so that parallel read-ahead is less aggressive,
     which is beneficial when your DB cluster encounters many parallel
     workloads.
    + Improved stability on smaller tables.

- **Efficient storage of Binary Logs (lab
  mode)** – MySQL binary log files are now stored more
  efficiently in Aurora MySQL. The new storage implementation enables binary log
  files to be deleted much earlier and improves system performance for an
  instance in an Aurora MySQL DB cluster that is a binary log replication
  master.

To enable efficient storage of binary logs, set the
`aurora_lab_mode` parameter to `1` in the
parameter group for your primary instance or Aurora Replica. The
`aurora_lab_mode` parameter is an instance-level parameter
that is in the `default.aurora5.6` parameter group by default.
For information on modifying a DB parameter group, see
[Modifying parameters in a DB parameter group](../AuroraUserGuide/USER_WorkingWithParamGroups.md#USER_WorkingWithParamGroups.Modifying "../AuroraUserGuide/USER_WorkingWithParamGroups.md#USER_WorkingWithParamGroups.Modifying") in the _Amazon Aurora User Guide_.
For information on parameter groups and Aurora MySQL, see
[Aurora MySQL configuration parameters](../AuroraUserGuide/AuroraMySQL.Reference.md#AuroraMySQL.Reference.ParameterGroups "../AuroraUserGuide/AuroraMySQL.Reference.md#AuroraMySQL.Reference.ParameterGroups") in the _Amazon Aurora User Guide_.

Only turn on efficient storage of binary logs for instances in an
Aurora MySQL DB cluster that are MySQL binary log replication master
instances.

- **AURORA\_VERSION system variable** –
  You can now get the Aurora version of your Aurora MySQL DB cluster by querying for the
  `AURORA_VERSION` system variable.

To get the Aurora version, use one of the following queries:

```

select AURORA_VERSION();
select @@aurora_version;
show variables like '%version';

```

You can also see the Aurora version in the AWS Management Console when you modify a
DB cluster, or by calling the [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS CLI command or the [DescribeDBEngineVersions](../APIReference/API_DescribeDBEngineVersions.md "../APIReference/API_DescribeDBEngineVersions.md") API operation.

- **Lock manager memory usage metric** –
  Information about lock manager memory usage is now available as a
  metric.

To get the lock manager memory usage metric, use one of the following
queries:

```

show global status where variable_name in ('aurora_lockmgr_memory_used');
select * from INFORMATION_SCHEMA.GLOBAL_STATUS where variable_name in ('aurora_lockmgr_memory_used');

```

## Improvements

- Improved stability during binlog and XA transaction recovery.
- Fixed a memory issue resulting from a large number of connections.
- Improved accuracy in the following metrics: `Read
 Throughput`, `Read IOPS`, `Read Latency`,
  `Write Throughput`, `Write IOPS`, `Write
 Latency`, and `Disk Queue Depth`.
- Fixed a stability issue causing slow startup for large instances after a
  crash.
- Improved concurrency in the data dictionary regarding synchronization
  mechanisms and cache eviction.
- Stability and performance improvements for Aurora Replicas:

  - Fixed a stability issue for Aurora Replicas during heavy or burst
    write workloads for the primary instance.
  - Improved replica lag for db.r3.4xlarge and db.r3.8xlarge
    instances.
  - Improved performance by reducing contention between application of
    log records and concurrent reads on an Aurora Replica.
  - Fixed an issue for refreshing statistics on Aurora Replicas for
    newly created or updated statistics.
  - Improved stability for Aurora Replicas when there are many
    transactions on the primary instance and concurrent reads on the
    Aurora Replicas across the same data.
  - Improved stability for Aurora Replicas when running
    `UPDATE` and `DELETE` statements with
    `JOIN` statements.
  - Improved stability for Aurora Replicas when running `INSERT ...
   SELECT` statements.

## Integration of MySQL bug fixes

- BACKPORT Bug #18694052 FIX FOR ASSERTION `!M\_ORDERED\_REC\_BUFFER' FAILED TO
  5.6 (Port Bug #18305270)
- SEGV IN MEMCPY(), HA\_PARTITION::POSITION (Port Bug # 18383840)
- WRONG RESULTS WITH PARTITIONING,INDEX\_MERGE AND NO PK (Port Bug #

18167648.

- FLUSH TABLES FOR EXPORT: ASSERTION IN HA\_PARTITION::EXTRA (Port Bug #

16943907.

- SERVER CRASH IN VIRTUAL HA\_ROWS HANDLER::MULTI\_RANGE\_READ\_INFO\_CONST (Port
  Bug # 16164031)
- RANGE OPTIMIZER CRASHES IN SEL\_ARG::RB\_INSERT() (Port Bug #

16241773.
