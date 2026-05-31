# Logging and monitoring in Amazon DocumentDB

Amazon DocumentDB (with MongoDB compatibility) provides a variety of Amazon CloudWatch metrics that you can monitor
to determine the health and performance of your Amazon DocumentDB clusters and
instances. You can view Amazon DocumentDB metrics using various tools, including
the Amazon DocumentDB console, the AWS CLI, the Amazon CloudWatch console, and the CloudWatch API.
For more information about monitoring, see [Monitoring Amazon DocumentDB](monitoring_docdb.md "monitoring_docdb.md").

In addition to Amazon CloudWatch metrics, you can use the profiler to log the
execution time and details of operations that were performed on your
cluster. Profiler is useful for monitoring the slowest operations on your
cluster to help you improve individual query performance and overall
cluster performance. When enabled, operations are logged to Amazon CloudWatch
Logs and you can use CloudWatch Insight to analyze, monitor, and archive your
Amazon DocumentDB profiling data. For more information, see [Profiling Amazon DocumentDB operations](profiling.md "profiling.md").

Amazon DocumentDB also integrates with AWS CloudTrail, a service that provides a
record of actions taken by users, roles, or an AWS service in
Amazon DocumentDB (with MongoDB compatibility). CloudTrail captures all AWS CLI API calls for Amazon DocumentDB as events,
including calls from the Amazon DocumentDB AWS Management Console and from code calls to the
Amazon DocumentDB SDK. For more information, see [Logging Amazon DocumentDB API calls with AWS CloudTrail](logging-with-cloudtrail.md "logging-with-cloudtrail.md").

With Amazon DocumentDB, you can audit events that were performed in your cluster.
Examples of logged events include successful and failed authentication
attempts, dropping a collection in a database, or creating an index. By
default, auditing is disabled on Amazon DocumentDB and requires that you opt in to
this feature. For more information, see [Auditing Amazon DocumentDB events](event-auditing.md "event-auditing.md").
