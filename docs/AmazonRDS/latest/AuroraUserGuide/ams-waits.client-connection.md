# io/socket/sql/client\_connection

The `io/socket/sql/client_connection` event occurs
when a thread is in the process of handling a new connection.

###### Topics

- [Supported engine versions](#ams-waits.client-connection.context.supported "#ams-waits.client-connection.context.supported")
- [Context](#ams-waits.client-connection.context "#ams-waits.client-connection.context")
- [Likely causes of increased waits](#ams-waits.client-connection.causes "#ams-waits.client-connection.causes")
- [Actions](#ams-waits.client-connection.actions "#ams-waits.client-connection.actions")

## Supported engine versions

This wait event information is supported for the following engine versions:

- Aurora MySQL versions 2 and 3

## Context

The event `io/socket/sql/client_connection` indicates that mysqld is busy creating threads
to handle incoming new client connections. In this scenario, the processing of servicing new client connection
requests slows down while connections wait for the thread to be assigned. For more information, see [MySQL server (mysqld)](AuroraMySQL.Managing.Tuning.concepts.md#AuroraMySQL.Managing.Tuning.concepts.processes.mysqld "AuroraMySQL.Managing.Tuning.concepts.md#AuroraMySQL.Managing.Tuning.concepts.processes.mysqld").

## Likely causes of increased waits

When this event appears more than normal, possibly indicating a performance problem, typical causes
include the following:

- There is a sudden increase in new user connections from the application to your Amazon RDS instance.
- Your DB instance can't process new connections because the network, CPU, or memory is being
  throttled.

## Actions

If `io/socket/sql/client_connection` dominates database activity,
it doesn't necessarily indicate a performance problem. In a database that isn't idle, a
wait event is always on top. Act only when performance degrades. We recommend different
actions depending on the causes of your wait event.

###### Topics

- [Identify the problematic sessions and queries](#ams-waits.client-connection.actions.identify-queries "#ams-waits.client-connection.actions.identify-queries")
- [Follow best practices for connection management](#ams-waits.client-connection.actions.manage-connections "#ams-waits.client-connection.actions.manage-connections")
- [Scale up your instance if resources are being throttled](#ams-waits.client-connection.upgrade "#ams-waits.client-connection.upgrade")
- [Check the top hosts and top users](#ams-waits.client-connection.top-hosts "#ams-waits.client-connection.top-hosts")
- [Query the performance\_schema tables](#ams-waits.client-connection.perf-schema "#ams-waits.client-connection.perf-schema")
- [Check the thread states of your queries](#ams-waits.client-connection.thread-states "#ams-waits.client-connection.thread-states")
- [Audit your requests and queries](#ams-waits.client-connection.auditing "#ams-waits.client-connection.auditing")
- [Pool your database connections](#ams-waits.client-connection.pooling "#ams-waits.client-connection.pooling")

### Identify the problematic sessions and queries

If your DB instance is experiencing a bottleneck, your first task is to find the sessions and queries that
cause it. For a useful blog post, see [Analyze Amazon Aurora
MySQL Workloads with Performance Insights](https://aws.amazon.com/blogs/database/analyze-amazon-aurora-mysql-workloads-with-performance-insights/ "https://aws.amazon.com/blogs/database/analyze-amazon-aurora-mysql-workloads-with-performance-insights/").

###### To identify sessions and queries causing a bottleneck

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Performance Insights**.
3. Choose your DB instance.
4. In **Database load**, choose **Slice by wait**.
5. Choose the **Top SQL** tab.

The queries listed first are causing the highest load on the database.

### Follow best practices for connection management

To manage your connections, consider the following strategies:

- Use connection pooling.

You can gradually increase the number of connections as required. For more
information, see the whitepaper [Amazon Aurora MySQL Database Administrator’s Handbook](https://d1.awsstatic.com/whitepapers/RDS/amazon-aurora-mysql-database-administrator-handbook.pdf "https://d1.awsstatic.com/whitepapers/RDS/amazon-aurora-mysql-database-administrator-handbook.pdf").

- Use a reader node to redistribute read-only traffic.

For more information, see [Aurora Replicas](Aurora.Replication.md#Aurora.Replication.Replicas "Aurora.Replication.md#Aurora.Replication.Replicas") and [Amazon Aurora endpoint connections](Aurora.Overview.Endpoints.md "Aurora.Overview.Endpoints.md").

### Scale up your instance if resources are being throttled

Look for examples of throttling in the following resources:

- CPU

Check your Amazon CloudWatch metrics for high CPU usage.

- Network

Check for an increase in the value of the CloudWatch metrics `network
 receive throughput` and `network transmit throughput`.
If your instance has reached the network bandwidth limit for your instance
class, consider scaling up your RDS instance to a higher instance class
type. For more information, see [Amazon AuroraDB instance classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

- Freeable memory

Check for a drop in the CloudWatch metric `FreeableMemory`. Also,
consider turning on Enhanced Monitoring. For more information, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.OS.md "USER_Monitoring.OS.md").

### Check the top hosts and top users

Use Performance Insights to check the top hosts and top users. For more information, see [Database Insights](USER_DatabaseInsights.md "USER_DatabaseInsights.md").

### Query the performance\_schema tables

To get an accurate count of the current and total connections, query the `performance_schema`
tables. With this technique, you identify the source user or host that is responsible for creating a high
number of connections. For example, query the `performance_schema` tables as follows.

```
SELECT * FROM performance_schema.accounts;
SELECT * FROM performance_schema.users;
SELECT * FROM performance_schema.hosts;
```

### Check the thread states of your queries

If your performance issue is ongoing, check the thread states of your queries. In the `mysql`
client, issue the following command.

```
show processlist;
```

### Audit your requests and queries

To check the nature of the requests and queries from user accounts, use AuroraAurora MySQL Advanced Auditing.
To learn how to turn on auditing, see [Using Advanced Auditing with an Amazon Aurora MySQL DB cluster](AuroraMySQL.Auditing.md "AuroraMySQL.Auditing.md").

### Pool your database connections

Consider using Amazon RDS Proxy for connection management. By using RDS Proxy, you can allow your applications
to pool and share database connections to improve their ability to scale. RDS Proxy makes applications more
resilient to database failures by automatically connecting to a standby DB instance while preserving
application connections. For more information, see [Amazon RDS Proxy for Aurora](rds-proxy.md "rds-proxy.md").
