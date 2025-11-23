# Automating log analysis with scheduled queries

Scheduled queries enable you to automate the execution of CloudWatch Logs Insights queries on a regular
schedule. Instead of manually running queries to analyze your log data, you can configure
scheduled queries to run automatically and deliver results to destinations such as Amazon S3
buckets or Amazon EventBridge event buses. This automation is ideal for generating regular reports,
monitoring trends, or triggering downstream processes based on log analysis results.

Scheduled queries support all three query languages available in CloudWatch Logs Insights:

- [Logs Insights query
  language (Logs Insights QL)](CWL_AnalyzeLogData_LogsInsights.md "CWL_AnalyzeLogData_LogsInsights.md")
- [OpenSearch Service Piped Processing Language
  (PPL)](CWL_AnalyzeLogData_PPL.md "CWL_AnalyzeLogData_PPL.md")
- [OpenSearch Service Structured Query Language
  (SQL)](CWL_AnalyzeLogData_SQL.md "CWL_AnalyzeLogData_SQL.md")

###### Contents

- [Understanding scheduled queries
  concepts](scheduled-queries-concepts.md "scheduled-queries-concepts.md")
- [Schedule expression
  reference](scheduled-queries-schedule-reference.md "scheduled-queries-schedule-reference.md")
- [Best practices](scheduled-queries-best-practices.md "scheduled-queries-best-practices.md")
- [Getting started with scheduled
  queries](scheduled-queries-getting-started.md "scheduled-queries-getting-started.md")
- [Configuring S3 destinations for
  scheduled queries](scheduled-queries-s3-destination.md "scheduled-queries-s3-destination.md")
- [Troubleshooting scheduled
  queries](scheduled-queries-troubleshooting.md "scheduled-queries-troubleshooting.md")
