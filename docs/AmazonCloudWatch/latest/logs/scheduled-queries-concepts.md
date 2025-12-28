# Understanding scheduled queries

concepts

Before creating scheduled queries, understand these key concepts that affect how your
queries run and where results are delivered.

## IAM role separation

Scheduled queries require two separate IAM roles: one for executing queries and
another for delivering results to Amazon S3 or Amazon EventBridge event buses. Understanding why this separation exists helps you
configure permissions correctly and use the security and operational benefits it
provides.

The two-role architecture divides responsibilities between data access and data
delivery. The query execution role accesses your log data and runs queries, while
the destination delivery role writes results to your chosen destination. This
separation follows the principle of least privilege—each role has only the
permissions it needs for its specific function.

**Query execution role**

Allows CloudWatch Logs to run CloudWatch Logs Insights queries on your behalf. This role needs
permissions to access your log groups and execute queries, but doesn't
need access to destination resources. Required permissions:

- `logs:StartQuery`
- `logs:StopQuery`
- `logs:GetQueryResults`
- `logs:DescribeLogGroups`
- `logs:Unmask` if unmask data is required

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

Allows CloudWatch Logs to deliver query results to your chosen destination. This
role only needs permissions for the specific destination service,
following the principle of least privilege. Required permissions vary by
destination type.

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

This separation provides practical benefits for your operations. From a security
perspective, if you need to change where results are delivered, you only modify the
destination delivery role without changing the query execution permissions. For
compliance and auditing, you can clearly track which role accesses sensitive log
data and which role writes to external systems. This makes it easier to demonstrate
that your log analysis infrastructure follows security best practices.

## Cross-region and cross-account

usage

A scheduled query is created in a specific region and runs in that region.
However, you can query log groups and deliver results across regions and
accounts. You need to set up one or more AWS accounts as _monitoring accounts_ and link them with multiple _source accounts_. A monitoring account is a central AWS account that can view and interact with observability data generated from source accounts. A source account is an individual AWS account that generates observability data for the resources that reside in it. Source accounts share their observability data with the monitoring account. So you can setup scheduled queries from the monitoring account using the log groups of all linked accounts.

**Querying cross-region log groups**

Your scheduled query can access log groups in any region. Specify log
groups using their full ARN format:
`arn:aws:logs:region:account-id:log-group:log-group-name`.
The query execution role needs `logs:StartQuery` and
`logs:GetQueryResults` permissions for log groups in all
target regions.

###### Important

When querying log groups or delivering results across regions, log data
crosses regional boundaries. Consider the following:

- **Data residency requirements** - Ensure
  cross-region data transfer complies with your organization's data
  governance policies and regulatory requirements
- **Data transfer costs** - Cross-region
  data transfer incurs additional charges
- **Network latency** - Queries accessing
  log groups in distant regions may experience higher latency
  For optimal performance and cost efficiency, create scheduled queries in the
  same region as your primary log groups.

**Alternative approach:** Use [CloudWatch Logs
centralization](CloudWatchLogs_Centralization.md "CloudWatchLogs_Centralization.md") to replicate log data from multiple accounts and regions
into a central monitoring account. This allows you to create scheduled queries in a
single region that access all your centralized logs, avoiding cross-region queries
and simplifying IAM permissions management.

## Schedule expressions and

timezone handling

The schedule you define determines when your query runs and how often it executes.
Choosing the right schedule expression affects when you receive results and how much
data you query. Understanding the expression types helps you choose between simplicity and precision.

Cron expressions provide precise control over timing, allowing you to specify exact
times, days of the week, or days of the month. Use cron expressions when you need
queries to run at specific business hours or align with operational schedules. In the console you can also scheduled queries using easy calendar options.

**Cron expressions**

Run queries at specific times. Format: `cron(minute hour
 day-of-month month day-of-week year)`. Examples:

- `cron(0 9 * * ? *)` - Every day at 9:00 AM
  UTC
- `cron(0 18 ? * MON-FRI *)` - Weekdays at 6:00 PM
  UTC
- `cron(0 0 1 * ? *)` - First day of every month at
  midnight UTC
- `cron(0 12 ? * SUN *)` - Every Sunday at noon UTC
- `cron(30 8 1 1 ? *)` - January 1st at 8:30 AM UTC

All scheduled queries run in UTC, regardless of your local timezone or where your
AWS resources are located. This is particularly important when you schedule
queries for business hours or time-sensitive analysis. For example, if your business
operates in US Eastern Time and you want a daily report at 9 AM ET, you need to
account for the UTC offset (14:00 UTC during daylight saving time, 13:00 UTC
otherwise). Plan your schedule expressions with UTC in mind to ensure queries run at
the intended times.

## Choosing a query

language

Scheduled queries support three different query languages, and your choice affects
both how you write queries and how easily your team can maintain them. The right
language depends on your analysis requirements and your team's existing skills.

If you are primarily filtering and aggregating log data, CloudWatch Logs Insights Query Language
offers the most straightforward syntax. For complex data transformations where you
need to reshape or enrich data through multiple steps, PPL's pipeline approach makes
the logic easier to follow. When you need to perform joins or complex aggregations
similar to database operations, SQL provides familiar syntax that
database-experienced teams can adopt quickly.

**CloudWatch Logs Insights Query Language (CWLI)**

Purpose-built for log analysis with intuitive syntax. Best for:

- Text-based log analysis and filtering
- Time-series aggregations and statistics
- Teams new to log analysis

**OpenSearch Service Piped Processing Language (PPL)**

Pipeline-based query language with powerful data transformation
capabilities. Best for:

- Complex data transformations and enrichment
- Multi-step data processing workflows
- Teams familiar with pipeline-based processing

**OpenSearch Service Structured Query Language (SQL)**

Standard SQL syntax for familiar database-style queries. Best
for:

- Complex joins and aggregations
- Business intelligence and reporting
- Teams with strong SQL experience

## Destination selection and use

cases

Where you send query results determines what you can do with them. This choice
shapes your entire downstream workflow—whether you are building long-term analytics,
triggering automated responses, or both. Understanding the strengths of each
destination type helps you design the right architecture for your use case.

Amazon S3 destinations are optimized for storage and batch processing. When you need to
keep query results for months or years, analyze trends over time, or feed data into
analytics platforms, Amazon S3 provides cost-effective storage with unlimited retention.
EventBridge destinations are optimized for real-time automation. When query results should
trigger immediate actions—like sending alerts, starting workflows, or updating
systems—EventBridge delivers results as events that your applications can respond to
instantly. By default all query completion events are automatically sent as events to the default event bus, enabling integration with downstream processing systems, Lambda functions, or other event-driven architectures. Results are only published to destinations when query is executed successfully.

**Amazon S3 destinations**

Store query results as JSON files for long-term retention and batch
processing. Best for:

- Historical analysis and data archiving
- Integration with data lakes and analytics platforms
- Compliance and audit requirements
- Cost-effective storage of large result sets

**EventBridge destinations**

Send query results as events for real-time processing and automation. You can retrieve query results using the queryId sent in the event upto 30 days only as we store results for 30 days.
Best for:

- Triggering automated responses to query results
- Integration with serverless workflows and Lambda
  functions
- Real-time alerting and notification systems
- Event-driven architectures and microservices

## Query result format and

structure

For Amazon S3 destinations - Query results are delivered in JSON format with the same structure as the GetQueryResults API response. For Amazon EventBridge understanding the format of scheduled query results helps you design downstream
processing and integration workflows.

Query results are delivered in JSON format with the following structure:

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
        "queryString": "fields @timestamp, @message, @logStream, @log\n| sort @timestamp desc\n| limit 10000",
        "logGroupIdentifiers": [
            "/aws/lambda/my-function"
        ],
        "status": "Complete",
        "startTime": 1763465460,
        "statistics": {
            "recordsMatched": 0,
            "recordsScanned": 0,
            "estimatedRecordsSkipped": 0,
            "bytesScanned": 0,
            "estimatedBytesSkipped": 0,
            "logGroupsScanned": 1
        }
    }
}
```

Key elements include:

- `statistics` - Query performance metrics including records matched, scanned, bytes processed, and estimated skipped data
- `startTime` - When the query execution started (Unix timestamp)
- `queryString` - The actual query that was executed
- `queryId` - Query id of the query using which results can be retrieved
- `logGroupIdentifiers` - List of log groups that were queried
- `status` - Query execution status (Complete, Failed, etc.)
