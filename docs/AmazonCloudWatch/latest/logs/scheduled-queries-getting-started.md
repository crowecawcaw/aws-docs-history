# Getting started with scheduled queries

When you create a scheduled query, you'll configure several key components that define
how your query runs and where results are delivered. Understanding these components will
help you set up effective automated log analysis.

Each scheduled query consists of the following key components:

**Query configuration**

The CloudWatch Logs Insights query string, target log groups, and query language to use for
analysis.

**Schedule expression**

A cron expression or frequency calendar that defines when the query runs.
You can specify timezone settings to ensure queries run at the correct local
time. The console displays a human-readable description of your schedule,
such as "Run query on every Tuesday at 15:10 for a time range of 5 minutes,
effective immediately, on UTC, until indefinitely."

**Time range**

The lookback period for each query execution, defined by a start time
offset from the execution time. This determines how much historical data
each query execution will analyze.

**Execution schedule preview**

The console shows the next three scheduled query runs with exact dates and
times (for example, 2025/10/28 15:10, UTC; 2025/11/04 15:10, UTC; 2025/11/11
15:10, UTC), helping you verify that the schedule is configured
correctly.

**Destinations**

Where query results are delivered after successful execution. Supported
destinations include Amazon S3 buckets and by default result metadata is send to the default event bus.

**Execution role**

An IAM role that CloudWatch Logs assumes to execute the query and deliver results
to the specified destinations.

Before creating scheduled queries, ensure you have the necessary permissions and
resources configured.
