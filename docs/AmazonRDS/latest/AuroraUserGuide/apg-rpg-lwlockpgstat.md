# LWLock:pg_stat_statements

The LWLock:pg_stat_statements wait event occurs when the `pg_stat_statements`
extension takes an exclusive lock on the hash table that tracks SQL statements. This happens
in the following scenarios:

- When the number of tracked statements reaches the configured
  `pg_stat_statements.max` parameter value and there is a need to make
  room for more entries, the extension performs a sort on the number of calls, removes
  the 5% of the least-executed statements, and re-populates the hash with the
  remaining entries.
- When `pg_stat_statements` performs a `garbage collection`
  operation to the `pgss_query_texts.stat` file on disk and rewrites the
  file.

###### Topics

- [Supported engine versions](#apg-rpg-lwlockpgstat.supported "#apg-rpg-lwlockpgstat.supported")
- [Context](#apg-rpg-lwlockpgstat.context "#apg-rpg-lwlockpgstat.context")
- [Likely causes of increased waits](#apg-rpg-lwlockpgstat.causes "#apg-rpg-lwlockpgstat.causes")
- [Actions](#apg-rpg-lwlockpgstat.actions "#apg-rpg-lwlockpgstat.actions")

## Supported engine versions

This wait event information is supported for all versions of Aurora PostgreSQL.

## Context

Understanding the pg_stat_statements extension –
The pg_stat_statements extension tracks SQL statement execution statistics in a hash
table. The extension tracks SQL statements up to the limit defined by the `pg_stat_statements.max`
parameter. This parameter determines the maximum number of statements that can be tracked which corresponds to the maximum number of rows in the pg_stat_statements view.

Statement statistics persistence – The extension
persists statement statistics across instance restarts by:

- Writing data to a file named pg_stat_statements.stat
- Using the pg_stat_statements.save parameter to control persistence
  behavior

When pg_stat_statements.save is set to:

- on (default): Statistics are saved at shutdown and reloaded at server
  start
- off: Statistics are neither saved at shutdown nor reloaded at server
  start

Query text storage – The extension stores the
text of tracked queries in a file named `pgss_query_texts.stat`. This
file can grow to double the average size of all tracked SQL statements before
garbage collection occurs. The extension requires an exclusive lock on the hash table during cleanup operations and
rewrite `pgss_query_texts.stat` file.

Statement deallocation process – When the number
of tracked statements reaches the `pg_stat_statements.max` limit and new statements need
to be tracked, the extension:

- Takes an exclusive lock (LWLock:pg_stat_statements) on the hash table.
- Loads existing data into local memory.
- Performs a quicksort based on the number of calls.
- Removes the least-called statements (bottom 5%).
- Re-populates the hash table with the remaining entries.

Monitoring statement deallocation – In
PostgreSQL 14 and later, you can monitor statement deallocation using the
pg_stat_statements_info view. This view includes a dealloc column that shows how many
times statements were deallocated to make room for new ones

If the deallocation of statements occurs frequently, it will lead to more frequent
garbage collection of the `pgss_query_texts.stat` file on disk.

## Likely causes of increased waits

The typical causes of increased `LWLock:pg_stat_statements` waits
include:

- An increase in the number of unique queries used by the application.
- The `pg_stat_statements.max` parameter value being small compared
  to the number of unique queries being used.

## Actions

We recommend different actions depending on the causes of your wait event. You might
identify `LWLock:pg_stat_statements` events by using Amazon RDS Performance
Insights or by querying the view `pg_stat_activity`.

Adjust the following `pg_stat_statements` parameters to control
tracking behavior and reduce LWLock:pg_stat\_
statements wait events.

###### Topics

- [Disable pg_stat_statements.track parameter](#apg-rpg-lwlockpgstat.actions.disabletrack "#apg-rpg-lwlockpgstat.actions.disabletrack")
- [Increase pg_stat_statements.max parameter](#apg-rpg-lwlockpgstat.actions.increasemax "#apg-rpg-lwlockpgstat.actions.increasemax")
- [Disable pg_stat_statements.track_utility parameter](#apg-rpg-lwlockpgstat.actions.disableutility "#apg-rpg-lwlockpgstat.actions.disableutility")

### Disable pg_stat_statements.track parameter

If the LWLock:pg_stat_statements wait event is adversely impacting database
performance, and a rapid solution is required before further analysis of the
`pg_stat_statements` view to identify the root cause, the
`pg_stat_statements.track` parameter can be disabled by setting it to
`none`. This will disable the collection of statement
statistics.

### Increase pg_stat_statements.max parameter

To reduce deallocation and minimize garbage collection of the
`pgss_query_texts.stat` file on disk, increase the value of the
`pg_stat_statements.max` parameter. The default value is
`5,000`.

###### Note

The `pg_stat_statements.max` parameter is static. You must restart
your DB instance to apply any changes to this parameter.

### Disable pg_stat_statements.track_utility parameter

You can analyze the pg_stat_statements view to determine which utility commands
are consuming the most resources tracked by `pg_stat_statements`.

The `pg_stat_statements.track_utility` parameter controls whether the
module tracks utility commands, which include all commands except SELECT, INSERT,
UPDATE, DELETE, and MERGE. By default, this parameter is set to
`on`.

For example, when your application uses many savepoint queries, which are inherently unique, it
can increase statement deallocation. To address this, you can disable the
`pg_stat_statements.track_utility` parameter to stop
`pg_stat_statements` from tracking savepoint queries.

###### Note

The `pg_stat_statements.track_utility` parameter is a dynamic
parameter. You can change its value without restarting your database
instance.

###### Example of unique save point queries in pg_stat_statements

```

                     query                       |       queryid
-------------------------------------------------+---------------------
 SAVEPOINT JDBC_SAVEPOINT_495701                 | -7249565344517699703
 SAVEPOINT JDBC_SAVEPOINT_1320                   | -1572997038849006629
 SAVEPOINT JDBC_SAVEPOINT_26739                  |  54791337410474486
 SAVEPOINT JDBC_SAVEPOINT_1294466                |  8170064357463507593
 ROLLBACK TO SAVEPOINT JDBC_SAVEPOINT_65016      | -33608214779996400
 SAVEPOINT JDBC_SAVEPOINT_14185                  | -2175035613806809562
 SAVEPOINT JDBC_SAVEPOINT_45837                  | -6201592986750645383
 SAVEPOINT JDBC_SAVEPOINT_1324                   |  6388797791882029332
```

PostgreSQL 17 introduces several enhancements for utility command tracking:

- Savepoint names are now displayed as constants.
- Global Transaction IDs (GIDs) of two-phase commit commands are now displayed as constants.
- Names of DEALLOCATE statements are shown as constants.
- CALL parameters are now displayed as constants.
