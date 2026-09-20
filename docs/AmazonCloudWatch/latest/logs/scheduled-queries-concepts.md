

# Understanding scheduled queries concepts
<a name="scheduled-queries-concepts"></a>

Before creating scheduled queries, understand these key concepts that affect how your queries run and where results are delivered.

## IAM role separation
<a name="scheduled-queries-iam-roles"></a>

Scheduled queries require two separate IAM roles: one for executing queries and another for delivering results to destinations such as Amazon S3 buckets, Amazon EventBridge event buses, or lookup tables. Understanding why this separation exists helps you configure permissions correctly and use the security and operational benefits it provides.

The two-role architecture divides responsibilities between data access and data delivery. The query execution role accesses your log data and runs queries, while the destination delivery role writes results to your chosen destination. This separation follows the principle of least privilege—each role has only the permissions it needs for its specific function.

**Query execution role**  
Allows CloudWatch Logs to run CloudWatch Logs Insights queries on your behalf. This role needs permissions to access your log groups and execute queries, but doesn't need access to destination resources. Required permissions:  
+ `logs:StartQuery`
+ `logs:StopQuery`
+ `logs:GetQueryResults`
+ `logs:DescribeLogGroups`
+ `logs:Unmask` if unmask data is required
**For KMS-encrypted log groups:** `kms:Decrypt` and `kms:DescribeKey` permissions for the KMS key used to encrypt the log groups. These permissions need to be added as well.  
**Trust relationship requirement:** The query execution role must include a trust policy that allows the CloudWatch Logs service (`logs.amazonaws.com`) to assume the role. Without this trust relationship, scheduled queries will fail with permission errors.  
Example trust policy for the query execution role:  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```
Example permissions policy for the query execution role:  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:StartQuery",
                "logs:StopQuery",
                "logs:GetQueryResults",
                "logs:DescribeLogGroups"
            ],
            "Resource": "*"
        }
    ]
}
```

**Destination delivery role**  
Allows CloudWatch Logs to deliver query results to your chosen destination. This role only needs permissions for the specific destination service, following the principle of least privilege. Required permissions vary by destination type.  
**Trust relationship requirement:** The destination delivery role must also include a trust policy that allows the CloudWatch Logs service (`logs.amazonaws.com`) to assume the role.  
Example permissions policy for S3 destination delivery role:  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::your-scheduled-query-results-bucket/*"
        }
    ]
}
```
Example permissions policy for a lookup table destination delivery role:  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLookupTable",
                "logs:UpdateLookupTable",
                "logs:GetQueryResults"
            ],
            "Resource": "*"
        }
    ]
}
```

This separation provides practical benefits for your operations. From a security perspective, if you need to change where results are delivered, you only modify the destination delivery role without changing the query execution permissions. For compliance and auditing, you can clearly track which role accesses sensitive log data and which role writes to external systems. This makes it easier to demonstrate that your log analysis infrastructure follows security best practices.

## Cross-region and cross-account usage
<a name="scheduled-queries-cross-account"></a>

A scheduled query is created in a specific region and runs in that region. However, you can query log groups and deliver results across regions and accounts. You need to set up one or more AWS accounts as *monitoring accounts* and link them with multiple *source accounts*. A monitoring account is a central AWS account that can view and interact with observability data generated from source accounts. A source account is an individual AWS account that generates observability data for the resources that reside in it. Source accounts share their observability data with the monitoring account. So you can setup scheduled queries from the monitoring account using the log groups of all linked accounts.

**Querying cross-region log groups**  
Your scheduled query can access log groups in any region. Specify log groups using their full ARN format: `arn:aws:logs:region:account-id:log-group:log-group-name`. The query execution role needs `logs:StartQuery` and `logs:GetQueryResults` permissions for log groups in all target regions.

**Important**  
When querying log groups or delivering results across regions, log data crosses regional boundaries. Consider the following:  
**Data residency requirements** - Ensure cross-region data transfer complies with your organization's data governance policies and regulatory requirements
**Data transfer costs** - Cross-region data transfer incurs additional charges
**Network latency** - Queries accessing log groups in distant regions may experience higher latency
For optimal performance and cost efficiency, create scheduled queries in the same region as your primary log groups.

**Alternative approach:** Use [CloudWatch Logs centralization](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_Centralization.html) to replicate log data from multiple accounts and regions into a central monitoring account. This allows you to create scheduled queries in a single region that access all your centralized logs, avoiding cross-region queries and simplifying IAM permissions management.

## Schedule expressions and timezone handling
<a name="scheduled-queries-schedule-expressions"></a>

The schedule you define determines when your query runs and how often it executes. Choosing the right schedule expression affects when you receive results and how much data you query. Understanding the expression types helps you choose between simplicity and precision.

Cron expressions provide precise control over timing, allowing you to specify exact times, days of the week, or days of the month. Use cron expressions when you need queries to run at specific business hours or align with operational schedules. In the console you can also scheduled queries using easy calendar options.

**Cron expressions**  
Run queries at specific times. Format: `cron(minute hour day-of-month month day-of-week year)`. Examples:  
+ `cron(0 9 * * ? *)` - Every day at 9:00 AM UTC
+ `cron(0 18 ? * MON-FRI *)` - Weekdays at 6:00 PM UTC
+ `cron(0 0 1 * ? *)` - First day of every month at midnight UTC
+ `cron(0 12 ? * SUN *)` - Every Sunday at noon UTC
+ `cron(30 8 1 1 ? *)` - January 1st at 8:30 AM UTC

All scheduled queries run in UTC, regardless of your local timezone or where your AWS resources are located. This is particularly important when you schedule queries for business hours or time-sensitive analysis. For example, if your business operates in US Eastern Time and you want a daily report at 9 AM ET, you need to account for the UTC offset (14:00 UTC during daylight saving time, 13:00 UTC otherwise). Plan your schedule expressions with UTC in mind to ensure queries run at the intended times.

## Choosing a query language
<a name="scheduled-queries-query-languages"></a>

Scheduled queries support three different query languages, and your choice affects both how you write queries and how easily your team can maintain them. The right language depends on your analysis requirements and your team's existing skills.

If you are primarily filtering and aggregating log data, CloudWatch Logs Insights Query Language offers the most straightforward syntax. For complex data transformations where you need to reshape or enrich data through multiple steps, PPL's pipeline approach makes the logic easier to follow. When you need to perform joins or complex aggregations similar to database operations, SQL provides familiar syntax that database-experienced teams can adopt quickly.

**CloudWatch Logs Insights Query Language (CWLI)**  
Purpose-built for log analysis with intuitive syntax. Best for:  
+ Text-based log analysis and filtering
+ Time-series aggregations and statistics
+ Teams new to log analysis

**OpenSearch Service Piped Processing Language (PPL)**  
Pipeline-based query language with powerful data transformation capabilities. Best for:  
+ Complex data transformations and enrichment
+ Multi-step data processing workflows
+ Teams familiar with pipeline-based processing

**OpenSearch Service Structured Query Language (SQL)**  
Standard SQL syntax for familiar database-style queries. Best for:  
+ Complex joins and aggregations
+ Business intelligence and reporting
+ Teams with strong SQL experience

## Destination selection and use cases
<a name="scheduled-queries-destinations"></a>

Where you send query results determines what you can do with them. This choice shapes your entire downstream workflow—whether you are building long-term analytics, triggering automated responses, or both. Understanding the strengths of each destination type helps you design the right architecture for your use case.

Amazon S3 destinations are optimized for storage and batch processing. When you need to keep query results for months or years, analyze trends over time, or feed data into analytics platforms, Amazon S3 provides cost-effective storage with unlimited retention. EventBridge destinations are optimized for real-time automation. When query results should trigger immediate actions—like sending alerts, starting workflows, or updating systems—EventBridge delivers results as events that your applications can respond to instantly. By default all query completion events are automatically sent as events to the default event bus, enabling integration with downstream processing systems, Lambda functions, or other event-driven architectures. Results are only published to destinations when query is executed successfully. Lookup table destinations are optimized for keeping reference data current. A lookup table destination automatically populates or refreshes the specified lookup table with the query results on each scheduled execution, so other queries can reference the latest data with the `lookup` command.

**Amazon S3 destinations**  
Store query results as JSON files for long-term retention and batch processing. Amazon S3 destinations work best for the following scenarios:  
+ Historical analysis and data archiving
+ Integration with data lakes and analytics platforms
+ Compliance and audit requirements
+ Cost-effective storage of large result sets

**EventBridge destinations**  
Send query results as events for real-time processing and automation. Use the `queryId` in the event to retrieve the query results, which remain available for 30 days after the query runs. EventBridge destinations work best for the following scenarios:  
+ Triggering automated responses to query results
+ Integration with serverless workflows and Lambda functions
+ Real-time alerting and notification systems
+ Event-driven architectures and microservices

**Lookup table destinations**  
Automatically create or refresh a lookup table with query results on each scheduled execution. Each refresh is a full replacement of the table content. Lookup table destinations work best for the following scenarios:  
+ Keeping reference data current for the `lookup` command in your log queries
+ Maintaining allowlists, denylists, or entity inventories derived from log data
+ Enriching queries with recent activity summaries, such as active user or resource lists

## Query result format and structure
<a name="scheduled-queries-result-format"></a>

Scheduled queries deliver results in JSON format, but each destination type receives a different payload. For a lookup table destination, the query results become the content of the lookup table, and each run replaces that content. For more information, see [Configuring lookup table destinations for scheduled queries](scheduled-queries-lookup-table-destination.md).

Amazon S3 destinations receive the result rows of the query. Each object contains a JSON array with one entry for each row in the result set, and each entry maps the output field names of the query to their values. The object does not contain query metadata or query statistics, and it omits the `@ptr` field even if the query requests it, because that field is usable only in the console.

EventBridge destinations receive query metadata, including the query statistics, but no result rows. To retrieve the rows of a completed query, call [GetQueryResults](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html) with the value of `queryId` from the event.

The following example shows the event that CloudWatch Logs publishes to EventBridge when a scheduled query completes.

```
{
    "version": "0",
    "id": "be72061b-eca2-e068-a7e1-83e01d6fe807",
    "detail-type": "Scheduled Query Completed",
    "source": "aws.logs",
    "account": "123456789012",
    "time": "2025-11-18T11:31:48Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:logs:us-east-1:123456789012:scheduled-query:477b4380-b098-474e-9c5e-e10a8cc2e6e7"
    ],
    "detail": {
        "queryId": "2038fd57-ab4f-4018-bb2f-61d363f4a004",
        "queryString": "fields @timestamp, @message, @logStream\n| filter @message like /ERROR/\n| sort @timestamp desc\n| limit 10000",
        "logGroupIdentifiers": [
            "/aws/lambda/my-function"
        ],
        "status": "Complete",
        "startTime": 1763465460,
        "statistics": {
            "recordsMatched": 1842,
            "recordsScanned": 48325,
            "estimatedRecordsSkipped": 0,
            "bytesScanned": 12081250,
            "estimatedBytesSkipped": 0,
            "logGroupsScanned": 1,
            "resultCount": 1842
        }
    }
}
```

This query does not aggregate, and it returned fewer rows than its `limit` of 10,000, so each of the 1,842 matching log events became one output row and `recordsMatched` and `resultCount` are equal. A query that aggregates, or one whose result set is truncated by `limit`, produces a `resultCount` lower than `recordsMatched`. For more information, see [Understanding recordsScanned, recordsMatched, and resultCount](#scheduled-queries-record-counts).

Key elements include:
+ `statistics` - Counters that describe how much log data the query read and how large the result set is. For a description of each field, see the following table.
+ `startTime` - When the query execution started (Unix timestamp)
+ `queryString` - The actual query that was executed
+ `queryId` - Query id of the query using which results can be retrieved
+ `logGroupIdentifiers` - List of log groups that were queried
+ `status` - Query execution status (Complete, Failed, etc.)

The following table describes each field in the `statistics` object. For the API definitions of these fields, see [QueryStatistics](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_QueryStatistics.html).


| Field | Description | 
| --- | --- | 
| recordsScanned | The total number of log events scanned during the query. | 
| recordsMatched | The number of log events that matched the query string. This value counts log events, not output rows. For the number of rows in the result set, use resultCount. | 
| resultCount | The number of rows in the query result set. This value counts only the rows that survived all operations in the query, so it might be less than recordsMatched. It covers all pages of results that GetQueryResults returns. For more information, see [Understanding recordsScanned, recordsMatched, and resultCount](#scheduled-queries-record-counts). | 
| estimatedRecordsSkipped | An estimate of the number of log events that were skipped when processing this query, because the query contained an indexed field. Skipping these entries lowers query costs and improves the query performance time. For more information, see [Create field indexes to improve query performance and reduce scan volume](CloudWatchLogs-Field-Indexing.md). | 
| bytesScanned | The total number of bytes in the log events scanned during the query. | 
| estimatedBytesSkipped | An estimate of the number of bytes in the log events that were skipped when processing this query, because the query contained an indexed field. | 
| logGroupsScanned | The number of log groups that were scanned by this query. | 

## Understanding recordsScanned, recordsMatched, and resultCount
<a name="scheduled-queries-record-counts"></a>

Three of the query statistics count different things, and comparing them directly can be misleading. Each one measures a different stage of query processing:
+ `recordsScanned` - The number of log events that the query read from your log groups. This is the input to the query.
+ `recordsMatched` - The number of those log events that matched the query string. This value counts log events.
+ `resultCount` - The number of rows in the result set that the query produced. This value counts output rows.

Each stage narrows the data. A command such as `stats` combines many log events into a single output row, so `resultCount` can be much smaller than `recordsMatched`. A large `recordsMatched` with a small `resultCount` does not mean that rows are missing from the result set.

**Example – Aggregation**

The following query counts the error messages in each log stream of one log group over a one-hour period.

```
filter @message like /ERROR/
| stats count(*) as errorCount by @logStream
```

If the query reads 1,500,000 log events, 24,318 of them contain `ERROR`, and those matching log events come from 12 log streams, then the query completes with the following statistics.

```
"statistics": {
    "recordsMatched": 24318,
    "recordsScanned": 1500000,
    "estimatedRecordsSkipped": 0,
    "bytesScanned": 450000000,
    "estimatedBytesSkipped": 0,
    "logGroupsScanned": 1,
    "resultCount": 12
}
```

`stats` produces one row for each log stream, so `resultCount` is 12 while `recordsMatched` is 24,318. The 12 values of `errorCount` add up to 24,318.

**Example – Post-aggregation filter**

The following query keeps only the log streams that produced more than 1,000 errors.

```
filter @message like /ERROR/
| stats count(*) as errorCount by @logStream
| filter errorCount > 1000
```

The final `filter` command runs after grouping, so it removes rows from the result set instead of log events from the scan. If 3 of the 12 log streams have an `errorCount` greater than 1,000, then `resultCount` is 3 instead of 12. `recordsScanned` and `bytesScanned` do not change, because the query reads the same log data either way.

**Example – Limit**

A `limit` command reduces `resultCount` without any aggregation. The following query returns the 100 most recent error messages.

```
filter @message like /ERROR/
| sort @timestamp desc
| limit 100
```

If the query scans the same 1,500,000 log events and matches the same 24,318, then `resultCount` is 100, because `limit` caps the result set at 100 rows. In the console, you see this relationship as **Showing 100 of 24,318 records matched**.

Each statistic answers a different question.

**How many rows did this query return?**  
Use `resultCount`. A value of 0 means that the query produced no rows. Do not use `recordsMatched` for this purpose, because it counts log events rather than rows.

**How much log data did this query read?**  
Use `recordsScanned` and `bytesScanned`. Scan volume determines the cost and the run time of a query. To reduce it, shorten the time range, query fewer log groups, or create field indexes. For more information, see [Create field indexes to improve query performance and reduce scan volume](CloudWatchLogs-Field-Indexing.md).

**How many log events matched this query?**  
Use `recordsMatched`.

**Note**  
CloudWatch Logs omits a statistic from the `statistics` object when no value is available for it, rather than reporting the statistic as 0.  
If your event consumer does not find `resultCount` in an event, treat the value as unknown rather than as 0. Write event consumers so that they tolerate statistics that are absent and ignore statistics that they do not recognize.