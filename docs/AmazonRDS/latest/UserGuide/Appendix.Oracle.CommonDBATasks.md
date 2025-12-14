# Retaining archived

redo logs

You can retain archived redo logs locally on your DB instance for use with
products like Oracle LogMiner (`DBMS_LOGMNR`). After you have retained
the redo logs, you can use LogMiner to analyze the logs. For more information, see
[Using LogMiner to analyze redo log files](http://docs.oracle.com/cd/E11882_01/server.112/e22490/logminer.htm "http://docs.oracle.com/cd/E11882_01/server.112/e22490/logminer.htm") in the Oracle documentation.

To retain archived redo logs, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.set_configuration`. If you use this procedure
on a primary instance in Oracle Data Guard, RDS changes the archive log retention
setting on the primary instance and open read replicas, but not on mounted replicas.
RDS retains the latest archive redo logs on mounted replicas for a short period of
time. RDS automatically deletes older logs downloaded to mounted replicas.

The `set_configuration` procedure has the following parameters.

| Parameter name | Data type | Default | Required | Description                                                                                                                                   |
| -------------- | --------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`         | varchar   | —       | Yes      | The name of the configuration to update. To change the<br>archived redo log retention hours, set the name to<br>`archivelog retention hours`. |
| `value`        | varchar   | —       | Yes      | The value for the configuration. Set the value the number of<br>hours to retain the logs.                                                     |

The following example retains 24 hours of redo logs.

```
begin
    rdsadmin.rdsadmin_util.set_configuration(
        name  => 'archivelog retention hours',
        value => '24');
end;
/
commit;
```

###### Note

The commit is required for the change to take effect.

To view how long archived redo logs are kept for your DB instance, use the Amazon
RDS procedure `rdsadmin.rdsadmin_util.show_configuration`.

The following example shows the log retention time.

```
set serveroutput on
EXEC rdsadmin.rdsadmin_util.show_configuration;
```

The output shows the current setting for `archivelog retention hours`.
The following output shows that archived redo logs are kept for 48 hours.

```
NAME:archivelog retention hours
VALUE:48
DESCRIPTION:ArchiveLog expiration specifies the duration in hours before archive/redo log files are automatically deleted.
```

Because the archived redo logs are retained on your DB instance, ensure that your
DB instance has enough allocated storage for the retained logs. To determine how
much space your DB instance has used in the last X hours, you can run the following
query, replacing X with the number of hours.

```
SELECT SUM(BLOCKS * BLOCK_SIZE) bytes
  FROM V$ARCHIVED_LOG
 WHERE FIRST_TIME >= SYSDATE-(`X`/24) AND DEST_ID=1;
```

RDS for Oracle only generates archived redo logs when the backup retention period of your DB instance is greater
than zero. By default the backup retention period is greater than zero.

When the archived log retention period expires, RDS for Oracle removes the archived redo logs from your DB
instance. To support restoring your DB instance to a point in time, Amazon RDS retains the archived redo logs
outside of your DB instance based on the backup retention period. To modify the backup retention period, see
[Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

###### Note

In some cases, you might be using JDBC on Linux to download archived redo logs
and experience long latency times and connection resets. In such cases, the
issues might be caused by the default random number generator setting on your
Java client. We recommend setting your JDBC drivers to use a nonblocking random
number generator.
