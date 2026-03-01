# Using anomaly detection in CloudWatch Logs Insights

In addition to creating log anomaly detectors for continuous monitoring, you can also
use the `anomaly` command in CloudWatch Logs Insights queries to identify unusual
patterns in your log data on-demand. This command extends the existing
`pattern` functionality and uses machine learning to detect five types of
anomalies including pattern frequency changes, new patterns, and token
variations.

The `anomaly` command is particularly useful for:

- Ad-hoc analysis of historical log data to identify unusual patterns
- Investigating specific time periods for anomalous behavior
- Monitoring applications like Lambda functions for execution issues
  For more information about using the `anomaly` command in your queries, see
  [anomaly](CWL_QuerySyntax-Anomaly.md "CWL_QuerySyntax-Anomaly.md").

This query-based anomaly detection complements the continuous anomaly detectors
described in the following sections, giving you both real-time monitoring and on-demand
analysis capabilities.
