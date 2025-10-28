Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Diagnostic queries for query tuning

Use the following queries to identify issues with queries or underlying tables that
can affect query performance. We recommend using these
queries with the query tuning processes discussed in [Query analysis and improvement](c-query-tuning.md "c-query-tuning.md").

###### Note

These queries are for Amazon Redshift provisioned clusters. These queries are not for use with Redshift Serverless workgroups.

###### Topics

- [Identifying queries that are
  top candidates for tuning](identify-queries-that-are-top-candidates-for-tuning.md "identify-queries-that-are-top-candidates-for-tuning.md")
- [Identifying tables with data skew
  or unsorted rows](identify-tables-with-data-skew-or-unsorted-rows.md "identify-tables-with-data-skew-or-unsorted-rows.md")
- [Identifying queries with nested loops](identify-queries-with-nested-loops.md "identify-queries-with-nested-loops.md")
- [Reviewing queue wait times for queries](review-queue-wait-times-for-queries.md "review-queue-wait-times-for-queries.md")
- [Reviewing query alerts by table](review-query-alerts-by-table.md "review-query-alerts-by-table.md")
- [Identifying tables with missing
  statistics](identify-tables-with-missing-statistics.md "identify-tables-with-missing-statistics.md")
