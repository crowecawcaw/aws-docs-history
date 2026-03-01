# SQL Server Agent and MySQL Agent

This topic provides reference information about the differences between SQL Server Agent functionality in Microsoft SQL Server 2019 and comparable features in Amazon Aurora MySQL. You can understand the limitations and alternatives available when migrating from SQL Server to Aurora MySQL, particularly regarding scheduling, automation, and alerting capabilities.

| Feature compatibility    | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                 | Key differences                                                                                                                                                                                                                                 |
| ------------------------ | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No feature compatibility | No automation                      | [SQL Server Agent](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.agent "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.agent") | For more information, see [Alerting](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md") and [Maintenance Plans](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md"). |

## SQL Server Usage

SQL Server Agent provides two main functions: scheduling automated maintenance and backup jobs, and for alerting.

###### Note

Other SQL built-in frameworks such as replication, also use SQL Server Agent jobs under the covers.

Maintenance plans, backups and alerting are covered in separate sections.

For more information, see [SQL Server Agent](https://docs.microsoft.com/en-us/sql/ssms/agent/sql-server-agent?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/ssms/agent/sql-server-agent?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) does provide a native, in-database scheduler. It is limited to the cluster scope and can’t be used to manage multiple clusters. There are no native alerting capabilities in Aurora MySQL similar to SQL Server Agent alerts.

Although Amazon Relational Database Service (Amazon RDS) doesn’t currently provide an external scheduling agent like SQL Server Agent, CloudWatch Events provides the ability to specify a cron-like schedule to run Lambda functions. This approach requires writing custom code in C#, NodeJS, Java, or Python. Additionally, any task that runs longer than five minutes will not work due to the AWS Lambda time out limit. For example, this limit may pose a challenge for index rebuild operations. Other options include:

1. Running an SQL Server for the sole purpose of using the Agent.
2. Using a t2 or container to schedule your code (C#, NodeJS, Java, Python) with Cron. A t2.nano is simple to deploy and can run tasks indefinitely at a very modest cost. For most scheduling applications, the low resources shouldn’t be an issue.

### Aurora MySQL Database Events

Aurora MySQL also provides a native, in-database scheduling framework that can be used to trigger scheduled operations including maintenance tasks.

Events are running by a dedicated thread, which can be seen in the process list. The global `event_scheduler` must be turned on explicitly from its default state of `OFF` for the event thread to run. Event errors are written to the error log. Event metadata can be viewed using the `INFORMATION_SCHEMA.EVENTS` view.

### Syntax

```
CREATE EVENT <Event Name>
    ON SCHEDULE <Schedule>
    [ON COMPLETION [NOT] PRESERVE][ENABLE | DISABLE | DISABLE ON SLAVE]
    [COMMENT 'string']
    DO <Event Body>;

<Schedule>:
    AT <Time Stamp> [+ INTERVAL <Interval>] ...
    | EVERY <Interval>
    [STARTS <Time Stamp> [+ INTERVAL <Interval>] ...]
    [ENDS <Time Stamp> [+ INTERVAL <Interval>] ...]

<Interval>:
    quantity {YEAR | QUARTER | MONTH | DAY | HOUR | MINUTE |
        WEEK | SECOND | YEAR_MONTH | DAY_HOUR | DAY_MINUTE |
        DAY_SECOND | HOUR_MINUTE | HOUR_SECOND | MINUTE_SECOND}
```

### Examples

Create an event to collect login data statistics that runs once five hours after creation.

```
CREATE EVENT Update_T1_In_5_Hours
    ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 5 HOUR
    DO
        INSERT INTO LoginStatistics
        SELECT UserID,
            COUNT(*) AS LoginAttempts
        FROM Logins AS L
        GROUP BY UserID
        WHERE LoginData = '20180502';
```

Create an event to run every hour and delete session information older than four hours.

```
CREATE EVENT Clear_Old_Sessions
    ON SCHEDULE
        EVERY 4 HOUR
    DO
        DELETE FROM Sessions
        WHERE LastCommandTime < CURRENT_TIMESTAMP - INTERVAL 4 HOUR;
```

Schedule weekly index rebuilds and pass parameters.

```
CREATE EVENT Rebuild_Indexes
    ON SCHEDULE
        EVERY 1 WEEK
    DO
        CALL IndexRebuildProcedure(1, 80)
```

## Summary

For more information, see [CREATE EVENT Statement](https://dev.mysql.com/doc/refman/5.7/en/create-event.html "https://dev.mysql.com/doc/refman/5.7/en/create-event.html") and [Event Scheduler Configuration](https://dev.mysql.com/doc/refman/5.7/en/events-configuration.html "https://dev.mysql.com/doc/refman/5.7/en/events-configuration.html") in the _MySQL documentation_; [Amazon CloudWatch](https://aws.amazon.com/cloudwatch "https://aws.amazon.com/cloudwatch") and [AWS Lambda](https://aws.amazon.com/lambda "https://aws.amazon.com/lambda").
