# RDS for Oracle initialization

parameters

In Amazon RDS, you manage parameters using a DB parameter group. Using this group, you can
customize initialization parameters. For example, you can configure the sort area size with
`sort_area_size`. All RDS for Oracle DB instances associated with a specific DB parameter
group use the same parameter settings. For more information, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Supported

initialization parameters in RDS for Oracle

Supported parameters for your DB instance depend on your Oracle Database edition and
version. To view the supported initialization parameters for a specific Oracle Database
edition and version, run the AWS CLI command [`describe-engine-default-parameters`](../../../cli/latest/reference/rds/describe-engine-default-parameters.md "../../../cli/latest/reference/rds/describe-engine-default-parameters.md"). For example, to list
names of the supported initialization parameters for the Enterprise Edition of Oracle
Database 19c, run the following command (sample output included).

```
aws rds describe-engine-default-parameters \
    --db-parameter-group-family oracle-ee-19 \
    --output json | jq -r '.EngineDefaults.Parameters[].ParameterName'

_add_col_optim_enabled
_adg_parselock_timeout
_allow_insert_with_update_check
_allow_level_without_connect_by
_always_semi_join
_autotask_max_window
_awr_disabled_flush_tables
_awr_mmon_cpuusage
_awr_mmon_deep_purge_all_expired
_b_tree_bitmap_plans
_bct_bitmaps_per_file
_bloom_filter_enabled
_buffered_publisher_flow_control_threshold
_bug29394014_allow_triggers_on_vpd_table
_cleanup_rollback_entries
_client_enable_auto_unregister
_clusterwide_global_transactions
_complex_view_merging
_connect_by_use_union_all
_cost_equality_semi_join
_cursor_features_enabled
_cursor_obsolete_threshold
_datafile_write_errors_crash_instance
_db_block_buffers
...
```

To describe a single initialization parameter, use the following command, replacing
`sga_max_size` with the name of your parameter (sample output
included).

```
aws rds describe-engine-default-parameters \
    --db-parameter-group-family oracle-ee-19 \
    --query 'EngineDefaults.Parameters[?ParameterName==``sga_max_size``]' \
    --output json

[
    {
        "ParameterName": "sga_max_size",
        "Description": "max total SGA size",
        "Source": "engine-default",
        "ApplyType": "static",
        "DataType": "integer",
        "AllowedValues": "0-2199023255552",
        "IsModifiable": true
    }
]
```

To find general documentation for the Oracle database initialization parameters, see
[Initialization Parameters](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/initialization-parameters.html#GUID-6F1C3203-0AA0-4AF1-921C-A027DD7CB6A9 "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/initialization-parameters.html#GUID-6F1C3203-0AA0-4AF1-921C-A027DD7CB6A9") in the Oracle Database documentation. Note that
the parameter `ARCHIVE_LAG_TARGET` has special considerations in RDS for Oracle.
This parameter forces an online redo log switch after the specified time elapses. In
RDS for Oracle, `ARCHIVE_LAG_TARGET` is set to `300` because the
recovery point objective (RPO) is 5 minutes. To honor this objective, RDS for Oracle switches
the online redo log every 5 minutes and stores it in an Amazon S3 bucket.

If the frequency of the online redo log switch degrades the performance of your
RDS for Oracle database, you can scale your DB instance and storage to use higher IOPS and
throughput. Alternatively, if you use RDS Custom for Oracle or deploy an Oracle database on Amazon EC2,
you can adjust the setting of the `ARCHIVE_LAG_TARGET` initialization
parameter.

## Valid parameter values in

RDS for Oracle

In RDS for Oracle, only the following characters are valid for parameter values:

- Letters (`A-Z` and `a-z`)
- Numbers (`0-9`)
- Whitespace (spaces, tabs, and line breaks)
- The following special characters: `_ / . : + = ( ) ' * , % $ -`
  (hyphen)
