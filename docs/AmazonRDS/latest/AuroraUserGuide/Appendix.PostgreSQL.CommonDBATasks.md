# Working with PostgreSQL

autovacuum on Amazon Aurora PostgreSQL

We strongly recommend that you use the autovacuum feature to maintain the health of your
PostgreSQL DB instance. Autovacuum automates the start of the VACUUM and the ANALYZE commands.
It checks for tables with a large number of inserted, updated, or deleted tuples. After this
check, it reclaims storage by removing obsolete data or tuples from the PostgreSQL
database.

By default, autovacuum is turned on for the Aurora PostgreSQL DB instances that you
create using any of the default PostgreSQL DB parameter groups. Other configuration parameters
associated with the autovacuum feature are also set by default. Because these defaults are
somewhat generic, you can benefit from tuning some of the parameters associated with the
autovacuum feature for your specific workload.

Following, you can find more information about the autovacuum and how to tune some of its
parameters on your Aurora PostgreSQL DB instance.

###### Topics

- [Allocating memory
  for autovacuum](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.WorkMemory "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.WorkMemory")
- [Reducing
  the likelihood of transaction ID wraparound](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AdaptiveAutoVacuuming "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AdaptiveAutoVacuuming")
- [Determining if
  the tables in your database need vacuuming](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")
- [Determining
  which tables are currently eligible for autovacuum](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")
- [Determining
  if autovacuum is currently running and for how long](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")
- [Performing a
  manual vacuum freeze](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")
- [Reindexing a table
  when autovacuum is running](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")
- [Managing
  autovacuum with large indexes](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")
- [Other parameters
  that affect autovacuum](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")
- [Setting
  table-level autovacuum parameters](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")
- [Logging autovacuum and
  vacuum activities](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")
- [Understanding the behavior of
  autovacuum with invalid databases](appendix.postgresql.commondbatasks.md "appendix.postgresql.commondbatasks.md")
- [Identify and resolve
  aggressive vacuum blockers in Aurora PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md")

## Allocating memory

for autovacuum

One of the most important parameters influencing autovacuum performance is the [`autovacuum_work_mem`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-AUTOVACUUM-WORK-MEM "https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-AUTOVACUUM-WORK-MEM") parameter. In Aurora PostgreSQL versions 14 and
prior, the `autovacuum_work_mem` parameter is set to -1, indicating that the
setting of `maintenance_work_mem` is used instead. For all other versions,
`autovacuum_work_mem` is determined by GREATEST({DBInstanceClassMemory/32768},
65536).

Manual vacuum operations always use the `maintenance_work_mem` setting, with a
default setting of GREATEST({DBInstanceClassMemory/63963136\*1024}, 65536), and it can also be
adjusted at the session level using the `SET` command for more targeted manual
`VACUUM` operations.

The `autovacuum_work_mem` determines memory for autovacuum to hold identifiers
of dead tuples (`pg_stat_all_tables.n_dead_tup`) for vacuuming indexes.

When doing calculations to determine the `autovacuum_work_mem` parameter's
value, be aware of the following:

- If you set the parameter too low, the vacuum process might have to scan the table
  multiple times to complete its work. Such multiple scans can have a negative impact on
  performance. For larger instances, setting `maintenance_work_mem` or
  `autovacuum_work_mem` to at least 1 GB can improve the performance of
  vacuuming tables with a high number of dead tuples. However, in PostgreSQL versions 16 and
  prior, vacuum’s memory usage is capped at 1 GB, which is sufficient to process
  approximately 179 million dead tuples in a single pass. If a table has more dead tuples
  than this, vacuum will need to make multiple passes through the table's indexes,
  significantly increasing the time required. Starting with PostgreSQL version 17, there
  isn't a limit of 1 GB, and autovacuum can process more than 179 million tuples by using
  radix trees.

A tuple identifier is 6 bytes in size. To estimate the memory needed for vacuuming an
index of a table, query `pg_stat_all_tables.n_dead_tup` to find the number of
dead tuples, then multiply this number by 6 to determine the memory required for vacuuming
the index in a single pass. You may use the following query:

```
SELECT
    relname AS table_name,
    n_dead_tup,
    pg_size_pretty(n_dead_tup * 6) AS estimated_memory
FROM
    pg_stat_all_tables
WHERE
    relname = '`name_of_the_table`';
```

- The `autovacuum_work_mem` parameter works in conjunction with the
  `autovacuum_max_workers` parameter. Each worker among
  `autovacuum_max_workers` can use the memory that you allocate. If you have
  many small tables, allocate more `autovacuum_max_workers` and less
  `autovacuum_work_mem`. If you have large tables (larger than 100 GB),
  allocate more memory and fewer worker processes. You need to have enough memory allocated
  to succeed on your biggest table. Thus, make sure that the combination of worker processes
  and memory equals the total memory that you want to allocate.

## Reducing

the likelihood of transaction ID wraparound

In some cases, parameter group settings related to autovacuum might not be aggressive
enough to prevent transaction ID wraparound. To address this, Aurora PostgreSQL provides a
mechanism that adapts the autovacuum parameter values automatically. _Adaptive
autovacuum_ is a feature for Aurora PostgreSQL. A detailed
explanation of [TransactionID wraparound](https://www.postgresql.org/docs/current/static/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND "https://www.postgresql.org/docs/current/static/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND") is found in the PostgreSQL documentation.

Adaptive autovacuum is turned on by default for Aurora PostgreSQL instances with the
dynamic parameter `rds.adaptive_autovacuum` set to ON. We strongly recommend that
you keep this turned on. However, to turn off adaptive autovacuum parameter tuning, set the
`rds.adaptive_autovacuum` parameter to 0 or OFF.

Transaction ID wraparound is still possible even when Aurora Amazon RDS tunes the autovacuum
parameters. We encourage you to implement an Amazon CloudWatch alarm for transaction ID wraparound. For
more information, see the post [Implement an early warning system for transaction ID wraparound in RDS for PostgreSQL](https://aws.amazon.com/blogs/database/implement-an-early-warning-system-for-transaction-id-wraparound-in-amazon-rds-for-postgresql/ "https://aws.amazon.com/blogs/database/implement-an-early-warning-system-for-transaction-id-wraparound-in-amazon-rds-for-postgresql/") on
the AWS Database Blog.

With adaptive autovacuum parameter tuning turned on, Amazon RDS begins adjusting autovacuum
parameters when the CloudWatch metric `MaximumUsedTransactionIDs` reaches the value of
the `autovacuum_freeze_max_age` parameter or 500,000,000, whichever is greater.

Amazon RDS continues to adjust parameters for autovacuum if a table continues to trend toward
transaction ID wraparound. Each of these adjustments dedicates more resources to autovacuum to
avoid wraparound. Amazon RDS updates the following autovacuum-related parameters:

- [autovacuum_vacuum_cost_delay](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-DELAY "https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-DELAY")
- [autovacuum_vacuum_cost_limit](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-LIMIT "https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-LIMIT")
- [`autovacuum_work_mem`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-AUTOVACUUM-WORK-MEM "https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-AUTOVACUUM-WORK-MEM")
- [autovacuum_naptime](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html#GUC-AUTOVACUUM-NAPTIME "https://www.postgresql.org/docs/current/runtime-config-autovacuum.html#GUC-AUTOVACUUM-NAPTIME")

RDS modifies these parameters only if the new value makes autovacuum more aggressive. The
parameters are modified in memory on the DB instance. The values in the parameter group
aren't changed. To view the current in-memory settings, use the PostgreSQL [SHOW](https://www.postgresql.org/docs/current/sql-show.html "https://www.postgresql.org/docs/current/sql-show.html") SQL command.

When Amazon RDS modifies any of these autovacuum parameters, it generates an event for the
affected DB instance. This event is visible on the AWS Management Console and through the Amazon RDS API. After
the `MaximumUsedTransactionIDs` CloudWatch metric returns below the threshold, Amazon RDS
resets the autovacuum-related parameters in memory back to the values specified in the
parameter group. It then generates another event corresponding to this change.
