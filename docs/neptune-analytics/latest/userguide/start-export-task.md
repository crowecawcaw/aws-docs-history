# start-export-task

This command starts an export task on a graph in Neptune Analytics. It allows you to export your graph into columnar structured .csv
and .parquet files. Calling export on a graph will generate a unique `taskId` that you can use to track the progress of
your export. When an export is triggered, a clone of your graph is created to process the export request, allowing your
graph to continue servicing queries and analytics with no performance impact.

## start-export-task syntax

```
aws neptune-graph start-export-task \
 --graph-identifier <GRAPH_ID> \
 --region <region> \
 --role-arn <arn> \
 --format <format> \
 [--parquet-type <parquet-type>] \
 --kms-key-identifier <kms-key> \
 --destination <s3-url> \
 [--export-filter <filter-json>] #See filtering section for details.
```

## start-export-task inputs

- `--graph-identifier <GRAPH_ID>` - The unique identifier of the Neptune Analytics graph to export.
- `--region <region>` - The AWS region where the Neptune Analytics graph is located.
- `--role-arn <arn>` - The ARN of an IAM role that grants Neptune Analytics the necessary permissions
  to access the Amazon S3 bucket for the export.
- `--format <format>` - The output format for the exported data, either CSV or PARQUET.
- `--kms-key-identifier <kms-key>` - The AWS KMS key to use for server-side encryption of the exported data in Amazon S3.
  For more information see [Create and configure IAM role and AWS KMS key](import-export-permissions.md#create-iam-and-kms "import-export-permissions.md#create-iam-and-kms").
- `--destination <s3-url>` - The Amazon S3 location where the exported data will be written. The provided
  `role-arn` must have permission to write to this location. Exported data will be written to this folder in a
  sub-directory given by the export taskId. See [start-export-task output](#start-export-task-output "#start-export-task-output")
  for more information.
- `--export-filter <filter-json>` - A JSON object that specifies which vertices and edges to include
  in the export, based on their labels and properties. This field is optional, and if not provided, a value of
  `‘{}'` is used, corresponding to an export of the whole property graph. For more detail on the export filter
  JSON object, see [Specifying a filter](export-filter.md "export-filter.md") for expanded syntax and examples.

## start-export-task output

The response from the `start-export-task` is a JSON string. The `taskId` is the most significant value
in the return, as this can be used to identify the export process when calling
[get-export-task](get-export-task.md "get-export-task.md") or
[list-export-task](list-export-task.md "list-export-task.md"), as well as identifying the export process in CloudWatch logs.
Other values in the return can be used to keep track of which expert parameters were invoked for a given `taskId`.

```
{
    "graphId": "$GRAPH_ID", // The identifier of the graph being exported.
    "roleArn": "$arn", // The ARN of the IAM role being used to give
                       // export the required permissions.
    "taskId": "$taskId", // A unique id corresponding to the requested export.
    "status": "INITIALIZING", // The status of the export.
                              // One of INITIALIZING,
                              //  EXPORTING,
                              //  SUCCEEDED,
                              //  FAILED,
                              //  CANCELLING,
                              //  CANCELLED
    "format": "PARQUET", // The requested format of the export.
                         // One of CSV or PARQUET.
    "destination": "$s3-uri", // The Amazon S3 location where the exported
                              // data will be written.
    "kmsKeyIdentifier": "$kms_key", // The AWS KMS key to use for server-side
                                    // encryption of the exported data in Amazon S3.
    "parquetType": "COLUMNAR" // If a Parquet export was requested,
                              // gives the Parquet type.
}
```
