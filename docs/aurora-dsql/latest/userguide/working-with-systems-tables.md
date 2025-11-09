# System tables and commands in Aurora DSQL

See the following sections to learn about the supported system tables and catalogs in
Aurora DSQL.

## System tables

Aurora DSQL is compatible with PostgreSQL, so many [system catalog
tables](https://www.PostgreSQL.org/docs/current/catalogs-overview.html "https://www.PostgreSQL.org/docs/current/catalogs-overview.html") and [views](https://www.PostgreSQL.org/docs/current/views.html "https://www.PostgreSQL.org/docs/current/views.html") from PostgreSQL also exist in Aurora DSQL.

### Important PostgreSQL catalog tables and

views

The following table describes the most common tables and views you might use in
Aurora DSQL.

| Name            | Description                                                |
| --------------- | ---------------------------------------------------------- |
| `pg_namespace`  | Information on all schemas                                 |
| `pg_tables`     | Information on the all tables                              |
| `pg_attribute`  | Information on all attributes                              |
| `pg_views`      | Information on (pre-)defined views                         |
| `pg_class`      | Describes all tables, column, indices, and similar objects |
| `pg_stats`      | A view on the planner statistics                           |
| `pg_user`       | Information on users                                       |
| `pg_roles`      | Information on users and groups                            |
| `pg_indexes`    | Lists all indexes                                          |
| `pg_constraint` | Lists constraints on tables                                |

### Supported and unsupported catalog

tables

The following table indicates which tables are supported and unsupported in
Aurora DSQL.

| Name                       | Applicable to Aurora DSQL |
| -------------------------- | ------------------------- |
| `pg_aggregate`             | No                        |
| `pg_am`                    | Yes                       |
| `pg_amop`                  | No                        |
| `pg_amproc`                | No                        |
| `pg_attrdef`               | Yes                       |
| `pg_attribute`             | Yes                       |
| `pg_authid`                | No (use `pg_roles`)       |
| `pg_auth_members`          | Yes                       |
| `pg_cast`                  | Yes                       |
| `pg_class`                 | Yes                       |
| `pg_collation`             | Yes                       |
| `pg_constraint`            | Yes                       |
| `pg_conversion`            | No                        |
| `pg_database`              | No                        |
| `pg_db_role_setting`       | Yes                       |
| `pg_default_acl`           | Yes                       |
| `pg_depend`                | Yes                       |
| `pg_description`           | Yes                       |
| `pg_enum`                  | No                        |
| `pg_event_trigger`         | No                        |
| `pg_extension`             | No                        |
| `pg_foreign_data_wrapper`  | No                        |
| `pg_foreign_server`        | No                        |
| `pg_foreign_table`         | No                        |
| `pg_index`                 | Yes                       |
| `pg_inherits`              | Yes                       |
| `pg_init_privs`            | No                        |
| `pg_language`              | No                        |
| `pg_largeobject`           | No                        |
| `pg_largeobject_metadata`  | Yes                       |
| `pg_namespace`             | Yes                       |
| `pg_opclass`               | No                        |
| `pg_operator`              | Yes                       |
| `pg_opfamily`              | No                        |
| `pg_parameter_acl`         | Yes                       |
| `pg_partitioned_table`     | No                        |
| `pg_policy`                | No                        |
| `pg_proc`                  | No                        |
| `pg_publication`           | No                        |
| `pg_publication_namespace` | No                        |
| `pg_publication_rel`       | No                        |
| `pg_range`                 | Yes                       |
| `pg_replication_origin`    | No                        |
| `pg_rewrite`               | No                        |
| `pg_seclabel`              | No                        |
| `pg_sequence`              | No                        |
| `pg_shdepend`              | Yes                       |
| `pg_shdescription`         | Yes                       |
| `pg_shseclabel`            | No                        |
| `pg_statistic`             | Yes                       |
| `pg_statistic_ext`         | No                        |
| `pg_statistic_ext_data`    | No                        |
| `pg_subscription`          | No                        |
| `pg_subscription_rel`      | No                        |
| `pg_tablespace`            | No                        |
| `pg_transform`             | No                        |
| `pg_trigger`               | No                        |
| `pg_ts_config`             | Yes                       |
| `pg_ts_config_map`         | Yes                       |
| `pg_ts_dict`               | Yes                       |
| `pg_ts_parser`             | Yes                       |
| `pg_ts_template`           | Yes                       |
| `pg_type`                  | Yes                       |
| `pg_user_mapping`          | No                        |

### Supported and unsupported system

views

The following table indicates which views are supported and unsupported in
Aurora DSQL.

| Name                              | Applicable to Aurora DSQL |
| --------------------------------- | ------------------------- |
| `pg_available_extensions`         | No                        |
| `pg_available_extension_versions` | No                        |
| `pg_backend_memory_contexts`      | Yes                       |
| `pg_config`                       | No                        |
| `pg_cursors`                      | No                        |
| `pg_file_settings`                | No                        |
| `pg_group`                        | Yes                       |
| `pg_hba_file_rules`               | No                        |
| `pg_ident_file_mappings`          | No                        |
| `pg_indexes`                      | Yes                       |
| `pg_locks`                        | No                        |
| `pg_matviews`                     | No                        |
| `pg_policies`                     | No                        |
| `pg_prepared_statements`          | No                        |
| `pg_prepared_xacts`               | No                        |
| `pg_publication_tables`           | No                        |
| `pg_replication_origin_status`    | No                        |
| `pg_replication_slots`            | No                        |
| `pg_roles`                        | Yes                       |
| `pg_rules`                        | No                        |
| `pg_seclabels`                    | No                        |
| `pg_sequences`                    | No                        |
| `pg_settings`                     | Yes                       |
| `pg_shadow`                       | Yes                       |
| `pg_shmem_allocations`            | Yes                       |
| `pg_stats`                        | Yes                       |
| `pg_stats_ext`                    | No                        |
| `pg_stats_ext_exprs`              | No                        |
| `pg_tables`                       | Yes                       |
| `pg_timezone_abbrevs`             | Yes                       |
| `pg_timezone_names`               | Yes                       |
| `pg_user`                         | Yes                       |
| `pg_user_mappings`                | No                        |
| `pg_views`                        | Yes                       |
| `pg_stat_activity`                | No                        |
| `pg_stat_replication`             | No                        |
| `pg_stat_replication_slots`       | No                        |
| `pg_stat_wal_receiver`            | No                        |
| `pg_stat_recovery_prefetch`       | No                        |
| `pg_stat_subscription`            | No                        |
| `pg_stat_subscription_stats`      | No                        |
| `pg_stat_ssl`                     | Yes                       |
| `pg_stat_gssapi`                  | No                        |
| `pg_stat_archiver`                | No                        |
| `pg_stat_io`                      | No                        |
| `pg_stat_bgwriter`                | No                        |
| `pg_stat_wal`                     | No                        |
| `pg_stat_database`                | No                        |
| `pg_stat_database_conflicts`      | No                        |
| `pg_stat_all_tables`              | No                        |
| `pg_stat_all_indexes`             | No                        |
| `pg_statio_all_tables`            | No                        |
| `pg_statio_all_indexes`           | No                        |
| `pg_statio_all_sequences`         | No                        |
| `pg_stat_slru`                    | No                        |
| `pg_statio_user_tables`           | No                        |
| `pg_statio_user_sequences`        | No                        |
| `pg_stat_user_functions`          | No                        |
| `pg_stat_user_indexes`            | No                        |
| `pg_stat_progress_analyze`        | No                        |
| `pg_stat_progress_basebackup`     | No                        |
| `pg_stat_progress_cluster`        | No                        |
| `pg_stat_progress_create_index`   | No                        |
| `pg_stat_progress_vacuum`         | No                        |
| `pg_stat_sys_indexes`             | No                        |
| `pg_stat_sys_tables`              | No                        |
| `pg_stat_xact_all_tables`         | No                        |
| `pg_stat_xact_sys_tables`         | No                        |
| `pg_stat_xact_user_functions`     | No                        |
| `pg_stat_xact_user_tables`        | No                        |
| `pg_statio_sys_indexes`           | No                        |
| `pg_statio_sys_sequences`         | No                        |
| `pg_statio_sys_tables`            | No                        |
| `pg_statio_user_indexes`          | No                        |

### The sys.jobs and sys.iam_pg_role_mappings views

Aurora DSQL supports the following system views:

**`sys.jobs`**

`sys.jobs` provides status information about asynchronous jobs. For
example, after you [create an
asynchronous index](working-with-create-index-async.md "working-with-create-index-async.md"), Aurora DSQL returns a `job_uuid`. You can use
this `job_uuid` with `sys.jobs` to look up the status of the
job.

```
SELECT * FROM sys.jobs WHERE job_id = 'example_job_uuid';

        job_id        |   status   | details
------------------+------------+---------
 example_job_uuid | processing |
(1 row)
```

**`sys.iam_pg_role_mappings`**

The view `sys.iam_pg_role_mappings` provides information about the
permissions granted to IAM users. For example, if
`DQSLDBConnect` is an IAM role that gives Aurora DSQL access to
non-admins and a user named `testuser` is granted the
`DQSLDBConnect` role and corresponding permissions, you can query the
`sys.iam_pg_role_mappings` view to see which users are granted which
permissions.

```
SELECT * FROM sys.iam_pg_role_mappings;
```

## Useful system metadata queries

Use these queries to get table statistics and metadata without performing expensive operations like full table scans.

### Get estimated row count for a table

To get the approximate count of rows in a table without performing a full table scan, use the following query:

```
SELECT reltuples FROM pg_class WHERE relname = '`table_name`';
```

The command returns output similar to the following:

```
  reltuples
--------------
 9.993836e+08
```

This approach is more efficient than `SELECT COUNT(*)` for large tables in Aurora DSQL.

## The `ANALYZE` command

The `ANALYZE` command collects statistics about the contents of tables in the database and stores the results in the `pg_stats` system view. Subsequently, the query planner uses these statistics to help determine the most efficient execution plans for queries.

In Aurora DSQL, you can't run the `ANALYZE` command within an explicit transaction. `ANALYZE` isn't subject to the database transaction timeout limit.

To reduce the need for manual intervention and keep statistics consistently up to date, Aurora DSQL automatically runs `ANALYZE` as a background process. This background job is triggered automatically based on the observed rate of change in the table. It is linked to the number of rows (tuples) that have been inserted, updated, or deleted since the last analyze.

`ANALYZE` runs asynchronously in the background and its activity can be monitored in the system view sys.jobs with the following query:

```
SELECT * FROM sys.jobs WHERE job_type = 'ANALYZE';
```

**Key considerations**

###### Note

`ANALYZE` jobs are billed like other asynchronous jobs in Aurora DSQL. When you modify a table, this may indirectly trigger an automatic background statistics collection job, which can result in metering charges due to the associated system-level activity.

Background `ANALYZE`jobs, triggered automatically, collect the same types of statistics as a manual `ANALYZE` and apply them by default to user tables. System and catalog tables are excluded from this automated process.
