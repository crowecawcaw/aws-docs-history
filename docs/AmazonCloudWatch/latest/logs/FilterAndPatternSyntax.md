# Filter pattern syntax for metric filters,

subscription filters, filter log events, and Live Tail

Filter patterns make up the syntax that metric filters, subscription filters, log events,
and Live Tail use to match terms in log events. Terms can be words, exact phrases, or
numeric values. Regular expressions (regex) can be used to create standalone filter
patterns, or can be incorporated with JSON and space-delimited filter patterns.

Create filter patterns with the terms that you want to match. Filter patterns only return
the log events that contain the terms you define. You can test filter patterns in the CloudWatch
console.

With CloudWatch Logs, you can use [metric filters](MonitoringLogData.md "MonitoringLogData.md") to
transform log data into actionable metrics, [subscription filters](SubscriptionFilters.md "SubscriptionFilters.md")
to route log events to other AWS services, [filter log
events](SearchDataFilterPattern.md "SearchDataFilterPattern.md") to search for log events, and [Live Tail](CloudWatchLogs_LiveTail.md "CloudWatchLogs_LiveTail.md") to
interactively view your logs in real-time as they are ingested.

###### Note

Filter patterns are designed for matching and filtering log events in real-time or for
specific operations. For interactive analysis and complex queries across your log data,
see [Analyzing log data with CloudWatch Logs Insights](AnalyzingLogData.md "AnalyzingLogData.md").

Here are common scenarios where you'll use these filter patterns:

- **Monitor application errors:** Use
  `ERROR` to track error occurrences across your application
  logs
- **Track API activity:** Use `{ $.eventType =
"UpdateTrail" }` to monitor specific CloudTrail events
- **Analyze web server issues:** Use `[ip, user,
 timestamp, request, status_code = 4*, bytes]` to find failed HTTP
  requests
  The following sections show the complete syntax for each pattern type, with examples for
  each use case.

###### Topics

- [Supported regular expressions (regex) syntax](regex-expressions.md "regex-expressions.md")
- [Using filter patterns to match
  terms in unstructured log events](matching-terms-unstructured-log-events.md "matching-terms-unstructured-log-events.md")
- [Using filter patterns to match terms in JSON log events](matching-terms-json-log-events.md "matching-terms-json-log-events.md")
