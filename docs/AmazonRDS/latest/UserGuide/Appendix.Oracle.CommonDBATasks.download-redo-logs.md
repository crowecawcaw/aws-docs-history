

# Downloading archived redo logs from Amazon S3
<a name="Appendix.Oracle.CommonDBATasks.download-redo-logs"></a>

You can download archived redo logs on your DB instance using the `rdsadmin.rdsadmin_archive_log_download` package. If archived redo logs are no longer on your DB instance, you might want to download them again from Amazon S3. Then you can mine the logs or use them to recover or replicate your database.

**Note**  
You can't download archived redo logs on read replica instances.

## Downloading archived redo logs: basic steps
<a name="Appendix.Oracle.CommonDBATasks.download-redo-logs.basic-process"></a>

The availability of your archived redo logs depends on the following retention policies:
+ Backup retention policy – Logs inside of this policy are available in Amazon S3. Logs outside of this policy are removed.
+ Archived log retention policy – Logs inside of this policy are available on your DB instance. Logs outside of this policy are removed.

If logs aren't on your instance but are protected by your backup retention period, use `rdsadmin.rdsadmin_archive_log_download` to download them again. RDS for Oracle saves the logs to the `/rdsdbdata/log/arch` directory on your DB instance.

**To download archived redo logs from Amazon S3**

1. Configure your retention period to ensure your downloaded archived redo logs are retained for the duration you need them. Make sure to `COMMIT` your change. 

   RDS retains your downloaded logs according to the archived log retention policy, starting from the time the logs were downloaded. To learn how to set the retention policy, see [Retaining archived redo logs](Appendix.Oracle.CommonDBATasks.RetainRedoLogs.md).

1. Wait up to 5 minutes for the archived log retention policy change to take effect.

1. Download the archived redo logs from Amazon S3 using `rdsadmin.rdsadmin_archive_log_download`.

   For more information, see [Downloading a single archived redo log](#Appendix.Oracle.CommonDBATasks.download-redo-logs.single-log) and [Downloading a series of archived redo logs](#Appendix.Oracle.CommonDBATasks.download-redo-logs.series).
**Note**  
RDS automatically checks the available storage before downloading. If the requested logs consume a high percentage of space, you receive an alert.

1. Confirm that the logs were downloaded from Amazon S3 successfully.

   You can view the status of your download task in a bdump file. The bdump files have the path name `/rdsdbdata/log/trace/dbtask-{{task-id}}.log`. In the preceding download step, you run a `SELECT` statement that returns the task ID in a `VARCHAR2` data type. For more information, see similar examples in [Monitoring the status of a file transfer](oracle-s3-integration.using.md#oracle-s3-integration.using.task-status).

## Downloading a single archived redo log
<a name="Appendix.Oracle.CommonDBATasks.download-redo-logs.single-log"></a>

To download a single archived redo log to the `/rdsdbdata/log/arch` directory, use `rdsadmin.rdsadmin_archive_log_download.download_log_with_seqnum`. This procedure has the following parameter.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `seqnum` | number | — | Yes | The sequence number of the archived redo log. | 

To find valid archived redo log sequence numbers, run the following query:

```
SELECT SEQUENCE#, FIRST_TIME, NEXT_TIME FROM V$ARCHIVED_LOG WHERE DEST_ID = 1 ORDER BY SEQUENCE# DESC FETCH FIRST 20 ROWS ONLY;
```

The following example downloads the log with sequence number 20.

```
SELECT rdsadmin.rdsadmin_archive_log_download.download_log_with_seqnum(seqnum => 20) 
       AS TASK_ID 
FROM   DUAL;
```

## Downloading a series of archived redo logs
<a name="Appendix.Oracle.CommonDBATasks.download-redo-logs.series"></a>

To download a series of archived redo logs to the `/rdsdbdata/log/arch` directory, use `download_logs_in_seqnum_range`. Your download is limited to 300 logs per request. The `download_logs_in_seqnum_range` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `start_seq` | number | — | Yes | The starting sequence number for the series. | 
| `end_seq` | number | — | Yes | The ending sequence number for the series. | 

The following example downloads the logs from sequence 50 to 100.

```
SELECT rdsadmin.rdsadmin_archive_log_download.download_logs_in_seqnum_range(start_seq => 50, end_seq => 100) 
       AS TASK_ID 
FROM   DUAL;
```