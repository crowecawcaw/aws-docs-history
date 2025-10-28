Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Query analysis and improvement

Retrieving information from an Amazon Redshift data warehouse involves running
complex queries on extremely large amounts of data, which can take a long time to process.
To make sure that queries process as quickly as possible, there are a number of
tools you can use to identify potential performance issues.

###### Topics

- [Query analysis workflow](c-query-analysis-process.md "c-query-analysis-process.md")
- [Reviewing query alerts](c-reviewing-query-alerts.md "c-reviewing-query-alerts.md")
- [Analyzing the query plan](c-analyzing-the-query-plan.md "c-analyzing-the-query-plan.md")
- [Analyzing the query summary](c-analyzing-the-query-summary.md "c-analyzing-the-query-summary.md")
- [Query performance improvement](query-performance-improvement-opportunities.md "query-performance-improvement-opportunities.md")
- [Diagnostic queries for query tuning](diagnostic-queries-for-query-tuning.md "diagnostic-queries-for-query-tuning.md")
