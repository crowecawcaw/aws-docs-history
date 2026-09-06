

# Delivering logs to Amazon CloudWatch Logs
<a name="sal-cw-section"></a>

When you deliver server access logs to Amazon CloudWatch Logs, you get structured JSON logs that you can query interactively with CloudWatch Logs Insights, aggregate across accounts and Regions, and optionally mirror to S3 Tables in Apache Iceberg format for SQL analytics. You can also deliver logs to Amazon S3 in JSON or Apache Parquet format or route them through Amazon Data Firehose.

**Topics**
+ [Delivering server access logs to CloudWatch Logs](sal-cw-enabling.md)
+ [Log format in CloudWatch Logs](sal-cw-log-format.md)
+ [Managing log retention](sal-cw-retention.md)
+ [Querying logs with CloudWatch Logs Insights](sal-cw-querying-insights.md)
+ [Querying access logs in S3 Tables](sal-cw-querying-s3tables.md)
+ [Troubleshooting CloudWatch Logs delivery](sal-cw-troubleshooting.md)