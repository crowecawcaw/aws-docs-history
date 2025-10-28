# Recommendations for using direct queries

in Amazon OpenSearch Service

This page provides recommendations for using Amazon OpenSearch Service direct queries to analyze data
from CloudWatch Logs, Amazon S3, and Amazon Security Lake. These best practices help you optimize performance and
ensure efficient querying without the need for data ingestion or duplication.

###### Topics

- [General recommendations](#general-recommendations "#general-recommendations")
- [Amazon S3 recommendations](#s3-recommendations "#s3-recommendations")
- [CloudWatch Logs Recommendations](#cloudwatch-logs-recommendations "#cloudwatch-logs-recommendations")
- [Security Lake recommendations](#security-lake-recommendations "#security-lake-recommendations")

## General recommendations

We recommend you do the following when using direct query:

- Use the `COALESCE SQL` function to handle missing columns
  and ensure results are returned.

- Use limits on your queries to ensure you aren't pulling too much data
  back.
- If you plan to analyze the same dataset many times, create an indexed view
  to fully ingest and index the data into OpenSearch and drop it when you have
  completed the analysis.
- Drop acceleration jobs and indexes when they're no longer needed.
- Queries containing field names that are identical but differ only in case
  (such as `field1` and `FIELD1`) are not
  supported.

For example, the following queries are not supported:

```
Select AWSAccountId, AwsAccountId from LogGroup
Select a.@LogStream, b.@logStream from Table A INNER Join Table B ona.id = b.id
```

However, the following query is supported because the field name
(@logStream) is identical in both log groups:

```
Select a.@logStream, b.@logStream from Table A INNER Join Table B on a.id = b.id
```

- Functions and expressions must operate on field names and be part of a
  `SELECT` statement with a log group specified in the
  `FROM` clause.

For example, this query is not supported:

```
SELECT cos(10) FROM LogGroup
```

This query is supported:

```
SELECT cos(field1) FROM LogGroup
```

## Amazon S3 recommendations

If you’re using Amazon OpenSearch Service to direct query data in Amazon S3, we also recommend the
following:

- Ingest data into Amazon S3 using partition formats of year, month, day, hour to
  speed up queries.
- When you build skipping indexes, use Bloom filters for fields with high
  cardinality and min/max indexes for fields with large value ranges. For
  high-cardinality fields, consider using a value-based approach to improve
  query efficiency.
- Use Index State Management to maintain storage for materialized views and
  covering indexes.

## CloudWatch Logs Recommendations

If you’re using Amazon OpenSearch Service to direct query data in CloudWatch Logs, we also recommend the
following:

- When searching multiple log groups in one query, use the appropriate
  syntax. For more information, see [Multi-log group functions](supported-directquery-sql.md#multi-log-queries "supported-directquery-sql.md#multi-log-queries").
- When using SQL or PPL commands, enclose certain fields in backticks to
  successfully query them. Backticks are needed for fields with special
  characters (non-alphabetic and non-numeric). For example, enclose
  `@message`, `Operation.Export,` and
  `Test::Field` in backticks. You don't need to enclose columns
  with purely alphabetic names in backticks.

Example query with simple fields:

```
SELECT SessionToken, Operation, StartTime  FROM `LogGroup-A`
LIMIT 1000;
```

Similar query with backticks appended:

```
SELECT `@SessionToken`, `@Operation`, `@StartTime` FROM `LogGroup-A`
LIMIT 1000;
```

## Security Lake recommendations

If you’re using Amazon OpenSearch Service to direct query data in Security Lake, we also recommend the
following:

- Check your Security Lake status and ensure that it's running smoothly without any
  problems. For detailed troubleshooting steps, see [Troubleshooting data lake status](../../../security-lake/latest/userguide/securitylake-data-lake-troubleshoot.md "../../../security-lake/latest/userguide/securitylake-data-lake-troubleshoot.md") in the Amazon Security Lake User
  Guide.
- Verify your query access:
  - If you're querying Security Lake from a different account than the Security Lake
    delegated administrator account, [set up a subscriber with query access in Security Lake](../../../security-lake/latest/userguide/subscriber-query-access.md "../../../security-lake/latest/userguide/subscriber-query-access.md").
  - If you're querying Security Lake from the same account, check for any
    messages in Security Lake about registering your managed S3 buckets with
    LakeFormation.

- Explore the query templates and pre-built dashboards to jumpstart your
  analysis.
- Familiarize yourself with Open Cybersecurity Schema Framework (OCSF) and
  Security Lake:
  - Review schema mapping examples for AWS sources in the [OCSF GitHub repository](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/CloudTrail "https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/CloudTrail")
  - Learn how to query Security Lake effectively by visiting [Security Lake queries for AWS source version 2 (OCSF
    1.1.0)](../../../security-lake/latest/userguide/subscriber-query-examples2.md "../../../security-lake/latest/userguide/subscriber-query-examples2.md")
  - Improve query performance by using partitions:
    `accountid`, `region`, and
    `time_dt`

- Get comfortable with SQL syntax, which Security Lake supports for querying. For
  more information, see [Supported OpenSearch SQL commands and
  functions](supported-directquery-sql.md "supported-directquery-sql.md").
