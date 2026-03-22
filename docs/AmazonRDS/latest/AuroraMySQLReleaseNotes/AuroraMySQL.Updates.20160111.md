# Aurora MySQL database engine updates: 2016-01-11 (version 1.5) (Deprecated)

**Version:** 1.5

This update includes the following improvements:

## Improvements

- Fixed a 10 second pause of write operations for idle instances during
  Aurora storage deployments.
- Logical read-ahead now works when `innodb_file_per_table` is
  set to `No`. For more information on logical read-ahead, see
  [Aurora MySQL database engine updates: 2015-12-03 (version 1.4) (Deprecated)](AuroraMySQL.Updates.20151203.md "AuroraMySQL.Updates.20151203.md").
- Fixed issues with Aurora Replicas reconnecting with the primary instance.
  This improvement also fixes an issue when you specify a large value for the
  `quantity` parameter when testing Aurora Replica failures
  using fault-injection queries. For more information, see [Testing an Aurora replica failure](../AuroraUserGuide/AuroraMySQL.Managing.FaultInjectionQueries.md#AuroraMySQL.Managing.FaultInjectionQueries.ReplicaFailure "../AuroraUserGuide/AuroraMySQL.Managing.FaultInjectionQueries.md#AuroraMySQL.Managing.FaultInjectionQueries.ReplicaFailure") in the _Amazon Aurora User Guide_.
- Improved monitoring of Aurora Replicas falling behind and
  restarting.
- Fixed an issue that caused an Aurora Replica to lag, become deregistered,
  and then restart.
- Fixed an issue when you run the `show innodb status` command
  during a deadlock.
- Fixed an issue with failovers for larger instances during high write
  throughput.

## Integration of MySQL bug fixes

- Addressed incomplete fix in MySQL full text search affecting tables where
  the database name begins with a digit. (Port Bug #17607956)
