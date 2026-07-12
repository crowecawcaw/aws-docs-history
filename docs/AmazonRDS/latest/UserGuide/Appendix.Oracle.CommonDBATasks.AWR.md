# Generating performance reports with Automatic Workload Repository (AWR)

To gather performance data and generate reports, Oracle recommends Automatic
Workload Repository (AWR). AWR requires Oracle Database Enterprise Edition and a
license for the Diagnostics and Tuning packs. To enable AWR, set the
`CONTROL_MANAGEMENT_PACK_ACCESS` initialization parameter to either
`DIAGNOSTIC` or `DIAGNOSTIC+TUNING`.

## Working with AWR reports in RDS

To generate AWR reports, you can run scripts such as
`awrrpt.sql`. These scripts are installed on the database
host server. In Amazon RDS, you don't have direct access to the host. However, you
can get copies of SQL scripts from another installation of Oracle Database.

You can also use AWR by running procedures in the
`SYS.DBMS_WORKLOAD_REPOSITORY` PL/SQL package. You can use this
package to manage baselines and snapshots, and also to display ASH and AWR
reports. For example, to generate an AWR report in text format run the
`DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_TEXT` procedure. However,
you can't reach these AWR reports from the AWS Management Console.

When working with AWR, we recommend using the
`rdsadmin.rdsadmin_diagnostic_util` procedures. You can use these
procedures to generate the following:

- AWR reports
- Active Session History (ASH) reports
- Automatic Database Diagnostic Monitor (ADDM) reports
- Oracle Data Pump Export dump files of AWR data

The `rdsadmin_diagnostic_util` procedures save the reports to the
DB instance file system. You can access these reports from the console. You can
also access reports using the `rdsadmin.rds_file_util` procedures,
and you can access reports that are copied to Amazon S3 using the S3 Integration
option. For more information, see [Reading files in a DB instance directory](Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.ReadingFiles "Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.ReadingFiles") and [Amazon S3 integration](oracle-s3-integration.md "oracle-s3-integration.md").

You can use the `rdsadmin_diagnostic_util` procedures in the following Amazon RDS for Oracle DB
engine versions:

- All Oracle Database 26ai versions
- All Oracle Database 21c versions
- 19.0.0.0.ru-2020-04.rur-2020-04.r1 and higher Oracle Database 19c versions

For a blog that explains how to work with diagnostic reports in a replication
scenario, see [Generate AWR reports for Amazon RDS for Oracle read replicas](https://aws.amazon.com/blogs/database/generate-awr-reports-for-amazon-rds-for-oracle-read-replicas/ "https://aws.amazon.com/blogs/database/generate-awr-reports-for-amazon-rds-for-oracle-read-replicas/").

## Common parameters for the diagnostic utility package

You typically use the following parameters when managing AWR and ADDM with the
`rdsadmin_diagnostic_util` package.

| Parameter        | Data type  | Default | Required | Description                                                                                                                                                                                                            |
| ---------------- | ---------- | ------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `begin_snap_id`  | `NUMBER`   | —       | Yes      | The ID of the beginning snapshot.                                                                                                                                                                                      |
| `end_snap_id`    | `NUMBER`   | —       | Yes      | The ID of the ending snapshot.                                                                                                                                                                                         |
| `dump_directory` | `VARCHAR2` | `BDUMP` | No       | The directory to write the report or export file to. If<br>you specify a nondefault directory, the user that runs the<br>`rdsadmin_diagnostic_util` procedures must<br>have write permissions for the directory.       |
| `p_tag`          | `VARCHAR2` | —       | No       | A tag to identify the report output file. You can specify<br>up to 30 characters. Valid characters are `a-z`,<br>`A-Z`, `0-9`, underscore (`_`), dash<br>(`-`), and period (`.`).                                      |
| `report_type`    | `VARCHAR2` | `HTML`  | No       | The format of the report. Valid values are<br>`TEXT` and `HTML`.                                                                                                                                                       |
| `dbid`           | `NUMBER`   | —       | No       | A valid database identifier (DBID) shown in the<br>`DBA_HIST_DATABASE_INSTANCE` view for Oracle.<br>If this parameter is not specified, RDS uses the current<br>DBID, which is shown in the `V$DATABASE.DBID`<br>view. |

You typically use the following parameters when managing ASH with the
rdsadmin\_diagnostic\_util package.

| Parameter      | Data type  | Default | Required | Description                                                                                                                                                                                                                |
| -------------- | ---------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `begin_time`   | `DATE`     | —       | Yes      | The beginning time of the ASH analysis.                                                                                                                                                                                    |
| `end_time`     | `DATE`     | —       | Yes      | The ending time of the ASH analysis.                                                                                                                                                                                       |
| `slot_width`   | `NUMBER`   | `0`     | No       | The duration of the slots (in seconds) used in the "Top<br>Activity" section of the ASH report. If this parameter isn't<br>specified, the time interval between `begin_time`<br>and `end_time` uses no more than 10 slots. |
| `sid`          | `NUMBER`   | Null    | No       | The session ID.                                                                                                                                                                                                            |
| `sql_id`       | `VARCHAR2` | Null    | No       | The SQL ID.                                                                                                                                                                                                                |
| `wait_class`   | `VARCHAR2` | Null    | No       | The wait class name.                                                                                                                                                                                                       |
| `service_hash` | `NUMBER`   | Null    | No       | The service name hash.                                                                                                                                                                                                     |
| `module_name`  | `VARCHAR2` | Null    | No       | The module name.                                                                                                                                                                                                           |
| `action_name`  | `VARCHAR2` | Null    | No       | The action name.                                                                                                                                                                                                           |
| `client_id`    | `VARCHAR2` | Null    | No       | The application-specific ID of the database<br>session.                                                                                                                                                                    |
| `plsql_entry`  | `VARCHAR2` | Null    | No       | The PL/SQL entry point.                                                                                                                                                                                                    |

## Generating an AWR report

To generate an AWR report, use the
`rdsadmin.rdsadmin_diagnostic_util.awr_report` procedure.

To find valid snapshot IDs for your AWR report, run the following query:

```
SELECT SNAP_ID, BEGIN_INTERVAL_TIME, END_INTERVAL_TIME FROM DBA_HIST_SNAPSHOT ORDER BY SNAP_ID DESC FETCH FIRST 10 ROWS ONLY;
```

The following example generates a AWR report for the snapshot range
101–106. The output text file is named
`awrrpt_101_106.txt`. You can access this report from the
AWS Management Console.

```
EXEC rdsadmin.rdsadmin_diagnostic_util.awr_report(101,106,'TEXT');
```

The following example generates an HTML report for the snapshot range
63–65. The output HTML file is named
`awrrpt_63_65.html`. The procedure writes the report to
the nondefault database directory named
`AWR_RPT_DUMP`.

```
EXEC rdsadmin.rdsadmin_diagnostic_util.awr_report(63,65,'HTML','AWR_RPT_DUMP');
```

## Extracting AWR data into a dump file

To extract AWR data into a dump file, use the
`rdsadmin.rdsadmin_diagnostic_util.awr_extract` procedure. You can use this function only at the PDB level.

The following example extracts the snapshot range 101–106. The output
dump file is named `awrextract_101_106.dmp`. You can access
this file through the console.

```
EXEC rdsadmin.rdsadmin_diagnostic_util.awr_extract(101,106);
```

The following example extracts the snapshot range 63–65. The output
dump file is named `awrextract_63_65.dmp`. The file is stored
in the nondefault database directory named
`AWR_RPT_DUMP`.

```
EXEC rdsadmin.rdsadmin_diagnostic_util.awr_extract(63,65,'AWR_RPT_DUMP');
```

## Generating an ADDM report

To generate an ADDM report, use the
`rdsadmin.rdsadmin_diagnostic_util.addm_report` procedure.

The following example generates an ADDM report for the snapshot range
101–106. The output text file is named
`addmrpt_101_106.txt`. You can access the report through
the console.

```
EXEC rdsadmin.rdsadmin_diagnostic_util.addm_report(101,106);
```

The following example generates an ADDM report for the snapshot range
63–65. The output text file is named
`addmrpt_63_65.txt`. The file is stored in the nondefault
database directory named `ADDM_RPT_DUMP`.

```
EXEC rdsadmin.rdsadmin_diagnostic_util.addm_report(63,65,'ADDM_RPT_DUMP');
```

## Generating an ASH report

To generate an ASH report, use the
`rdsadmin.rdsadmin_diagnostic_util.ash_report` procedure.

The following example generates an ASH report that includes the data from 14
minutes ago until the current time. The name of the output file uses the format
`ashrpt`begin_time``end_time`.txt`,
 where ``begin_time`and
`end_time`` use the format
`YYYYMMDDHH24MISS`. You can access the file through the
console.

```
BEGIN
    rdsadmin.rdsadmin_diagnostic_util.ash_report(
        begin_time     =>     SYSDATE-14/1440,
        end_time       =>     SYSDATE,
        report_type    =>     'TEXT');
END;
/
```

The following example generates an ASH report that includes the data from
September 18, 2019, at 6:07 PM through September 18, 2019, at 6:15 PM. The name of
the output HTML report is
`ashrpt_20190918180700_20190918181500.html`. The report
is stored in the nondefault database directory named
`AWR_RPT_DUMP`.

```
BEGIN
    rdsadmin.rdsadmin_diagnostic_util.ash_report(
        begin_time     =>    TO_DATE('2019-09-18 18:07:00', 'YYYY-MM-DD HH24:MI:SS'),
        end_time       =>    TO_DATE('2019-09-18 18:15:00', 'YYYY-MM-DD HH24:MI:SS'),
        report_type    =>    'html',
        dump_directory =>    'AWR_RPT_DUMP');
END;
/
```

## Accessing AWR reports from the console or CLI

To access AWR reports or export dump files, you can use the AWS Management Console or
AWS CLI. For more information, see [Downloading a database log file](USER_LogAccess.Procedural.Downloading.md "USER_LogAccess.Procedural.Downloading.md").
