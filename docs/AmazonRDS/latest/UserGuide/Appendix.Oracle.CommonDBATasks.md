# Performing common log-related tasks

for Oracle DB instances

Following, you can find how to perform certain common DBA tasks related to logging on
your Amazon RDS DB instances running Oracle. To deliver a managed service experience, Amazon RDS
doesn't provide shell access to DB instances, and restricts access to certain system
procedures and tables that require advanced privileges.

For more information, see [Amazon RDS for Oracle database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md").

###### Topics

- [Setting force
  logging](#Appendix.Oracle.CommonDBATasks.SettingForceLogging "#Appendix.Oracle.CommonDBATasks.SettingForceLogging")
- [Setting
  supplemental logging](#Appendix.Oracle.CommonDBATasks.AddingSupplementalLogging "#Appendix.Oracle.CommonDBATasks.AddingSupplementalLogging")
- [Switching online
  log files](#Appendix.Oracle.CommonDBATasks.SwitchingLogfiles "#Appendix.Oracle.CommonDBATasks.SwitchingLogfiles")
- [Adding online redo
  logs](#Appendix.Oracle.CommonDBATasks.RedoLogs "#Appendix.Oracle.CommonDBATasks.RedoLogs")
- [Dropping online
  redo logs](#Appendix.Oracle.CommonDBATasks.DroppingRedoLogs "#Appendix.Oracle.CommonDBATasks.DroppingRedoLogs")
- [Resizing online
  redo logs](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md")
- [Retaining archived
  redo logs](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md")
- [Accessing online and
  archived redo logs](Appendix.Oracle.CommonDBATasks.Log.md "Appendix.Oracle.CommonDBATasks.Log.md")
- [Downloading
  archived redo logs from Amazon S3](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md")

## Setting force

logging

In force logging mode, Oracle logs all changes to the database except changes in
temporary tablespaces and temporary segments (`NOLOGGING` clauses are
ignored). For more information, see [Specifying FORCE LOGGING mode](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11096 "https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11096") in the Oracle documentation.

To set force logging, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.force_logging`. The
`force_logging` procedure has the following parameters.

| Parameter name | Data type | Default | Yes | Description                                                                                                            |
| -------------- | --------- | ------- | --- | ---------------------------------------------------------------------------------------------------------------------- |
| `p_enable`     | boolean   | true    | No  | Set to `true` to put the database in force logging<br>mode, `false` to remove the database from force<br>logging mode. |

The following example puts the database in force logging mode.

```
EXEC rdsadmin.rdsadmin_util.force_logging(p_enable => `true`);
```

## Setting

supplemental logging

If you enable supplemental logging, LogMiner has the necessary information to
support chained rows and clustered tables. For more information, see [Supplemental logging](https://docs.oracle.com/cd/E11882_01/server.112/e22490/logminer.htm#SUTIL1582 "https://docs.oracle.com/cd/E11882_01/server.112/e22490/logminer.htm#SUTIL1582") in the Oracle documentation.

Oracle Database doesn't enable supplemental logging by default. To enable and
disable supplemental logging, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.alter_supplemental_logging`. For more
information about how Amazon RDS manages the retention of archived redo logs for Oracle
DB instances, see [Retaining archived
redo logs](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").

The `alter_supplemental_logging` procedure has the following
parameters.

| Parameter name | Data type | Default | Required | Description                                                                                                                         |
| -------------- | --------- | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `p_action`     | varchar2  | —       | Yes      | `'ADD'` to add supplemental logging,<br>`'DROP'` to drop supplemental logging.                                                      |
| `p_type`       | varchar2  | null    | No       | The type of supplemental logging. Valid values are<br>`'ALL'`, `'FOREIGN KEY'`,<br>`'PRIMARY KEY'`, `'UNIQUE'`, or<br>`PROCEDURAL`. |

The following example enables supplemental logging.

```
begin
    rdsadmin.rdsadmin_util.alter_supplemental_logging(
        p_action => '`ADD`');
end;
/
```

The following example enables supplemental logging for all fixed-length maximum
size columns.

```
begin
    rdsadmin.rdsadmin_util.alter_supplemental_logging(
        p_action => '`ADD`',
        p_type   => '`ALL`');
end;
/
```

The following example enables supplemental logging for primary key columns.

```
begin
    rdsadmin.rdsadmin_util.alter_supplemental_logging(
        p_action => '`ADD`',
        p_type   => '`PRIMARY KEY`');
end;
/
```

## Switching online

log files

To switch log files, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.switch_logfile`. The
`switch_logfile` procedure has no parameters.

The following example switches log files.

```
EXEC rdsadmin.rdsadmin_util.switch_logfile;
```

## Adding online redo

logs

An Amazon RDS DB instance running Oracle starts with four online redo logs, 128 MB
each. To add additional redo logs, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.add_logfile`.

The `add_logfile` procedure has the following parameters.

###### Note

The parameters are mutually exclusive.

| Parameter name | Data type | Default | Required | Description                                                                                                                                                                                                                               |
| -------------- | --------- | ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bytes`        | positive  | null    | No       | The size of the log file in bytes.<br>Use this parameter only if the size of the log is under<br>2147483648 bytes (2 GiB). Otherwise, RDS issues an error. For<br>log sizes above this byte value, use the `p_size`<br>parameter instead. |
| `p_size`       | varchar2  | —       | Yes      | The size of the log file in kilobytes (K), megabytes (M), or<br>gigabytes (G).                                                                                                                                                            |

The following command adds a 100 MB log file.

```
EXEC rdsadmin.rdsadmin_util.add_logfile(p_size => '`100M`');
```

## Dropping online

redo logs

To drop redo logs, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.drop_logfile`. The `drop_logfile`
procedure has the following parameters.

| Parameter name | Data type | Default | Required | Description                  |
| -------------- | --------- | ------- | -------- | ---------------------------- |
| `grp`          | positive  | —       | Yes      | The group number of the log. |

The following example drops the log with group number 3.

```
EXEC rdsadmin.rdsadmin_util.drop_logfile(grp => `3`);
```

You can only drop logs that have a status of unused or inactive. The following
example gets the statuses of the logs.

```
SELECT GROUP#, STATUS FROM V$LOG;

GROUP#     STATUS
---------- ----------------
1          CURRENT
2          INACTIVE
3          INACTIVE
4          UNUSED
```
