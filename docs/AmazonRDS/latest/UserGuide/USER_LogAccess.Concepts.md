# Amazon RDS for Oracle database log files

You can access Oracle alert logs, audit files, and trace files by using the Amazon RDS console
or API. For more information about viewing, downloading, and watching file-based database
logs, see [Monitoring Amazon RDS log files](USER_LogAccess.md "USER_LogAccess.md").

The Oracle audit files provided are the standard Oracle auditing files. Amazon RDS supports the
Oracle fine-grained auditing (FGA) feature. However, log access doesn't provide access
to FGA events that are stored in the `SYS.FGA_LOG$` table and that are accessible
through the `DBA_FGA_AUDIT_TRAIL` view.

The [`DescribeDBLogFiles`](../APIReference/API_DescribeDBLogFiles.md "../APIReference/API_DescribeDBLogFiles.md") API operation that
lists the Oracle log files that are available for a DB instance ignores the `MaxRecords` parameter and
returns up to 1,000 records. The call returns `LastWritten` as a POSIX date in milliseconds.

###### Topics

- [Retention schedule](#USER_LogAccess.Concepts.Oracle.Retention "#USER_LogAccess.Concepts.Oracle.Retention")
- [Working with
  Oracle trace files](#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles "#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles")
- [Publishing Oracle logs to
  Amazon CloudWatch Logs](#USER_LogAccess.Oracle.PublishtoCloudWatchLogs "#USER_LogAccess.Oracle.PublishtoCloudWatchLogs")
- [Accessing alert logs and
  listener logs](#USER_LogAccess.Concepts.Oracle.AlertLogAndListenerLog "#USER_LogAccess.Concepts.Oracle.AlertLogAndListenerLog")

## Retention schedule

The Oracle database engine might rotate log files if they get very large. To retain audit or trace files, download
them. If you store the files locally, you reduce your Amazon RDS storage costs and make more space available for your
data.

The following table shows the retention schedule for Oracle alert logs, audit files, and trace files on Amazon RDS.

| Log type      | Retention schedule                                                                                                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Alert logs    | The text alert log is rotated daily<br>with 30-day retention managed by Amazon RDS. The XML alert log is<br>retained for at least seven days. You can access this log by using<br>the `ALERTLOG` view. |
| Audit files   | The default retention period for audit<br>files is seven days. Amazon RDS might delete audit files older than seven<br>days.                                                                           |
| Trace files   | The default retention period for trace files is seven days. Amazon RDS might delete trace<br>files older than seven days.                                                                              |
| Listener logs | The default retention period for the<br>listener logs is seven days. Amazon RDS might delete listener logs older<br>than seven days.                                                                   |

###### Note

Audit files and trace files share the same retention configuration.

## Working with

Oracle trace files

Following, you can find descriptions of Amazon RDS procedures to create, refresh, access, and delete trace files.

###### Topics

- [Listing files](#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles.ViewingBackgroundDumpDest "#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles.ViewingBackgroundDumpDest")
- [Generating trace files and tracing a session](#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles.Generating "#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles.Generating")
- [Retrieving trace files](#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles.Retrieving "#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles.Retrieving")
- [Purging trace files](#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles.Purging "#USER_LogAccess.Concepts.Oracle.WorkingWithTracefiles.Purging")

### Listing files

You can use either of two procedures to allow access to any file in the
`background_dump_dest` path. The first procedure refreshes a view
containing a listing of all files currently in `background_dump_dest`.

```
EXEC rdsadmin.manage_tracefiles.refresh_tracefile_listing;
```

After the view is refreshed, query the following view to access the results.

```
SELECT * FROM rdsadmin.tracefile_listing;
```

An alternative to the previous process is to use `FROM table` to stream nonrelational data in a
table-like format to list database directory contents.

```
SELECT * FROM TABLE(rdsadmin.rds_file_util.listdir('BDUMP'));
```

The following query shows the text of a log file.

```
SELECT text FROM TABLE(rdsadmin.rds_file_util.read_text_file('BDUMP','alert_`dbname`.log.`date`'));
```

On a read replica, get the name of the BDUMP directory by querying
`V$DATABASE.DB_UNIQUE_NAME`. If the unique name is
`DATABASE_B`, then the BDUMP directory is `BDUMP_B`. The
following example queries the BDUMP name on a replica and then uses this name to
query the contents of `alert_DATABASE.log.2020-06-23`.

```
SELECT 'BDUMP' || (SELECT regexp_replace(DB_UNIQUE_NAME,'.*(_[A-Z])', '\1') FROM V$DATABASE) AS BDUMP_VARIABLE FROM DUAL;

BDUMP_VARIABLE
--------------
BDUMP_B

SELECT TEXT FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP_B','alert_DATABASE.log.2020-06-23'));
```

### Generating trace files and tracing a session

Because there are no restrictions on `ALTER SESSION`, many standard methods to generate trace files in
Oracle remain available to an Amazon RDS DB instance. The following procedures are provided for trace files that
require greater access.

| Oracle method                   | Amazon RDS method                                   |
| ------------------------------- | --------------------------------------------------- |
| `oradebug hanganalyze 3`        | `EXEC rdsadmin.manage_tracefiles.hanganalyze;`      |
| `oradebug dump systemstate 266` | `EXEC rdsadmin.manage_tracefiles.dump_systemstate;` |

You can use many standard methods to trace individual sessions connected to an Oracle DB instance in Amazon RDS. To
enable tracing for a session, you can run subprograms in PL/SQL packages supplied by Oracle, such as
`DBMS_SESSION` and `DBMS_MONITOR`. For more information, see [Enabling tracing for a session](https://docs.oracle.com/database/121/TGSQL/tgsql_trace.htm#GUID-F872D6F9-E015-481F-80F6-8A7036A6AD29 "https://docs.oracle.com/database/121/TGSQL/tgsql_trace.htm#GUID-F872D6F9-E015-481F-80F6-8A7036A6AD29") in the Oracle documentation.

### Retrieving trace files

You can retrieve any trace file in `background_dump_dest` using a standard SQL query on an
Amazon RDS–managed external table. To use this method, you must execute the procedure to set the location
for this table to the specific trace file.

For example, you can use the `rdsadmin.tracefile_listing` view mentioned
preceding to list all of the trace files on the system. You can then set the
`tracefile_table` view to point to the intended trace file using the
following procedure.

```
EXEC rdsadmin.manage_tracefiles.set_tracefile_table_location('CUST01_ora_3260_SYSTEMSTATE.trc');
```

The following example creates an external table in the current schema with the location set
to the file provided. You can retrieve the contents into a local file using a SQL
query.

```
SPOOL /tmp/tracefile.txt
SELECT * FROM tracefile_table;
SPOOL OFF;
```

### Purging trace files

Trace files can accumulate and consume disk space. Amazon RDS purges trace files by default and
log files that are older than seven days. You can view and set the trace file
retention period using the `show_configuration` procedure. You should run
the command `SET SERVEROUTPUT ON` so that you can view the configuration
results.

The following example shows the current trace file retention period, and then sets
a new trace file retention period.

```
# Show the current tracefile retention
SQL> EXEC rdsadmin.rdsadmin_util.show_configuration;
NAME:tracefile retention
VALUE:10080
DESCRIPTION:tracefile expiration specifies the duration in minutes before tracefiles in bdump are automatically deleted.

# Set the tracefile retention to 24 hours:
SQL> EXEC rdsadmin.rdsadmin_util.set_configuration('tracefile retention',1440);
SQL> commit;

#show the new tracefile retention
SQL> EXEC rdsadmin.rdsadmin_util.show_configuration;
NAME:tracefile retention
VALUE:1440
DESCRIPTION:tracefile expiration specifies the duration in minutes before tracefiles in bdump are automatically deleted.
```

In addition to the periodic purge process, you can manually remove files from the
`background_dump_dest`. The following example shows how to purge all
files older than five minutes.

```
EXEC rdsadmin.manage_tracefiles.purge_tracefiles(5);
```

You can also purge all files that match a specific pattern (if you do, don't include
the file extension, such as .trc). The following example shows how to purge all
files that start with `SCHPOC1_ora_5935`.

```
EXEC rdsadmin.manage_tracefiles.purge_tracefiles('SCHPOC1_ora_5935');
```

## Publishing Oracle logs to

Amazon CloudWatch Logs

You can configure your RDS for Oracle DB instance to publish log data to a log group in Amazon CloudWatch Logs.
With CloudWatch Logs, you can analyze the log data, and use CloudWatch to create alarms and view
metrics. You can use CloudWatch Logs to store your log records in highly durable storage.

Amazon RDS publishes each Oracle database log as a separate database stream in the log group. For
example, if you configure the export function to include the audit log, audit data is
stored in an audit log stream in the `/aws/rds/instance/my_instance/audit`
log group. The following table summarizes the requirements for RDS for Oracle to publish logs
to Amazon CloudWatch Logs.

| Log name                    | Requirement                                                                                 | Default |
| --------------------------- | ------------------------------------------------------------------------------------------- | ------- | --------------- | ------------------------- | ------ |
| Alert log                   | None. You can't disable this log.                                                           | Enabled |
| Trace log                   | Set the `trace_enabled` parameter to `TRUE` or leave it set at<br>the default.              | `TRUE`  |
| Audit log                   | Set the `audit_trail` parameter to any of the following allowed<br>values:<br>```<br>{ none | os      | db [, extended] | xml [, extended] }<br>``` | `none` |
| Listener log                | None. You can't disable this log.                                                           | Enabled |
| Oracle Management Agent log | None. You can't disable this log.                                                           | Enabled |

This Oracle Management Agent log consists of the log groups shown in the following table.

| Log name           | CloudWatch log group    |
| ------------------ | ----------------------- |
| emctl.log          | oemagent-emctl          |
| emdctlj.log        | oemagent-emdctlj        |
| gcagent.log        | oemagent-gcagent        |
| gcagent_errors.log | oemagent-gcagent-errors |
| emagent.nohup      | oemagent-emagent-nohup  |
| secure.log         | oemagent-secure         |

For more information, see [Locating Management Agent Log and Trace Files](https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.4/emadm/locating-management-agent-log-and-trace-files1.html#GUID-9C710D78-6AA4-42E4-83CD-47B5FF4892DF "https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.4/emadm/locating-management-agent-log-and-trace-files1.html#GUID-9C710D78-6AA4-42E4-83CD-47B5FF4892DF") in the Oracle documentation.

###### To publish Oracle DB logs to CloudWatch Logs from the AWS Management Console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB
   instance that you want to modify.
3. Choose **Modify**.
4. In the **Log exports** section, choose the logs that you want to start
   publishing to CloudWatch Logs.
5. Choose **Continue**, and then choose **Modify
   DB Instance** on the summary page.
   To publish Oracle logs, you can use the [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command with the following
   parameters:

- `--db-instance-identifier`
- `--cloudwatch-logs-export-configuration`

###### Note

A change to the `--cloudwatch-logs-export-configuration` option is always applied to the DB instance
immediately. Therefore, the `--apply-immediately` and `--no-apply-immediately` options have no effect.

You can also publish Oracle logs using the following commands:

- [`create-db-instance`](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md")
- [`restore-db-instance-from-db-snapshot`](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md")
- [`restore-db-instance-from-s3`](../../../cli/latest/reference/rds/restore-db-instance-from-s3.md "../../../cli/latest/reference/rds/restore-db-instance-from-s3.md")
- [`restore-db-instance-to-point-in-time`](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md")

###### Example

The following example creates an Oracle DB instance with CloudWatch Logs publishing enabled. The
`--cloudwatch-logs-export-configuration` value is a JSON array of strings. The strings
can be any combination of `alert`, `audit`, `listener`, and
`trace`.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mydbinstance` \
    --cloudwatch-logs-export-configuration '["trace","audit","alert","listener","oemagent"]' \
    --db-instance-class `db.m5.large` \
    --allocated-storage `20` \
    --engine `oracle-ee` \
    --engine-version `19.0.0.0.ru-2024-04.rur-2024-04.r1` \
    --license-model `bring-your-own-license` \
    --master-username `myadmin` \
    --manage-master-user-password
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --cloudwatch-logs-export-configuration `trace alert audit listener oemagent` ^
    --db-instance-class `db.m5.large` ^
    --allocated-storage `20` ^
    --engine `oracle-ee` ^
    --engine-version `19.0.0.0.ru-2024-04.rur-2024-04.r1` ^
    --license-model `bring-your-own-license` ^
    --master-username `myadmin` ^
    --manage-master-user-password
```

###### Example

The following example modifies an existing Oracle DB instance to publish
log files to CloudWatch Logs. The `--cloudwatch-logs-export-configuration`
value is a JSON object. The key for this object is
`EnableLogTypes`, and its value is an array of strings with
any combination of `alert`, `audit`,
`listener`, and `trace`.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["trace","alert","audit","listener","oemagent"]}'
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --cloudwatch-logs-export-configuration EnableLogTypes=\"trace\",\"alert\",\"audit\",\"listener\",\"oemagent\"
```

###### Example

The following example modifies an existing Oracle DB instance to disable
publishing audit and listener log files to CloudWatch Logs. The
`--cloudwatch-logs-export-configuration` value is a JSON
object. The key for this object is `DisableLogTypes`, and its
value is an array of strings with any combination of `alert`,
`audit`, `listener`, and `trace`.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --cloudwatch-logs-export-configuration '{"DisableLogTypes":["audit","listener"]}'
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --cloudwatch-logs-export-configuration DisableLogTypes=\"audit\",\"listener\"
```

You can publish Oracle DB logs with the RDS API. You can call the [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") action with the following parameters:

- `DBInstanceIdentifier`
- `CloudwatchLogsExportConfiguration`

###### Note

A change to the `CloudwatchLogsExportConfiguration` parameter is always applied to the DB instance
immediately. Therefore, the `ApplyImmediately` parameter has no effect.

You can also publish Oracle logs by calling the following RDS API operations:

- [`CreateDBInstance`](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md")
- [`RestoreDBInstanceFromDBSnapshot`](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md")
- [`RestoreDBInstanceFromS3`](../APIReference/API_RestoreDBInstanceFromS3.md "../APIReference/API_RestoreDBInstanceFromS3.md")
- [`RestoreDBInstanceToPointInTime`](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md")
  Run one of these RDS API operations with the following parameters:

- `DBInstanceIdentifier`
- `EnableCloudwatchLogsExports`
- `Engine`
- `DBInstanceClass`
  Other parameters might be required depending on the RDS operation that you run.

## Accessing alert logs and

listener logs

You can view the alert log using the Amazon RDS console. You can also use the following SQL
statement.

```
SELECT message_text FROM alertlog;
```

Access the listener log using Amazon CloudWatch Logs.

###### Note

Oracle rotates the alert and listener logs when they exceed 10 MB, at which point they are unavailable from Amazon RDS
views.
