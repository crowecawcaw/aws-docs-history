# Wait events for Aurora PostgreSQL Limitless Database

A wait event in Aurora PostgreSQL indicates a resource for which a session is waiting, such as input/output (I/O) and locks. Wait
events are helpful in finding out why sessions are waiting for resources, and identifying bottlenecks. For more information, see
[Aurora PostgreSQL wait events](AuroraPostgreSQL.Tuning.md#AuroraPostgreSQL.Tuning.concepts.waits "AuroraPostgreSQL.Tuning.md#AuroraPostgreSQL.Tuning.concepts.waits").

Aurora PostgreSQL Limitless Database has its own wait events that are related to routers and shards. Many of them are for routers waiting on shards to
complete tasks. Shard wait events contain details on tasks that are being performed.

###### Topics

- [Querying for wait events](#limitless-monitoring-waits.query "#limitless-monitoring-waits.query")
- [Limitless Database wait events](limitless-waits-reference.md "limitless-waits-reference.md")

## Querying for wait events

You can use the [limitless_stat_activity](limitless-monitoring-views.md#limitless_stat_activity "limitless-monitoring-views.md#limitless_stat_activity") view to query for wait events, as
shown in the following example.

```
SELECT wait_event FROM rds_aurora.limitless_stat_activity WHERE wait_event_type='AuroraLimitless';

      wait_event
----------------------
 RemoteStatementSetup
 RemoteStatementSetup
(2 rows)
```

You can also use the `aurora_stat_system_waits` function to list the number of waits and the total time spent
on each wait event, as shown in the following example.

```
postgres_limitless=> SELECT type_name,event_name,waits,wait_time
    FROM aurora_stat_system_waits()
    NATURAL JOIN aurora_stat_wait_event()
    NATURAL JOIN aurora_stat_wait_type()
    WHERE type_name='AuroraLimitless'
    ORDER BY wait_time DESC;

    type_name    |       event_name          |  waits  |  wait_time
-----------------+---------------------------+---------+-------------
 AuroraLimitless | RemoteStatementSetup      |    7518 | 75236507897
 AuroraLimitless | RemoteStatementExecution  |      40 |      132986
 AuroraLimitless | Connect                   |       5 |        1453
(3 rows)
```
