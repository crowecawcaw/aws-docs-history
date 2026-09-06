

# System tables and commands in Aurora DSQL
<a name="working-with-systems-tables"></a>

See the following sections to learn about the supported system tables and catalogs in Aurora DSQL as well as useful queries for fetching information about the system, such as the version.

## System tables
<a name="working-with-system-tables-queries"></a>

Aurora DSQL is compatible with PostgreSQL, so many [ system catalog tables](https://www.PostgreSQL.org/docs/current/catalogs-overview.html) and [ views](https://www.PostgreSQL.org/docs/current/views.html) from PostgreSQL also exist in Aurora DSQL.

### Important PostgreSQL catalog tables and views
<a name="dsql-catalog-tables"></a>

The following table describes the most common tables and views you might use in Aurora DSQL.


| Name | Description | 
| --- | --- | 
| `pg_namespace` | Information on all schemas | 
| `pg_tables` | Information on the all tables | 
| `pg_attribute` | Information on all attributes | 
| `pg_views` | Information on (pre-)defined views | 
| `pg_class` | Describes all tables, column, indices, and similar objects | 
| `pg_stats` | A view on the planner statistics | 
| `pg_user` | Information on users | 
| `pg_roles` | Information on users and groups | 
| `pg_indexes` | Lists all indexes | 
| `pg_constraint` | Lists constraints on tables | 

### Supported and unsupported catalog tables
<a name="dsql-catalog-tables-supported"></a>

The following table indicates which tables are supported and unsupported in Aurora DSQL.


| Name | Applicable to Aurora DSQL | 
| --- | --- | 
| `pg_aggregate` | No | 
| `pg_am` | Yes | 
| `pg_amop` | No | 
| `pg_amproc` | No | 
| `pg_attrdef` | Yes | 
| `pg_attribute` | Yes | 
| `pg_authid` | No (use `pg_roles`) | 
| `pg_auth_members` | Yes | 
| `pg_cast` | Yes | 
| `pg_class` | Yes | 
| `pg_collation` | Yes | 
| `pg_constraint` | Yes | 
| `pg_conversion` | No | 
| `pg_database` | No | 
| `pg_db_role_setting` | Yes | 
| `pg_default_acl` | Yes | 
| `pg_depend` | Yes | 
| `pg_description` | Yes | 
| `pg_enum` | No | 
| `pg_event_trigger` | No | 
| `pg_extension` | No | 
| `pg_foreign_data_wrapper` | No | 
| `pg_foreign_server` | No | 
| `pg_foreign_table` | No | 
| `pg_index` | Yes | 
| `pg_inherits` | Yes | 
| `pg_init_privs` | No | 
| `pg_language` | No | 
| `pg_largeobject` | No | 
| `pg_largeobject_metadata` | Yes | 
| `pg_namespace` | Yes | 
| `pg_opclass` | No | 
| `pg_operator` | Yes | 
| `pg_opfamily` | No | 
| `pg_parameter_acl` | Yes | 
| `pg_partitioned_table` | No | 
| `pg_policy` | No | 
| `pg_proc` | No | 
| `pg_publication` | No | 
| `pg_publication_namespace` | No | 
| `pg_publication_rel` | No | 
| `pg_range` | Yes | 
| `pg_replication_origin` | No | 
| `pg_rewrite` | No | 
| `pg_seclabel` | No | 
| `pg_sequence` | No | 
| `pg_shdepend` | Yes | 
| `pg_shdescription` | Yes | 
| `pg_shseclabel` | No | 
| `pg_statistic` | Yes | 
| `pg_statistic_ext` | No | 
| `pg_statistic_ext_data` | No | 
| `pg_subscription` | No | 
| `pg_subscription_rel` | No | 
| `pg_tablespace` | No | 
| `pg_transform` | No | 
| `pg_trigger` | No | 
| `pg_ts_config` | Yes | 
| `pg_ts_config_map` | Yes | 
| `pg_ts_dict` | Yes | 
| `pg_ts_parser` | Yes | 
| `pg_ts_template` | Yes | 
| `pg_type` | Yes | 
| `pg_user_mapping` | No | 

### Supported and unsupported system views
<a name="dsql-system-tables-supported"></a>

The following table indicates which views are supported and unsupported in Aurora DSQL.


| Name | Applicable to Aurora DSQL | 
| --- | --- | 
| `pg_available_extensions` | No | 
| `pg_available_extension_versions` | No | 
| `pg_backend_memory_contexts` | Yes | 
| `pg_config` | No | 
| `pg_cursors` | No | 
| `pg_file_settings` | No | 
| `pg_group` | Yes | 
| `pg_hba_file_rules` | No | 
| `pg_ident_file_mappings` | No | 
| `pg_indexes` | Yes | 
| `pg_locks` | No | 
| `pg_matviews` | No | 
| `pg_policies` | No | 
| `pg_prepared_statements` | No | 
| `pg_prepared_xacts` | No | 
| `pg_publication_tables` | No | 
| `pg_replication_origin_status` | No | 
| `pg_replication_slots` | No | 
| `pg_roles` | Yes | 
| `pg_rules` | No | 
| `pg_seclabels` | No | 
| `pg_sequences` | No | 
| `pg_settings` | Yes | 
| `pg_shadow` | Yes | 
| `pg_shmem_allocations` | Yes | 
| `pg_stats` | Yes | 
| `pg_stats_ext` | No | 
| `pg_stats_ext_exprs` | No | 
| `pg_tables` | Yes | 
| `pg_timezone_abbrevs` | Yes | 
| `pg_timezone_names` | Yes | 
| `pg_user` | Yes | 
| `pg_user_mappings` | No | 
| `pg_views` | Yes | 
| `pg_stat_activity` | No | 
| `pg_stat_replication` | No | 
| `pg_stat_replication_slots` | No | 
| `pg_stat_wal_receiver` | No | 
| `pg_stat_recovery_prefetch` | No | 
| `pg_stat_subscription` | No | 
| `pg_stat_subscription_stats` | No | 
| `pg_stat_ssl` | Yes | 
| `pg_stat_gssapi` | No | 
| `pg_stat_archiver` | No | 
| `pg_stat_io` | No | 
| `pg_stat_bgwriter` | No | 
| `pg_stat_wal` | No | 
| `pg_stat_database` | No | 
| `pg_stat_database_conflicts` | No | 
| `pg_stat_all_tables` | No | 
| `pg_stat_all_indexes` | No | 
| `pg_statio_all_tables` | No | 
| `pg_statio_all_indexes` | No | 
| `pg_statio_all_sequences` | No | 
| `pg_stat_slru` | No | 
| `pg_statio_user_tables` | No | 
| `pg_statio_user_sequences` | No | 
| `pg_stat_user_functions` | No | 
| `pg_stat_user_indexes` | No | 
| `pg_stat_progress_analyze` | No | 
| `pg_stat_progress_basebackup` | No | 
| `pg_stat_progress_cluster` | No | 
| `pg_stat_progress_create_index` | No | 
| `pg_stat_progress_vacuum` | No | 
| `pg_stat_sys_indexes` | No | 
| `pg_stat_sys_tables` | No | 
| `pg_stat_xact_all_tables` | No | 
| `pg_stat_xact_sys_tables` | No | 
| `pg_stat_xact_user_functions` | No | 
| `pg_stat_xact_user_tables` | No | 
| `pg_statio_sys_indexes` | No | 
| `pg_statio_sys_sequences` | No | 
| `pg_statio_sys_tables` | No | 
| `pg_statio_user_indexes` | No | 

### The sys.jobs view
<a name="dsql-sys-jobs"></a>

`sys.jobs` provides status information about asynchronous jobs. For example, after you [create an asynchronous index](working-with-create-index-async.md), Aurora DSQL returns a `job_uuid`. You can use this `job_uuid` with `sys.jobs` to look up the status of the job.

```
SELECT * FROM sys.jobs;
```

Aurora DSQL returns a response similar to the following.

```
           job_id           |  status   | details |  job_type   | class_id | object_id |    object_name    |       start_time       |      update_time
----------------------------+-----------+---------+-------------+----------+-----------+-------------------+------------------------+------------------------
 wqhu6ewifze5xitg3umt24h5ua | completed |         | INDEX_BUILD |     1259 |     26433 | public.nt2_c1_idx | 2025-09-25 22:07:31+00 | 2025-09-25 22:07:46+00
 kkngzf33dndl3daacxehpx5eba | completed |         | ANALYZE     |     1259 |     26419 | public.nt         | 2025-09-25 21:57:05+00 | 2025-09-25 21:57:27+00
 fyopxjb6ovdn7po6lrkj63cyea | completed |         | DROP        |     1259 |     26422 |                   | 2025-09-25 22:05:57+00 | 2025-09-25 22:06:03+00
```

The following table describes the columns in the `sys.jobs` view.


**sys.jobs view columns**  

| Column | Type | Description | 
| --- | --- | --- | 
| job\_id | text | A base-32 UUID representing the job. | 
| status | text | The current status of the job. Possible values are submitted, processing, completed, and failed. For more information, see [sys.jobs status values](#dsql-sys-jobs-status-values). | 
| details | text | Any relevant details about the job. If the job fails, a detailed reason is provided. | 
| job\_type | text | The type of asynchronous job. Possible values are: INDEX\_BUILD – an asynchronous index build. ANALYZE – a system-submitted auto-analyze job. DROP – removes physical data after a DROP TABLE or DROP INDEX operation. | 
| class\_id | oid | The OID of the catalog table which contains the object. | 
| object\_id | oid | The OID of the object. | 
| object\_name | text | The fully qualified name of the object. DROP jobs cannot reference already dropped objects. If a referenced object has already been dropped, the object\_name may be NULL. | 
| start\_time | timestamp with time zone | The timestamp at which the job was submitted. | 
| update\_time | timestamp with time zone | The timestamp at which the job row was last updated. | 


**sys.jobs status values**  

| Status | Description | 
| --- | --- | 
| submitted | The task is submitted, but Aurora DSQL hasn't started to process it yet. | 
| processing | Aurora DSQL is processing the task. | 
| failed | The task failed. See the details column for more information. | 
| completed | Aurora DSQL has completed the task successfully. | 

### The sys.iam\_pg\_role\_mappings view
<a name="dsql-sys-iam-pg-role-mappings"></a>

The view `sys.iam_pg_role_mappings` provides information about the permissions granted to IAM users. For example, if `DQSLDBConnect` is an IAM role that gives Aurora DSQL access to non-admins and a user named `testuser` is granted the `DQSLDBConnect` role and corresponding permissions, you can query the `sys.iam_pg_role_mappings` view to see which users are granted which permissions.

```
SELECT * FROM sys.iam_pg_role_mappings;
```

## Useful system metadata queries
<a name="dsql-useful-system-queries"></a>

Use these queries to get table statistics and system metadata without performing expensive operations like full table scans.

### Get estimated row count for a table
<a name="dsql-get-row-count"></a>

To get the approximate count of rows in a table without performing a full table scan, use the following query:

```
SELECT reltuples FROM pg_class WHERE relname = '{{table_name}}';
```

The command returns output similar to the following:

```
  reltuples
--------------
 9.993836e+08
```

This approach is more efficient than `SELECT COUNT(*)` for large tables in Aurora DSQL.

### Get current Aurora DSQL major version
<a name="dsql-get-major-version"></a>

To get the current major version of the Aurora DSQL cluster, use the following query:

```
SELECT * FROM sys.dsql_major_version();
```

The command returns output similar to the following:

```
 dsql_major_version
--------------------
                  1
```

This returns the major version the SQL connection is on in Aurora DSQL.

### Get current PostgreSQL version
<a name="dsql-get-pg-version"></a>

To get the current PostgreSQL version of the Aurora DSQL cluster, use the following query:

```
SHOW server_version;
```

The command returns output similar to the following:

```
 server_version
----------------
 16.13
```

This returns the PostgreSQL version the SQL connection is on in Aurora DSQL.

## The `ANALYZE` command
<a name="working-with-system-tables-analyze"></a>

 The `ANALYZE `command collects statistics about the contents of tables in the database and stores the results in the `pg_stats` system view. Subsequently, the query planner uses these statistics to help determine the most efficient execution plans for queries.

 In Aurora DSQL, you can't run the `ANALYZE` command within an explicit transaction. `ANALYZE` isn't subject to the database transaction timeout limit. 

 To reduce the need for manual intervention and keep statistics consistently up to date, Aurora DSQL automatically runs `ANALYZE` as a background process. This background job is triggered automatically based on the observed rate of change in the table. It is linked to the number of rows (tuples) that have been inserted, updated, or deleted since the last analyze. 

 `ANALYZE` runs asynchronously in the background and its activity can be monitored in the system view sys.jobs with the following query: 

```
SELECT * FROM sys.jobs WHERE job_type = 'ANALYZE';
```

**Key considerations**

**Note**  
 `ANALYZE` jobs are billed like other asynchronous jobs in Aurora DSQL. When you modify a table, this may indirectly trigger an automatic background statistics collection job, which can result in metering charges due to the associated system-level activity. 

 Background `ANALYZE`jobs, triggered automatically, collect the same types of statistics as a manual `ANALYZE` and apply them by default to user tables. System and catalog tables are excluded from this automated process. 