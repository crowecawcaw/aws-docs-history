# Functions of postgres_get_av_diag() in Aurora PostgreSQL

The `postgres_get_av_diag()` function retrieves diagnostic information about
autovacuum processes that are blocking or lagging behind in a Aurora PostgreSQL database. The query
needs to be executed in the database with the oldest transaction ID for accurate results. For
more information about using the database with the oldest transaction ID, see [Not connected to
the database with the age of oldest transaction ID](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md")

```
SELECT
    blocker,
    DATABASE,
    blocker_identifier,
    wait_event,
    TO_CHAR(autovacuum_lagging_by, 'FM9,999,999,999') AS autovacuum_lagging_by,
    suggestion,
    suggested_action
FROM (
    SELECT
        *
    FROM
        rds_tools.postgres_get_av_diag ()
    ORDER BY
        autovacuum_lagging_by DESC) q;
```

The `postgres_get_av_diag()` function returns a table with the following
information:

**blocker**

Specifies the category of database activity that is blocking the vacuum.

- [Active statement](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Active_statement "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Active_statement")
- [Idle in transaction](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Idle_in_transaction "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Idle_in_transaction")
- [Prepared transaction](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Prepared_transaction "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Prepared_transaction")
- [Logical replication slot](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Logical_replication_slot "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Logical_replication_slot")
- [Reader instances](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Reader_instances "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Reader_instances")
- [Temporary tables](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Temporary_tables "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Temporary_tables")

**database**

Specifies the name of the database where applicable and supported. This is the
database in which the activity is ongoing and blocking or will block the autovacuum.
This is the database you are required to connect to and take action.

**blocker_identifier**

Specifies the identifier of the activity that is blocking or will block the
autovacuum. The identifier can be a process ID along with a SQL statement, a prepared
transaction, an IP address of a read replica, and the name of the replication slot,
either logical or physical.

**wait_event**

Specifies the
[wait
event](AuroraPostgreSQL.md "AuroraPostgreSQL.md") of the blocking session and is applicable for the following
blockers:

- Active statement
- Idle in transaction

**autovacum_lagging_by**

Specifies the number of transactions that autovacuum is lagging behind in its
backlog work per category.

**suggestion**

Specifies suggestions to resolve the blocker. These instructions include the name of
the database in which the activity exists where applicable, the Process ID (PID) of the
session where applicable, and the action to be taken.

**suggested_action**

Suggests the action that needs to be taken to resolve the blocker.
