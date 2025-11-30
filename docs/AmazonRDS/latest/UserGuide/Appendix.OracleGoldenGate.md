# Troubleshooting Oracle GoldenGate

This section explains the most common issues when using Oracle GoldenGate with Amazon RDS for Oracle.

###### Topics

- [Error opening an online redo
  log](#Appendix.OracleGoldenGate.Troubleshooting.Logs "#Appendix.OracleGoldenGate.Troubleshooting.Logs")
- [Oracle GoldenGate appears to be properly
  configured but replication is not working](#Appendix.OracleGoldenGate.Troubleshooting.Replication "#Appendix.OracleGoldenGate.Troubleshooting.Replication")
- [Integrated REPLICAT slow due to query on
  SYS."\_DBA_APPLY_CDR_INFO"](#Appendix.OracleGoldenGate.IR "#Appendix.OracleGoldenGate.IR")

## Error opening an online redo

log

Make sure that you configure your databases to retain archived redo logs. Consider the
following guidelines:

- Specify the duration for log retention in hours. The minimum value is one
  hour.
- Set the duration to exceed any potential downtime of the source DB instance,
  any potential period of communication, and any potential period of networking
  issues for the source DB instance. Such a duration lets Oracle GoldenGate recover logs from the
  source DB instance as needed.
- Ensure that you have sufficient storage on your instance for the files.

If you don't have log retention enabled, or if the retention value is too small, you
receive an error message similar to the following.

```
2022-03-06 06:17:27  ERROR   OGG-00446  error 2 (No such file or directory)
opening redo log /rdsdbdata/db/GGTEST3_A/onlinelog/o1_mf_2_9k4bp1n6_.log for sequence 1306
Not able to establish initial position for begin time 2022-03-06 06:16:55.
```

## Oracle GoldenGate appears to be properly

configured but replication is not working

For pre-existing tables, you must specify the SCN that Oracle GoldenGate works from.

###### To fix this issue

1. Log in to the source database and launch the Oracle GoldenGate command line interface
   (`ggsci`). The following example shows the format for logging
   in.

```
dblogin userid oggadm1@OGGSOURCE
```

2. Using the `ggsci` command line, set up the start SCN for the
   `EXTRACT` process. The following example sets the SCN to 223274
   for the `EXTRACT`.

```
ALTER EXTRACT EABC SCN 223274
start EABC
```

3. Log in to the target database. The following example shows the format for
   logging in.

```
dblogin userid oggadm1@OGGTARGET
```

4. Using the `ggsci` command line, set up the start SCN for the
   `REPLICAT` process. The following example sets the SCN to 223274
   for the `REPLICAT`.

```
start RABC atcsn 223274
```

## Integrated REPLICAT slow due to query on

SYS."\_DBA_APPLY_CDR_INFO"

Oracle GoldenGate Conflict Detection and Resolution (CDR) provides basic conflict resolution routines. For
example, CDR can resolve a unique conflict for an `INSERT` statement.

When CDR resolves a collision, it can insert records into the exception table
`_DBA_APPLY_CDR_INFO` temporarily. Integrated `REPLICAT` deletes these records
later. In a rare scenario, the integrated `REPLICAT` can process a large number of collisions, but
a new integrated `REPLICAT` does not replace it. Instead of being removed, the existing rows in
`_DBA_APPLY_CDR_INFO` are orphaned. Any new integrated `REPLICAT` processes slow
down because they are querying orphaned rows in `_DBA_APPLY_CDR_INFO`.

To remove all rows from `_DBA_APPLY_CDR_INFO`, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.truncate_apply$_cdr_info`. This procedure is
released as part of the October 2020 release and patch update. The procedure is
available in the following database versions:

- [Version 21.0.0.0.ru-2022-01.rur-2022-01.r1](../OracleReleaseNotes/oracle-version-21-0.md#oracle-version-RU-RUR.21.0.0.0.ru-2022-01.rur-2022-01.r1 "../OracleReleaseNotes/oracle-version-21-0.md#oracle-version-RU-RUR.21.0.0.0.ru-2022-01.rur-2022-01.r1") and higher
- [Version 19.0.0.0.ru-2020-10.rur-2020-10.r1](../OracleReleaseNotes/oracle-version-19-0.md#oracle-version-RU-RUR.19.0.0.0.ru-2020-10.rur-2020-10.r1 "../OracleReleaseNotes/oracle-version-19-0.md#oracle-version-RU-RUR.19.0.0.0.ru-2020-10.rur-2020-10.r1") and higher

The following example truncates the table `_DBA_APPLY_CDR_INFO`.

```
SET SERVEROUTPUT ON SIZE 2000
EXEC rdsadmin.rdsadmin_util.truncate_apply$_cdr_info;
```
