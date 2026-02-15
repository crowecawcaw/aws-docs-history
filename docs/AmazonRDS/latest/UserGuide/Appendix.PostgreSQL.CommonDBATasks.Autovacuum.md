# Reindexing a table

when autovacuum is running

If an index has become corrupt, autovacuum continues to process the table and fails. If
you attempt a manual vacuum in this situation, you receive an error message like the
following.

```
`postgres=>`  `vacuum freeze pgbench_branches;`
`ERROR: index "pgbench_branches_test_index" contains unexpected
 zero page at block 30521
HINT: Please REINDEX it.`
```

When the index is corrupted and autovacuum is attempting to run on the table, you contend
with an already running autovacuum session. When you issue a [REINDEX](https://www.postgresql.org/docs/current/static/sql-reindex.html "https://www.postgresql.org/docs/current/static/sql-reindex.html")
command, you take out an exclusive lock on the table. Write operations are blocked, and also
read operations that use that specific index.

###### To reindex a table when autovacuum is running on the table

1. Open two sessions to the database containing the table that you want to vacuum. For
   the second session, use "screen" or another utility that maintains the session if your
   connection is dropped.
2. In session one, get the PID of the autovacuum session running on the table.

Run the following query to get the PID of the autovacuum session.

```
`SELECT datname, usename, pid, current_timestamp - xact_start
AS xact_runtime, query
FROM pg_stat_activity WHERE upper(query) like '%VACUUM%' ORDER BY
xact_start;`
```

3. In session two, issue the reindex command.

```
`\timing on`
`Timing is on.`
`reindex index pgbench_branches_test_index;`
`REINDEX
 Time: 9.966 ms`

```

4. In session one, if autovacuum was blocking the process, you see in
   `pg_stat_activity` that waiting is "T" for your vacuum session. In this case,
   you end the autovacuum process.

```
SELECT pg_terminate_backend('the_pid');
```

At this point, your session begins. It's important to note that autovacuum restarts
immediately because this table is probably the highest on its list of work. 5. Initiate your command in session two, and then end the autovacuum process in session

1.
