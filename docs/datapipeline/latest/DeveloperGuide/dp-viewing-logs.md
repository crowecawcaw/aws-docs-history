AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Viewing Pipeline Logs

Pipeline-level logging is supported at pipeline creation by specifying an Amazon S3
location in either the console or with a `pipelineLogUri` in the
default object in SDK/CLI. The directory structure for each pipeline within that URI
is like the following:

```
`pipelineId`
    -`componentName`
        -`instanceId`
            -`attemptId`
```

For pipeline, `df-00123456ABC7DEF8HIJK`, the directory structure looks
like:

```
df-00123456ABC7DEF8HIJK
    -ActivityId_fXNzc
        -@ActivityId_fXNzc_2014-05-01T00:00:00
            -@ActivityId_fXNzc_2014-05-01T00:00:00_Attempt=1
```

For `ShellCommandActivity`, logs for `stderr`
and `stdout` associated with these activities are stored in the
directory for each attempt.

For resources like, `EmrCluster`, where an `emrLogUri` is
set, that value takes precedence. Otherwise, resources (including TaskRunner logs
for those resources) follow the above pipeline logging structure.

To view logs for a given pipeline run:

1. Retrieve the `ObjectId` by calling `query-objects` to get the exact object ID. For example:

```
aws datapipeline query-objects --pipeline-id <pipeline-id> --sphere ATTEMPT --region ap-northeast-1
```

`query-objects` is a paginated CLI and may return a pagination token if there are more executions for the given `pipeline-id`. You can use the token to go through all the attempts until you find the expected object. For example, a returned ObjectId would look like: `@TableBackupActivity_2023-05-020T18:05:18_Attempt=1`. 2. Using the ObjectId, retrieve the log location using:

```
aws datapipeline describe-objects —pipeline-id <pipeline-id> --object-ids <object-id> --query "pipelineObjects[].fields[?key=='@logLocation'].stringValue"
```

###### Error message of a failed activity

To get the error message, first get the ObjectId using `query-objects`.

After retrieving the failed ObjectId, use the `describe-objects` CLI to get the actual error message.

```
aws datapipeline describe-objects --region ap-northeast-1 --pipeline-id <pipeline-id> --object-ids <object-id> --query "pipelineObjects[].fields[?key=='errorMessage'].stringValue"
```

###### Cancel or rerun or mark as finished an object

Use the `set-status` CLI to cancel a running object, or re-run a failed object or mark a running object as Finished.

First, get the object ID using the `query-objects` CLI. For example:

```
aws datapipeline query-objects --pipeline-id <pipeline-id> --sphere INSTANCE --region ap-northeast-1
```

Use the `set-status` CLI to change the status of the desired object. For example:

```
aws datapipeline set-status —pipeline-id <pipeline-id> --region ap-northeast-1 --status TRY_CANCEL --object-ids <object-id>
```
