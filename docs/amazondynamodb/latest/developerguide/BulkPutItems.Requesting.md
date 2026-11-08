

# Running a bulk put items operation
<a name="BulkPutItems.Requesting"></a>

You provide an Amazon S3 location for input files and a target table. DynamoDB reports items it could not write to an output bucket that you provide. You choose what the output report contains through the [OutputType](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html#DDB-Type-OutputS3Configuration-OutputType) parameter: request `ERROR` for items that failed validation, `CONDITION_CHECK_FAILURE` for items that did not meet their condition, or both.

You can run a bulk put items operation using the [AWS CLI](AccessingDynamoDB.md#Tools.CLI) or the AWS SDKs. To use the AWS CLI, first install it and configure it with your AWS credentials. For more information, see [Accessing DynamoDB](AccessingDynamoDB.md).

**Note**  
Do not modify the Amazon S3 objects while the operation is in progress. Modifying input objects can cause the operation to fail.

**Topics**
+ [Starting a bulk put items operation](#BulkPutItems.Requesting.Start)
+ [Monitoring progress](#BulkPutItems.Requesting.Describe)
+ [Listing bulk operations](#BulkPutItems.Requesting.List)
+ [Cancelling an operation](#BulkPutItems.Requesting.Cancel)
+ [Concurrency and quotas](#BulkPutItems.Requesting.Limits)

## Starting a bulk put items operation
<a name="BulkPutItems.Requesting.Start"></a>

To start a bulk put items operation, call [StartBulkPutItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html) and provide the following required inputs:
+ [TableName](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html#DDB-StartBulkPutItems-request-TableName) – The name or ARN of the target table. The table must be `ACTIVE`, or `UPDATING` with a change that doesn't conflict with bulk writes. For details, see [Table state requirements](BulkPutItems.Considerations.md#BulkPutItems.Considerations.TableState).
+ [InputS3Configuration](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html) – The Amazon S3 location of your input files. You must specify [S3Bucket](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html#DDB-Type-InputS3Configuration-S3Bucket) and [InputFormat](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html#DDB-Type-InputS3Configuration-InputFormat). Optionally specify [S3BucketOwner](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html#DDB-Type-InputS3Configuration-S3BucketOwner), [S3KeyPrefix](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html#DDB-Type-InputS3Configuration-S3KeyPrefix), and [InputCompressionType](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html#DDB-Type-InputS3Configuration-InputCompressionType).
+ [OutputS3Configuration](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html) – The Amazon S3 location for the output report. You must specify `S3Bucket` and `OutputType`. An output configuration is mandatory.

The following optional parameters are also available:
+ [PerformanceTier](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html#DDB-StartBulkPutItems-request-PerformanceTier) – Choose `STANDARD` (default) or `ACCELERATED`. Standard suits most operations where completion time is flexible. Accelerated is designed for workloads where completion time is more rigid and targets higher throughput than Standard, so large operations can finish faster. For more information, see [Performance tiers](BulkPutItems.Tiers.md).
+ **MaxWriteRequestUnits** – In the context of bulk operation, [MaxWriteRequestUnits](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html#DDB-StartBulkPutItems-request-MaxWriteRequestUnits) is the maximum number of write request units per second that the bulk operation can write with. The limit applies to the total write request units that the operation consumes on the table and on all of its indexes. For example, on a table with two global secondary indexes that both project the item, a limit of 1,024 allows about 340 items of 1 KB per second. It is to be used if you have downstream operations sensitive to higher write throughputs. This setting applies only to the bulk operation and has no relation to the table's provisioned or on-demand capacity. The minimum value is 1,024.
+ [ClientToken](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html#DDB-StartBulkPutItems-request-ClientToken) – An idempotency token. If you retry a request with the same client token, DynamoDB returns the existing operation rather than creating a new one. DynamoDB keeps the token for 8 hours.

### Supported input formats
<a name="BulkPutItems.Requesting.Start.Formats"></a>

`InputFormat` accepts the following values:
+ `DYNAMODB_JSON`
+ `ION`

`InputCompressionType` accepts the following values:
+ `GZIP`
+ `ZSTD`
+ `NONE`

### Output types
<a name="BulkPutItems.Requesting.Start.OutputType"></a>

`OutputType` is a list and you can request one or both of the following report types:
+ `ERROR` – Provides a report of the items that failed for deterministic reasons such as validation errors.
+ `CONDITION_CHECK_FAILURE` – Provides a report of the items whose per-item condition expression was not met.

### Starting an operation (AWS CLI)
<a name="BulkPutItems.Requesting.Start.CLI"></a>

The following example starts a bulk put items operation that reads DynamoDB JSON files from an Amazon S3 bucket and outputs the report to a separate bucket.

```
aws dynamodb start-bulk-put-items \
    --table-name MusicCollection \
    --input-s3-configuration '{
        "S3Bucket": "amzn-s3-demo-bucket",
        "S3KeyPrefix": "daily/",
        "InputFormat": "DYNAMODB_JSON",
        "InputCompressionType": "NONE"
    }' \
    --output-s3-configuration '{
        "OutputType": ["ERROR"],
        "S3Bucket": "amzn-s3-demo-bucket1",
        "S3KeyPrefix": "bulk-put-items-output/"
    }' \
    --performance-tier STANDARD
```

### Starting an operation (Python)
<a name="BulkPutItems.Requesting.Start.Python"></a>

The following example uses the AWS SDK for Python (Boto3) to start a bulk put items operation.

```
import boto3

client = boto3.client("dynamodb")

response = client.start_bulk_put_items(
    TableName="MusicCollection",
    InputS3Configuration={
        "S3Bucket": "amzn-s3-demo-bucket",
        "S3KeyPrefix": "daily/",
        "InputFormat": "DYNAMODB_JSON",
        "InputCompressionType": "NONE",
    },
    OutputS3Configuration={
        "S3Bucket": "amzn-s3-demo-bucket1",
        "OutputType": ["ERROR", "CONDITION_CHECK_FAILURE"],
    },
    PerformanceTier="STANDARD",
)

bulk_operation_arn = response["BulkOperationDescription"]["BulkOperationArn"]
print(f"Started operation: {bulk_operation_arn}")
```

## Monitoring progress
<a name="BulkPutItems.Requesting.Describe"></a>

Call [DescribeBulkOperation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBulkOperation.html) to monitor the progress of a bulk put items operation. Three fields report progress:
+ [ProcessedItemCount](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-ProcessedItemCount) – The number of input records read so far, including records that failed validation or a condition check. This is a count of records read, not items written.
+ **ProcessedInputBytes** – The number of bytes read and processed from Amazon S3 so far.
+ **TotalInputBytes** – The total size of all input objects in Amazon S3.

To estimate progress, compare [ProcessedInputBytes](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-ProcessedInputBytes) to [TotalInputBytes](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-TotalInputBytes). For example, if your input totals 50 GB and `ProcessedInputBytes` shows 35 GB, the operation is roughly 70 percent complete.

`TotalInputBytes` is absent from the response until DynamoDB calculates the total during initial input validation. The calculation time varies with the operation and service conditions. Poll `DescribeBulkOperation` until the field is present.

The progress fields update periodically and can update at different times. They are not live counters. Do not rely on a fixed refresh interval.

### Status values
<a name="BulkPutItems.Requesting.Describe.Status"></a>

The [BulkOperationStatus](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-BulkOperationStatus) field returns one of the following values:
+ `IN_PROGRESS` – The operation is reading input and writing items.
+ `COMPLETED` – All input was read and `FailedItemCount` is 0. Items can still have failed a condition check. If you requested it, read the `CONDITION_CHECK_FAILURE` report to find them.
+ `COMPLETED_WITH_ERRORS` – All input was read and `FailedItemCount` is above 0. Review the `ERROR` report.
+ `CANCELLING` – A cancellation request is being applied.
+ `CANCELLED` – The operation stopped in response to a cancellation request. Items already written remain in the table. `CANCELLED` does not mean data is missing. The completion manifest records what was processed. `FailureCode` is `RequestCancelled`.
+ `FAILED` – The operation could not complete. See the failure code.

If an operation exceeds the maximum processing time, DynamoDB stops ingestion and the operation ends `FAILED` with failure code `Timeout` and the message "The bulk operation exceeded the maximum allowed processing time." Timeout is an expected outcome for a very large input, or for an operation whose rate you cap with `MaxWriteRequestUnits`, rather than a fault. Items already written stay in the table, and the completion manifest records how far each object was processed, so you can resubmit the remainder. Raising `MaxWriteRequestUnits` in the `StartBulkPutItems` call or splitting the input into more objects reduces the chance of a timeout.

The following table lists the failure codes that a `FAILED` operation can report.


| Failure code | Cause | What to do | 
| --- | --- | --- | 
| `Timeout` | The operation exceeded the maximum processing time | Resubmit the remainder from the completion manifest | 
| `ValidationException` | An error stopped DynamoDB reading an input object, and DynamoDB could not confirm that it read all stored input bytes | Fix the record, then resubmit it with the records outside `processedRanges` | 
| `InputObjectTooLarge` | An input object exceeds 5 GB | Split the object | 
| `S3ObjectsCountLimitExceeded` | More than 50,000 input objects | Reduce the object count or request a quota increase | 
| `SizeLimitExceeded` | Total input above the per-request limit (100 GB for Standard, 1 TB for Accelerated) | Split the input, or use Accelerated | 
| `ObjectModifiedInS3DuringImport` | An input object changed during the run | Keep input objects unchanged while the operation runs | 
| `KmsAccessDeniedException`, `KmsDisabledException`, `KmsNotFoundException`, `KmsInvalidKeyUsageException`, `KmsInvalidStateException` | DynamoDB could not use an AWS KMS key for the table or the Amazon S3 objects during the operation | Check the key state and the caller's key permissions | 
| `S3AccessDenied` | DynamoDB was denied access to the input or output location in Amazon S3. This code also occurs when `S3BucketOwner` does not match the bucket owner. | Check the caller's Amazon S3 permissions, the bucket policy, and `S3BucketOwner`. | 
| `ResourceInUseException` | Another operation on the same table already started | Wait for that operation to finish, then start again | 
| `DynamoDBResourceNotFoundException` | The table was not found or was not accessible | Verify the table name and state | 
| `DynamoDBAccessDeniedException` | The caller no longer has permission to write to the table | Restore `dynamodb:BulkPutItems` on the table, then resubmit the remainder | 
| `DynamoDBItemCollectionSizeLimitExceededException` | An item collection on a table with a local secondary index exceeded the size limit | Reduce the data for that partition key value | 

If DynamoDB cannot output the completion manifest to the output location, the operation ends `FAILED` even if every item was written. The failure message starts with "Manifest is not available." and the failure code identifies the cause, for example `S3AccessDenied`. Items already written stay in the table. Check the caller's Amazon S3 and AWS KMS permissions for the output prefix, then compare the table with your input to find what was written.

### Describing an operation (AWS CLI)
<a name="BulkPutItems.Requesting.Describe.CLI"></a>

```
aws dynamodb describe-bulk-operation \
    --bulk-operation-arn arn:aws:dynamodb:us-east-1:111122223333:bulk-operation/01759414677739-041d6d92
```

### Describing an operation (Python)
<a name="BulkPutItems.Requesting.Describe.Python"></a>

```
import boto3

client = boto3.client("dynamodb")

response = client.describe_bulk_operation(
    BulkOperationArn="arn:aws:dynamodb:us-east-1:111122223333:bulk-operation/01759414677739-041d6d92"
)

status = response["BulkOperationDescription"]["BulkOperationStatus"]
processed_items = response["BulkOperationDescription"].get("ProcessedItemCount", 0)
processed_bytes = response["BulkOperationDescription"].get("ProcessedInputBytes", 0)
total_bytes = response["BulkOperationDescription"].get("TotalInputBytes")

print(f"Status: {status}")
print(f"Items processed: {processed_items}")

if total_bytes:
    pct = (processed_bytes / total_bytes) * 100
    print(f"Progress: {pct:.1f}%")
```

## Listing bulk operations
<a name="BulkPutItems.Requesting.List"></a>

Call [ListBulkOperations](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListBulkOperations.html) to retrieve a paginated list of bulk operations in your account. Each page returns a maximum of 25 operations.

### Listing operations (AWS CLI)
<a name="BulkPutItems.Requesting.List.CLI"></a>

```
aws dynamodb list-bulk-operations
```

The AWS CLI paginates automatically and prints all available pages. To page manually, turn off auto-pagination and use `--max-items` with `--starting-token`.

```
aws dynamodb list-bulk-operations \
    --max-items 25 \
    --starting-token "{{token-from-a-previous-NextToken}}"
```

### Listing operations (Python)
<a name="BulkPutItems.Requesting.List.Python"></a>

```
import boto3

client = boto3.client("dynamodb")

paginator = client.get_paginator("list_bulk_operations")

for page in paginator.paginate():
    for op in page["BulkOperationsSummaryList"]:
        print(f"{op['BulkOperationArn']} - {op['BulkOperationStatus']}")
```

## Cancelling an operation
<a name="BulkPutItems.Requesting.Cancel"></a>

Call [CancelBulkOperation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CancelBulkOperation.html) to stop an in-progress operation. The operation transitions to `CANCELLING` and then to `CANCELLED`.

**Important**  
Items already written before cancellation are *not* rolled back. They remain in the table and are immediately readable.

While the status is `CANCELLING`, the progress counters can be lower than the final values. Wait for `CANCELLED` before you check your results. In the manifest, a partly processed object has the status `PARTIALLY_PROCESSED`, and `processedRanges` lists the records that DynamoDB processed. Records outside `processedRanges` were not processed. Resubmit them, together with any records from the `ERROR` report that you corrected.

### Cancelling an operation (AWS CLI)
<a name="BulkPutItems.Requesting.Cancel.CLI"></a>

```
aws dynamodb cancel-bulk-operation \
    --bulk-operation-arn arn:aws:dynamodb:us-east-1:111122223333:bulk-operation/01759414677739-041d6d92
```

### Cancelling an operation (Python)
<a name="BulkPutItems.Requesting.Cancel.Python"></a>

```
import boto3

client = boto3.client("dynamodb")

client.cancel_bulk_operation(
    BulkOperationArn="arn:aws:dynamodb:us-east-1:111122223333:bulk-operation/01759414677739-041d6d92"
)

print("Cancellation requested. Items already written remain in the table.")
```

## Concurrency and quotas
<a name="BulkPutItems.Requesting.Limits"></a>

For the quotas that apply to bulk put items operations, see [Bulk put items](ServiceQuotas.md#limits-bulk-put-items).

You cannot start a bulk put items operation on a table that is creating an index. Attempting to do so returns a `ResourceInUseException`.

A table can have only one bulk put items operation in progress at a time. If another operation is in progress on the table, `StartBulkPutItems` returns a `ResourceInUseException`. If you start several operations on the same table at the same time, each call can return an ARN. One operation then runs, and the others fail with `FailureCode` `ResourceInUseException`. Call `DescribeBulkOperation` to confirm that your operation is running. To load several tables at the same time, start one operation for each table.