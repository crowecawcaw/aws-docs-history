# Viewing metrics in the Amazon RDS console

Amazon RDS integrates with Amazon CloudWatch to display a variety of Aurora DB cluster metrics in the RDS console. Some
metrics are apply at the cluster level, whereas others apply at the instance level. For descriptions of
the instance-level and
cluster-level metrics, see [Metrics reference for Amazon Aurora](metrics-reference.md "metrics-reference.md").

For your Aurora DB cluster, the following categories of metrics are monitored:

- **CloudWatch** – Shows the Amazon CloudWatch metrics for Aurora
  that you can access in the RDS console. You can also access
  these metrics in the CloudWatch console. Each metric includes a graph that shows the metric monitored over
  a specific time span. For a list of CloudWatch metrics,

see [Amazon CloudWatch metrics for Amazon Aurora](Aurora.AuroraMonitoring.Metrics.md "Aurora.AuroraMonitoring.Metrics.md").

- **Enhanced monitoring** – Shows a summary of
  operating-system metrics when your Aurora DB
  cluster has
  turned on Enhanced Monitoring. RDS delivers the metrics from Enhanced Monitoring to
  your Amazon CloudWatch Logs account. Each OS metric includes a graph showing
  the metric monitored over a specific time span. For an overview, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.OS.md "USER_Monitoring.OS.md"). For a list of
  Enhanced Monitoring metrics, see [OS metrics in Enhanced Monitoring](USER_Monitoring-Available-OS-Metrics.md "USER_Monitoring-Available-OS-Metrics.md").
- **OS Process list** – Shows details for each process running in your DB cluster.
- **Database Insights** – Opens the Amazon CloudWatch Database Insights dashboard
  for a DB instance in your Aurora DB cluster.
  Database Insights isn't supported at the cluster level.
  For an overview, see [Monitoring DB load with Amazon CloudWatch Database Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md"). For a list of metrics, see [Amazon CloudWatch metrics for Amazon RDS Performance Insights](USER_PerfInsights.Cloudwatch.md "USER_PerfInsights.Cloudwatch.md").
  Amazon CloudWatch Database Insights provides a consolidated view of database load and CloudWatch metrics for your
  DB cluster.
  For more information, see [Monitoring Amazon Aurora databases with CloudWatch Database Insights](USER_DatabaseInsights.md "USER_DatabaseInsights.md").
