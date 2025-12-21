# How DevOps Guru for RDS works

DevOps Guru for RDS collects metric data, analyzes it, and then publishes anomalies in the dashboard.

###### Topics

- [Data collection and analysis](#working-with-rds.overview.how-it-works.collects "#working-with-rds.overview.how-it-works.collects")
- [Anomaly publication](#working-with-rds.overview.how-it-works.publishing "#working-with-rds.overview.how-it-works.publishing")

## Data collection and analysis

DevOps Guru for RDS collects data about your Amazon RDS databases from Amazon RDS Performance
Insights. This feature monitors Amazon RDS DB instances, collects metrics, and makes
it possible for you to explore the metrics in a chart. The most important
performance metric is `DBLoad`. DevOps Guru for RDS consumes Performance
Insights metrics and analyzes them to detect anomalies. For more information
about Performance Insights, see [Monitoring DB
load with Performance Insights on Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md") in the
_Amazon Aurora User Guide_ or
[Monitoring DB
load with Performance Insights on Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md") in the
_Amazon RDS User Guide_.

DevOps Guru for RDS uses machine learning and advanced statistical analysis to analyze the data that it collects from Performance Insights. If
DevOps Guru for RDS finds performance issues, it proceeds to the next step.

## Anomaly publication

A database performance issue such as high DB load can degrade the quality of service for your database. When DevOps Guru
detects an issue in an RDS database, it publishes an insight in the dashboard. The insight contains an
anomaly for the resource **AWS/RDS**.

If Performance Insights is turned on for your instances, the anomaly contains a detailed analysis of the problem.
DevOps Guru for RDS also recommends that you perform an investigation or specific corrective action. For
example, the recommendation might be to investigate a specific high-load SQL statement, consider
increasing CPU capacity, or to close idle-in-transaction sessions.
