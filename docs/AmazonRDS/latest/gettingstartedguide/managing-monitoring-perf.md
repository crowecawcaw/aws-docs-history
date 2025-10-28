# Monitoring your Amazon RDS DB instance

Effective monitoring is essential to maintain the health and performance of your Amazon RDS DB
instance. AWS provides multiple tools and features to help you track key metrics, identify
potential issues, and optimize your database performance. This section introduces the primary
monitoring tools available in Amazon RDS and explains how they address different aspects of
database health and performance.

###### Topics

- [Monitoring with Amazon CloudWatch](#managing-cloudwatch "#managing-cloudwatch")
- [Monitoring with Amazon CloudWatch Logs](#managing-logs "#managing-logs")
- [Using Enhanced Monitoring](#managing-enhanced-monitoring "#managing-enhanced-monitoring")
- [Monitoring with Performance Insights](#managing-perf-insights "#managing-perf-insights")
- [Monitoring with Database Activity Streams](#managing-database-activity-streams "#managing-database-activity-streams")

## Monitoring with Amazon CloudWatch

Amazon CloudWatch collects and tracks metrics related to your DB instance, such as CPU
utilization, storage usage, and read/write operations. You can create alarms and dashboards
for real-time visibility into the status of your database.

**Key features**:

- Tracks over 50 default metrics for Amazon RDS DB instances.
- Provides historical data retention for trend analysis.
- Lets you set alarms to notify you when thresholds are breached.

**Use cases**:

- Monitor storage utilization to ensure adequate capacity.
- Detect unusual spikes in CPU or memory usage.
- Track connection counts to optimize application scaling.

For more information, see [Monitoring Amazon RDS metrics
with Amazon CloudWatch](../UserGuide/monitoring-cloudwatch.md "../UserGuide/monitoring-cloudwatch.md") in the _Amazon RDS User Guide_.

## Monitoring with Amazon CloudWatch Logs

Amazon RDS provides database logs that help you diagnose issues, analyze performance, and
track security-related events. You can access logs through the RDS console, the AWS CLI or the
RDS API and enable monitoring with Amazon CloudWatch Logs.

**Key features**:

- Supports error logs, slow query logs, and general logs for troubleshooting.
- Integrates with CloudWatch Logs for real-time analysis and alerting.
- Allows download and viewing of logs directly from the RDS console.

**Use cases**:

- Identify and troubleshoot database errors by analyzing error logs.
- Monitor slow query logs to optimize database performance.
- Track authentication attempts and security-related events in audit logs.

For more information, see [Monitoring Amazon RDS log
files](../UserGuide/USER_LogAccess.md "../UserGuide/USER_LogAccess.md") in the _Amazon RDS User Guide_.

## Using Enhanced Monitoring

Enhanced Monitoring provides detailed, real-time metrics about the operating system
running on your Amazon RDS DB instance. It collects these metrics at a granularity of up to one
second and give you deeper insight into the underlying hardware and software
performance.

**Key features**:

- Monitors over 50 OS-level metrics, including disk I/O, swap usage, and
  processes.
- Provides a more granular view of system resource usage compared to
  CloudWatch.
- RDS can export data to CloudWatch Logs for further analysis.

**Use cases**:

- Diagnose performance bottlenecks related to disk or memory.
- Gain insights into background processes consuming resources.
- Monitor the impact of maintenance tasks or application updates.

For setup instructions, see [Monitoring OS metrics with
Enhanced Monitoring](../UserGuide/USER_Monitoring.md "../UserGuide/USER_Monitoring.md") in the _Amazon RDS User Guide_.

## Monitoring with Performance Insights

Performance Insights is a tool for analyzing database performance and identifying
bottlenecks. It provides a visual interface that highlights resource consumption trends and
offers insights to optimize your queries and workloads.

**Key features**:

- Monitors database load in real time and over historical periods.
- Identifies top SQL queries consuming resources.
- Visualizes wait events to pinpoint delays in database processing.

**Use cases**:

- Optimize queries that consume excessive resources.
- Identify and address high latency due to locking or I/O issues.
- Plan capacity upgrades by analyzing historical load trends.

Most database engines support Performance Insights, but its availability varies by
engine and instance type. For more information, see [Monitoring DB load with
Performance Insights on Amazon RDS](../UserGuide/USER_PerfInsights.md "../UserGuide/USER_PerfInsights.md") in the _Amazon RDS User
Guide_.

## Monitoring with Database Activity Streams

Database Activity Streams provide a real-time stream of database activity, which helps
you monitor and audit database operations for security and compliance. You can integrate
activity streams with AWS services like Amazon CloudWatch and AWS Key Management Service (AWS KMS) for
encryption.

**Key features**:

- Captures database activity in near real-time for security monitoring.
- Encrypts all activity streams using AWS KMS.
- Integrates with Amazon CloudWatch and third-party security tools for analysis.

**Use cases**:

- Detect and investigate suspicious or unauthorized database activity.
- Maintain compliance by auditing changes and access patterns.
- Monitor SQL commands and administrative actions for security insights.

For more information, see [Monitoring Amazon RDS with Database
Activity Streams](../UserGuide/DBActivityStreams.md "../UserGuide/DBActivityStreams.md") in the _Amazon RDS User Guide_.
