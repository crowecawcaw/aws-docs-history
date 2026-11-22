

# Query results

Answers aggregate by default. Asking which resources drove a cost increase returns the resources that explain the change, not every line item behind it.

A query returns up to 10,000 rows, inline in the answer. When your question matches more than 10,000 rows, AWS FinOps Agent answers in aggregate, so its totals cover every row, and tells you when a list stops at 10,000 rows. To see the individual rows, narrow your question, for example to one account or one day. See [Quotas and restrictions](billing-limits.md).

**Note**  
During public preview, Data Hub returns query results inside AWS FinOps Agent answers, up to 10,000 rows for each query. To get complete CUR 2.0 files in your own Amazon S3 bucket, use AWS Data Exports.