# Determining

if autovacuum is currently running and for how long

If you need to manually vacuum a table, make sure to determine if autovacuum is currently
running. If it is, you might need to adjust parameters to make it run more efficiently, or
turn off autovacuum temporarily so that you can manually run VACUUM.

Use the following query to determine if autovacuum is running, how long it has been
running, and if it is waiting on another session.

```
SELECT datname, usename, pid, state, wait_event, current_timestamp - xact_start AS xact_runtime, query
FROM pg_stat_activity
WHERE upper(query) LIKE '%VACUUM%'
ORDER BY xact_start;
```

After running the query, you should see output similar to the following.

```

 datname | usename  |  pid  | state  | wait_event |      xact_runtime       | query
 --------+----------+-------+--------+------------+-------------------------+--------------------------------------------------------------------------------------------------------
 mydb    | rdsadmin | 16473 | active |            | 33 days 16:32:11.600656 | autovacuum: VACUUM ANALYZE public.mytable1 (to prevent wraparound)
 mydb    | rdsadmin | 22553 | active |            | 14 days 09:15:34.073141 | autovacuum: VACUUM ANALYZE public.mytable2 (to prevent wraparound)
 mydb    | rdsadmin | 41909 | active |            | 3 days 02:43:54.203349  | autovacuum: VACUUM ANALYZE public.mytable3
 mydb    | rdsadmin |   618 | active |            | 00:00:00                | SELECT datname, usename, pid, state, wait_event, current_timestamp - xact_start AS xact_runtime, query+
         |          |       |        |            |                         | FROM pg_stat_activity                                                                                 +
         |          |       |        |            |                         | WHERE query like '%VACUUM%'                                                                           +
         |          |       |        |            |                         | ORDER BY xact_start;                                                                                  +

```

Several issues can cause a long-running autovacuum session (that is, multiple days long).
The most common issue is that your [`maintenance_work_mem`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM "https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM") parameter value is set too low for the size of
the table or rate of updates.

We recommend that you use the following formula to set the
`maintenance_work_mem` parameter value.

```
GREATEST({DBInstanceClassMemory/63963136*1024},65536)
```

Short running autovacuum sessions can also indicate problems:

- It can indicate that there aren't enough `autovacuum_max_workers` for
  your workload. In this case, you need to indicate the number of workers.
- It can indicate that there is an index corruption (autovacuum crashes and restarts on
  the same relation but makes no progress). In this case, run a manual `vacuum freeze
verbose `table`` to see the exact cause.
