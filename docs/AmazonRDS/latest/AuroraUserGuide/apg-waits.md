# LWLock:MultiXact

The `LWLock:MultiXactMemberBuffer`, `LWLock:MultiXactOffsetBuffer`,
`LWLock:MultiXactMemberSLRU`, and `LWLock:MultiXactOffsetSLRU` wait events
indicate that a session is waiting to retrieve a list of transactions that modifies the same row in a given table.

- `LWLock:MultiXactMemberBuffer` – A process is waiting
  for I/O on a simple least-recently used (SLRU) buffer for a multixact member.
- `LWLock:MultiXactMemberSLRU` – A process is waiting
  to access the simple least-recently used (SLRU) cache for a multixact member.
- `LWLock:MultiXactOffsetBuffer` – A process is waiting
  for I/O on a simple least-recently used (SLRU) buffer for a multixact offset.
- `LWLock:MultiXactOffsetSLRU` – A process is waiting
  to access the simple least-recently used (SLRU) cache for a multixact offset.

###### Topics

- [Supported engine versions](#apg-waits.xactsync.context.supported "#apg-waits.xactsync.context.supported")
- [Context](#apg-waits.lwlockmultixact.context "#apg-waits.lwlockmultixact.context")
- [Likely causes of increased waits](#apg-waits.lwlockmultixact.causes "#apg-waits.lwlockmultixact.causes")
- [Actions](#apg-waits.lwlockmultixact.actions "#apg-waits.lwlockmultixact.actions")

## Supported engine versions

This wait event information is supported for all versions of Aurora PostgreSQL.

## Context

A _multixact_ is a data structure that stores
a list of transaction IDs (XIDs) that modify the same table row. When a single transaction
references a row in a table, the transaction ID is stored in the table header row. When multiple transactions
reference the same row in a table, the list of transaction IDs is stored in the
multixact data structure. The multixact wait events indicate that a session is retrieving
from the data structure the list of transactions that refer to a given row in a table.

## Likely causes of increased waits

Three common causes of multixact use are as follows:

- Sub-transactions from explicit savepoints – Explicitly
  creating a savepoint in your transactions spawns new transactions for the same row. For example, using
  `SELECT FOR UPDATE`, then `SAVEPOINT`, and then `UPDATE`.

Some drivers, object-relational mappers (ORMs), and abstraction layers have configuration
options for automatically wrapping all operations with savepoints. This can generate many
multixact wait events in some workloads. The PostgreSQL JDBC Driver's
`autosave` option is an example of this. For more information,
see [pgJDBC](https://jdbc.postgresql.org/ "https://jdbc.postgresql.org/") in the PostgreSQL JDBC documentation.
Another example is the PostgreSQL ODBC driver and its `protocol` option. For more information,
see [psqlODBC Configuration Options](https://odbc.postgresql.org/docs/config.html "https://odbc.postgresql.org/docs/config.html") in the
PostgreSQL ODBC driver documentation.

- Sub-transactions from PL/pgSQL EXCEPTION clauses – Each
  `EXCEPTION` clause that you write in your PL/pgSQL functions or procedures
  creates a `SAVEPOINT` internally.
- Foreign keys – Multiple transactions acquire
  a shared lock on the parent record.

When a given row is included in a multiple transaction operation, processing the row requires
retrieving transaction IDs from the `multixact` listings. If lookups can't get the
multixact from the memory cache, the data structure must be read from the Aurora storage layer. This
I/O from storage means that SQL queries can take longer. Memory cache misses
can start occurring with heavy usage due to a large number of multiple transactions. All these factors
contribute to an increase in this wait event.

## Actions

We recommend different actions depending on the causes of your wait event. Some of these actions can help in
immediate reduction of the wait events. But, others might require investigation and correction to scale your workload.

###### Topics

- [Perform vacuum freeze on tables with this wait event](#apg-waits.lwlockmultixact.actions.vacuumfreeze "#apg-waits.lwlockmultixact.actions.vacuumfreeze")
- [Increase autovacuum frequency on tables with this wait event](#apg-waits.lwlockmultixact.actions.autovacuum "#apg-waits.lwlockmultixact.actions.autovacuum")
- [Increase memory parameters](#apg-waits.lwlockmultixact.actions.memoryparam "#apg-waits.lwlockmultixact.actions.memoryparam")
- [Reduce long-running transactions](#apg-waits.lwlockmultixact.actions.longtransactions "#apg-waits.lwlockmultixact.actions.longtransactions")
- [Long term actions](#apg-waits.lwlockmultixact.actions.longactions "#apg-waits.lwlockmultixact.actions.longactions")

### Perform vacuum freeze on tables with this wait event

If this wait event spikes suddenly and affects your production environment, you can use any of the following temporary methods to reduce its count.

- Use _VACUUM FREEZE_ on the affected table or table partition
  to resolve the issue immediately. For more information, see [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "https://www.postgresql.org/docs/current/sql-vacuum.html").
- Use the VACUUM (FREEZE, INDEX_CLEANUP FALSE) clause to perform a quick vacuum by skipping the indexes.
  For more information, see [Vacuuming a table as quickly as possible](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.LargeIndexes.Executing "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.LargeIndexes.Executing").

### Increase autovacuum frequency on tables with this wait event

After scanning all tables in all databases, VACUUM will eventually remove multixacts, and their oldest multixact values are advanced.
For more information, see [Multixacts and Wraparound](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-MULTIXACT-WRAPAROUND "https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-MULTIXACT-WRAPAROUND").
To keep the LWLock:MultiXact wait events to its minimum, you must run the VACUUM as often as necessary. To do so, ensure that
the VACUUM in your Aurora PostgreSQL DB cluster is configured optimally.

If using VACUUM FREEZE on the affected table or table partition resolves the wait event issue, we recommend using a scheduler, such as `pg_cron`,
to perform the VACUUM instead of adjusting autovacuum at the instance level.

For the autovacuum to happen more frequently, you can reduce the value of the storage parameter `autovacuum_multixact_freeze_max_age` in the affected table.
For more information, see [autovacuum_multixact_freeze_max_age](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html#GUC-AUTOVACUUM-MULTIXACT-FREEZE-MAX-AGE "https://www.postgresql.org/docs/current/runtime-config-autovacuum.html#GUC-AUTOVACUUM-MULTIXACT-FREEZE-MAX-AGE").

### Increase memory parameters

You can optimize memory usage for multixact caches by adjusting the following parameters. These settings control how much memory is reserved for these caches,
which can help reduce multixact wait events in your workload. We recommend starting with the following values:

For Aurora PostgreSQL 17 and later:

- `multixact_offset_buffers` = 128
- `multixact_member_buffers` = 256

For Aurora PostgreSQL 16 and earlier:

- `multixact_offsets_cache_size` = 128
- `multixact_members_cache_size` = 256

###### Note

In Aurora PostgreSQL 17, parameter names were changed from `multixact_offsets_cache_size` to `multixact_offset_buffers` and from `multixact_members_cache_size` to `multixact_member_buffers` to align with community PostgreSQL 17.

You can set these parameters at the cluster level so that all instances in your cluster remain consistent. We recommend you to test and
adjust the values to best suit your specific workload requirements and instance class. You must reboot the writer instance for the parameter changes to take effect.

The parameters are expressed in terms of multixact cache entries. Each cache entry uses `8 KB` of memory. To calculate the total memory reserved, multiply each
parameter value by `8 KB`. For example, if you set a parameter to 128, the total reserved memory would be `128 * 8 KB = 1 MB`.

### Reduce long-running transactions

Long-running transaction causes the vacuum to retain its information until the transaction is committed or until the
read-only transaction is closed. We recommend that you proactively monitor and manage long-running transactions. For more information,
see [Database has long running idle in transaction connection](PostgreSQL.md#proactive-insights.idle-txn "PostgreSQL.md#proactive-insights.idle-txn").
Try to modify your application to avoid or minimize your use of long-running transactions.

### Long term actions

Examine your workload to discover the cause for the multixact spillover. You must fix the issue in order to scale your workload and reduce the wait event.

- You must analyze the DDL (data definition language) used to create your tables. Make sure that the table structures and indexes are well designed.
- When the affected tables have foreign keys, determine whether they are needed or if there is another way to enforce referential integrity.
- When a table has large unused indexes, it can cause autovacuum to not fit your workload and might block it from running. To avoid this, check for unused indexes and remove them completely. For more information, see
  [Managing autovacuum with large indexes](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md").
- Reduce the use of savepoints in your transactions.
