AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Locating Error Logs

This section explains how to find the various logs that AWS Data Pipeline writes, which you can use to determine
the source of certain failures and errors.

## Pipeline Logs

We recommend that you configure pipelines to create log files in a persistent
location, such as in the following example where you use the
`pipelineLogUri` field on a pipeline's `Default` object to
cause all pipeline components to use an Amazon S3 log location by default (you can
override this by configuring a log location in a specific pipeline
component).

###### Note

Task Runner stores its logs in a different location by default, which may be unavailable when the pipeline finishes and the instance that runs Task Runner terminates. For more information,
see [Verifying Task Runner Logging](dp-how-task-runner-user-managed.md#dp-verify-task-runner "dp-how-task-runner-user-managed.md#dp-verify-task-runner").

To configure the log location using the AWS Data Pipeline CLI in a pipeline JSON file,
begin your pipeline file with the following text:

```
{ "objects": [
{
  "id":"Default",
  "pipelineLogUri":"s3://amzn-s3-demo-bucket/error_logs"
},
...
```

After you configure a pipeline log directory, Task Runner creates a copy of
the logs in your directory, with the same formatting and file names described in the
previous section about Task Runner logs.

## Hadoop Job and Amazon EMR Step Logs

With any Hadoop-based activity such as [HadoopActivity](dp-object-hadoopactivity.md "dp-object-hadoopactivity.md"), [HiveActivity](dp-object-hiveactivity.md "dp-object-hiveactivity.md"), or [PigActivity](dp-object-pigactivity.md "dp-object-pigactivity.md") you can view Hadoop job
logs at the location returned in the runtime slot, hadoopJobLog. [EmrActivity](dp-object-emractivity.md "dp-object-emractivity.md") has its own logging features and those logs are stored using
the location chosen by Amazon EMR and returned by the runtime slot, emrStepLog. For more
information, see [View
Log Files](../../../emr/latest/DeveloperGuide/emr-manage-view-web-log-files.md "../../../emr/latest/DeveloperGuide/emr-manage-view-web-log-files.md") in the Amazon EMR Developer Guide.
