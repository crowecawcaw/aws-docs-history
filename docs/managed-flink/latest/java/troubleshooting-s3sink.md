Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# S3 StreamingFileSink FileNotFoundExceptions

Managed Service for Apache Flink applications can run into In-progress part file `FileNotFoundException` when starting from snapshots if an
In-progress part file referred to by its savepoint is missing. When this failure mode occurs, the Managed Service for Apache Flink application’s operator state
is usually non-recoverable and must be restarted without snapshot using `SKIP_RESTORE_FROM_SNAPSHOT`. See following example stacktrace:

```
java.io.FileNotFoundException: No such file or directory: s3://amzn-s3-demo-bucket/pathj/INSERT/2023/4/19/7/_part-2-1234_tmp_12345678-1234-1234-1234-123456789012
        at org.apache.hadoop.fs.s3a.S3AFileSystem.s3GetFileStatus(S3AFileSystem.java:2231)
        at org.apache.hadoop.fs.s3a.S3AFileSystem.innerGetFileStatus(S3AFileSystem.java:2149)
        at org.apache.hadoop.fs.s3a.S3AFileSystem.getFileStatus(S3AFileSystem.java:2088)
        at org.apache.hadoop.fs.s3a.S3AFileSystem.open(S3AFileSystem.java:699)
        at org.apache.hadoop.fs.FileSystem.open(FileSystem.java:950)
        at org.apache.flink.fs.s3hadoop.HadoopS3AccessHelper.getObject(HadoopS3AccessHelper.java:98)
        at org.apache.flink.fs.s3.common.writer.S3RecoverableMultipartUploadFactory.recoverInProgressPart(S3RecoverableMultipartUploadFactory.java:97)
...
```

Flink `StreamingFileSink` writes records to filesystems supported by the [File Systems](https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/deployment/filesystems/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/deployment/filesystems/overview/"). Given that the incoming streams can be unbounded, data is
organized into part files of finite size with new files added as data is written. Part lifecycle and rollover policy determine the timing,
size and the naming of the part files.

During checkpointing and savepointing (snapshotting), all Pending files are renamed and committed. However, In-progress part files are not committed but renamed and their reference is kept within checkpoint or savepoint metadata to be used when restoring jobs.
These In-progress part files will eventually rollover to Pending, renamed and committed by a subsequent checkpoint or savepoint.

Following are the root causes and mitigation for missing In-progress part file:

- Stale snapshot used to start the Managed Service for Apache Flink application – only the latest system snapshot taken when an application is stopped or updated can be used to start a Managed Service for Apache Flink application with Amazon S3 StreamingFileSink. To avoid this class of failure, use the latest system snapshot.
  - This happens for example when you pick a snapshot created using `CreateSnapshot` instead of a system-triggered Snapshot
    during stop or update. The older snapshot’s savepoint keeps an out-of-date reference to In-progress part file that has been renamed
    and committed by subsequent checkpoint or savepoint.
  - This can also happen when a system triggered snapshot from non-latest Stop/Update event is picked. An example is an application with system snapshot disabled but has `RESTORE_FROM_LATEST_SNAPSHOT`
    configured. Generally, Managed Service for Apache Flink applications with Amazon S3 StreamingFileSink should always have system snapshot enabled and `RESTORE_FROM_LATEST_SNAPSHOT`
    configured.

- In-progress part file removed – As the In-progress part file is located in an S3 bucket, it can be removed by other components or actors which have access to the bucket.
  - This can happen when you have stopped your app for too long and the In-progress part file
    referred to by your app’s savepoint has been removed by [S3 bucket MultiPartUpload](../../../AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.md "../../../AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.md") lifecycle policy.
    To avoid this class of failure, make sure that your S3 Bucket MPU lifecycle policy covers a sufficiently large period for your use case.
  - This can also happen when the In-progress part file has been removed manually or by another one of your system’s components. To avoid this class of failure, please make sure that In-progress part files are not removed by other actors or components.

- Race condition where an automated checkpoint is triggered after savepoint – This
  affects Managed Service for Apache Flink versions up to and including 1.13. This issue is fixed in
  Managed Service for Apache Flink version 1.15. Migrate your application to the latest version of
  Managed Service for Apache Flink to prevent recurrence. We also suggest migrating from
  StreamingFileSink to [FileSink](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/datastream/filesystem/#file-sink "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/datastream/filesystem/#file-sink").
  - When applications are stopped or updated, Managed Service for Apache Flink triggers a savepoint and stops the application in two steps. If an automated checkpoint triggers between the two steps, the savepoint will be unusable as its In-progress part file would be renamed and potentially committed.
