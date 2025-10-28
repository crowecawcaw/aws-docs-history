Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL views for logging

STL system views are generated from Amazon Redshift log files to provide a history of the
system.

These files reside on every node in the data warehouse cluster. The STL views take the
information from the logs and format them into usable views for system
administrators.

**Log retention** – STL system views retain seven
days of log history. Log retention is guaranteed for all cluster sizes and node types, and
it isn't affected by changes in cluster workload. Log retention also isn't affected by
cluster status, such as when the cluster is paused. You have less than seven days of log history
only in the case where the cluster is new. You don't need to take any action to retain logs,
but you have to periodically copy log data to other tables or unload it to Amazon S3 to keep log data
that's more than 7 days old.

###### Topics

- [STL_AGGR](r_STL_AGGR.md "r_STL_AGGR.md")
- [STL_ALERT_EVENT_LOG](r_STL_ALERT_EVENT_LOG.md "r_STL_ALERT_EVENT_LOG.md")
- [STL_ANALYZE](r_STL_ANALYZE.md "r_STL_ANALYZE.md")
- [STL_ANALYZE_COMPRESSION](r_STL_ANALYZE_COMPRESSION.md "r_STL_ANALYZE_COMPRESSION.md")
- [STL_BCAST](r_STL_BCAST.md "r_STL_BCAST.md")
- [STL_COMMIT_STATS](r_STL_COMMIT_STATS.md "r_STL_COMMIT_STATS.md")
- [STL_CONNECTION_LOG](r_STL_CONNECTION_LOG.md "r_STL_CONNECTION_LOG.md")
- [STL_DDLTEXT](r_STL_DDLTEXT.md "r_STL_DDLTEXT.md")
- [STL_DELETE](r_STL_DELETE.md "r_STL_DELETE.md")
- [STL_DISK_FULL_DIAG](r_STL_DISK_FULL_DIAG.md "r_STL_DISK_FULL_DIAG.md")
- [STL_DIST](r_STL_DIST.md "r_STL_DIST.md")
- [STL_ERROR](r_STL_ERROR.md "r_STL_ERROR.md")
- [STL_EXPLAIN](r_STL_EXPLAIN.md "r_STL_EXPLAIN.md")
- [STL_FILE_SCAN](r_STL_FILE_SCAN.md "r_STL_FILE_SCAN.md")
- [STL_HASH](r_STL_HASH.md "r_STL_HASH.md")
- [STL_HASHJOIN](r_STL_HASHJOIN.md "r_STL_HASHJOIN.md")
- [STL_INSERT](r_STL_INSERT.md "r_STL_INSERT.md")
- [STL_LIMIT](r_STL_LIMIT.md "r_STL_LIMIT.md")
- [STL_LOAD_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md")
- [STL_LOAD_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md")
- [STL_LOADERROR_DETAIL](r_STL_LOADERROR_DETAIL.md "r_STL_LOADERROR_DETAIL.md")
- [STL_MERGE](r_STL_MERGE.md "r_STL_MERGE.md")
- [STL_MERGEJOIN](r_STL_MERGEJOIN.md "r_STL_MERGEJOIN.md")
- [STL_MV_STATE](r_STL_MV_STATE.md "r_STL_MV_STATE.md")
- [STL_NESTLOOP](r_STL_NESTLOOP.md "r_STL_NESTLOOP.md")
- [STL_PARSE](r_STL_PARSE.md "r_STL_PARSE.md")
- [STL_PLAN_INFO](r_STL_PLAN_INFO.md "r_STL_PLAN_INFO.md")
- [STL_PROJECT](r_STL_PROJECT.md "r_STL_PROJECT.md")
- [STL_QUERY](r_STL_QUERY.md "r_STL_QUERY.md")
- [STL_QUERY_METRICS](r_STL_QUERY_METRICS.md "r_STL_QUERY_METRICS.md")
- [STL_QUERYTEXT](r_STL_QUERYTEXT.md "r_STL_QUERYTEXT.md")
- [STL_REPLACEMENTS](r_STL_REPLACEMENTS.md "r_STL_REPLACEMENTS.md")
- [STL_RESTARTED_SESSIONS](r_STL_RESTARTED_SESSIONS.md "r_STL_RESTARTED_SESSIONS.md")
- [STL_RETURN](r_STL_RETURN.md "r_STL_RETURN.md")
- [STL_S3CLIENT](r_STL_S3CLIENT.md "r_STL_S3CLIENT.md")
- [STL_S3CLIENT_ERROR](r_STL_S3CLIENT_ERROR.md "r_STL_S3CLIENT_ERROR.md")
- [STL_SAVE](r_STL_SAVE.md "r_STL_SAVE.md")
- [STL_SCAN](r_STL_SCAN.md "r_STL_SCAN.md")
- [STL_SCHEMA_QUOTA_VIOLATIONS](r_STL_SCHEMA_QUOTA_VIOLATIONS.md "r_STL_SCHEMA_QUOTA_VIOLATIONS.md")
- [STL_SESSIONS](r_STL_SESSIONS.md "r_STL_SESSIONS.md")
- [STL_SORT](r_STL_SORT.md "r_STL_SORT.md")
- [STL_SSHCLIENT_ERROR](r_STL_SSHCLIENT_ERROR.md "r_STL_SSHCLIENT_ERROR.md")
- [STL_STREAM_SEGS](r_STL_STREAM_SEGS.md "r_STL_STREAM_SEGS.md")
- [STL_TR_CONFLICT](r_STL_TR_CONFLICT.md "r_STL_TR_CONFLICT.md")
- [STL_UNDONE](r_STL_UNDONE.md "r_STL_UNDONE.md")
- [STL_UNIQUE](r_STL_UNIQUE.md "r_STL_UNIQUE.md")
- [STL_UNLOAD_LOG](r_STL_UNLOAD_LOG.md "r_STL_UNLOAD_LOG.md")
- [STL_USAGE_CONTROL](r_STL_USAGE_CONTROL.md "r_STL_USAGE_CONTROL.md")
- [STL_USERLOG](r_STL_USERLOG.md "r_STL_USERLOG.md")
- [STL_UTILITYTEXT](r_STL_UTILITYTEXT.md "r_STL_UTILITYTEXT.md")
- [STL_VACUUM](r_STL_VACUUM.md "r_STL_VACUUM.md")
- [STL_WINDOW](r_STL_WINDOW.md "r_STL_WINDOW.md")
- [STL_WLM_ERROR](r_STL_WLM_ERROR.md "r_STL_WLM_ERROR.md")
- [STL_WLM_RULE_ACTION](r_STL_WLM_RULE_ACTION.md "r_STL_WLM_RULE_ACTION.md")
- [STL_WLM_QUERY](r_STL_WLM_QUERY.md "r_STL_WLM_QUERY.md")
