# Setting up enhanced binlog for Aurora MySQL

Enhanced binlog reduces the compute performance overhead caused by turning on binlog, which can reach up to 50% in certain cases.
With enhanced binlog, this overhead can be reduced to about 13%. To reduce overhead, enhanced binlog writes the binary and transactions logs
to storage in parallel, which minimizes the data written at the transaction commit time.

Using enhanced binlog also improves database recovery time after restarts and failovers by up to 99% compared to community MySQL binlog.
The enhanced binlog is compatible with existing binlog-based workloads, and you interact with it the same way you interact with the community MySQL binlog.

Enhanced binlog is available on Aurora MySQL version 3.03.1 and higher.

###### Topics

- [Configuring enhanced binlog parameters](#AuroraMySQL.Enhanced.binlog.enhancedbinlog.parameters "#AuroraMySQL.Enhanced.binlog.enhancedbinlog.parameters")
- [Other related parameters](#AuroraMySQL.Enhanced.binlog.other.parameters "#AuroraMySQL.Enhanced.binlog.other.parameters")
- [Differences between enhanced binlog and community MySQL binlog](#AuroraMySQL.Enhanced.binlog.differences "#AuroraMySQL.Enhanced.binlog.differences")
- [Amazon CloudWatch metrics for enhanced binlog](#AuroraMySQL.Enhanced.binlog.cloudwatch.metrics "#AuroraMySQL.Enhanced.binlog.cloudwatch.metrics")
- [Enhanced binlog limitations](#AuroraMySQL.Enhanced.binlog.limitations "#AuroraMySQL.Enhanced.binlog.limitations")

## Configuring enhanced binlog parameters

You can switch between community MySQL binlog and enhanced binlog by turning on/off the enhanced binlog parameters.
The existing binlog consumers can continue to read and consume the binlog files without any gaps in the binlog file sequence.

To turn on enhanced binlog, set the following parameters:

| Parameter                     | Default | Description                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `binlog_format`               | –       | Set the `binlog_format` parameter to the binary<br>logging format of your choice to turn on enhanced binlog. Make<br>sure the `binlog_format parameter` isn't set to OFF.<br>For more information, see [Configuring Aurora MySQL binary logging](USER_LogAccess.MySQL.md "USER_LogAccess.MySQL.md"). |
| `aurora_enhanced_binlog`      | `0`     | Set the value of this parameter to `1`<br>in the DB cluster parameter group associated with the Aurora MySQL cluster. When you change the<br>value of this parameter, you must reboot the writer instance when the `DBClusterParameterGroupStatus` value is shown as `pending-reboot`.               |
| `binlog_backup`               | `1`     | Turn off this parameter to turn on enhanced binlog. To do so,<br>set the value of this parameter to `0`.                                                                                                                                                                                             |
| `binlog_replication_globaldb` | `1`     | Turn off this parameter to turn on enhanced binlog. To do so,<br>set the value of this parameter to `0`.                                                                                                                                                                                             |

###### Important

You can turn off the `binlog_backup` and `binlog_replication_globaldb` parameters only when you use enhanced binlog.

To turn off enhanced binlog, set the following parameters:

| Parameter                     | Description                                                                                                                                                                                                                                                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `aurora_enhanced_binlog`      | Set the value of this parameter to `0`<br>in the DB cluster parameter group associated with the Aurora MySQL cluster. Whenever you change the<br>value of this parameter, you must reboot the writer instance when the `DBClusterParameterGroupStatus` value is shown as `pending-reboot`. |
| `binlog_backup`               | Turn on this parameter when you turn off enhanced binlog. To do<br>so, set the value of this parameter to `1`.                                                                                                                                                                             |
| `binlog_replication_globaldb` | Turn on this parameter when you turn off enhanced binlog. To do<br>so, set the value of this parameter to `1`.                                                                                                                                                                             |

To check whether enhanced binlog is turned on, use the following command in the MySQL client:

```
`mysql>`show status like 'aurora_enhanced_binlog';
              `+------------------------+--------+
| Variable_name | Value |
+------------------------+--------+
| aurora_enhanced_binlog | ACTIVE |
+------------------------+--------+
1 row in set (0.00 sec)`
```

When enhanced binlog is turned on, the output shows `ACTIVE` for `aurora_enhanced_binlog`.

## Other related parameters

When you turn on the enhanced binlog, the following parameters are affected:

- The `max_binlog_size` parameter is visible but not modifiable. It's default value `134217728`
  is automatically adjusted to `268435456` when enhanced binlog is turned on.
- Unlike in community MySQL binlog, the `binlog_checksum` doesn't act as a dynamic parameter when the enhanced binlog is turned on.
  For the change to this parameter to take effect, you must manually reboot the DB cluster even when the `ApplyMethod` is `immediate`.
- The value you set on the `binlog_order_commits` parameter has no effect on the order of the commits when enhanced binlog is turned on.
  The commits are always ordered without any further performance implications.

## Differences between enhanced binlog and community MySQL binlog

Enhanced binlog interacts differently with clones, backups, and Aurora global database when compared to community MySQL
binlog. We recommend that you understand the following differences before using enhanced binlog.

- Enhanced binlog files from the source DB cluster aren't available on a cloned DB cluster.
- Enhanced binlog files aren't included in Aurora backups. Therefore, enhanced binlog files from the source DB cluster aren't
  available after restoring a DB cluster despite any retention period set on it.
- When used with an Aurora global database, the enhanced binlog files of the primary DB cluster aren't replicated to the DB cluster in the
  secondary regions.

###### **Examples**

The following examples illustrate the differences between enhanced binlog and community MySQL binlog.

**On a restored or cloned DB cluster**

When enhanced binlog is turned on, the historical binlog files aren't available in the restored or cloned DB cluster. After a restore or clone operation, if binlog is turned on, the new DB cluster
starts writing its own sequence of binlog files, starting from 1 (mysql-bin-changelog.000001).

To turn on enhanced binlog after a restore or clone operation, set the required DB cluster parameters on the restored or cloned DB cluster. For more information,
see [Configuring enhanced binlog parameters](#AuroraMySQL.Enhanced.binlog.enhancedbinlog.parameters "#AuroraMySQL.Enhanced.binlog.enhancedbinlog.parameters").

###### Example: Clone or restore operation performed when enhanced binlog is turned on

Source DB Cluster:

```
`mysql>` show binary logs;
                      `+----------------------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+----------------------------+-----------+-----------+
| mysql-bin-changelog.000001 | 156 | No |
| mysql-bin-changelog.000002 | 156 | No |
| mysql-bin-changelog.000003 | 156 | No |
| mysql-bin-changelog.000004 | 156 | No | --> Enhanced Binlog turned on
| mysql-bin-changelog.000005 | 156 | No | --> Enhanced Binlog turned on
| mysql-bin-changelog.000006 | 156 | No | --> Enhanced Binlog turned on
+----------------------------+-----------+-----------+
6 rows in set (0.00 sec)`

```

On a restored or cloned DB cluster, binlog files aren't backed up when enhanced binlog is turned on. To avoid discontinuity in the binlog data,
the binlog files written before turning on the enhanced binlog are also not available.

```
`mysql>`show binary logs;
                      `+----------------------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+----------------------------+-----------+-----------+
| mysql-bin-changelog.000001 | 156 | No | --> New sequence of Binlog files
+----------------------------+-----------+-----------+
1 row in set (0.00 sec)`

```

###### Example: Clone or restore operation performed when enhanced binlog is turned off

Source DB cluster:

```
`mysql>`show binary logs;
                       `+----------------------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+----------------------------+-----------+-----------+
| mysql-bin-changelog.000001 | 156 | No |
| mysql-bin-changelog.000002 | 156 | No | --> Enhanced Binlog enabled
| mysql-bin-changelog.000003 | 156 | No | --> Enhanced Binlog enabled
| mysql-bin-changelog.000004 | 156 | No |
| mysql-bin-changelog.000005 | 156 | No |
| mysql-bin-changelog.000006 | 156 | No |
+----------------------------+-----------+-----------+
6 rows in set (0.00 sec)`

```

Enhanced binlog is disabled after `mysql-bin-changelog.000003`. On a restored or cloned DB cluster, binlog files written after turning off the enhanced binlog are available.

```
`mysql>`show binary logs;
                      `+----------------------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+----------------------------+-----------+-----------+
| mysql-bin-changelog.000004 | 156 | No |
| mysql-bin-changelog.000005 | 156 | No |
| mysql-bin-changelog.000006 | 156 | No |
+----------------------------+-----------+-----------+
1 row in set (0.00 sec)`

```

**On an Amazon Aurora global database**

On an Amazon Aurora global database, the binlog data of the primary DB cluster isn't replicated to the secondary DB clusters. After a cross-Region failover process,
the binlog data isn't available in the newly promoted primary DB cluster. If binlog is turned on, the newly promoted DB cluster starts its
own sequence of binlog files, starting from 1 (mysql-bin-changelog.000001).

To turn on enhanced binlog after failover, you must set the required DB cluster parameters on the secondary DB cluster. For more information,
see [Configuring enhanced binlog parameters](#AuroraMySQL.Enhanced.binlog.enhancedbinlog.parameters "#AuroraMySQL.Enhanced.binlog.enhancedbinlog.parameters").

###### Example: Global database failover operation is performed when enhanced binlog is turned on

Old primary DB Cluster (before failover):

```
`mysql>`show binary logs;
                  `+----------------------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+----------------------------+-----------+-----------+
| mysql-bin-changelog.000001 | 156 | No |
| mysql-bin-changelog.000002 | 156 | No |
| mysql-bin-changelog.000003 | 156 | No |
| mysql-bin-changelog.000004 | 156 | No | --> Enhanced Binlog enabled
| mysql-bin-changelog.000005 | 156 | No | --> Enhanced Binlog enabled
| mysql-bin-changelog.000006 | 156 | No | --> Enhanced Binlog enabled
+----------------------------+-----------+-----------+
6 rows in set (0.00 sec)`
```

New primary DB cluster (after failover):

Binlog files aren't replicated to secondary regions when enhanced binlog is turned on. To avoid discontinuity in the binlog data,
the binlog files written before turning on the enhanced binlog aren't available.

```
`mysql>`show binary logs;
                      `+----------------------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+----------------------------+-----------+-----------+
| mysql-bin-changelog.000001 | 156 | No | --> Fresh sequence of Binlog files
+----------------------------+-----------+-----------+
1 row in set (0.00 sec)`

```

###### Example: Global database failover operation is performed when enhanced binlog is turned off

Source DB Cluster:

```
`mysql>`show binary logs;
                  `+----------------------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+----------------------------+-----------+-----------+
| mysql-bin-changelog.000001 | 156 | No |
| mysql-bin-changelog.000002 | 156 | No | --> Enhanced Binlog enabled
| mysql-bin-changelog.000003 | 156 | No | --> Enhanced Binlog enabled
| mysql-bin-changelog.000004 | 156 | No |
| mysql-bin-changelog.000005 | 156 | No |
| mysql-bin-changelog.000006 | 156 | No |
+----------------------------+-----------+-----------+
6 rows in set (0.00 sec)`

```

**Restored or cloned DB cluster:**

Enhanced binlog is disabled after `mysql-bin-changelog.000003`. Binlog files that are written after turning off the enhanced binlog are replicated and are available in the newly promoted DB cluster.

```
`mysql>`show binary logs;
                  `+----------------------------+-----------+-----------+
| Log_name | File_size | Encrypted |
+----------------------------+-----------+-----------+
| mysql-bin-changelog.000004 | 156 | No |
| mysql-bin-changelog.000005 | 156 | No |
| mysql-bin-changelog.000006 | 156 | No |
+----------------------------+-----------+-----------+
3 rows in set (0.00 sec)`
```

## Amazon CloudWatch metrics for enhanced binlog

The following Amazon CloudWatch metrics are published only when enhanced binlog is turned on.

| CloudWatch metric  | Description                                                                                             | Units               |
| ------------------ | ------------------------------------------------------------------------------------------------------- | ------------------- |
| ChangeLogBytesUsed | The amount of storage used by the enhanced binlog.                                                      | Bytes               |
| ChangeLogReadIOPs  | The number of read I/O operations performed in the enhanced binlog within a 5-minute interval.          | Count per 5 minutes |
| ChangeLogWriteIOPs | The number of write disk I/O operations performed in the enhanced binlog within a 5-minute<br>interval. | Count per 5 minutes |

## Enhanced binlog limitations

The following limitations apply to Amazon Aurora DB clusters when enhanced binlog is turned on.

- Enhanced binlog is only supported on Aurora MySQL version3.03.1 and higher.
- The enhanced binlog ﬁles written on the primary DB cluster aren't copied to the cloned or restored DB clusters.
- When used with Amazon Aurora global database, the enhanced binlog files of the primary DB cluster aren't
  replicated to the secondary DB clusters. Therefore, after the failover process, the historical binlog data isn't available in the new primary DB cluster.
- The following binlog conﬁguration parameters are ignored:
  - `binlog_group_commit_sync_delay`
  - `binlog_group_commit_sync_no_delay_count`
  - `binlog_max_flush_queue_time`

- You can't drop or rename a corrupted table in a database. To drop these tables, you can contact Support.
- The binlog I/O cache is disabled when enhanced binlog is turned on. For more information, see [Optimizing binary log replication for Aurora MySQL](binlog-optimization.md "binlog-optimization.md").

###### Note

Enhanced binlog provides similar read performance improvements as binlog I/O cache and better write performance improvements.

- The backtrack feature is not supported. Enhanced binlog can't be turned on in a DB cluster under the following conditions:
  - DB cluster with the backtrack feature currently enabled.
  - DB cluster where the backtrack feature was previously enabled, but is now disabled.
  - DB cluster restored from a source DB cluster or a snapshot with the backtrack feature enabled.
