Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# System view mapping for migrating to SYS monitoring views

When you migrate your Amazon Redshift provisioned cluster to Amazon Redshift Serverless, your monitoring or diagnostic queries might reference
system views that are only available on provisioned clusters.
You can update your queries to use the SYS monitoring views. This page provides provisioned-only to SYS view mappings for you to reference when updating
your queries.

###### Topics

- [SYS\_QUERY\_HISTORY](#sys_view_migration-SYS_QUERY_HISTORY "#sys_view_migration-SYS_QUERY_HISTORY")
- [SYS\_QUERY\_DETAIL](#sys_view_migration-SYS_QUERY_DETAIL "#sys_view_migration-SYS_QUERY_DETAIL")
- [SYS\_RESTORE\_LOG](#sys_view_migration-SYS_RESTORE_LOG "#sys_view_migration-SYS_RESTORE_LOG")
- [SYS\_RESTORE\_STATE](#sys_view_migration-SYS_RESTORE_STATE "#sys_view_migration-SYS_RESTORE_STATE")
- [SYS\_TRANSACTION\_HISTORY](#sys_view_migration-SYS_TRANSACTION_HISTORY "#sys_view_migration-SYS_TRANSACTION_HISTORY")
- [SYS\_QUERY\_TEXT](#sys_view_migration-SYS_QUERY_TEXT "#sys_view_migration-SYS_QUERY_TEXT")
- [SYS\_CONNECTION\_LOG](#sys_view_migration-SYS_CONNECTION_LOG "#sys_view_migration-SYS_CONNECTION_LOG")
- [SYS\_SESSION\_HISTORY](#sys_view_migration-SYS_SESSION_HISTORY "#sys_view_migration-SYS_SESSION_HISTORY")
- [SYS\_LOAD\_DETAIL](#sys_view_migration-SYS_LOAD_DETAIL "#sys_view_migration-SYS_LOAD_DETAIL")
- [SYS\_LOAD\_HISTORY](#sys_view_migration-SYS_LOAD_HISTORY "#sys_view_migration-SYS_LOAD_HISTORY")
- [SYS\_LOAD\_ERROR\_DETAIL](#sys_view_migration-SYS_LOAD_ERROR_DETAIL "#sys_view_migration-SYS_LOAD_ERROR_DETAIL")
- [SYS\_UNLOAD\_HISTORY](#sys_view_migration-SYS_UNLOAD_HISTORY "#sys_view_migration-SYS_UNLOAD_HISTORY")
- [SYS\_UNLOAD\_DETAIL](#sys_view_migration-SYS_UNLOAD_DETAIL "#sys_view_migration-SYS_UNLOAD_DETAIL")
- [SYS\_COPY\_REPLACEMENTS](#sys_view_migration-SYS_COPY_REPLACEMENTS "#sys_view_migration-SYS_COPY_REPLACEMENTS")
- [SYS\_DATASHARE\_USAGE\_CONSUMER](#sys_view_migration-SYS_DATASHARE_USAGE_CONSUMER "#sys_view_migration-SYS_DATASHARE_USAGE_CONSUMER")
- [SYS\_DATASHARE\_USAGE\_PRODUCER](#sys_view_migration-SYS_DATASHARE_USAGE_PRODUCER "#sys_view_migration-SYS_DATASHARE_USAGE_PRODUCER")
- [SYS\_DATASHARE\_CROSS\_REGION\_USAGE](#sys_view_migration-SYS_DATASHARE_CROSS_REGION_USAGE "#sys_view_migration-SYS_DATASHARE_CROSS_REGION_USAGE")
- [SYS\_DATASHARE\_CHANGE\_LOG](#sys_view_migration-SYS_DATASHARE_CHANGE_LOG "#sys_view_migration-SYS_DATASHARE_CHANGE_LOG")
- [SYS\_EXTERNAL\_QUERY\_DETAIL](#sys_view_migration-SYS_EXTERNAL_QUERY_DETAIL "#sys_view_migration-SYS_EXTERNAL_QUERY_DETAIL")
- [SYS\_EXTERNAL\_QUERY\_ERROR](#sys_view_migration-SYS_EXTERNAL_QUERY_ERROR "#sys_view_migration-SYS_EXTERNAL_QUERY_ERROR")
- [SYS\_VACUUM\_HISTORY](#sys_view_migration-SYS_VACUUM_HISTORY "#sys_view_migration-SYS_VACUUM_HISTORY")
- [SYS\_ANALYZE\_HISTORY](#sys_view_migration-SYS_ANALYZE_HISTORY "#sys_view_migration-SYS_ANALYZE_HISTORY")
- [SYS\_ANALYZE\_COMPRESSION\_HISTORY](#sys_view_migration-SYS_ANALYZE_COMPRESSION_HISTORY "#sys_view_migration-SYS_ANALYZE_COMPRESSION_HISTORY")
- [SYS\_MV\_REFRESH\_HISTORY](#sys_view_migration-SYS_MV_REFRESH_HISTORY "#sys_view_migration-SYS_MV_REFRESH_HISTORY")
- [SYS\_MV\_STATE](#sys_view_migration-SYS_MV_STATE "#sys_view_migration-SYS_MV_STATE")
- [SYS\_PROCEDURE\_CALL](#sys_view_migration-SYS_PROCEDURE_CALL "#sys_view_migration-SYS_PROCEDURE_CALL")
- [SYS\_PROCEDURE\_MESSAGES](#sys_view_migration-SYS_PROCEDURE_MESSAGES "#sys_view_migration-SYS_PROCEDURE_MESSAGES")
- [SYS\_UDF\_LOG](#sys_view_migration-SYS_UDF_LOG "#sys_view_migration-SYS_UDF_LOG")
- [SYS\_USERLOG](#sys_view_migration-SYS_USERLOG "#sys_view_migration-SYS_USERLOG")
- [SYS\_SCHEMA\_QUOTA\_VIOLATIONS](#sys_view_migration-SYS_SCHEMA_QUOTA_VIOLATIONS "#sys_view_migration-SYS_SCHEMA_QUOTA_VIOLATIONS")
- [SYS\_SPATIAL\_SIMPLIFY](#sys_view_migration-SYS_SPATIAL_SIMPLIFY "#sys_view_migration-SYS_SPATIAL_SIMPLIFY")

## SYS\_QUERY\_HISTORY

Some or all of the columns in the following tables are also defined in [SYS\_QUERY\_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md").

- [STL\_DDLTEXT](r_STL_DDLTEXT.md "r_STL_DDLTEXT.md")
- [STL\_ERROR](r_STL_ERROR.md "r_STL_ERROR.md")
- [STL\_QUERY](r_STL_QUERY.md "r_STL_QUERY.md")
- [STL\_UTILITYTEXT](r_STL_UTILITYTEXT.md "r_STL_UTILITYTEXT.md")
- [STL\_WLM\_QUERY](r_STL_WLM_QUERY.md "r_STL_WLM_QUERY.md")
- [STV\_INFLIGHT](r_STV_INFLIGHT.md "r_STV_INFLIGHT.md")
- [STV\_RECENTS](r_STV_RECENTS.md "r_STV_RECENTS.md")
- [STV\_WLM\_QUERY\_STATE](r_STV_WLM_QUERY_STATE.md "r_STV_WLM_QUERY_STATE.md")
- [SVL\_COMPILE](r_SVL_COMPILE.md "r_SVL_COMPILE.md")
- [SVL\_MULTI\_STATEMENT\_VIOLATIONS](r_SVL_MULTI_STATEMENT_VIOLATIONS.md "r_SVL_MULTI_STATEMENT_VIOLATIONS.md")
- [SVL\_QLOG](r_SVL_QLOG.md "r_SVL_QLOG.md")
- [SVL\_QUERY\_QUEUE\_INFO](r_SVL_QUERY_QUEUE_INFO.md "r_SVL_QUERY_QUEUE_INFO.md")
- [SVL\_STATEMENTTEXT](r_SVL_STATEMENTTEXT.md "r_SVL_STATEMENTTEXT.md")
- [SVL\_TERMINATE](r_SVL_TERMINATE.md "r_SVL_TERMINATE.md")

## SYS\_QUERY\_DETAIL

Some or all of the columns in the following tables are also defined in [SYS\_QUERY\_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md").

- [STL\_AGGR](r_STL_AGGR.md "r_STL_AGGR.md")
- [STL\_ALERT\_EVENT\_LOG](r_STL_ALERT_EVENT_LOG.md "r_STL_ALERT_EVENT_LOG.md")
- [STL\_BCAST](r_STL_BCAST.md "r_STL_BCAST.md")
- [STL\_DELETE](r_STL_DELETE.md "r_STL_DELETE.md")
- [STL\_DIST](r_STL_DIST.md "r_STL_DIST.md")
- [STL\_EXPLAIN](r_STL_EXPLAIN.md "r_STL_EXPLAIN.md")
- [STL\_HASH](r_STL_HASH.md "r_STL_HASH.md")
- [STL\_HASHJOIN](r_STL_HASHJOIN.md "r_STL_HASHJOIN.md")
- [STL\_INSERT](r_STL_INSERT.md "r_STL_INSERT.md")
- [STL\_LIMIT](r_STL_LIMIT.md "r_STL_LIMIT.md")
- [STL\_MERGE](r_STL_MERGE.md "r_STL_MERGE.md")
- [STL\_MERGEJOIN](r_STL_MERGEJOIN.md "r_STL_MERGEJOIN.md")
- [STL\_NESTLOOP](r_STL_NESTLOOP.md "r_STL_NESTLOOP.md")
- [STL\_PARSE](r_STL_PARSE.md "r_STL_PARSE.md")
- [STL\_PLAN\_INFO](r_STL_PLAN_INFO.md "r_STL_PLAN_INFO.md")
- [STL\_PROJECT](r_STL_PROJECT.md "r_STL_PROJECT.md")
- [STL\_QUERY\_METRICS](r_STL_QUERY_METRICS.md "r_STL_QUERY_METRICS.md")
- [STL\_RETURN](r_STL_RETURN.md "r_STL_RETURN.md")
- [STL\_SAVE](r_STL_SAVE.md "r_STL_SAVE.md")
- [STL\_SCAN](r_STL_SCAN.md "r_STL_SCAN.md")
- [STL\_SORT](r_STL_SORT.md "r_STL_SORT.md")
- [STL\_STREAM\_SEGS](r_STL_STREAM_SEGS.md "r_STL_STREAM_SEGS.md")
- [STL\_UNIQUE](r_STL_UNIQUE.md "r_STL_UNIQUE.md")
- [STL\_WINDOW](r_STL_WINDOW.md "r_STL_WINDOW.md")
- [STV\_EXEC\_STATE](r_STV_EXEC_STATE.md "r_STV_EXEC_STATE.md")
- [STV\_QUERY\_METRICS](r_STV_QUERY_METRICS.md "r_STV_QUERY_METRICS.md")
- [SVCS\_QUERY\_SUMMARY](r_SVCS_QUERY_SUMMARY.md "r_SVCS_QUERY_SUMMARY.md")
- [SVL\_QUERY\_METRICS](r_SVL_QUERY_METRICS.md "r_SVL_QUERY_METRICS.md")
- [SVL\_QUERY\_METRICS\_SUMMARY](r_SVL_QUERY_METRICS_SUMMARY.md "r_SVL_QUERY_METRICS_SUMMARY.md")
- [SVL\_QUERY\_REPORT](r_SVL_QUERY_REPORT.md "r_SVL_QUERY_REPORT.md")
- [SVL\_QUERY\_SUMMARY](r_SVL_QUERY_SUMMARY.md "r_SVL_QUERY_SUMMARY.md")
- [SVV\_QUERY\_STATE](r_SVV_QUERY_STATE.md "r_SVV_QUERY_STATE.md")

## SYS\_RESTORE\_LOG

Some or all of the columns in the following table are also defined in [SYS\_RESTORE\_LOG](SYS_RESTORE_LOG.md "SYS_RESTORE_LOG.md").

- [SVL\_RESTORE\_ALTER\_TABLE\_PROGRESS](r_SVL_RESTORE_ALTER_TABLE_PROGRESS.md "r_SVL_RESTORE_ALTER_TABLE_PROGRESS.md")

## SYS\_RESTORE\_STATE

Some or all of the columns in the following table are also defined in [SYS\_RESTORE\_STATE](SYS_RESTORE_STATE.md "SYS_RESTORE_STATE.md").

- [STV\_XRESTORE\_ALTER\_QUEUE\_STATE](r_STV_XRESTORE_ALTER_QUEUE_STATE.md "r_STV_XRESTORE_ALTER_QUEUE_STATE.md")

## SYS\_TRANSACTION\_HISTORY

Some or all of the columns in the following tables are also defined in [SYS\_TRANSACTION\_HISTORY](SYS_TRANSACTION_HISTORY.md "SYS_TRANSACTION_HISTORY.md").

- [STL\_COMMIT\_STATS](r_STL_COMMIT_STATS.md "r_STL_COMMIT_STATS.md")
- [STL\_TR\_CONFLICT](r_STL_TR_CONFLICT.md "r_STL_TR_CONFLICT.md")
- [STL\_UNDONE](r_STL_UNDONE.md "r_STL_UNDONE.md")

## SYS\_QUERY\_TEXT

Some or all of the columns in the following table are also defined in [SYS\_QUERY\_TEXT](SYS_QUERY_TEXT.md "SYS_QUERY_TEXT.md").

- [STL\_QUERYTEXT](r_STL_QUERYTEXT.md "r_STL_QUERYTEXT.md")

## SYS\_CONNECTION\_LOG

Some or all of the columns in the following table are also defined in [SYS\_CONNECTION\_LOG](SYS_CONNECTION_LOG.md "SYS_CONNECTION_LOG.md").

- [STL\_CONNECTION\_LOG](r_STL_CONNECTION_LOG.md "r_STL_CONNECTION_LOG.md")

## SYS\_SESSION\_HISTORY

Some or all of the columns in the following tables are also defined in [SYS\_SESSION\_HISTORY](SYS_SESSION_HISTORY.md "SYS_SESSION_HISTORY.md").

- [STL\_SESSIONS](r_STL_SESSIONS.md "r_STL_SESSIONS.md")
- [STL\_RESTARTED\_SESSIONS](r_STL_RESTARTED_SESSIONS.md "r_STL_RESTARTED_SESSIONS.md")
- [STV\_SESSIONS](r_STV_SESSIONS.md "r_STV_SESSIONS.md")

## SYS\_LOAD\_DETAIL

Some or all of the columns in the following table are also defined in [SYS\_LOAD\_DETAIL](SYS_LOAD_DETAIL.md "SYS_LOAD_DETAIL.md").

- [STL\_LOAD\_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md")

## SYS\_LOAD\_HISTORY

Some or all of the columns in the following table are also defined in [SYS\_LOAD\_HISTORY](SYS_LOAD_HISTORY.md "SYS_LOAD_HISTORY.md").

- [STL\_LOAD\_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md")

## SYS\_LOAD\_ERROR\_DETAIL

Some or all of the columns in the following tables are also defined in [SYS\_LOAD\_ERROR\_DETAIL](SYS_LOAD_ERROR_DETAIL.md "SYS_LOAD_ERROR_DETAIL.md").

- [STL\_LOADERROR\_DETAIL](r_STL_LOADERROR_DETAIL.md "r_STL_LOADERROR_DETAIL.md")
- [STL\_LOAD\_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md")

## SYS\_UNLOAD\_HISTORY

Some or all of the columns in the following table are also defined in [SYS\_UNLOAD\_HISTORY](SYS_UNLOAD_HISTORY.md "SYS_UNLOAD_HISTORY.md").

- [STL\_UNLOAD\_LOG](r_STL_UNLOAD_LOG.md "r_STL_UNLOAD_LOG.md")

## SYS\_UNLOAD\_DETAIL

Some or all of the columns in the following table are also defined in [SYS\_UNLOAD\_DETAIL](SYS_UNLOAD_DETAIL.md "SYS_UNLOAD_DETAIL.md").

- [STL\_UNLOAD\_LOG](r_STL_UNLOAD_LOG.md "r_STL_UNLOAD_LOG.md")

## SYS\_COPY\_REPLACEMENTS

Some or all of the columns in the following table are also defined in [SYS\_COPY\_REPLACEMENTS](SYS_COPY_REPLACEMENTS.md "SYS_COPY_REPLACEMENTS.md").

- [STL\_REPLACEMENTS](r_STL_REPLACEMENTS.md "r_STL_REPLACEMENTS.md")

## SYS\_DATASHARE\_USAGE\_CONSUMER

Some or all of the columns in the following table are also defined in [SYS\_DATASHARE\_USAGE\_CONSUMER](SYS_DATASHARE_USAGE_CONSUMER.md "SYS_DATASHARE_USAGE_CONSUMER.md").

- [SVL\_DATASHARE\_USAGE\_CONSUMER](r_SVL_DATASHARE_USAGE_CONSUMER.md "r_SVL_DATASHARE_USAGE_CONSUMER.md")

## SYS\_DATASHARE\_USAGE\_PRODUCER

Some or all of the columns in the following table are also defined in [SYS\_DATASHARE\_USAGE\_PRODUCER](SYS_DATASHARE_USAGE_PRODUCER.md "SYS_DATASHARE_USAGE_PRODUCER.md").

- [SVL\_DATASHARE\_USAGE\_PRODUCER](r_SVL_DATASHARE_USAGE_PRODUCER.md "r_SVL_DATASHARE_USAGE_PRODUCER.md")

## SYS\_DATASHARE\_CROSS\_REGION\_USAGE

Some or all of the columns in the following table are also defined in [SYS\_DATASHARE\_CROSS\_REGION\_USAGE](r_SYS_DATASHARE_CROSS_REGION_USAGE.md "r_SYS_DATASHARE_CROSS_REGION_USAGE.md").

- [SVL\_DATASHARE\_CROSS\_REGION\_USAGE](r_SVL_DATASHARE_CROSS_REGION_USAGE.md "r_SVL_DATASHARE_CROSS_REGION_USAGE.md")

## SYS\_DATASHARE\_CHANGE\_LOG

Some or all of the columns in the following table are also defined in [SYS\_DATASHARE\_CHANGE\_LOG](SYS_DATASHARE_CHANGE_LOG.md "SYS_DATASHARE_CHANGE_LOG.md").

- [SVL\_DATASHARE\_CHANGE\_LOG](r_SVL_DATASHARE_CHANGE_LOG.md "r_SVL_DATASHARE_CHANGE_LOG.md")

## SYS\_EXTERNAL\_QUERY\_DETAIL

Some or all of the columns in the following tables are also defined in [SYS\_EXTERNAL\_QUERY\_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md "SYS_EXTERNAL_QUERY_DETAIL.md").

- [SVL\_FEDERATED\_QUERY](r_SVL_FEDERATED_QUERY.md "r_SVL_FEDERATED_QUERY.md")
- [SVL\_S3LIST](r_SVL_S3LIST.md "r_SVL_S3LIST.md")
- [SVL\_S3QUERY](r_SVL_S3QUERY.md "r_SVL_S3QUERY.md")
- [SVL\_S3QUERY\_SUMMARY](r_SVL_S3QUERY_SUMMARY.md "r_SVL_S3QUERY_SUMMARY.md")

## SYS\_EXTERNAL\_QUERY\_ERROR

Some or all of the columns in the following tables are also defined in [SYS\_EXTERNAL\_QUERY\_ERROR](SYS_EXTERNAL_QUERY_ERROR.md "SYS_EXTERNAL_QUERY_ERROR.md").

- [SVL\_SPECTRUM\_SCAN\_ERROR](r_SVL_SPECTRUM_SCAN_ERROR.md "r_SVL_SPECTRUM_SCAN_ERROR.md")

## SYS\_VACUUM\_HISTORY

Some or all of the columns in the following tables are also defined in [SYS\_VACUUM\_HISTORY](SYS_VACUUM_HISTORY.md "SYS_VACUUM_HISTORY.md").

- [STL\_VACUUM](r_STL_VACUUM.md "r_STL_VACUUM.md")
- [SVL\_VACUUM\_PERCENTAGE](r_SVL_VACUUM_PERCENTAGE.md "r_SVL_VACUUM_PERCENTAGE.md")
- [SVV\_VACUUM\_PROGRESS](r_SVV_VACUUM_PROGRESS.md "r_SVV_VACUUM_PROGRESS.md")
- [SVV\_VACUUM\_SUMMARY](r_SVV_VACUUM_SUMMARY.md "r_SVV_VACUUM_SUMMARY.md")

## SYS\_ANALYZE\_HISTORY

Some or all of the columns in the following tables are also defined in [SYS\_ANALYZE\_HISTORY](SYS_ANALYZE_HISTORY.md "SYS_ANALYZE_HISTORY.md").

- [STL\_ANALYZE](r_STL_ANALYZE.md "r_STL_ANALYZE.md")

## SYS\_ANALYZE\_COMPRESSION\_HISTORY

Some or all of the columns in the following tables are also defined in [SYS\_ANALYZE\_COMPRESSION\_HISTORY](r_SYS_ANALYZE_COMPRESSION_HISTORY.md "r_SYS_ANALYZE_COMPRESSION_HISTORY.md").

- [STL\_ANALYZE\_COMPRESSION](r_STL_ANALYZE_COMPRESSION.md "r_STL_ANALYZE_COMPRESSION.md")

## SYS\_MV\_REFRESH\_HISTORY

Some or all of the columns in the following tables are also defined in [SYS\_MV\_REFRESH\_HISTORY](SYS_MV_REFRESH_HISTORY.md "SYS_MV_REFRESH_HISTORY.md").

- [SVL\_MV\_REFRESH\_STATUS](r_SVL_MV_REFRESH_STATUS.md "r_SVL_MV_REFRESH_STATUS.md")

## SYS\_MV\_STATE

Some or all of the columns in the following tables are also defined in [SYS\_MV\_STATE](SYS_MV_STATE.md "SYS_MV_STATE.md").

- [STL\_MV\_STATE](r_STL_MV_STATE.md "r_STL_MV_STATE.md")

## SYS\_PROCEDURE\_CALL

Some or all of the columns in the following tables are also defined in [SYS\_PROCEDURE\_CALL](SYS_PROCEDURE_CALL.md "SYS_PROCEDURE_CALL.md").

- [SVL\_STORED\_PROC\_CALL](r_SVL_STORED_PROC_CALL.md "r_SVL_STORED_PROC_CALL.md")

## SYS\_PROCEDURE\_MESSAGES

Some or all of the columns in the following tables are also defined in [SYS\_PROCEDURE\_MESSAGES](SYS_PROCEDURE_MESSAGES.md "SYS_PROCEDURE_MESSAGES.md").

- [SVL\_STORED\_PROC\_MESSAGES](r_SVL_STORED_PROC_MESSAGES.md "r_SVL_STORED_PROC_MESSAGES.md")

## SYS\_UDF\_LOG

Some or all of the columns in the following tables are also defined in [SYS\_UDF\_LOG](SYS_UDF_LOG.md "SYS_UDF_LOG.md").

- [SVL\_UDF\_LOG](r_SVL_UDF_LOG.md "r_SVL_UDF_LOG.md")

## SYS\_USERLOG

Some or all of the columns in the following tables are also defined in [SYS\_USERLOG](SYS_USERLOG.md "SYS_USERLOG.md").

- [STL\_USERLOG](r_STL_USERLOG.md "r_STL_USERLOG.md")

## SYS\_SCHEMA\_QUOTA\_VIOLATIONS

Some or all of the columns in the following tables are also defined in [SYS\_SCHEMA\_QUOTA\_VIOLATIONS](r_SYS_SCHEMA_QUOTA_VIOLATIONS.md "r_SYS_SCHEMA_QUOTA_VIOLATIONS.md").

- [STL\_SCHEMA\_QUOTA\_VIOLATIONS](r_STL_SCHEMA_QUOTA_VIOLATIONS.md "r_STL_SCHEMA_QUOTA_VIOLATIONS.md")

## SYS\_SPATIAL\_SIMPLIFY

Some or all of the columns in the following tables are also defined in [SYS\_SPATIAL\_SIMPLIFY](SYS_SPATIAL_SIMPLIFY.md "SYS_SPATIAL_SIMPLIFY.md").

- [SVL\_SPATIAL\_SIMPLIFY](r_SVL_SPATIAL_SIMPLIFY.md "r_SVL_SPATIAL_SIMPLIFY.md")
