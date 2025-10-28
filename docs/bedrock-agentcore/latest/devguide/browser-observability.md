# Observability and session replay

The AgentCore Browser provides the following observability features:

Session replay

You can replay browser sessions using the Amazon Bedrock AgentCore SDK to view
session recordings stored in Amazon S3. This feature enables you to review past browser
interactions for debugging, auditing, or training purposes. The recordings in S3 include
DOM change events, browser network activity, and console logs for comprehensive session
analysis.

Metrics

You can view browser session metrics in Amazon CloudWatch, including session counts,
durations, and error rates to monitor usage and performance.

###### Topics

- [CloudWatch Metrics for AgentCore Browser](browser-metrics.md "browser-metrics.md")
- [Browser session recording and replay](browser-session-replay.md "browser-session-replay.md")
