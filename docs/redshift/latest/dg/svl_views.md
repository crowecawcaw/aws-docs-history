Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL views for main cluster

SVL views are system views in Amazon Redshift that contain references to STL tables and logs for
more detailed information.

These views provide quicker and easier access to commonly queried data found in those tables.

###### Note

The SVL_QUERY_SUMMARY view only contains information about queries run by
Amazon Redshift, not other utility and DDL commands. For a complete listing and information on
all statements run by Amazon Redshift, including DDL and utility commands, you can query
the SVL_STATEMENTTEXT view.

###### Topics

- [SVL_AUTO_WORKER_ACTION](r_SVL_AUTO_WORKER_ACTION.md "r_SVL_AUTO_WORKER_ACTION.md")
- [SVL_COMPILE](r_SVL_COMPILE.md "r_SVL_COMPILE.md")
- [SVL_DATASHARE_CHANGE_LOG](r_SVL_DATASHARE_CHANGE_LOG.md "r_SVL_DATASHARE_CHANGE_LOG.md")
- [SVL_DATASHARE_CROSS_REGION_USAGE](r_SVL_DATASHARE_CROSS_REGION_USAGE.md "r_SVL_DATASHARE_CROSS_REGION_USAGE.md")
- [SVL_DATASHARE_USAGE_CONSUMER](r_SVL_DATASHARE_USAGE_CONSUMER.md "r_SVL_DATASHARE_USAGE_CONSUMER.md")
- [SVL_DATASHARE_USAGE_PRODUCER](r_SVL_DATASHARE_USAGE_PRODUCER.md "r_SVL_DATASHARE_USAGE_PRODUCER.md")
- [SVL_FEDERATED_QUERY](r_SVL_FEDERATED_QUERY.md "r_SVL_FEDERATED_QUERY.md")
- [SVL_MULTI_STATEMENT_VIOLATIONS](r_SVL_MULTI_STATEMENT_VIOLATIONS.md "r_SVL_MULTI_STATEMENT_VIOLATIONS.md")
- [SVL_MV_REFRESH_STATUS](r_SVL_MV_REFRESH_STATUS.md "r_SVL_MV_REFRESH_STATUS.md")
- [SVL_QERROR](r_SVL_QERROR.md "r_SVL_QERROR.md")
- [SVL_QLOG](r_SVL_QLOG.md "r_SVL_QLOG.md")
- [SVL_QUERY_METRICS](r_SVL_QUERY_METRICS.md "r_SVL_QUERY_METRICS.md")
- [SVL_QUERY_METRICS_SUMMARY](r_SVL_QUERY_METRICS_SUMMARY.md "r_SVL_QUERY_METRICS_SUMMARY.md")
- [SVL_QUERY_QUEUE_INFO](r_SVL_QUERY_QUEUE_INFO.md "r_SVL_QUERY_QUEUE_INFO.md")
- [SVL_QUERY_REPORT](r_SVL_QUERY_REPORT.md "r_SVL_QUERY_REPORT.md")
- [SVL_QUERY_SUMMARY](r_SVL_QUERY_SUMMARY.md "r_SVL_QUERY_SUMMARY.md")
- [SVL_RESTORE_ALTER_TABLE_PROGRESS](r_SVL_RESTORE_ALTER_TABLE_PROGRESS.md "r_SVL_RESTORE_ALTER_TABLE_PROGRESS.md")
- [SVL_S3LIST](r_SVL_S3LIST.md "r_SVL_S3LIST.md")
- [SVL_S3LOG](r_SVL_S3LOG.md "r_SVL_S3LOG.md")
- [SVL_S3PARTITION](r_SVL_S3PARTITION.md "r_SVL_S3PARTITION.md")
- [SVL_S3PARTITION_SUMMARY](r_SVL_S3PARTITION_SUMMARY.md "r_SVL_S3PARTITION_SUMMARY.md")
- [SVL_S3QUERY](r_SVL_S3QUERY.md "r_SVL_S3QUERY.md")
- [SVL_S3QUERY_SUMMARY](r_SVL_S3QUERY_SUMMARY.md "r_SVL_S3QUERY_SUMMARY.md")
- [SVL_S3RETRIES](r_SVL_S3RETRIES.md "r_SVL_S3RETRIES.md")
- [SVL_SPATIAL_SIMPLIFY](r_SVL_SPATIAL_SIMPLIFY.md "r_SVL_SPATIAL_SIMPLIFY.md")
- [SVL_SPECTRUM_SCAN_ERROR](r_SVL_SPECTRUM_SCAN_ERROR.md "r_SVL_SPECTRUM_SCAN_ERROR.md")
- [SVL_STATEMENTTEXT](r_SVL_STATEMENTTEXT.md "r_SVL_STATEMENTTEXT.md")
- [SVL_STORED_PROC_CALL](r_SVL_STORED_PROC_CALL.md "r_SVL_STORED_PROC_CALL.md")
- [SVL_STORED_PROC_MESSAGES](r_SVL_STORED_PROC_MESSAGES.md "r_SVL_STORED_PROC_MESSAGES.md")
- [SVL_TERMINATE](r_SVL_TERMINATE.md "r_SVL_TERMINATE.md")
- [SVL_UDF_LOG](r_SVL_UDF_LOG.md "r_SVL_UDF_LOG.md")
- [SVL_USER_INFO](r_SVL_USER_INFO.md "r_SVL_USER_INFO.md")
- [SVL_VACUUM_PERCENTAGE](r_SVL_VACUUM_PERCENTAGE.md "r_SVL_VACUUM_PERCENTAGE.md")
