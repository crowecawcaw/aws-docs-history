

# Alerting features
<a name="chap-sql-server-aurora-mysql.management.alerting"></a>

This topic provides reference information about event notifications and alerts in SQL Server and Amazon Aurora MySQL. You can use event notifications to monitor and respond to various database events, performance conditions, and system changes.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-1.png)  | N/A | N/A | Use event notifications subscription with Amazon SNS. For more information, see [Using Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html) and [Amazon Simple Notification Service](https://aws.amazon.com/sns). | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.management.alerting.sqlserver"></a>

SQL Server provides SQL Server Agent to generate alerts. When running, SQL Server Agent constantly monitors SQL Server windows application log messages, performance counters, and Windows Management Instrumentation (WMI) objects. When a new error event is detected, the agent checks the MSDB database for configured alerts and runs the specified action.

You can define SQL Server Agent alerts for the following categories:
+ SQL Server events
+ SQL Server performance conditions
+ WMI events

For SQL Server events, the alert options include the following settings:
+  **Error number** — Alert when a specific error is logged.
+  **Severity level** — Alert when any error in the specified severity level is logged.
+  **Database** — Filter the database list for which the event will generate an alert.
+  **Event text** — Filter specific text in the event message.

**Note**  
SQL Server Agent is pre-configured with several high severity alerts. It is highly recommended to enable these alerts.

To generate an alert in response to a specific performance condition, specify the performance counter to be monitored, the threshold values for the alert, and the predicate for the alert to occur. The following list identifies the performance alert settings:
+  **Object** — The performance counter *category* or the monitoring area of performance.
+  **Counter** — A counter is a specific attribute value of the object.
+  **Instance** — Filter by SQL Server instance (multiple instances can share logs).
+  **Alert if counter and Value** — The threshold for the alert and the predicate. The threshold is a number. Predicates are *falls below*, *becomes equal to*, or *rises above the threshold*.

WMI events require the WMI namespace and the WMI Query Language (WQL) query for specific events.

Alerts can be assigned to specific operators with schedule limitations and multiple response types including:
+ Run an SQL Server Agent job.
+ Send email, net send command, or a pager notification.

You can configure alerts and responses with SQL Server Management Studio or with a set of system stored procedures.

### Examples
<a name="chap-sql-server-aurora-mysql.management.alerting.sqlserver.examples"></a>

Configure an alert for all errors with severity 20.

```
EXEC msdb.dbo.sp_add_alert
    @name = N'Severity 20 Error Alert',
    @severity = 20,
    @notification_message = N'A severity 20 Error has occurred. Initiating emergency procedure',
    @job_name = N'Error 20 emergency response';
```

For more information, see [Alerts](https://docs.microsoft.com/en-us/sql/ssms/agent/alerts?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.management.alerting.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) doesn’t support direct configuration of engine alerts.

Use the event notifications infrastructure to collect history logs or receive event notifications in near real-time.

 Amazon Relational Database Service (Amazon RDS) uses Amazon Simple Notification Service (Amazon SNS) to provide notifications for events. SNS can send notifications in any form supported by the region including email, text messages, or calls to HTTP endpoints for response automation.

Events are grouped into categories. You can only subscribe to event categories, not individual events. SNS sends notifications when any event in a category occurs.

You can subscribe to alerts for database instances, database clusters, database snapshots, database cluster snapshots, database security groups and database parameter groups. For example, a subscription to the backup category for a specific database instance sends notifications when backup related events occur on that instance.

A subscription to a configuration change category for a database security group sends notifications when the security group changes.

**Note**  
For Amazon Aurora, some events occur at the cluster rather than instance level. You will not receive those events if you subscribe to an Aurora DB instance.

SNS sends event notifications to the address specified when the subscription was created. Typically, administrators create several subscriptions. For example, one subscription to receive logging events and another to receive only critical events for a production environment requiring immediate responses.

You can turn off notifications without deleting a subscription by setting the `Enabled` radio button to `No` in the Amazon RDS console. Alternatively, use the Command Line Interface (CLI) or Amazon RDS API to change the `Enabled` setting.

Subscriptions are identified by the Amazon Resource Name (ARN) of an Amazon SNS topic. The Amazon RDS console creates ARNs when subscriptions are created. When using the CLI or API, make sure that you create the ARN using the Amazon SNS console or the Amazon SNS API.

### Examples
<a name="chap-sql-server-aurora-mysql.management.alerting.mysql.examples"></a>

The following walkthrough demonstrates how to create an event notification subscription:

1. Sign in to your AWS account, and choose **RDS**.

1. Choose **Events** on the left navigation pane. This screen that presents relevant Amazon RDS events occurs.

1. Choose **Event subscriptions** and then choose **Create event subscription**.

1. Enter the **Name of the subscription** and select a **Target of ARN** or **Email**. For email subscriptions, enter values for **Topic** name and **With these recipients**.

1. Select the event source, choose specific event categories to be monitored, and choose **Create**.

1. On the Amazon RDS dashboard, choose **Recent events**.

For more information, see [Using Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html) in the *Amazon Relational Database Service User Guide*.