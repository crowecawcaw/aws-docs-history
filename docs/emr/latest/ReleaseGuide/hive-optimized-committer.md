# Enabling Hive EMRFS S3 optimized

committer

The Hive EMRFS S3 Optimized Committer is an alternative way using which EMR Hive
writes files for insert queries when using EMRFS. The Committer eliminates list and
rename operations done on Amazon S3 and improves application’s performance. The feature
is available beginning with EMR 5.34 and EMR 6.5.

## Enabling the committer

If you want to enable EMR Hive to use `HiveEMRFSOptimizedCommitter`
to commit data as the default for all Hive managed and external tables, use the
following `hive-site` configuration in EMR 6.5.0 or EMR 5.34.0
clusters.

```
[
   {
      "classification": "hive-site",
      "properties": {
         "hive.blobstore.use.output-committer": "true"
      }
   }
]
```

###### Note

Do not turn this feature on when `hive.exec.parallel` is set to
`true`.

## Limitations

The following basic restrictions apply to tags:

- Enabling Hive to merge small files automatically is not supported. The
  default Hive commit logic will be used even when the optimized committer
  is enabled.
- Hive ACID tables are not supported. The default Hive commit logic will
  be used even when the optimized committer is enabled.
- File naming nomenclature for files written is changed from Hive’s
  `<task_id>_<attempt_id>_<copy_n>` to
  `<task_id>_<attempt_id>_<copy_n>_<query_id>`.
  For example, a file named

`s3://warehouse/table/partition=1/000000_0` will be changed
to
`s3://warehouse/table/partition=1/000000_0-hadoop_20210714130459_ba7c23ec-5695-4947-9d98-8a40ef759222-1`.
The `query_id` here is a combination of the username, time
stamp, and UUID.

- When custom partitions are on different file systems (HDFS, S3), this
  feature is automatically disabled. The default Hive commit logic will be
  used when enabled.
