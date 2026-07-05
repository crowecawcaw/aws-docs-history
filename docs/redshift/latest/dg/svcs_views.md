Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVCS views for main and concurrency scaling clusters

SVCS system views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters. The views are similar to the tables with the prefix STL except that the STL tables provide information only for queries run on the main cluster.

###### Topics

- [SVCS\_ALERT\_EVENT\_LOG](r_SVCS_ALERT_EVENT_LOG.md "r_SVCS_ALERT_EVENT_LOG.md")
- [SVCS\_COMPILE](r_SVCS_COMPILE.md "r_SVCS_COMPILE.md")
- [SVCS\_CONCURRENCY\_SCALING\_USAGE](r_SVCS_CONCURRENCY_SCALING_USAGE.md "r_SVCS_CONCURRENCY_SCALING_USAGE.md")
- [SVCS\_EXPLAIN](r_SVCS_EXPLAIN.md "r_SVCS_EXPLAIN.md")
- [SVCS\_PLAN\_INFO](r_SVCS_PLAN_INFO.md "r_SVCS_PLAN_INFO.md")
- [SVCS\_QUERY\_SUMMARY](r_SVCS_QUERY_SUMMARY.md "r_SVCS_QUERY_SUMMARY.md")
- [SVCS\_S3LIST](r_SVCS_S3LIST.md "r_SVCS_S3LIST.md")
- [SVCS\_S3LOG](r_SVCS_S3LOG.md "r_SVCS_S3LOG.md")
- [SVCS\_S3PARTITION\_SUMMARY](r_SVCS_S3PARTITION_SUMMARY.md "r_SVCS_S3PARTITION_SUMMARY.md")
- [SVCS\_S3QUERY\_SUMMARY](r_SVCS_S3QUERY_SUMMARY.md "r_SVCS_S3QUERY_SUMMARY.md")
- [SVCS\_STREAM\_SEGS](r_SVCS_STREAM_SEGS.md "r_SVCS_STREAM_SEGS.md")
- [SVCS\_UNLOAD\_LOG](r_SVCS_UNLOAD_LOG.md "r_SVCS_UNLOAD_LOG.md")
