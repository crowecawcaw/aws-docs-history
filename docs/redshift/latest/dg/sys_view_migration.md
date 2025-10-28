Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# System view mapping for migrating to SYS monitoring views

When you migrate your Amazon Redshift provisioned cluster to Amazon Redshift Serverless, your monitoring or diagnostic queries might reference
system views that are only available on provisioned clusters.
You can update your queries to use the SYS monitoring views. This page provides provisioned-only to SYS view mappings for you to reference when updating
your queries.

###### Topics

- [SYS_QUERY_HISTORY](#sys_view_migration-SYS_QUERY_HISTORY "#sys_view_migration-SYS_QUERY_HISTORY")
- [SYS_QUERY_DETAIL](#sys_view_migration-SYS_QUERY_DETAIL "#sys_view_migration-SYS_QUERY_DETAIL")
- [SYS_RESTORE_LOG](#sys_view_migration-SYS_RESTORE_LOG "#sys_view_migration-SYS_RESTORE_LOG")
- [SYS_RESTORE_STATE](#sys_view_migration-SYS_RESTORE_STATE "#sys_view_migration-SYS_RESTORE_STATE")
- [SYS_TRANSACTION_HISTORY](#sys_view_migration-SYS_TRANSACTION_HISTORY "#sys_view_migration-SYS_TRANSACTION_HISTORY")
- [SYS_QUERY_TEXT](#sys_view_migration-SYS_QUERY_TEXT "#sys_view_migration-SYS_QUERY_TEXT")
- [SYS_CONNECTION_LOG](#sys_view_migration-SYS_CONNECTION_LOG "#sys_view_migration-SYS_CONNECTION_LOG")
- [SYS_SESSION_HISTORY](#sys_view_migration-SYS_SESSION_HISTORY "#sys_view_migration-SYS_SESSION_HISTORY")
- [SYS_LOAD_DETAIL](#sys_view_migration-SYS_LOAD_DETAIL "#sys_view_migration-SYS_LOAD_DETAIL")
- [SYS_LOAD_HISTORY](#sys_view_migration-SYS_LOAD_HISTORY "#sys_view_migration-SYS_LOAD_HISTORY")
- [SYS_LOAD_ERROR_DETAIL](#sys_view_migration-SYS_LOAD_ERROR_DETAIL "#sys_view_migration-SYS_LOAD_ERROR_DETAIL")
- [SYS_UNLOAD_HISTORY](#sys_view_migration-SYS_UNLOAD_HISTORY "#sys_view_migration-SYS_UNLOAD_HISTORY")
- [SYS_UNLOAD_DETAIL](#sys_view_migration-SYS_UNLOAD_DETAIL "#sys_view_migration-SYS_UNLOAD_DETAIL")
- [SYS_COPY_REPLACEMENTS](#sys_view_migration-SYS_COPY_REPLACEMENTS "#sys_view_migration-SYS_COPY_REPLACEMENTS")
- [SYS_DATASHARE_USAGE_CONSUMER](#sys_view_migration-SYS_DATASHARE_USAGE_CONSUMER "#sys_view_migration-SYS_DATASHARE_USAGE_CONSUMER")
- [SYS_DATASHARE_USAGE_PRODUCER](#sys_view_migration-SYS_DATASHARE_USAGE_PRODUCER "#sys_view_migration-SYS_DATASHARE_USAGE_PRODUCER")
- [SYS_DATASHARE_CROSS_REGION_USAGE](#sys_view_migration-SYS_DATASHARE_CROSS_REGION_USAGE "#sys_view_migration-SYS_DATASHARE_CROSS_REGION_USAGE")
- [SYS_DATASHARE_CHANGE_LOG](#sys_view_migration-SYS_DATASHARE_CHANGE_LOG "#sys_view_migration-SYS_DATASHARE_CHANGE_LOG")
- [SYS_EXTERNAL_QUERY_DETAIL](#sys_view_migration-SYS_EXTERNAL_QUERY_DETAIL "#sys_view_migration-SYS_EXTERNAL_QUERY_DETAIL")
- [SYS_EXTERNAL_QUERY_ERROR](#sys_view_migration-SYS_EXTERNAL_QUERY_ERROR "#sys_view_migration-SYS_EXTERNAL_QUERY_ERROR")
- [SYS_VACUUM_HISTORY](#sys_view_migration-SYS_VACUUM_HISTORY "#sys_view_migration-SYS_VACUUM_HISTORY")
- [SYS_ANALYZE_HISTORY](#sys_view_migration-SYS_ANALYZE_HISTORY "#sys_view_migration-SYS_ANALYZE_HISTORY")
- [SYS_ANALYZE_COMPRESSION_HISTORY](#sys_view_migration-SYS_ANALYZE_COMPRESSION_HISTORY "#sys_view_migration-SYS_ANALYZE_COMPRESSION_HISTORY")
- [SYS_MV_REFRESH_HISTORY](#sys_view_migration-SYS_MV_REFRESH_HISTORY "#sys_view_migration-SYS_MV_REFRESH_HISTORY")
- [SYS_MV_STATE](#sys_view_migration-SYS_MV_STATE "#sys_view_migration-SYS_MV_STATE")
- [SYS_PROCEDURE_CALL](#sys_view_migration-SYS_PROCEDURE_CALL "#sys_view_migration-SYS_PROCEDURE_CALL")
- [SYS_PROCEDURE_MESSAGES](#sys_view_migration-SYS_PROCEDURE_MESSAGES "#sys_view_migration-SYS_PROCEDURE_MESSAGES")
- [SYS_UDF_LOG](#sys_view_migration-SYS_UDF_LOG "#sys_view_migration-SYS_UDF_LOG")
- [SYS_USERLOG](#sys_view_migration-SYS_USERLOG "#sys_view_migration-SYS_USERLOG")
- [SYS_SCHEMA_QUOTA_VIOLATIONS](#sys_view_migration-SYS_SCHEMA_QUOTA_VIOLATIONS "#sys_view_migration-SYS_SCHEMA_QUOTA_VIOLATIONS")
- [SYS_SPATIAL_SIMPLIFY](#sys_view_migration-SYS_SPATIAL_SIMPLIFY "#sys_view_migration-SYS_SPATIAL_SIMPLIFY")

## SYS_QUERY_HISTORY

Some or all of the columns in the following tables are also defined in [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md").

- [STL_DDLTEXT](r_STL_DDLTEXT.md "r_STL_DDLTEXT.md")
- [STL_ERROR](r_STL_ERROR.md "r_STL_ERROR.md")
- [STL_QUERY](r_STL_QUERY.md "r_STL_QUERY.md")
- [STL_UTILITYTEXT](r_STL_UTILITYTEXT.md "r_STL_UTILITYTEXT.md")
- [STL_WLM_QUERY](r_STL_WLM_QUERY.md "r_STL_WLM_QUERY.md")
- [STV_INFLIGHT](r_STV_INFLIGHT.md "r_STV_INFLIGHT.md")
- [STV_RECENTS](r_STV_RECENTS.md "r_STV_RECENTS.md")
- [STV_WLM_QUERY_STATE](r_STV_WLM_QUERY_STATE.md "r_STV_WLM_QUERY_STATE.md")
- [SVL_COMPILE](r_SVL_COMPILE.md "r_SVL_COMPILE.md")
- [SVL_MULTI_STATEMENT_VIOLATIONS](r_SVL_MULTI_STATEMENT_VIOLATIONS.md "r_SVL_MULTI_STATEMENT_VIOLATIONS.md")
- [SVL_QLOG](r_SVL_QLOG.md "r_SVL_QLOG.md")
- [SVL_QUERY_QUEUE_INFO](r_SVL_QUERY_QUEUE_INFO.md "r_SVL_QUERY_QUEUE_INFO.md")
- [SVL_STATEMENTTEXT](r_SVL_STATEMENTTEXT.md "r_SVL_STATEMENTTEXT.md")
- [SVL_TERMINATE](r_SVL_TERMINATE.md "r_SVL_TERMINATE.md")

## SYS_QUERY_DETAIL

Some or all of the columns in the following tables are also defined in [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md").

- [STL_AGGR](r_STL_AGGR.md "r_STL_AGGR.md")
- [STL_ALERT_EVENT_LOG](r_STL_ALERT_EVENT_LOG.md "r_STL_ALERT_EVENT_LOG.md")
- [STL_BCAST](r_STL_BCAST.md "r_STL_BCAST.md")
- [STL_DELETE](r_STL_DELETE.md "r_STL_DELETE.md")
- [STL_DIST](r_STL_DIST.md "r_STL_DIST.md")
- [STL_EXPLAIN](r_STL_EXPLAIN.md "r_STL_EXPLAIN.md")
- [STL_HASH](r_STL_HASH.md "r_STL_HASH.md")
- [STL_HASHJOIN](r_STL_HASHJOIN.md "r_STL_HASHJOIN.md")
- [STL_INSERT](r_STL_INSERT.md "r_STL_INSERT.md")
- [STL_LIMIT](r_STL_LIMIT.md "r_STL_LIMIT.md")
- [STL_MERGE](r_STL_MERGE.md "r_STL_MERGE.md")
- [STL_MERGEJOIN](r_STL_MERGEJOIN.md "r_STL_MERGEJOIN.md")
- [STL_NESTLOOP](r_STL_NESTLOOP.md "r_STL_NESTLOOP.md")
- [STL_PARSE](r_STL_PARSE.md "r_STL_PARSE.md")
- [STL_PLAN_INFO](r_STL_PLAN_INFO.md "r_STL_PLAN_INFO.md")
- [STL_PROJECT](r_STL_PROJECT.md "r_STL_PROJECT.md")
- [STL_QUERY_METRICS](r_STL_QUERY_METRICS.md "r_STL_QUERY_METRICS.md")
- [STL_RETURN](r_STL_RETURN.md "r_STL_RETURN.md")
- [STL_SAVE](r_STL_SAVE.md "r_STL_SAVE.md")
- [STL_SCAN](r_STL_SCAN.md "r_STL_SCAN.md")
- [STL_SORT](r_STL_SORT.md "r_STL_SORT.md")
- [STL_STREAM_SEGS](r_STL_STREAM_SEGS.md "r_STL_STREAM_SEGS.md")
- [STL_UNIQUE](r_STL_UNIQUE.md "r_STL_UNIQUE.md")
- [STL_WINDOW](r_STL_WINDOW.md "r_STL_WINDOW.md")
- [STV_EXEC_STATE](r_STV_EXEC_STATE.md "r_STV_EXEC_STATE.md")
- [STV_QUERY_METRICS](r_STV_QUERY_METRICS.md "r_STV_QUERY_METRICS.md")
- [SVCS_QUERY_SUMMARY](r_SVCS_QUERY_SUMMARY.md "r_SVCS_QUERY_SUMMARY.md")
- [SVL_QUERY_METRICS](r_SVL_QUERY_METRICS.md "r_SVL_QUERY_METRICS.md")
- [SVL_QUERY_METRICS_SUMMARY](r_SVL_QUERY_METRICS_SUMMARY.md "r_SVL_QUERY_METRICS_SUMMARY.md")
- [SVL_QUERY_REPORT](r_SVL_QUERY_REPORT.md "r_SVL_QUERY_REPORT.md")
- [SVL_QUERY_SUMMARY](r_SVL_QUERY_SUMMARY.md "r_SVL_QUERY_SUMMARY.md")
- [SVV_QUERY_STATE](r_SVV_QUERY_STATE.md "r_SVV_QUERY_STATE.md")

## SYS_RESTORE_LOG

Some or all of the columns in the following table are also defined in [SYS_RESTORE_LOG](SYS_RESTORE_LOG.md "SYS_RESTORE_LOG.md").

- [SVL_RESTORE_ALTER_TABLE_PROGRESS](r_SVL_RESTORE_ALTER_TABLE_PROGRESS.md "r_SVL_RESTORE_ALTER_TABLE_PROGRESS.md")

## SYS_RESTORE_STATE

Some or all of the columns in the following table are also defined in [SYS_RESTORE_STATE](SYS_RESTORE_STATE.md "SYS_RESTORE_STATE.md").

- [STV_XRESTORE_ALTER_QUEUE_STATE](r_STV_XRESTORE_ALTER_QUEUE_STATE.md "r_STV_XRESTORE_ALTER_QUEUE_STATE.md")

## SYS_TRANSACTION_HISTORY

Some or all of the columns in the following tables are also defined in [SYS_TRANSACTION_HISTORY](SYS_TRANSACTION_HISTORY.md "SYS_TRANSACTION_HISTORY.md").

- [STL_COMMIT_STATS](r_STL_COMMIT_STATS.md "r_STL_COMMIT_STATS.md")
- [STL_TR_CONFLICT](r_STL_TR_CONFLICT.md "r_STL_TR_CONFLICT.md")
- [STL_UNDONE](r_STL_UNDONE.md "r_STL_UNDONE.md")

## SYS_QUERY_TEXT

Some or all of the columns in the following table are also defined in [SYS_QUERY_TEXT](SYS_QUERY_TEXT.md "SYS_QUERY_TEXT.md").

- [STL_QUERYTEXT](r_STL_QUERYTEXT.md "r_STL_QUERYTEXT.md")

## SYS_CONNECTION_LOG

Some or all of the columns in the following table are also defined in [SYS_CONNECTION_LOG](SYS_CONNECTION_LOG.md "SYS_CONNECTION_LOG.md").

- [STL_CONNECTION_LOG](r_STL_CONNECTION_LOG.md "r_STL_CONNECTION_LOG.md")

## SYS_SESSION_HISTORY

Some or all of the columns in the following tables are also defined in [SYS_SESSION_HISTORY](SYS_SESSION_HISTORY.md "SYS_SESSION_HISTORY.md").

- [STL_SESSIONS](r_STL_SESSIONS.md "r_STL_SESSIONS.md")
- [STL_RESTARTED_SESSIONS](r_STL_RESTARTED_SESSIONS.md "r_STL_RESTARTED_SESSIONS.md")
- [STV_SESSIONS](r_STV_SESSIONS.md "r_STV_SESSIONS.md")

## SYS_LOAD_DETAIL

Some or all of the columns in the following table are also defined in [SYS_LOAD_DETAIL](SYS_LOAD_DETAIL.md "SYS_LOAD_DETAIL.md").

- [STL_LOAD_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md")

## SYS_LOAD_HISTORY

Some or all of the columns in the following table are also defined in [SYS_LOAD_HISTORY](SYS_LOAD_HISTORY.md "SYS_LOAD_HISTORY.md").

- [STL_LOAD_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md")

## SYS_LOAD_ERROR_DETAIL

Some or all of the columns in the following tables are also defined in [SYS_LOAD_ERROR_DETAIL](SYS_LOAD_ERROR_DETAIL.md "SYS_LOAD_ERROR_DETAIL.md").

- [STL_LOADERROR_DETAIL](r_STL_LOADERROR_DETAIL.md "r_STL_LOADERROR_DETAIL.md")
- [STL_LOAD_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md")

## SYS_UNLOAD_HISTORY

Some or all of the columns in the following table are also defined in [SYS_UNLOAD_HISTORY](SYS_UNLOAD_HISTORY.md "SYS_UNLOAD_HISTORY.md").

- [STL_UNLOAD_LOG](r_STL_UNLOAD_LOG.md "r_STL_UNLOAD_LOG.md")

## SYS_UNLOAD_DETAIL

Some or all of the columns in the following table are also defined in [SYS_UNLOAD_DETAIL](SYS_UNLOAD_DETAIL.md "SYS_UNLOAD_DETAIL.md").

- [STL_UNLOAD_LOG](r_STL_UNLOAD_LOG.md "r_STL_UNLOAD_LOG.md")

## SYS_COPY_REPLACEMENTS

Some or all of the columns in the following table are also defined in [SYS_COPY_REPLACEMENTS](SYS_COPY_REPLACEMENTS.md "SYS_COPY_REPLACEMENTS.md").

- [STL_REPLACEMENTS](r_STL_REPLACEMENTS.md "r_STL_REPLACEMENTS.md")

## SYS_DATASHARE_USAGE_CONSUMER

Some or all of the columns in the following table are also defined in [SYS_DATASHARE_USAGE_CONSUMER](SYS_DATASHARE_USAGE_CONSUMER.md "SYS_DATASHARE_USAGE_CONSUMER.md").

- [SVL_DATASHARE_USAGE_CONSUMER](r_SVL_DATASHARE_USAGE_CONSUMER.md "r_SVL_DATASHARE_USAGE_CONSUMER.md")

## SYS_DATASHARE_USAGE_PRODUCER

Some or all of the columns in the following table are also defined in [SYS_DATASHARE_USAGE_PRODUCER](SYS_DATASHARE_USAGE_PRODUCER.md "SYS_DATASHARE_USAGE_PRODUCER.md").

- [SVL_DATASHARE_USAGE_PRODUCER](r_SVL_DATASHARE_USAGE_PRODUCER.md "r_SVL_DATASHARE_USAGE_PRODUCER.md")

## SYS_DATASHARE_CROSS_REGION_USAGE

Some or all of the columns in the following table are also defined in [SYS_DATASHARE_CROSS_REGION_USAGE](r_SYS_DATASHARE_CROSS_REGION_USAGE.md "r_SYS_DATASHARE_CROSS_REGION_USAGE.md").

- [SVL_DATASHARE_CROSS_REGION_USAGE](r_SVL_DATASHARE_CROSS_REGION_USAGE.md "r_SVL_DATASHARE_CROSS_REGION_USAGE.md")

## SYS_DATASHARE_CHANGE_LOG

Some or all of the columns in the following table are also defined in [SYS_DATASHARE_CHANGE_LOG](SYS_DATASHARE_CHANGE_LOG.md "SYS_DATASHARE_CHANGE_LOG.md").

- [SVL_DATASHARE_CHANGE_LOG](r_SVL_DATASHARE_CHANGE_LOG.md "r_SVL_DATASHARE_CHANGE_LOG.md")

## SYS_EXTERNAL_QUERY_DETAIL

Some or all of the columns in the following tables are also defined in [SYS_EXTERNAL_QUERY_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md "SYS_EXTERNAL_QUERY_DETAIL.md").

- [SVL_FEDERATED_QUERY](r_SVL_FEDERATED_QUERY.md "r_SVL_FEDERATED_QUERY.md")
- [SVL_S3LIST](r_SVL_S3LIST.md "r_SVL_S3LIST.md")
- [SVL_S3QUERY](r_SVL_S3QUERY.md "r_SVL_S3QUERY.md")
- [SVL_S3QUERY_SUMMARY](r_SVL_S3QUERY_SUMMARY.md "r_SVL_S3QUERY_SUMMARY.md")

## SYS_EXTERNAL_QUERY_ERROR

Some or all of the columns in the following tables are also defined in [SYS_EXTERNAL_QUERY_ERROR](SYS_EXTERNAL_QUERY_ERROR.md "SYS_EXTERNAL_QUERY_ERROR.md").

- [SVL_SPECTRUM_SCAN_ERROR](r_SVL_SPECTRUM_SCAN_ERROR.md "r_SVL_SPECTRUM_SCAN_ERROR.md")

## SYS_VACUUM_HISTORY

Some or all of the columns in the following tables are also defined in [SYS_VACUUM_HISTORY](SYS_VACUUM_HISTORY.md "SYS_VACUUM_HISTORY.md").

- [STL_VACUUM](r_STL_VACUUM.md "r_STL_VACUUM.md")
- [SVL_VACUUM_PERCENTAGE](r_SVL_VACUUM_PERCENTAGE.md "r_SVL_VACUUM_PERCENTAGE.md")
- [SVV_VACUUM_PROGRESS](r_SVV_VACUUM_PROGRESS.md "r_SVV_VACUUM_PROGRESS.md")
- [SVV_VACUUM_SUMMARY](r_SVV_VACUUM_SUMMARY.md "r_SVV_VACUUM_SUMMARY.md")

## SYS_ANALYZE_HISTORY

Some or all of the columns in the following tables are also defined in [SYS_ANALYZE_HISTORY](SYS_ANALYZE_HISTORY.md "SYS_ANALYZE_HISTORY.md").

- [STL_ANALYZE](r_STL_ANALYZE.md "r_STL_ANALYZE.md")

## SYS_ANALYZE_COMPRESSION_HISTORY

Some or all of the columns in the following tables are also defined in [SYS_ANALYZE_COMPRESSION_HISTORY](r_SYS_ANALYZE_COMPRESSION_HISTORY.md "r_SYS_ANALYZE_COMPRESSION_HISTORY.md").

- [STL_ANALYZE_COMPRESSION](r_STL_ANALYZE_COMPRESSION.md "r_STL_ANALYZE_COMPRESSION.md")

## SYS_MV_REFRESH_HISTORY

Some or all of the columns in the following tables are also defined in [SYS_MV_REFRESH_HISTORY](SYS_MV_REFRESH_HISTORY.md "SYS_MV_REFRESH_HISTORY.md").

- [SVL_MV_REFRESH_STATUS](r_SVL_MV_REFRESH_STATUS.md "r_SVL_MV_REFRESH_STATUS.md")

## SYS_MV_STATE

Some or all of the columns in the following tables are also defined in [SYS_MV_STATE](SYS_MV_STATE.md "SYS_MV_STATE.md").

- [STL_MV_STATE](r_STL_MV_STATE.md "r_STL_MV_STATE.md")

## SYS_PROCEDURE_CALL

Some or all of the columns in the following tables are also defined in [SYS_PROCEDURE_CALL](SYS_PROCEDURE_CALL.md "SYS_PROCEDURE_CALL.md").

- [SVL_STORED_PROC_CALL](r_SVL_STORED_PROC_CALL.md "r_SVL_STORED_PROC_CALL.md")

## SYS_PROCEDURE_MESSAGES

Some or all of the columns in the following tables are also defined in [SYS_PROCEDURE_MESSAGES](SYS_PROCEDURE_MESSAGES.md "SYS_PROCEDURE_MESSAGES.md").

- [SVL_STORED_PROC_MESSAGES](r_SVL_STORED_PROC_MESSAGES.md "r_SVL_STORED_PROC_MESSAGES.md")

## SYS_UDF_LOG

Some or all of the columns in the following tables are also defined in [SYS_UDF_LOG](SYS_UDF_LOG.md "SYS_UDF_LOG.md").

- [SVL_UDF_LOG](r_SVL_UDF_LOG.md "r_SVL_UDF_LOG.md")

## SYS_USERLOG

Some or all of the columns in the following tables are also defined in [SYS_USERLOG](SYS_USERLOG.md "SYS_USERLOG.md").

- [STL_USERLOG](r_STL_USERLOG.md "r_STL_USERLOG.md")

## SYS_SCHEMA_QUOTA_VIOLATIONS

Some or all of the columns in the following tables are also defined in [SYS_SCHEMA_QUOTA_VIOLATIONS](r_SYS_SCHEMA_QUOTA_VIOLATIONS.md "r_SYS_SCHEMA_QUOTA_VIOLATIONS.md").

- [STL_SCHEMA_QUOTA_VIOLATIONS](r_STL_SCHEMA_QUOTA_VIOLATIONS.md "r_STL_SCHEMA_QUOTA_VIOLATIONS.md")

## SYS_SPATIAL_SIMPLIFY

Some or all of the columns in the following tables are also defined in [SYS_SPATIAL_SIMPLIFY](SYS_SPATIAL_SIMPLIFY.md "SYS_SPATIAL_SIMPLIFY.md").

- [SVL_SPATIAL_SIMPLIFY](r_SVL_SPATIAL_SIMPLIFY.md "r_SVL_SPATIAL_SIMPLIFY.md")
