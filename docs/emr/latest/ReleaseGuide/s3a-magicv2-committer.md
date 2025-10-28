# S3A MagicV2 Committer

With the EMR-6.15.0 release, Amazon EMR introduces a new S3A committer type known as the MagicV2 committer. For comprehensive information
about this feature, please consult the relevant documentation sections.

The MagicV2 Committer represents an enhanced implementation of the open-source [MagicCommitter](https://javadoc.io/static/org.apache.hadoop/hadoop-aws/3.4.0/org/apache/hadoop/fs/s3a/commit/magic/MagicS3GuardCommitter.html "https://javadoc.io/static/org.apache.hadoop/hadoop-aws/3.4.0/org/apache/hadoop/fs/s3a/commit/magic/MagicS3GuardCommitter.html"), specifically designed
to optimize file writing to Amazon S3 through the S3A filesystem. Like its predecessor, it leverages Amazon S3's multipart upload
capabilities to eliminate the traditional list and rename operations typically associated with job and task commit phases.

Compared to the original MagicCommitter, the MagicV2 committer demonstrates superior performance by writing files to the job's output
location during the task commit phase, rather than the job commit phase. This approach enables distributed file writing and eliminates the
need for temporary commit metadata storage on Amazon S3, resulting in improved cost-effectiveness. Furthermore,
the MagicV2 committer provides enhanced flexibility by allowing file path overwrites across multiple threads during the commit process.

## Enable the MagicV2 Committer

To enable MagicV2 committer, pass the following configuration in your job configuration or use the core-site configuration to set the
property. For more information, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

```
mapreduce.outputcommitter.factory.scheme.s3a=org.apache.hadoop.fs.s3a.commit.S3ACommitterFactory
fs.s3a.committer.magic.enabled=true
fs.s3a.committer.name=magicv2
fs.s3a.committer.magic.track.commits.in.memory.enabled=true
```

For workloads that require overwriting the existing directory before committing or writing the new files, the following additional
configuration is needed, along with the previously mentioned configuration.

```
fs.s3a.committer.magic.overwrite.and.commit=true
fs.s3a.committer.magic.delete.directory.threads=`thread size`
```

The default value for the `threads` configuration is `20`. However, this parameter should be tuned when there are a
large number of directories to be overwritten for better performance. This is available only in EMR-7.2.0 and above.

## Considerations

- If the Java Virtual Machine (JVM) crashes or is killed while tasks are running and writing data to Amazon S3, incomplete
  multipart uploads are more likely to be left behind. For this reason, when you use the MagicV2 committer, be sure to
  follow the best practices for managing failed multipart uploads. For more information, see
  the [Best practices for working
  with Amazon S3 buckets](../ManagementGuide/emr-plan-upload-s3.md#emr-bucket-bestpractices "../ManagementGuide/emr-plan-upload-s3.md#emr-bucket-bestpractices") section in the Amazon EMR Management Guide.
- If a job fails, any files committed by the successful tasks will still be visible in the destination path. In such cases, the
  user will need to manually clean up the committed files before re-running the job on the same destination path.
- The MagicV2 committer consumes a small amount of memory for each file written by a task attempt until the task gets committed
  or aborted. In most jobs, the amount of memory ry consumed is negligible. However, in some cases where a single executor process
  handles a large number of tasks concurrently, it can put a lot of memory pressure, and the container or executor
  might run out of memory (OOM). Increasing the container or executor memory should solve this issue.
