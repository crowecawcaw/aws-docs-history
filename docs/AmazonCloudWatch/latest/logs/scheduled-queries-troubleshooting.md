# Troubleshooting scheduled

queries

Use these troubleshooting topics to resolve common issues with scheduled
queries.

## Query execution fails with

permission errors

Resolve permission errors that prevent scheduled queries from executing or
delivering results to destinations.

Permission errors occur when the execution role lacks the necessary permissions to
read from log groups or write to destination resources.

###### To resolve permission errors

1. Verify that the execution role has `logs:StartQuery`,
   `logs:GetQueryResults`, and
   `logs:DescribeLogGroups` permissions for the target log
   groups.
2. Ensure the execution role has write permissions for the destination
   resources (such as `s3:PutObject` for S3 buckets).
3. Check that the trust policy allows CloudWatch Logs to assume the execution
   role. The role should trust the logs service principal (`logs.amazonaws.com`) in its trust policy.

Common causes include missing IAM permissions, incorrect resource ARNs in the
policy, or trust policy configuration issues.

To prevent permission errors, use the principle of least privilege when creating
execution roles and test permissions before deploying scheduled queries to
production.

## Query times out

Resolve timeout errors that occur when scheduled queries exceed the maximum
execution time limit.

Query timeouts happen when the query takes more than 60 mins to process the specified data
range, often due to large datasets or complex query logic.

###### To resolve timeout errors

1. Reduce the time range by decreasing the start time offset to process less
   data per execution.
2. Optimize the query by adding filters early in the query to reduce the
   amount of data processed. Use filter indexes to reduce the data scan size.
3. Consider breaking complex queries into simpler, more focused
   queries.

Common causes include querying large time ranges, processing high-volume log
groups, or using complex aggregations without proper filtering.

To prevent timeouts, test queries manually in CloudWatch Logs Insights with your
expected data volume and optimize performance before scheduling.

## Destination

processing fails

Resolve failures that occur when scheduled query results cannot be delivered to
the configured destinations.

Destination processing failures happen when the target Amazon S3 bucket or EventBridge event
bus is inaccessible or incorrectly configured.

###### To resolve failures where query results are not getting published to destination

1. Verify that the specified Amazon S3 bucket exists and is
   accessible.
2. Check the destination configuration for correct URIs.
3. Ensure the execution role has the necessary permissions to write to the
   destination.

Common causes include deleted or renamed destination resources, incorrect
destination URIs, or network connectivity issues.

To prevent destination failures, regularly validate destination configurations and
monitor destination resource availability.

## Invalid query errors

Resolve syntax and logic errors in scheduled query strings that prevent successful
execution.

Invalid query errors occur when the query string contains syntax errors,
references non-existent fields, or uses unsupported query language features.

###### To resolve invalid query errors

1. Test your query manually in CloudWatch Logs Insights to verify syntax and
   logic.
2. Check that all referenced log fields exist in your target log
   groups.
3. Verify that the query language features you're using are supported for
   scheduled queries.

Common causes include typos in field names, incorrect query syntax, or using query
features not supported in the scheduled execution environment.

To prevent invalid query errors, always test queries interactively before
scheduling and use field discovery features to verify field names.

## Query Concurrency Errors

There are some important points mentioned below to keep in mind when concurrency errors are seen as scheduled queries use the same quota as of Cloudwatch Logs insights queries. It is recommended to spread out your schedules to avoid hitting the concurrency limit.

- **Quota:** You can run up to 30 concurrent CloudWatch Logs Insights queries per AWS account.
- **Dashboards:** Queries added to CloudWatch dashboards also count towards this concurrency limit, as they are executed when the dashboard is loaded or refreshed.
- **OpenSearch Service PPL/SQL:** Within the 30 concurrent queries, a subset (currently 15) can utilize either OpenSearch PPL or OpenSearch SQL.
- **Cross-account queries:** The concurrency quota applies to both single and cross-account queries. When using CloudWatch cross-account observability, queries initiated in a monitoring account against a linked source account also count towards the monitoring account's concurrency limit.
- **Infrequent Access Log Groups:** For log groups in the infrequent access log class, the maximum number of concurrent Logs Insights queries is limited to five.
