# Using zero-downtime patching

Performing upgrades for Aurora MySQL DB clusters involves the possibility of an outage when the database is shut down and while
it's being upgraded. By default, if you start the upgrade while the database is busy, you lose all the connections and
transactions that the DB cluster is processing. If you wait until the database is idle to perform the upgrade, you might have to
wait a long time.

The zero-downtime patching (ZDP) feature attempts, on a best-effort basis, to preserve client connections through an Aurora MySQL
upgrade. If ZDP completes successfully, application sessions are preserved and the database engine restarts while the upgrade is in
progress. The database engine restart can cause a drop in throughput lasting for a few seconds to approximately one minute.

ZDP doesn't apply to the following:

- Operating system (OS) patches and upgrades
- Major version upgrades
  ZDP is available for all supported Aurora MySQL versions and DB instance classes.

ZDP isn't supported for Aurora Serverless v1 or Aurora global databases.

###### Note

We recommend using the T DB instance classes only for development and test servers, or other non-production servers. For more
details on the T instance classes, see [Using T instance classes for development and testing](AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.T2Medium "AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.T2Medium").

You can see metrics of important attributes during ZDP in the MySQL error log. You can also see information about when Aurora MySQL
uses ZDP or chooses not to use ZDP on the **Events** page in the AWS Management Console.

In Aurora MySQL, Aurora can perform a zero-downtime patch whether or not binary log replication is enabled. If binary log replication is enabled,
Aurora MySQL automatically drops the connection to the binlog target during a ZDP operation. Aurora MySQL automatically reconnects to the binlog target and
resumes replication after the restart finishes.

ZDP also works in combination with the reboot enhancements in Aurora MySQL. Patching the writer DB instance automatically patches readers at the same
time. After performing the patch, Aurora restores the connections on both the writer and reader DB instances.

ZDP might not complete successfully under the following conditions:

- Long-running queries or transactions are in progress. If Aurora can perform ZDP in this case, any open transactions are canceled but their
  connections are retained.
- Temporary tables, user locks, or table locks are in use, for example while data definition language (DDL) statements run. Aurora drops these
  connections.
- Pending parameter changes exist.
  If no suitable time window for performing ZDP becomes available because of one or more of these conditions, patching reverts to the standard behavior.

Although connections remain intact following a successful ZDP operation, some variables and features are reinitialized. The following kinds of information
aren't preserved through a restart caused by zero-downtime patching:

- Global variables. Aurora restores session variables, but it doesn't restore global variables after the restart.
- Status variables. In particular, the uptime value reported by the engine status is reset after a restart that uses the ZDR or
  ZDP mechanisms.
- `LAST_INSERT_ID`.
- In-memory `auto_increment` state for tables. The in-memory auto-increment state is reinitialized. For more
  information about auto-increment values, see
  [MySQL Reference Manual](https://dev.mysql.com/doc/refman/5.7/en/innodb-auto-increment-handling.html#innodb-auto-increment-initialization "https://dev.mysql.com/doc/refman/5.7/en/innodb-auto-increment-handling.html#innodb-auto-increment-initialization").
- Diagnostic information from `INFORMATION_SCHEMA` and `PERFORMANCE_SCHEMA` tables. This diagnostic
  information also appears in the output of commands such as `SHOW PROFILE` and `SHOW PROFILES`.
  The following activities related to zero-downtime restart are reported on the **Events** page:

- Attempting to upgrade the database with zero downtime.
- Attempting to upgrade the database with zero downtime finished. The event reports how long the process took. The event also
  reports how many connections were preserved during the restart and how many connections were dropped. You can consult the
  database error log to see more details about what happened during the restart.
