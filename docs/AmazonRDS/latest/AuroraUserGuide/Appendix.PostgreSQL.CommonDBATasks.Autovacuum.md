# Performing a

manual vacuum freeze

You might want to perform a manual vacuum on a table that has a vacuum process already
running. This is useful if you have identified a table with an age approaching 2 billion
transactions (or above any threshold you are monitoring).

The following steps are guidelines, with several variations to the process. For example,
during testing, suppose that you find that the [`maintenance_work_mem`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM "https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM") parameter value is set too small and that you
need to take immediate action on a table. However, perhaps you don't want to bounce the
instance at the moment. Using the queries in previous sections, you determine which table is
the problem and notice a long running autovacuum session. You know that you need to change the
`maintenance_work_mem` parameter setting, but you also need to take immediate
action and vacuum the table in question. The following procedure shows what to do in this
situation.

###### To manually perform a vacuum freeze

1. Open two sessions to the database containing the table you want to vacuum. For the
   second session, use "screen" or another utility that maintains the session if your
   connection is dropped.
2. In session one, get the process ID (PID) of the autovacuum session running on the
   table.

Run the following query to get the PID of the autovacuum session.

```
SELECT datname, usename, pid, current_timestamp - xact_start
AS xact_runtime, query
FROM pg_stat_activity WHERE upper(query) LIKE '%VACUUM%' ORDER BY
xact_start;
```

3. In session two, calculate the amount of memory that you need for this operation. In
   this example, we determine that we can afford to use up to 2 GB of memory for this
   operation, so we set [`maintenance_work_mem`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM "https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM") for the current session to 2 GB.

```
`SET maintenance_work_mem='2 GB';`
`SET`
```

4. In session two, issue a `vacuum freeze verbose` command for the table. The
   verbose setting is useful because, although there is no progress report for this in
   PostgreSQL currently, you can see activity.

```
`\timing on`
`Timing is on.`
`vacuum freeze verbose pgbench_branches;`
```

```
INFO:  vacuuming "public.pgbench_branches"
INFO:  index "pgbench_branches_pkey" now contains 50 row versions in 2 pages
DETAIL:  0 index row versions were removed.
0 index pages have been deleted, 0 are currently reusable.
CPU 0.00s/0.00u sec elapsed 0.00 sec.
INFO:  index "pgbench_branches_test_index" now contains 50 row versions in 2 pages
DETAIL:  0 index row versions were removed.
0 index pages have been deleted, 0 are currently reusable.
CPU 0.00s/0.00u sec elapsed 0.00 sec.
INFO:  "pgbench_branches": found 0 removable, 50 nonremovable row versions
     in 43 out of 43 pages
DETAIL:  0 dead row versions cannot be removed yet.
There were 9347 unused item pointers.
0 pages are entirely empty.
CPU 0.00s/0.00u sec elapsed 0.00 sec.
VACUUM
Time: 2.765 ms

```

5. In session one, if autovacuum was blocking the vacuum session,
   `pg_stat_activity` shows that waiting is `T` for your vacuum
   session. In this case, end the autovacuum process as follows.

```
SELECT pg_terminate_backend('the_pid');
```

###### Note

Some lower versions of Amazon Aurora can't terminate an autovacuum process using the
preceding command and fail with the following error: `ERROR: 42501: must be a
 superuser to terminate superuser process LOCATION: pg_terminate_backend,
 signalfuncs.c:227`. To find the PostgreSQL versions
that have been patched, search for the following bullet in [Amazon Aurora PostgreSQL updates](../../../'.md "../../../'.md"):

```
Allow rds_superuser to terminate backends which are not explicitly associated with a role
```

At this point, your session begins. Autovacuum restarts immediately because this table
is probably the highest on its list of work. 6. Initiate your `vacuum freeze verbose` command in session two, and then end
the autovacuum process in session one.
