# Viewing metrics in the Amazon RDS console

Amazon RDS integrates with Amazon CloudWatch to display a variety of RDS DB instance metrics in the RDS console. For descriptions of
these metrics, see [Metrics reference for Amazon RDS](metrics-reference.md "metrics-reference.md").

For your DB instance, the following categories of metrics are monitored:

- **CloudWatch** – Shows the Amazon CloudWatch metrics for
  RDS that you can access in the RDS console. You can also access
  these metrics in the CloudWatch console. Each metric includes a graph that shows the metric monitored over
  a specific time span. For a list of CloudWatch metrics,

see [Amazon CloudWatch metrics for Amazon RDS](rds-metrics.md "rds-metrics.md").

- **Enhanced monitoring** – Shows a summary of
  operating-system metrics when your RDS DB instance has
  turned on Enhanced Monitoring. RDS delivers the metrics from Enhanced Monitoring to
  your Amazon CloudWatch Logs account. Each OS metric includes a graph showing
  the metric monitored over a specific time span. For an overview, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.md "USER_Monitoring.md"). For a list of
  Enhanced Monitoring metrics, see [OS metrics in Enhanced Monitoring](USER_Monitoring-Available-OS-Metrics.md "USER_Monitoring-Available-OS-Metrics.md").
- **OS Process list** – Shows details for each process running in your DB instance.
- **Performance Insights** – Opens the Amazon RDS Performance Insights dashboard
  for a DB instance.
  For an overview of Performance Insights, see [Monitoring DB load with Performance Insights on Amazon RDS](USER_PerfInsights.md "USER_PerfInsights.md"). For a list of Performance Insights metrics, see [Amazon CloudWatch metrics for Amazon RDS Performance Insights](USER_PerfInsights.md "USER_PerfInsights.md").
  Amazon RDS now provides a consolidated view of Performance Insights and CloudWatch metrics in the Performance Insights dashboard.
  Performance Insights must be turned on for your DB instance to use this view. You can choose the new monitoring
  view in the **Monitoring** tab or **Performance Insights** in the
  navigation pane. To view the instructions for choosing this view, see [Viewing combined metrics with the Performance Insights dashboard](Viewing_Unifiedmetrics.md "Viewing_Unifiedmetrics.md").
