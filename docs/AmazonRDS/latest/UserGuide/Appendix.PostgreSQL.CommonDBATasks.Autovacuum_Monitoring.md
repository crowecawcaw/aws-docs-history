# Explanation of the NOTICE messages in RDS for PostgreSQL

The `postgres_get_av_diag()` function provides the following NOTICE
messages:

**When the age has not reached the monitoring threshold yet**

The monitoring threshold for `postgres_get_av_diag()` to identify
blockers is 500 million transactions by default. If `postgres_get_av_diag()`
generates the following NOTICE, it indicates that the transaction age has not yet
reached this threshold.

```
NOTICE: postgres_get_av_diag() checks for blockers that prevent aggressive vacuums only, it does so only after exceeding dvb_threshold which is 500,000,000 and age of this PostgreSQL cluster is currently at 2.
```

**Not connected to the database with the age of oldest transaction ID**

The `postgres_get_av_diag()` function provides the most accurate output
when connected to the database with the oldest transaction ID age. The database with the
oldest transaction ID age reported by `postgres_get_av_diag()` will be
different than “my_database” in your case. If you are not connected to the correct
database, the following NOTICE is generated:

```
NOTICE: You are not connected to the database with the age of oldest transaction ID. Connect to my_database database and run postgres_get_av_diag() for accurate reporting.
```

Connecting to the database with the oldest transaction age is important for the
following reasons:

- **Identifying temporary table blockers:** Because
  the metadata for temporary tables is specific to each database, they are typically
  found in the database where they are created. However, if a temporary table happens
  to be the top blocker and resides in the database with the oldest transaction, this
  could be misleading. Connecting to the correct database ensures the accurate
  identification of the temporary table blocker.
- **Diagnosing slow vacuums:** The index metadata and
  table count information are database-specific and necessary for diagnosing slow
  vacuum issues.

**Database with oldest transaction by age is on an rdsadmin or template0 database**

In certain cases, the `rdsadmin` or `template0` databases may
be identified as the database with the oldest transaction ID age. If this happens,
`postgres_get_av_diag()` will issue the following NOTICE:

```
NOTICE: The database with the age of oldest transaction ID is rdsadmin or template0, reach out to support if the reported blocker is in rdsadmin or template0.
```

Verify that the listed blocker is not originating from either of these two
databases. If the blocker is reported to be present in either `rdsadmin` or
`template0`, contact support as these databases are not user-accessible and
require intervention.

It is highly unlikely for either the `rdsadmin` or `template0`
database to contain a top blocker.

**When an aggressive vacuum is already running**

The `postgres_get_av_diag()` function is designed to report when an
aggressive vacuum process is running, but it only triggers this output after the vacuum
has been active for at least 1 minute. This intentional delay helps reduce the chances
of false positives. By waiting, the function ensures that only effective, significant
vacuums are reported, leading to more accurate and reliable monitoring of vacuum
activity.

The `postgres_get_av_diag()` function generates the following NOTICE when
it detects one or more aggressive vacuums in progress.

```
NOTICE: Your database is currently running aggressive vacuum to prevent wraparound, monitor autovacuum performance.
```

As indicated in the NOTICE, continue to monitor the performance of vacuum. For more
information about aggressive vacuum see [Aggressive vacuum (to prevent wraparound) is running](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Aggressive_vacuum "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Aggressive_vacuum")

**When autovacuum is off**

The `postgres_get_av_diag()` function generates the following NOTICE if
autovacuum is disabled on your database instance:

```
NOTICE: Autovacuum is OFF, we strongly recommend to enable it, no restart is necessary.
```

Autovacuum is a critical feature of your RDS for PostgreSQL DB instance
that ensures smooth database operation. It automatically removes old row versions,
reclaims storage space, and prevents table bloat, helping to keep tables and indexes
efficient for optimal performance. Additionally, it protects against transaction ID
wraparound, which can halt transactions on your Amazon RDS instance. Disabling autovacuum can
lead to long-term declines in database performance and stability. We suggest you to keep
it on all the times. For more information, see [Understanding autovacuum in RDS for PostgreSQL
environments](https://aws.amazon.com/blogs/database/understanding-autovacuum-in-amazon-rds-for-postgresql-environments/ "https://aws.amazon.com/blogs/database/understanding-autovacuum-in-amazon-rds-for-postgresql-environments/").

###### Note

Turning off autovacuum doesn't stop aggressive vacuums. These will still occur
once your tables hit the `autovacuum_freeze_max_age` threshold.

**The number of transactions remaining is critically low**

The `postgres_get_av_diag()` function generates the following NOTICE when
a wraparound vacuum is imminent. This NOTICE is issued when your Amazon RDS instance is 100
million transactions away from potentially rejecting new transactions.

```
WARNING: Number of transactions remaining is critically low, resolve issues with autovacuum or perform manual VACUUM FREEZE before your instance stops accepting transactions.
```

Your immediate action is required to avoid database downtime. You should closely
monitor your vacuuming operations and consider manually initiating a `VACUUM
 FREEZE` on the affected database to prevent transaction failures.
