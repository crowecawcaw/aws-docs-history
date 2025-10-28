# Analyzing log data with CloudWatch Logs Insights

With CloudWatch Logs Insights, you can interactively search and analyze your log data in Amazon CloudWatch Logs. You can
perform queries to help you more efficiently and effectively respond to operational issues.
If an issue occurs, you can use CloudWatch Logs Insights to identify potential causes and validate deployed
fixes.

CloudWatch Logs Insights supports three query languages that you can use for your queries:

- A purpose-built **Logs Insights query language (Logs Insights
  QL)** with a few simple but powerful commands.
- **OpenSearch Service Piped Processing Language (PPL)**. OpenSearch PPL enables
  you to analyze your logs using a set of commands delimited by pipes (|).

With OpenSearch PPL you can retrieve, query, and analyze data by using commands
that are piped together, making it easier to understand and compose complex queries.
The syntax enables the chaining of commands to transform and process data. With PPL,
you can filter and aggregate data, and use a rich set of math, string, date,
conditional and other functions for analysis.

- **OpenSearch Service Structured Query Language (SQL)**. With OpenSearch SQL
  queries, you can analyze your logs in a declarative manner. You can use commands
  such as SELECT, FROM, WHERE, GROUP BY, HAVING, and various other commands and
  functions available in SQL. You can execute JOINs across log groups, correlate data
  across logs using sub-queries, and use the rich set of JSON, Mathematical, String,
  Conditional and other SQL functions to perform powerful analysis on logs.

When you use either SQL or PPL commands, make sure to enclose fields with special
characters (non-alphabetic and non-numeric) in backticks to successfully query them.
For example, enclose `@message`, `Operation.Export`, and
`Test::Field` in backticks. You don't need to enclose fields with
purely alphabetical names in backticks.
CloudWatch Logs Insights offers the following features that are available for use with any of the query
languages.

- Automatic [discovery of log fields](CWL_AnalyzeLogData-discoverable-fields.md "CWL_AnalyzeLogData-discoverable-fields.md") in logs from AWS
  services such as Amazon Route 53, AWS Lambda, AWS CloudTrail, and Amazon VPC, and any application or
  custom log that emits log events as JSON.
- Creating [field
  indexes](CloudWatchLogs-Field-Indexing.md "CloudWatchLogs-Field-Indexing.md") to reduce costs and speed results, especially for
  queries of large number of log groups or log events. After creating field indexes of
  fields that are common in your log events, you can use them in in a query. The query
  skips processing log events that are known to not include the indexed field, and
  processes less data.

###### Note

The `filterIndex` command is available only in Logs Insights
QL.

- [Detection and analysis of
  patterns](CWL_AnalyzeLogData_Patterns.md "CWL_AnalyzeLogData_Patterns.md") in your log events. A pattern is a shared text
  structure that recurs among your log fields. When you view the results of a query,
  you can choose the **Patterns** tab to see the patterns that CloudWatch Logs
  found based on a sample of your results.
- [Saving
  queries](CWL_Insights-Saving-Queries.md "CWL_Insights-Saving-Queries.md"), seeing your query history, and re-running saved
  queries. This can help you run complex queries when you need, without having to
  re-create them each time that you want to run them.
- [Adding queries to
  dashboards](CWL_ExportQueryResults.md "CWL_ExportQueryResults.md").
- [Encrypting query
  results with AWS Key Management Service](CloudWatchLogs-Insights-Query-Encrypt.md "CloudWatchLogs-Insights-Query-Encrypt.md").
- [Query generation using
  natural language](CloudWatchLogs-Insights-Query-Assist.md "CloudWatchLogs-Insights-Query-Assist.md") lets you use natural language to create CloudWatch Logs Insights queries.
  You can ask questions about or describe the data you're looking for, then the
  AI generates a query based on your prompt and provides a
  line-by-line explanation of how the query works.
  The following CloudWatch Logs Insights features are supported only when you use Logs Insights QL.

- Querying logs in the [Infrequent Access
  log class](CloudWatch_Logs_Log_Classes.md "CloudWatch_Logs_Log_Classes.md").
- [Comparison queries](CWL_AnalyzeLogData_Compare.md "CWL_AnalyzeLogData_Compare.md") that compare
  log events in a log group with log events from a previous time period.
- The [filterIndex
  command](CWL_QuerySyntax-FilterIndex.md "CWL_QuerySyntax-FilterIndex.md"), which forces the query to attempt to scan only
  log events that contain a _field index_ that you specify.

###### Important

CloudWatch Logs Insights can't access log events with timestamps that pre-date the creation time of the
log group.

If you are signed in to an account set up as a monitoring account in CloudWatch cross-account
observability, you can run CloudWatch Logs Insights queries on log groups in source accounts linked to
this monitoring account. You can run a query that queries multiple log groups located in
different accounts. For more information, see [CloudWatch cross-account observability](../monitoring/CloudWatch-Unified-Cross-Account.md "../monitoring/CloudWatch-Unified-Cross-Account.md").

When you create queries using Logs Insights QL, you can also use natural language to
create CloudWatch Logs Insights queries. To do so, ask questions about or describe the data you're looking
for. This AI-assisted capability generates a query based on your prompt and provides a
line-by-line explanation of how the query works. For more information, see [Use natural
language to generate and update CloudWatch Logs Insights queries](CloudWatchLogs-Insights-Query-Assist.md "CloudWatchLogs-Insights-Query-Assist.md").

Queries using any of the supported query languages time out after 60 minutes, if they have
not completed. Query results are available for seven days.

CloudWatch Logs Insights queries incur charges based on the amount of data that is queried,
regardless of query language. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

You can use CloudWatch Logs Insights to search log data that was sent to CloudWatch Logs on November 5, 2018 or
later.

###### Important

If your network security team doesn't allow the use of web sockets, you can't
currently access the CloudWatch Logs Insights portion of the CloudWatch console. You can use the CloudWatch Logs Insights query
capabilities using APIs. For more information, see [StartQuery](../../../AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.md") in the
_Amazon CloudWatch Logs API Reference_.

###### Contents

- [Supported query languages](CWL_AnalyzeLogData_Languages.md "CWL_AnalyzeLogData_Languages.md")
- [Use natural language to generate
  and update CloudWatch Logs Insights queries](CloudWatchLogs-Insights-Query-Assist.md "CloudWatchLogs-Insights-Query-Assist.md")
- [Supported logs and discovered
  fields](CWL_AnalyzeLogData-discoverable-fields.md "CWL_AnalyzeLogData-discoverable-fields.md")
- [Create field indexes to improve query
  performance and reduce scan volume](CloudWatchLogs-Field-Indexing.md "CloudWatchLogs-Field-Indexing.md")
- [Pattern analysis](CWL_AnalyzeLogData_Patterns.md "CWL_AnalyzeLogData_Patterns.md")
- [Save and re-run CloudWatch Logs Insights
  queries](CWL_Insights-Saving-Queries.md "CWL_Insights-Saving-Queries.md")
- [Add query to dashboard or export query
  results](CWL_ExportQueryResults.md "CWL_ExportQueryResults.md")
- [View running queries or query
  history](CloudWatchLogs-Insights-Query-History.md "CloudWatchLogs-Insights-Query-History.md")
- [Encrypt query results with
  AWS Key Management Service](CloudWatchLogs-Insights-Query-Encrypt.md "CloudWatchLogs-Insights-Query-Encrypt.md")
- [Generate a natural
  language summary from CloudWatch Logs Insights query results](CloudWatchLogs-Insights-Query-Results-Summary.md "CloudWatchLogs-Insights-Query-Results-Summary.md")
