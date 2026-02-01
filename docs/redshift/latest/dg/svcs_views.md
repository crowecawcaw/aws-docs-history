Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVCS views for main and concurrency scaling clusters

SVCS system views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters. The views are similar to the tables with the prefix STL except that the STL tables provide information only for queries run on the main cluster.

###### Topics

- [SVCS_ALERT_EVENT_LOG](r_SVCS_ALERT_EVENT_LOG.md "r_SVCS_ALERT_EVENT_LOG.md")
- [SVCS_COMPILE](r_SVCS_COMPILE.md "r_SVCS_COMPILE.md")
- [SVCS_CONCURRENCY_SCALING_USAGE](r_SVCS_CONCURRENCY_SCALING_USAGE.md "r_SVCS_CONCURRENCY_SCALING_USAGE.md")
- [SVCS_EXPLAIN](r_SVCS_EXPLAIN.md "r_SVCS_EXPLAIN.md")
- [SVCS_PLAN_INFO](r_SVCS_PLAN_INFO.md "r_SVCS_PLAN_INFO.md")
- [SVCS_QUERY_SUMMARY](r_SVCS_QUERY_SUMMARY.md "r_SVCS_QUERY_SUMMARY.md")
- [SVCS_S3LIST](r_SVCS_S3LIST.md "r_SVCS_S3LIST.md")
- [SVCS_S3LOG](r_SVCS_S3LOG.md "r_SVCS_S3LOG.md")
- [SVCS_S3PARTITION_SUMMARY](r_SVCS_S3PARTITION_SUMMARY.md "r_SVCS_S3PARTITION_SUMMARY.md")
- [SVCS_S3QUERY_SUMMARY](r_SVCS_S3QUERY_SUMMARY.md "r_SVCS_S3QUERY_SUMMARY.md")
- [SVCS_STREAM_SEGS](r_SVCS_STREAM_SEGS.md "r_SVCS_STREAM_SEGS.md")
- [SVCS_UNLOAD_LOG](r_SVCS_UNLOAD_LOG.md "r_SVCS_UNLOAD_LOG.md")
