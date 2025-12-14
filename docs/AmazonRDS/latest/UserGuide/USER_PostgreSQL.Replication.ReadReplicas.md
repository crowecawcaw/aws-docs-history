# Troubleshooting for RDS for PostgreSQL read replica

Following, you can find troubleshooting ideas for some common RDS for PostgreSQL read
replica issues.

**Terminate the query that causes the read replica lag**

Transactions either in active or idle in transaction state that are
running for a long time in the database might interfere with the WAL
replication process, thereby increasing the replication lag. Therefore, be
sure to monitor the runtime of these transactions with the PostgreSQL
`pg_stat_activity` view.

Run a query on the primary instance similar to the following to find the
process ID (PID) of the query that's running for a long time:

```

SELECT datname, pid,usename, client_addr, backend_start,
xact_start, current_timestamp - xact_start AS xact_runtime, state,
backend_xmin FROM pg_stat_activity WHERE state='active';

```

```
SELECT now() - state_change as idle_in_transaction_duration, now() - xact_start as xact_duration,*
FROM  pg_stat_activity
WHERE state  = 'idle in transaction'
AND   xact_start is not null
ORDER BY 1 DESC;
```

After identifying the PID of the query, you can choose to end the
query.

Run a query on the primary instance similar to the following to terminate
the query that's running for a long time:

```
SELECT pg_terminate_backend(PID);
```
