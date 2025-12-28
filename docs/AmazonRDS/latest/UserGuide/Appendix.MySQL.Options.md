# MariaDB Audit Plugin support for

MySQL

Amazon RDS offers an audit plugin for MySQL database instances based on the open source MariaDB
Audit Plugin. For more information, see the [Audit Plugin for MySQL Server GitHub
repository](https://github.com/aws/audit-plugin-for-mysql "https://github.com/aws/audit-plugin-for-mysql").

###### Note

The audit plugin for MySQL is based on the MariaDB Audit Plugin. Throughout this
article, we refer to it as MariaDB Audit Plugin.

The MariaDB Audit Plugin records database activity, including users logging on to the
database and queries run against the database. The record of database activity is stored in
a log file.

## Audit Plugin option settings

Amazon RDS supports the following settings for the MariaDB Audit Plugin option.

| Option setting                  | Valid values                                                                        | Default value           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SERVER_AUDIT_FILE_PATH`        | `/rdsdbdata/log/audit/`                                                             | `/rdsdbdata/log/audit/` | The location of the log file. The log file contains the record of the activity specified in `SERVER_AUDIT_EVENTS`.<br>For more information, see<br>[Viewing and listing database log files](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md")<br>and<br>[MySQL database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `SERVER_AUDIT_FILE_ROTATE_SIZE` | 1–1000000000                                                                        | 1000000                 | The size in bytes that when reached, causes the file to rotate.<br>For more information, see<br>[Overview of RDS for MySQL database logs](USER_LogAccess.MySQL.md "USER_LogAccess.MySQL.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `SERVER_AUDIT_FILE_ROTATIONS`   | 0–100                                                                               | 9                       | The number of log rotations to save when<br>`server_audit_output_type=file`. If set to 0, then<br>the log file never rotates. For more information, see [Overview of RDS for MySQL database logs](USER_LogAccess.MySQL.md "USER_LogAccess.MySQL.md") and [Downloading a database log file](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `SERVER_AUDIT_EVENTS`           | `CONNECT`, `QUERY`, `QUERY_DDL`,<br>`QUERY_DML`, `QUERY_DML_NO_SELECT`, `QUERY_DCL` | `CONNECT`, `QUERY`      | The types of activity to record in the log. Installing the MariaDB Audit Plugin is itself logged.<br>• `CONNECT`:<br>Log successful and unsuccessful connections to the database,<br>and disconnections from the database.<br>• `QUERY`:<br>Log the text of all queries run against the database.<br>• `QUERY_DDL`:<br>Similar to the `QUERY` event, but returns only data definition language<br>(DDL) queries (`CREATE`, `ALTER`, and so on).<br>• `QUERY_DML`:<br>Similar to the `QUERY` event, but returns only data manipulation language<br>(DML) queries (`INSERT`, `UPDATE`, and so on, and also `SELECT`).<br>• `QUERY_DML_NO_SELECT`:<br>Similar to the `QUERY_DML` event, but doesn't log `SELECT` queries.<br>• `QUERY_DCL`:<br>Similar to the `QUERY` event, but returns only data control language (DCL)<br>queries (`GRANT`, `REVOKE`, and so on).<br>For MySQL, `TABLE` is not supported. |
| `SERVER_AUDIT_INCL_USERS`       | Multiple comma-separated values                                                     | None                    | Include only activity from the specified users. By default, activity is recorded for all users.<br>`SERVER_AUDIT_INCL_USERS` and `SERVER_AUDIT_EXCL_USERS` are mutually exclusive.<br>If you add values to `SERVER_AUDIT_INCL_USERS`, make sure no values are added to<br>`SERVER_AUDIT_EXCL_USERS`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `SERVER_AUDIT_EXCL_USERS`       | Multiple comma-separated values                                                     | None                    | Exclude activity from the specified users. By default, activity is recorded for all users.<br>`SERVER_AUDIT_INCL_USERS` and `SERVER_AUDIT_EXCL_USERS` are mutually exclusive.<br>If you add values to `SERVER_AUDIT_EXCL_USERS`, make sure no values are added to<br>`SERVER_AUDIT_INCL_USERS`.<br>The `rdsadmin` user queries the database every second to check the health of the database.<br>Depending on your other settings, this activity can possibly cause the size of your log file to grow very large, very quickly.<br>If you don't need to record this activity,<br>add the `rdsadmin` user to the `SERVER_AUDIT_EXCL_USERS` list.<br>Note<br>`CONNECT` activity is always recorded for all users, even if the user is specified for this option setting.                                                                                                                                    |
| `SERVER_AUDIT_LOGGING`          | `ON`                                                                                | `ON`                    | Logging is active.<br>The only valid value is `ON`.<br>Amazon RDS does not support deactivating logging. If you want to deactivate logging, remove the MariaDB Audit Plugin.<br>For more information, see [Removing the MariaDB Audit Plugin](#Appendix.MySQL.Options.AuditPlugin.Remove "#Appendix.MySQL.Options.AuditPlugin.Remove").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `SERVER_AUDIT_QUERY_LOG_LIMIT`  | 0–2147483647                                                                        | 1024                    | The limit on the length of the query string in a record.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Adding the MariaDB Audit Plugin

The general process for adding the MariaDB Audit Plugin to a DB instance is the following:

- Create a new option group, or copy or modify an existing option group
- Add the option to the option group
- Associate the option group with the DB instance

After you add the MariaDB Audit Plugin, you don't need to restart your DB instance.
As soon as the option group is active, auditing begins immediately.

###### Important

Adding the MariaDB Audit Plugin to a DB instance might cause an outage. We recommend adding the MariaDB Audit Plugin
during a maintenance window or during a time of low database workload.

###### To add the MariaDB Audit Plugin

1. Determine the option group you want to use. You can create a new option group
   or use an existing option group. If you want to use an existing option group,
   skip to the next step. Otherwise, create a custom DB option group. Choose
   **mysql** for **Engine**, and choose
   **5.7**, **8.0**, or **8.4** for **Major engine version**. For more
   information, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create").
2. Add the **MARIADB_AUDIT_PLUGIN** option to the option group, and configure the option settings.
   For more information about adding options,
   see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption").
   For more information about each setting,
   see [Audit Plugin option settings](#Appendix.MySQL.Options.AuditPlugin.Options "#Appendix.MySQL.Options.AuditPlugin.Options").
3. Apply the option group to a new or existing DB instance.
   - For a new DB instance, you apply the option group when you launch the instance.
     For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
   - For an existing DB instance, you apply the option group by
     modifying the instance and attaching the new option group. For
     more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Audit log format

Log files are represented as comma-separated variable (CSV) files in UTF-8
format.

###### Tip

Log file entries are not in sequential order. To order the entries, use the timestamp value. To see the latest
events, you might have to review all log files. For more flexibility in sorting and searching the log data,
turn on the setting to upload the audit logs to CloudWatch and view them using the CloudWatch interface.

To view audit data with more types of fields and with output in JSON format, you can also use
the Database Activity Streams feature. For more information, see
[Monitoring Amazon RDS with Database Activity
Streams](DBActivityStreams.md "DBActivityStreams.md").

The audit log files include the following comma-delimited information in rows, in the specified order:

| Field           | Description                                                                                                                                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timestamp       | The `YYYYMMDD` followed by the `HH:MI:SS`<br>(24-hour clock) for the logged event.                                                                                          |
| serverhost      | The name of the instance that the event is logged for.                                                                                                                      |
| username        | The connected user name of the user.                                                                                                                                        |
| host            | The host that the user connected from.                                                                                                                                      |
| connectionid    | The connection ID number for the logged operation.                                                                                                                          |
| queryid         | The query ID number, which can be used for finding the relational<br>table events and related queries. For `TABLE` events,<br>multiple lines are added.                     |
| operation       | The recorded action type. Possible values are:<br>`CONNECT`, `QUERY`, `READ`,<br>`WRITE`, `CREATE`, `ALTER`,<br>`RENAME`, and `DROP`.                                       |
| database        | The active database, as set by the `USE`<br>command.                                                                                                                        |
| object          | For `QUERY` events, this value indicates the query that the database performed. For<br>`TABLE` events, it indicates the table name.                                         |
| retcode         | The return code of the logged operation.                                                                                                                                    |
| connection_type | The security state of the connection to the server. Possible values are:<br>• `Undefined`<br>• `TCP/IP`<br>• `Socket`<br>• `Named pipe`<br>• `SSL/TLS`<br>• `Shared memory` |

## Viewing and downloading the MariaDB Audit Plugin log

After you enable the MariaDB Audit Plugin, you access the results in the log files
the same way you access any other text-based log files. The audit log files are located at `/rdsdbdata/log/audit/`.
For information about viewing the log file in the console, see [Viewing and listing database log files](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md").
For information about downloading the log file, see [Downloading a database log file](USER_LogAccess.Procedural.md "USER_LogAccess.Procedural.md").

## Modifying MariaDB Audit Plugin settings

After you enable the MariaDB Audit Plugin, you can modify the settings. For more
information about how to modify option settings, see [Modifying an option setting](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.ModifyOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.ModifyOption"). For more
information about each setting, see [Audit Plugin option settings](#Appendix.MySQL.Options.AuditPlugin.Options "#Appendix.MySQL.Options.AuditPlugin.Options").

## Removing the MariaDB Audit Plugin

Amazon RDS doesn't support turning off logging in the MariaDB Audit Plugin.
However, you can remove the plugin from a DB instance. When you remove the MariaDB Audit Plugin, the DB instance is restarted automatically to stop auditing.

To remove the MariaDB Audit Plugin from a DB instance, do one of the following:

- Remove the MariaDB Audit Plugin option from the option group it belongs to. This change affects all DB
  instances that use the option group. For more information, see [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption")
- Modify the DB instance and specify a different option group that doesn't include the plugin. This change affects a single DB
  instance. You can specify the default (empty) option group, or a
  different custom option group. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
