# Oracle and PostgreSQL table statistics

With AWS DMS, you can analyze table statistics for your Oracle and PostgreSQL databases to optimize query performance and storage utilization. Table statistics provide information about the data distribution and storage characteristics of database tables, including row counts, data sizes, and index usage.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                      |
| -------------------------------- | ---------------------------------- | ------------------------- | ---------------------------------------------------- |
| Three star feature compatibility | N/A                                | N/A                       | Syntax and option differences, similar functionality |

## Oracle usage

Table statistics are one of the important aspects affecting SQL query performance. They enable the query optimizer to make informed assumptions when deciding how to generate the execution plan for each query. Oracle provides the DBMS_STATS package to manage and control the table statistics, which can be collected automatically or manually.

The following statistics are usually collected on database tables and indexes:

- Number of table rows.
- Number of table blocks.
- Number of distinct values or nulls.
- Data distribution histograms.

### Automatic optimizer statistics collection

By default, Oracle collects table and index statistics during predefined maintenance windows using the database scheduler and automated maintenance tasks. The automatic statistics collection mechanism uses Oracle’s data modification monitoring feature that tracks the approximate number of `INSERT`, `UPDATE`, and `DELETE` statements to determine which table statistics should be collected.

Oracle 19 now allows to gather real-time statistics on tables during regular `UPDATE`, `INSERT`, and `DELETE` operations, which ensures that statistics are always up-to-date and are not going stale.

Oracle 19 also introduces High-Frequency Automatic Optimizer Statistics Collection with an ability to set up automatic task that will collect statistics for stale objects.

### Manual optimizer statistics collection

When the automatic statistics collection is not suitable for a particular use case, the optimizer statistics collection can be performed manually at several levels.

| Statistics level        | Description                               |
| ----------------------- | ----------------------------------------- |
| GATHER_INDEX_STATS      | Index statistics.                         |
| GATHER_TABLE_STATS      | Table, column, and index statistics.      |
| GATHER_SCHEMA_STATS     | Statistics for all objects in a schema.   |
| GATHER_DICTIONARY_STATS | Statistics for all dictionary objects.    |
| GATHER_DATABASE_STATS   | Statistics for all objects in a database. |

**Examples**

Collect statistics at the table level from the `HR` schema and the `EMPLOYEES` table.

```
BEGIN
DBMS_STATS.GATHER_TABLE_STATS('HR','EMPLOYEES');
END;
/

PL/SQL procedure successfully completed.
```

Collect statistics at a specific column level from the `HR` schema, the `EMPLOYEES` table, and the `DEPARTMENT_ID` column.

```
BEGIN
DBMS_STATS.GATHER_TABLE_STATS('HR','EMPLOYEES',
METHOD_OPT=>'FOR COLUMNS department_id');
END;
/

PL/SQL procedure successfully completed.
```

For more information, see [Optimizer Statistics Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/optimizer-statistics-concepts.html#GUID-C0E74ACE-2706-48A1-97A2-33F52207166A "https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/optimizer-statistics-concepts.html#GUID-C0E74ACE-2706-48A1-97A2-33F52207166A") in the _Oracle documentation_.

## PostgreSQL usage

Use the `ANALYZE` command to collect statistics about a database, a table or a specific table column. The PostgreSQL `ANALYZE` command collects table statistics which support generation of efficient query execution plans by the query planner.

- **Histograms** — `ANALYZE` will collect statistics on table columns values and create a histogram of the approximate data distribution in each column.
- **Pages and rows** — `ANALYZE` will collect statistics on the number of database pages and rows from which each table is comprised.
- **Data sampling** — For large tables, the `ANALYZE` command will take random samples of values rather than examining each and every single row. This allows the `ANALYZE` command to scan very large tables in a relatively small amount of time.
- **Statistic collection granularity** — Running the `ANALYZE` command without any parameter will instruct PostgreSQL to examine every table in the current schema. Supplying the table name or column name to the `ANALYZE`, will instruct the database to examine a specific table or table column.

### PostgreSQL automatic statistics collection

By default, PostgreSQL is configured with an autovacuum daemon, which automates the execution of statistics collection using the `ANALYZE` commands (in addition to automation of the `VACUUM` command). The autovacuum daemon scans for tables which show signs of large modifications in data to collect the current statistics. Autovacuum is controlled by several parameters.

Individual tables have several storage parameters which can trigger autovacuum process sooner or later. These parameters, such as `autovacuum_enabled`, `autovacuum_vacuum_threshold`, and others can be set or changed using `CREATE TABLE` or `ALTER TABLE` statements.

```
ALTER TABLE custom_autovaccum
  SET (autovacuum_enabled = true,
    autovacuum_vacuum_cost_delay = 10ms,
    autovacuum_vacuum_scale_factor = 0.01,
    autovacuum_analyze_scale_factor = 0.005);
```

The preceding command enables `autovaccum` for the `custom_autovaccum` table and will specify the `autovacuum` process to sleep for 10 milliseconds each run.

It also specifies a 1% of the table size to be added to `autovacuum_vacuum_threshold` and 0.5% of the table size to be added to `autovacuum_analyze_threshold` when deciding whether to trigger a VACUUM.

For more information, see [Automatic Vacuuming](https://www.postgresql.org/docs/13/runtime-config-autovacuum.html "https://www.postgresql.org/docs/13/runtime-config-autovacuum.html") in the _PostgreSQL documentation_.

### PostgreSQL manual statistics collection

PostgreSQL allows collecting statistics on-demand using the `ANALYZE` command at a database level, table level or column level.

- `ANALYZE` on indexes is not currently supported.
- `ANALYZE` requires only a read-lock on the target table, so it can run in parallel with other activity on the table.
- For large tables, `ANALYZE` takes a random sample of the table contents. Configured via the show `default_statistics_target` parameter. The default value is 100 entries. Raising the limit might allow more accurate planner estimates to be made at the price of consuming more space in the `pg_statistic` table.

**Examples**

Gather statistics for the entire database.

```
ANALYZE;
```

Gather statistics for a specific table. The `VERBOSE` keyword displays progress.

```
ANALYZE VERBOSE EMPLOYEES;
```

Gather statistics for a specific column.

```
ANALYZE EMPLOYEES (HIRE_DATE);
```

Specify the `default_statistics_target` parameter for an individual table column and reset it back to default.

```
ALTER TABLE EMPLOYEES ALTER COLUMN SALARY SET STATISTICS 150;

ALTER TABLE EMPLOYEES ALTER COLUMN SALARY SET STATISTICS -1;
```

Larger values increase the time needed to complete an `ANALYZE`, but improve the quality of the collected planner’s statistics which can potentially lead to better execution plans.

View the current (session / global) `default_statistics_target`, modify it to 150 and analyze the `EMPLOYEES` table.

```
SHOW default_statistics_target ;
SET default_statistics_target to 150;
ANALYZE EMPLOYEES;
```

View the last time statistics were collected for a table.

```
SELECT relname, last_analyze FROM pg_stat_all_tables;
```

## Summary

| Feature                                                   | Oracle                                                                                                                                                       | PostgreSQL                                                                                                                    |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Analyze a specific database table                         | `<br>BEGIN dbms_stats.gather_table_stats(<br>ownname =>'hr',<br>tabname => 'employees' , …<br>);<br>END;<br>`                                                | `<br>ANALYZE EMPLOYEES;<br>`                                                                                                  |
| Analyze a database table while only sampling certain rows | Configure using percentage of table rows to sample.<br>`<br>BEGIN dbms_stats.gather_tabke_stats(<br>ownname=>'HR', …<br>ESTIMATE_PERCENT=>100);<br>END;<br>` | Configure using the number of entries for the table.<br>`<br>SET default_statistics_target to 150;<br>ANALYZE EMPLOYEES;<br>` |
| Collect statistics for a schema                           | `<br>BEGIN<br>EXECUTE DBMS_STATS.GATHER_SCHEMA_STATS(<br>ownname => 'HR');<br>END<br>`                                                                       | `<br>ANALYZE;<br>`                                                                                                            |
| View last time statistics were collected                  | `<br>select owner, table_name, last_analyzed;<br>`                                                                                                           | `<br>select relname, last_analyze<br>from pg_stat_all_tables;<br>`                                                            |

For more information, see [ANALYZE](https://www.postgresql.org/docs/13/sql-analyze.html "https://www.postgresql.org/docs/13/sql-analyze.html") and [The Autovacuum Daemon](https://www.postgresql.org/docs/13/routine-vacuuming.html#AUTOVACUUM "https://www.postgresql.org/docs/13/routine-vacuuming.html#AUTOVACUUM") in the _PostgreSQL documentation_.
