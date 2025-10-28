# get-export-task

This command queries the status of an export task that was started using the `start-export-task` command. This
gives information such as the current state of the export, the approximate progress of the export, how long the export has
been running etc.

###### Note

When exporting a graph in which the vertices have no vertex labels or vertex properties, the
`numVerticesWritten` is expected to be 0 in the response of get-export-task.

## get-export-task syntax

```
aws neptune-graph get-export-task \
--task-identifier <taskId> \
--region <region>
```

## get-export-task inputs

- `--task-identifier <taskId>` - The unique identifier of the export task for which you want to retrieve
  the status.
- `--region <region>` - The AWS region where the Neptune Analytics graph is located.

## get-export-task output

```
{
    // The unique identifier of the Neptune Analytics graph that was exported
    "graphId": "$GRAPH_ID",

    // The ARN of the IAM role that was used to grant Neptune Analytics the necessary permissions to access the Amazon S3 bucket for the export
    "roleArn": "$arn",

    // The unique identifier of the export task
    "taskId": "$taskId",

    // The current status of the export task,
    // which is one of INITIALIZING, EXPORTING, SUCCEEDED, FAILED, CANCELLING, CANCELLED
    "status": "SUCCEEDED",

    // The output format of the exported data, which is "PARQUET"/"CSV".
    "format": "PARQUET",

    // The Amazon S3 location where the exported data was written
    "destination": "$s3-url",

    // The AWS KMS key used for server-side encryption of the exported data in Amazon S3
    "kmsKeyIdentifier": "$kms_key",

    // The type of Parquet file generated, which is "COLUMNAR".
    "parquetType": "COLUMNAR",

    // If provided, the exportFilter being used with the export task.
    "exportFilter": "$export_json"

    // Details of export progress.
    "exportTaskDetails": {
    // The time when the export began
     "startTime": "2024-10-07T17:14:03.502000-04:00",

     // The amount of time that has been spent executing the export request.
     "timeElapsedSeconds": 360,

    // The percentage of relevant data in the database that has been scanned for export.
     "progressPercentage": 100,

    // The number of total vertices which are included in the exported files.
     "numVerticesWritten": 30090921,

    // The number of total edges which are included in the exported files.
     "numEdgesWritten": 177654205
}
```
