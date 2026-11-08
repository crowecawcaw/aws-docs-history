

# Bulk put items output and reconciliation
<a name="BulkPutItems.Output"></a>

When a bulk put items operation completes, DynamoDB outputs a report to the Amazon S3 bucket you specified in [OutputS3Configuration](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html). This report contains details about items that were not written.

**Topics**
+ [Report types](#BulkPutItems.Output.Types)
+ [Counts from DescribeBulkOperation](#BulkPutItems.Output.Counts)
+ [Reconciling results](#BulkPutItems.Output.Reconciliation)
+ [Manifest file](#BulkPutItems.Output.Manifest)
+ [Output file layout](#BulkPutItems.Output.FileLayout)
+ [Billing for reports and failed items](#BulkPutItems.Output.Billing)
+ [Permissions for the output bucket](#BulkPutItems.Output.Permissions)
+ [Understanding BulkOperationUsage](#BulkPutItems.Output.Usage)

## Report types
<a name="BulkPutItems.Output.Types"></a>

When you start the operation, the [OutputType](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html#DDB-Type-OutputS3Configuration-OutputType) parameter specifies which categories of items appear in the report. You can request one or both of the following types.


| OutputType value | Contents | 
| --- | --- | 
| ERROR | Items that failed for deterministic reasons such as validation errors (for example, an item exceeding the maximum item size, or a missing required key attribute). | 
| CONDITION\_CHECK\_FAILURE | Items whose per-item condition expression was not met. For example, an attribute\_not\_exists(id) condition that failed because the item already exists in the table. | 

## Counts from DescribeBulkOperation
<a name="BulkPutItems.Output.Counts"></a>

The [DescribeBulkOperation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBulkOperation.html) response provides the following counts:
+ **ProcessedItemCount** – The number of input records read during the operation, including records that failed validation or a condition check. This is a count of records read, not items written.
+ **FailedItemCount** – The number of items that failed for deterministic reasons, such as validation errors. Condition-check failures are not included in this count.

**Important**  
Condition-check failures are not exposed as a separate count in the `DescribeBulkOperation` response. To find these items, see [Reconciling results](#BulkPutItems.Output.Reconciliation).

## Reconciling results
<a name="BulkPutItems.Output.Reconciliation"></a>

To get a complete picture of your operation results, follow this workflow:

1. Call `DescribeBulkOperation` until the status is `COMPLETED`, `COMPLETED_WITH_ERRORS`, `CANCELLED`, or `FAILED`. Record [ProcessedItemCount](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-ProcessedItemCount) and [FailedItemCount](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-FailedItemCount).

1. List all objects that start with `{{output-prefix}}/AWSDynamoDB/BulkOperation/{{account-id}}:{{operation-id}}`. This returns the manifest and every report file. If no manifest exists, check `FailureCode`. Read the manifest. For each input object, check `fileProcessingStatus` and `processedRanges`, and confirm that `etag` matches your object. Then read every report file. To list and read these objects, the caller needs `s3:ListBucket` and `s3:GetObject` on the output bucket. The example write policy does not grant those read permissions.

1. Use the Amazon S3 report to identify specific items that require action, such as correcting malformed items and resubmitting them, or reviewing items that failed a condition check.

Bulk put items does not need these read permissions. Grant them in a separate statement to the principal that checks the results.

This approach (API counts plus Amazon S3 report parsing) gives you the most accurate reconciliation. The API provides the high-level summary, and the Amazon S3 report provides the per-item detail.

## Manifest file
<a name="BulkPutItems.Output.Manifest"></a>

In addition to the report files, DynamoDB outputs a manifest file to the output location. The manifest reports the processing status of each input object, so you can discover which input objects were not processed, or were only partly processed. DynamoDB outputs the manifest to the following path:

```
s3://{{output-bucket}}/{{output-prefix}}/AWSDynamoDB/BulkOperation/{{account-id}}:{{operation-id}}/manifest-files.json
```

The manifest contains one JSON object per input object. The manifest is uncompressed JSON Lines. The report files are gzip-compressed. Each object has the following fields:
+ **inputSourceArn** – Identifies the input object in Amazon S3.
+ **fileProcessingStatus** – How completely DynamoDB processed that object.
+ **processedRanges** – The ranges of item indexes that DynamoDB processed, as an array of `[start, end]` pairs. The array is empty when DynamoDB processed no records, and for an input object that contains no items.
+ **etag** – The entity tag of the input object.

The `fileProcessingStatus` field takes one of the following values:
+ **FULLY\_PROCESSED** – DynamoDB processed every item in the object. For an object with no items, `processedRanges` is empty.
+ **PARTIALLY\_PROCESSED** – DynamoDB did not process every item in the object. `processedRanges` shows the processed range and can be empty, for example when the first record cannot be parsed.
+ **NOT\_PROCESSED** – The operation ended before DynamoDB reached this object, for example because the operation was cancelled, failed, or timed out. DynamoDB outputs the manifest only after the operation ends, so this status never means the object is still waiting to be processed.
+ **NOT\_AVAILABLE** – DynamoDB could not confirm exactly how much of this object it processed, so it reports no ranges rather than risk reporting items as processed when they were not. Treat the object as not fully processed.

The following example shows one line per status value. Each line is a single JSON object.

```
{"inputSourceArn":"arn:aws:s3:::amzn-s3-demo-bucket/bulk-input/customers-done.json.gz","fileProcessingStatus":"FULLY_PROCESSED","processedRanges":[[0,9999]],"etag":"9b2cf535f27731c974343645a3985328"}
{"inputSourceArn":"arn:aws:s3:::amzn-s3-demo-bucket/bulk-input/orders-partial.json.gz","fileProcessingStatus":"PARTIALLY_PROCESSED","processedRanges":[[0,4999]],"etag":"8f14e45fceea167a5a36dedd4bea2543"}
{"inputSourceArn":"arn:aws:s3:::amzn-s3-demo-bucket/bulk-input/inventory-queued.json.gz","fileProcessingStatus":"NOT_PROCESSED","processedRanges":[],"etag":"c9f0f895fb98ab9159f51fd0297e236d"}
{"inputSourceArn":"arn:aws:s3:::amzn-s3-demo-bucket/bulk-input/placeholder-not-available.json.gz","fileProcessingStatus":"NOT_AVAILABLE","processedRanges":[],"etag":"45c48cce2e2d7fbdea1afc51c7c6ad26"}
```

In the `FULLY_PROCESSED` example, the range `[0,9999]` represents an object whose 10,000 items were all processed. In the `PARTIALLY_PROCESSED` example, the range `[0,4999]` means that items 0 through 4999 were processed and the rest were not.

Use the manifest to identify input objects that were not processed, or were only partly processed. This is distinct from individual items that failed or whose condition was not met, which are reported in the per-item output. For more information about the per-item output, see [Report types](#BulkPutItems.Output.Types).

## Output file layout
<a name="BulkPutItems.Output.FileLayout"></a>

DynamoDB outputs one directory per internal job, for example `{{output-prefix}}/AWSDynamoDB/BulkOperation/{{account-id}}:{{operation-id}}-{{n}}/output/errors/output-{{NNNNN}}.json.gz`, with a matching `condition-check-failures/` directory. Output files are gzip-compressed JSON Lines. DynamoDB closes each output file at 200 MiB and starts a new one, so output files can appear while the operation is still `IN_PROGRESS`.

Report records include `itemLocation` and `errorMessages`. `itemLocation` contains `inputSourceArn` and `itemIndex`. `itemIndex` can be absent, for example when a truncated record stops DynamoDB from reading the rest of the object. Condition-check-failure records also include `newImage` and `oldImage`, so condition-check output can be larger than the input it describes. `ERROR` records can omit `newImage`, for example for an item that exceeds the maximum item size or a record with an invalid condition operand. DynamoDB outputs a file for a requested report type only if at least one item belongs to that type. If `S3BucketOwner` does not match the output bucket owner, the operation fails and outputs no report or manifest. An operation that fails with `ResourceInUseException` because another operation is in progress on the table outputs no manifest or report.

## Billing for reports and failed items
<a name="BulkPutItems.Output.Billing"></a>

The following billing details apply to bulk put items output:
+ **Report storage** – Report objects in Amazon S3 are billed at standard Amazon S3 storage rates.
+ **Failed items** – Items rejected by validation before a table write is attempted are not metered or billed as table writes. Items that reach the table and fail a condition check are metered as table writes and billed. A condition check on a missing item is reported as 1,024 base-table bytes. Service-side failed attempts that do not produce a write or condition-check result are not metered.

## Permissions for the output bucket
<a name="BulkPutItems.Output.Permissions"></a>

DynamoDB reads the input and outputs the report and manifest with the credentials of the IAM principal that calls `StartBulkPutItems`. You do not grant access to a DynamoDB service principal. The input and output buckets can be in different AWS accounts, and the input bucket can be in a different AWS Region from the table. For the minimum permissions required, see [IAM permissions](BulkPutItems.Considerations.md#BulkPutItems.Considerations.IAM). Bulk put items does not require `s3:PutObjectAcl` (it sets no ACL on output objects), so its output-bucket policy is narrower than the one used by DynamoDB export to Amazon S3.

If the output bucket uses server-side encryption with an AWS KMS key, you can specify the encryption algorithm and key ID using the [S3SseAlgorithm](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html#DDB-Type-OutputS3Configuration-S3SseAlgorithm) and [S3SseKmsKeyId](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html#DDB-Type-OutputS3Configuration-S3SseKmsKeyId) parameters in `OutputS3Configuration`.

## Understanding BulkOperationUsage
<a name="BulkPutItems.Output.Usage"></a>

The `DescribeBulkOperation` response includes a [BulkOperationUsage](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-BulkOperationUsage) field that reports bytes written for each destination. This field maps to your bill. Bulk operations report usage through `BulkOperationUsage` rather than through the `ConsumedCapacity` field returned by item-level operations such as `PutItem`.

The following example shows the structure of `BulkOperationUsage`:

```
"BulkOperationUsage": [{
    "TableName": "Orders",
    "BulkPutBytes": 1792000,
    "Table": {"BulkPutBytes": 1024000},
    "LocalSecondaryIndexes": {"lsi1": {"BulkPutBytes": 256000}},
    "GlobalSecondaryIndexes": {"gsi1": {"BulkPutBytes": 512000}},
    "VectorIndexes": {"vec1": {"BulkPutVectorBytes": 42000}}
}]
```

Each index write is metered independently. Items rejected by validation add no bytes to `BulkOperationUsage`. Bulk put items updates global secondary indexes and local secondary indexes automatically during the operation. You do not need to take additional steps.

**Important**  
The top-level `BulkPutBytes` total covers table and secondary index writes. Vector index writes are metered separately in `BulkPutVectorBytes`, in the `VectorIndexes` map, consistent with how `PutItem` meters vector capacity. Add `BulkPutVectorBytes` to `BulkPutBytes` for the complete total.