# Generate a natural language summary from CloudWatch Logs Insights query results

Analyzing log data is crucial for understanding your applications' behavior, but
interpreting large volumes of log entries can be time-consuming. CloudWatch Logs Insights now offers a
natural language summarization capability that transforms complex query results into
clear, concise summaries. This capability helps you quickly identify issues and gain
actionable insights from your log data.

## How it works

CloudWatch Logs Insights can generate a human-readable summary from your query results using
Amazon Bedrock. The feature supports all CloudWatch Logs Insights query languages and provides clear,
actionable insights from your log data.

## Regional availability and data processing

###### Important

When you use this feature, your query results might be processed in a
different AWS Region. For example, if you run a query in US East (N.
Virginia), the summarization might occur in US West (Oregon).

The following table lists the possible processing AWS Region for the different
geographies in which the query results feature is available:

| Supported CloudWatch Logs geography | Possible Processing Region                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| United States (US)                  | US East (N. Virginia) Region<br>US East (Ohio) Region<br>US West (Oregon) Region                                                     |
| Europe                              | Europe (Frankfurt) Region<br>Europe (Ireland) Region<br>Europe (Paris) Region<br>Europe (Stockholm) Region<br>Europe (London) Region |
| Asia Pacific                        | US East (N. Virginia) Region<br>US East (Ohio) Region<br>US West (Oregon) Region                                                     |
| South America                       | US East (N. Virginia) Region<br>US East (Ohio) Region<br>US West (Oregon) Region                                                     |

## Getting started

###### To generate a natural language summary

1. Run your CloudWatch Logs Insights query.
2. After the query completes, select **Summarize
   results**.

## Permissions

You must have one of the following:

- `CloudWatchLogsFullAccess` permission
- `CloudWatchLogsReadOnlyAccess` permission
- Custom IAM policy including the
  `cloudwatch:GenerateQueryResultsSummary`,
  `logs:GetQueryResults`, `logs:DescribeQueries` and
  `logs:FilterLogEvents` actions

## Data privacy

Your query results are processed securely and aren't used to train or improve CloudWatch
Logs Insights or Amazon Bedrock. If you choose to provide feedback on the query results
summary using the feedback buttons, your feedback indicates your level of
satisfaction with the capability provided in CloudWatch Logs Insights.
