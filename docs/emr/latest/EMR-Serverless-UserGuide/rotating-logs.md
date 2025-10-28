# Rotating logs

Amazon EMR Serverless can rotate Spark application logs and
event logs. Log rotation helps with the issue of long running jobs generating large log files
that can take up all of your disk space. Rotating logs helps you save disk storage and
reduces the amount of job failures because you have no more space left on your disk.

Log rotation is enabled by default and is available only for Spark jobs.

**Spark event logs**

###### Note

Spark event log rotation is available across all Amazon EMR release labels.

Instead of generating a single event log file, EMR Serverless rotates the event log
at a regular time interval and removes the older event log files. Rotating logs doesn't
affect the logs uploaded to the S3 bucket.

**Spark application logs**

###### Note

Spark application log rotation is available across all Amazon EMR release labels.

EMR Serverless also rotates the spark application logs for drivers and executors, such as
`stdout` and `stderr` files. You can access the latest log files by choosing
the log links in Studio by using the Spark History Server and Live UI links. Log files are the
truncated versions of the latest logs. To refer to the older rotated logs, specify an Amazon S3 location when
storing logs. Refer to [Logging for EMR Serverless with Amazon S3 buckets](logging.md#jobs-log-storage-s3-buckets "logging.md#jobs-log-storage-s3-buckets") for more information.

You can find the latest log files at the following location. EMR Serverless
refreshes the files every 15 seconds. These files can range from 0 MB to 128 MB.

```
<example-S3-logUri>/applications/<application-id>/jobs/<job-id>/SPARK_DRIVER/stderr.gz
```

The following location contains the older rotated files. Each file is 128 MB.

```
<example-S3-logUri>/applications/<application-id>/jobs/<job-id>/SPARK_DRIVER/archived/stderr_<index>.gz
```

The same behavior applies to Spark executors as well. This change is only applicable to S3 logging. Log rotation doesn't introduce any changes to log streams uploaded to Amazon CloudWatch.

EMR Serverless releases 7.1.0 and higher support retry attempts for streaming and batch jobs. If you enabled retry attempts with your job, EMR Serverless adds a prefix to the log path for such jobs so you can better track
and distinguish the logs from one another. This path contains all rotated logs.

```
'/applications/<applicationId>/jobs/<jobId>/attempts/<attemptNumber>/'.
```
