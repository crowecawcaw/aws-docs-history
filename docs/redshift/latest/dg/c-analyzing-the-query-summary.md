Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Analyzing the query summary

To get execution steps and statistics in more detail than in the query plan that
[EXPLAIN](r_EXPLAIN.md "r_EXPLAIN.md") produces, use the [SVL_QUERY_SUMMARY](r_SVL_QUERY_SUMMARY.md "r_SVL_QUERY_SUMMARY.md") and [SVL_QUERY_REPORT](r_SVL_QUERY_REPORT.md "r_SVL_QUERY_REPORT.md") system
views.

SVL_QUERY_SUMMARY provides query statistics by stream. You can use the information it
provides to identify issues with expensive steps, long-running steps, and steps that
write to disk.

The SVL_QUERY_REPORT system view enables you to see information similar to that for
SVL_QUERY_SUMMARY, only by compute node slice rather than by stream. You can use the
slice-level information for detecting uneven data distribution across the cluster (also
known as data distribution skew), which forces some nodes to do more work than others
and impairs query performance.

###### Topics

- [Using the SVL_QUERY_SUMMARY view](using-SVL-Query-Summary.md "using-SVL-Query-Summary.md")
- [Using the SVL_QUERY_REPORT view](using-SVL-Query-Report.md "using-SVL-Query-Report.md")
- [Mapping the query plan to the query summary](query-plan-summary-map.md "query-plan-summary-map.md")
