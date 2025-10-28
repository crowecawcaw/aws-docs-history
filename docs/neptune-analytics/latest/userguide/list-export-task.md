# list-export-task

Since you may have many graphs in your account, and the export functionality includes the ability to specify filters and
different filetypes, you may execute multiple exports against your graph over time. The `list-export-tasks` CLI
gives returns all Neptune Analytics exports that have been triggered in your account.

## list-export-task syntax

```
aws neptune-graph list-export-tasks
  --region <REGION>
```

## list-export-task inputs

- `--region <region>` - The AWS region where the Neptune Analytics graph is located.

## list-export-task output

```
{
    // The unique identifier of the Neptune Analytics graph that was exported
    "graphId": "$GRAPH_ID",

    // The ARN of the IAM role that was used to grant Neptune Analytics the necessary permissions to access the Amazon S3 bucket for the export
    "roleArn": "$arn",

    // The unique identifier of the export task
    "taskId": "$taskId",

    // The current status of the export task,
    // which is one of "SUCCEEDED"/"FAILED" etc.
    "status": "SUCCEEDED",

    // The output format of the exported data, which is "PARQUET"/"CSV".
    "format": "PARQUET",

    // The Amazon S3 location where the exported data was written
    "destination": "$s3-url",

    // The AWS KMS key used for server-side encryption of the exported data in S3
    "kmsKeyIdentifier": "$kms_key",

    // The type of Parquet file generated, which is "COLUMNAR".
    "parquetType": "COLUMNAR",

    // If there is an error, a reason will be provided.
    "statusReason": "$failureReason"
}
```
