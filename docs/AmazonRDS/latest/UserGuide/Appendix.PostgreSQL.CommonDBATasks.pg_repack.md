

# Reducing bloat in tables and indexes with the pg\_repack extension
<a name="Appendix.PostgreSQL.CommonDBATasks.pg_repack"></a>

You can use the `pg_repack` extension to remove bloat from tables and indexes as an alternative to `VACUUM FULL`. This extension is supported on RDS for PostgreSQL versions 9.6.3 and higher. For more information on the `pg_repack` extension and the full table repack, see the [GitHub project documentation](https://reorg.github.io/pg_repack/).

Unlike `VACUUM FULL`, the `pg_repack` extension requires an exclusive lock (AccessExclusiveLock) only for a short period of time during the table rebuild operation in the following cases:
+ Initial creation of log table – A log table is created to record changes that occur during initial copy of the data, as shown in the following example: 

  ```
  postgres=>\dt+ repack.log_*
  List of relations
  -[ RECORD 1 ]-+----------
  Schema        | repack
  Name          | log_16490
  Type          | table
  Owner         | postgres
  Persistence   | permanent
  Access method | heap
  Size          | 65 MB
  Description   |
  ```
+ Final swap-and-drop phase.

For the rest of the rebuild operation, it only needs an `ACCESS SHARE` lock on the original table to copy rows from it to the new table. This helps the INSERT, UPDATE, and DELETE operations to proceed as usual.

## Recommendations
<a name="Appendix.PostgreSQL.CommonDBATasks.pg_repack.Recommen"></a>

The following recommendations apply when you remove bloat from the tables and indexes using the `pg_repack` extension:
+ Perform repack during non-business hours or over a maintenance window to minimize its impact on performance of other database activities.
+ Closely monitor blocking sessions during the rebuild activity and ensure that there is no activity on the original table that could potentially block `pg_repack`, specifically during the final swap-and-drop phase when it needs an exclusive lock on the original table. For more information, see [Identifying what is blocking a query](https://repost.aws/knowledge-center/rds-aurora-postgresql-query-blocked). 

  When you see a blocking session, you can terminate it using the following command after careful consideration. This helps in the continuation of `pg_repack` to finish the rebuild:

  ```
  SELECT pg_terminate_backend({{pid}});
  ```
+ While applying the accrued changes from the `pg_repack's` log table on systems with a very high transaction rate, the apply process might not be able to keep up with the rate of changes. In such cases, `pg_repack` would not be able to complete the apply process. For more information, see [Monitoring the new table during the repack](#Appendix.PostgreSQL.CommonDBATasks.pg_repack.Monitoring). If indexes are severely bloated, an alternative solution is to perform an index only repack. This also helps VACUUM's index cleanup cycles to finish faster.

  You can skip the index cleanup phase using manual VACUUM from PostgreSQL version 12, and it is skipped automatically during emergency autovacuum from PostgreSQL version 14. This helps VACUUM complete faster without removing the index bloat and is only meant for emergency situations such as preventing wraparound VACUUM. For more information, see [ Avoiding bloat in indexes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.diag-table-ind-bloat.html#AuroraPostgreSQL.diag-table-ind-bloat.AvoidinginIndexes) in the Amazon Aurora User Guide.

## Pre-requisites
<a name="Appendix.PostgreSQL.CommonDBATasks.pg_repack.Prereq"></a>
+ The table must have PRIMARY KEY or not-null UNIQUE constraint.
+ The extension version must be the same for both the client and the server.
+ Ensure that the RDS instance has more `FreeStorageSpace` than the total size of the table without the bloat. As an example, consider the total size of the table including TOAST and indexes as 2TB, and total bloat in the table as 1TB. The required `FreeStorageSpace` must be more than value returned by the following calculation:

   `2TB (Table size)` - `1TB (Table bloat)` = `1TB`

  You can use the following query to check the total size of the table and use `pgstattuple` to derive bloat. For more information, see [Diagnosing table and index bloat](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.diag-table-ind-bloat.html) in the Amazon Aurora User Guide 

  ```
  SELECT pg_size_pretty(pg_total_relation_size('table_name')) AS total_table_size;
  ```

  This space is reclaimed after the completion of the activity. 
+ Ensure that the RDS instance has enough compute and IO capacity to handle the repack operation. You might consider to scale up the instance class for optimal balance of performance. 

**To use the `pg_repack` extension**

1. Install the `pg_repack` extension on your RDS for PostgreSQL DB instance by running the following command.

   ```
   CREATE EXTENSION pg_repack;
   ```

1. Run the following commands to grant write access to temporary log tables created by `pg_repack`.

   ```
   ALTER DEFAULT PRIVILEGES IN SCHEMA repack GRANT INSERT ON TABLES TO PUBLIC;
   ALTER DEFAULT PRIVILEGES IN SCHEMA repack GRANT USAGE, SELECT ON SEQUENCES TO PUBLIC;
   ```

1. Connect to the database using the `pg_repack` client utility. Use an account that has `rds_superuser` privileges. As an example, assume that `rds_test` role has `rds_superuser` privileges. The following syntax performs `pg_repack` for full tables including all the table indexes in the `postgres` database.

   ```
   pg_repack -h {{db-instance-name}}.111122223333.{{aws-region}}.rds.amazonaws.com -U {{rds_test}} -k {{postgres}}
   ```
**Note**  
You must connect using the -k option. The -a option is not supported.

   The response from the `pg_repack` client provides information on the tables on the DB instance that are repacked.

   ```
   INFO: repacking table "pgbench_tellers"
   INFO: repacking table "pgbench_accounts"
   INFO: repacking table "pgbench_branches"
   ```

1. The following syntax repacks a single table `orders` including indexes in `postgres` database.

   ```
   pg_repack -h db-instance-name.111122223333.aws-region.rds.amazonaws.com -U {{rds_test}} --table {{orders}} -k {{postgres}}
   ```

   The following syntax repacks only indexes for `orders` table in `postgres` database.

   ```
   pg_repack -h db-instance-name.111122223333.aws-region.rds.amazonaws.com -U {{rds_test}} --table {{orders}} --only-indexes -k {{postgres}}
   ```

## Monitoring the new table during the repack
<a name="Appendix.PostgreSQL.CommonDBATasks.pg_repack.Monitoring"></a>
+ The size of the database is increased by the total size of the table minus bloat, until swap-and-drop phase of repack. You can monitor the growth rate of the database size, calculate the speed of the repack, and roughly estimate the time it takes to complete initial data transfer.

  As an example, consider the total size of the table as 2TB, the size of the database as 4TB, and total bloat in the table as 1TB. The database total size value returned by the calculation at the end of the repack operation is the following:

   `2TB (Table size)` \+ `4 TB (Database size)` - `1TB (Table bloat)` = `5TB`

  You can roughly estimate the speed of the repack operation by sampling the growth rate in bytes between two points in time. If the growth rate is 1GB per minute, it can take 1000 minutes or 16.6 hours approximately to complete the initial table build operation. In addition to the initial table build, `pg_repack` also needs to apply accrued changes. The time it takes depends on the rate of applying ongoing changes plus accrued changes.
**Note**  
You can use `pgstattuple` extension to calculate the bloat in the table. For more information, see [pgstattuple ](https://www.postgresql.org/docs/current/pgstattuple.html).
+ The number of rows in the `pg_repack's` log table, under the repack schema represents the volume of changes pending to be applied to the new table after the initial load.

  You can check the `pg_repack's` log table in `pg_stat_all_tables` to monitor the changes applied to the new table. `pg_stat_all_tables.n_live_tup` indicates the number of records that are pending to be applied to the new table. For more information, see [pg\_stat\_all\_tables](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ALL-TABLES-VIEW). 

  ```
  postgres=>SELECT relname,n_live_tup FROM pg_stat_all_tables WHERE schemaname = 'repack' AND relname ILIKE '%log%';
          
  -[ RECORD 1 ]---------
  relname    | log_16490
  n_live_tup | 2000000
  ```
+ You can use the `pg_stat_statements` extension to find out the time taken by each step in the repack operation. This is helpful in preparation for applying the same repack operation in a production environment. You may adjust the `LIMIT` clause for extending the output further.

  ```
  postgres=>SELECT
       SUBSTR(query, 1, 100) query,
       round((round(total_exec_time::numeric, 6) / 1000 / 60),4) total_exec_time_in_minutes
   FROM
       pg_stat_statements
   WHERE
       query ILIKE '%repack%'
   ORDER BY
       total_exec_time DESC LIMIT 5;
          
   query                                                                 | total_exec_time_in_minutes
  -----------------------------------------------------------------------+----------------------------
   CREATE UNIQUE INDEX index_16493 ON repack.table_16490 USING btree (a) |                     6.8627
   INSERT INTO repack.table_16490 SELECT a FROM ONLY public.t1           |                     6.4150
   SELECT repack.repack_apply($1, $2, $3, $4, $5, $6)                    |                     0.5395
   SELECT repack.repack_drop($1, $2)                                     |                     0.0004
   SELECT repack.repack_swap($1)                                         |                     0.0004
  (5 rows)
  ```

Repacking is completely an out-of-place operation so the original table is not impacted and we do not anticipate any unexpected challenges that require recovery of the original table. If repack fails unexpectedly, you must inspect the cause of the error and resolve it.

After the issue is resolved, drop and recreate the `pg_repack` extension in the database where the table exists, and retry the `pg_repack` step. In addition, the availability of compute resources and concurrent accessibility of the table plays a crucial role in the timely completion of the repack operation.