# Monitoring metrics in an Amazon Aurora cluster

Amazon Aurora uses a cluster of replicated database servers. Typically, monitoring an Aurora cluster requires checking
the health of multiple DB instances. The instances might have specialized roles, handling mostly write operations,
only read operations, or a combination. You also monitor the overall health of the cluster by measuring the
_replication lag_. This is the amount of time for changes made by one DB instance to be
available to the other instances.

###### Topics

- [Monitoring plan](#MonitoringOverview.plan "#MonitoringOverview.plan")
- [Performance baseline](#MonitoringOverview.baseline "#MonitoringOverview.baseline")
- [Performance guidelines](#MonitoringOverview.guidelines "#MonitoringOverview.guidelines")
- [Monitoring tools for Amazon Aurora](MonitoringOverview.md "MonitoringOverview.md")
- [Viewing cluster status](accessing-monitoring.md "accessing-monitoring.md")
- [Recommendations from Amazon Aurora](monitoring-recommendations.md "monitoring-recommendations.md")
- [Viewing metrics in the Amazon RDS console](USER_Monitoring.md "USER_Monitoring.md")
- [Viewing combined metrics with the Performance Insights dashboard](Viewing_Unifiedmetrics.md "Viewing_Unifiedmetrics.md")
- [Monitoring Amazon Aurora metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Monitoring Amazon Aurora databases with CloudWatch Database Insights](USER_DatabaseInsights.md "USER_DatabaseInsights.md")
- [Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md")
- [Analyzing Aurora performance anomalies with Amazon DevOps Guru for Amazon RDS](devops-guru-for-rds.md "devops-guru-for-rds.md")
- [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.md "USER_Monitoring.md")
- [Metrics reference for Amazon Aurora](metrics-reference.md "metrics-reference.md")

## Monitoring plan

Before you start monitoring Amazon Aurora, create a monitoring plan. This plan should answer the following questions:

- What are your monitoring goals?
- Which resources will you monitor?
- How often will you monitor these resources?
- Which monitoring tools will you use?
- Who will perform the monitoring tasks?
- Whom should be notified when something goes wrong?

## Performance baseline

To achieve your monitoring goals, you need to establish a baseline. To do this, measure performance under
different load conditions at various times in your Amazon Aurora environment. You can monitor metrics such as the following:

- Network throughput
- Client connections
- I/O for read, write, or metadata operations
- Burst credit balances for your DB instances

We recommend that you store historical performance data for Amazon Aurora. Using the stored data, you can compare current performance against
past trends. You can also distinguish normal performance patterns from anomalies, and devise techniques to
address issues.

## Performance guidelines

In general, acceptable values for performance metrics depend on what your application is doing relative to your
baseline. Investigate consistent or trending variances from your baseline. The following metrics are often the
source of performance issues:

- **High CPU or RAM consumption** – High values for CPU or RAM
  consumption might be appropriate, if they're in keeping with your goals for your application (like
  throughput or concurrency) and are expected.
- **Disk space consumption** – Investigate disk space consumption if
  space used is consistently at or above 85 percent of the total disk space. See if it is possible to
  delete data from the instance or archive data to a different system to free up space.
- **Network traffic** – For network traffic, talk with your system
  administrator to understand what expected throughput is for your domain network and internet connection.
  Investigate network traffic if throughput is consistently lower than expected.
- **Database connections** – If you see high numbers of user
  connections and also decreases in instance performance and response time, consider constraining database
  connections. The best number of user connections for your DB instance varies based on your instance class
  and the complexity of the operations being performed. To determine the number of database connections,
  associate your DB instance with a parameter group where the `User Connections` parameter is
  set to a value other than 0 (unlimited). You can either use an existing parameter group or create a new
  one. For more information, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
- **IOPS metrics** – The expected values for IOPS metrics depend on
  disk specification and server configuration, so use your baseline to know what is typical. Investigate if
  values are consistently different than your baseline. For best IOPS performance, make sure that your
  typical working set fits into memory to minimize read and write operations.

When performance falls outside your established baseline, you might need to make changes to optimize your
database availability for your workload. For example, you might need to change the instance class of your DB
instance. Or you might need to change the number of DB instances and read replicas that are available for
clients.
