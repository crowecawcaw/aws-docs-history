

# Bulk put items considerations, quotas, and permissions
<a name="BulkPutItems.Considerations"></a>

This topic covers the quotas, IAM permissions, and feature interactions that apply to Amazon DynamoDB bulk put items operations. Review these constraints before you start a bulk put items operation.

## Quotas
<a name="BulkPutItems.Considerations.Quotas"></a>

Bulk put items operations are subject to quotas on concurrent operations, active operations per table, total input size, and the number and size of input objects. For the values and how DynamoDB enforces them, see [Quotas for bulk put items](ServiceQuotas.md#limits-bulk-put-items).

## Table state requirements
<a name="BulkPutItems.Considerations.TableState"></a>

To start a bulk put items operation, the target table must be in the `ACTIVE` state, or in the `UPDATING` state for a change that does not conflict with bulk writes. You cannot start an operation while the table is creating a secondary index. You also cannot start one while the table is transitioning to or from a global table, or restoring from a backup.

## Global tables
<a name="BulkPutItems.Considerations.GlobalTables"></a>

**Important**  
Bulk put items does not support global tables.

The following restrictions apply:
+ You cannot start a bulk put items operation on a table that is part of a global table.
+ You cannot add a replica to a table that has a bulk put items operation in progress.

If your workload requires writing data to a global table, use `BatchWriteItem` or individual `PutItem` operations instead.

## Vector indexes
<a name="BulkPutItems.Considerations.VectorIndexes"></a>

You can use bulk put items to ingest data into tables that have a vector index by using the Standard performance tier. The Accelerated performance tier is not available for these tables, and requesting it fails validation.

DynamoDB meters vector index bytes separately from table and secondary index bytes.

## Secondary indexes
<a name="BulkPutItems.Considerations.SecondaryIndexes"></a>

Bulk put items updates global secondary indexes (GSIs) and local secondary indexes (LSIs) automatically during an operation. You do not need to take additional steps to propagate data to your indexes.

Each index write is metered independently. The bytes written to each GSI and LSI count toward your bulk put items usage.

## Cancellation
<a name="BulkPutItems.Considerations.Cancellation"></a>

You can cancel a bulk put items operation by calling [CancelBulkOperation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CancelBulkOperation.html). When you cancel an operation, the following occurs:
+ Items already written to the table remain in place and are immediately readable. DynamoDB does not roll back items that were written before the cancellation.
+ The operation status transitions to `CANCELLING` and then `CANCELLED`.

## Billing for failed items
<a name="BulkPutItems.Considerations.Billing"></a>

Items rejected by validation before a table write is attempted are not billed as table writes. Items that reach the table and fail a condition check are billed. For the full billing details, see [Billing for reports and failed items](BulkPutItems.Output.md#BulkPutItems.Output.Billing).

## Streams
<a name="BulkPutItems.Considerations.Streams"></a>

On a table with DynamoDB Streams or a Kinesis data stream enabled, every bulk write produces a stream record, delivered at the operation's write rate. Items that fail a condition check do not produce a stream record. Consumers sized for normal traffic can fall behind. DynamoDB Streams retains records for 24 hours, so a consumer more than 24 hours behind loses records. Use [MaxWriteRequestUnits](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html#DDB-StartBulkPutItems-request-MaxWriteRequestUnits) in the `StartBulkPutItems` call to cap the bulk operation's write rate and protect downstream consumers.

## Metrics and Contributor Insights
<a name="BulkPutItems.Considerations.Metrics"></a>

Bulk writes do not appear in the table's `ConsumedWriteCapacityUnits` metric or in Contributor Insights, because they do not consume capacity. During an operation, use `DescribeBulkOperation` and the Amazon S3 output to track progress and failures rather than the table's CloudWatch metrics.

## Concurrent writes to the same keys
<a name="BulkPutItems.Considerations.ConcurrentWrites"></a>

During an operation, DynamoDB can write some records a second time after an internal failover. Each repeated write uses the record's condition expression, so a version guard on every record prevents a repeated write from replacing newer data. If your application writes to the same keys while an operation runs, a repeated bulk write with no condition can overwrite a newer application write. To protect such keys, carry a version attribute on each item and use a condition expression (for example `attribute_not_exists(#v) OR #v < :new`) so a repeated write cannot overwrite a newer value.

## Cross-account access
<a name="BulkPutItems.Considerations.CrossAccount"></a>

The caller must be in the table's account. Cross-account callers are blocked on start, describe, and cancel. For an Amazon S3 bucket in another account, set `S3BucketOwner`. DynamoDB sends `x-amz-expected-bucket-owner`, which defaults to the caller's account. DynamoDB uses the caller's credentials to access Amazon S3, so the caller's principal, not a DynamoDB service principal, needs bucket access.

If another account owns a bucket, the caller's identity policy and the bucket policy must both allow the access.

To read input from another account:

1. In the caller's identity policy, add the source bucket to `AllowS3ReadInput`.

1. In the bucket owner's account, add a bucket policy that grants the caller `s3:ListBucket` on the bucket and `s3:GetObject` on the input prefix.

1. In `InputS3Configuration`, set `S3BucketOwner` to the bucket owner's account ID.

To output results to another account:

1. In the output bucket, set Object Ownership to Bucket owner enforced. The bucket owner then owns the report and manifest objects.

1. In the caller's identity policy, allow `s3:PutObject` and `s3:AbortMultipartUpload` on the output prefix.

1. In the bucket owner's account, add a bucket policy that grants the caller the same two actions on the same prefix.

1. In `OutputS3Configuration`, set `S3BucketOwner` to the bucket owner's account ID.

With this policy, the bucket owner can read the output and the caller cannot. Condition-check report records contain the existing table item (`oldImage`), so the output bucket owner can read that data.

If `S3BucketOwner` is wrong, `StartBulkPutItems` still returns an operation ARN. DynamoDB can write items to the table before the operation fails with `S3AccessDenied`, and it outputs no report or manifest.

The following example shows an output bucket policy. Replace {{TABLE\_ACCOUNT\_ID}}, {{ROLE\_NAME}}, {{OUTPUT\_BUCKET}}, and {{OUTPUT\_PREFIX}} with your own values.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{TABLE_ACCOUNT_ID}}:role/{{ROLE_NAME}}" },
      "Action": ["s3:PutObject", "s3:AbortMultipartUpload"],
      "Resource": "arn:aws:s3:::{{OUTPUT_BUCKET}}/{{OUTPUT_PREFIX}}/*"
    }
  ]
}
```

## Cross-Region buckets
<a name="BulkPutItems.Considerations.CrossRegion"></a>

An input or output bucket in another AWS Region incurs cross-Region data-transfer bills, and if that Region is impaired the operation slows or stalls until it times out. Use buckets in the table's Region when you can.

## AWS KMS encryption
<a name="BulkPutItems.Considerations.KMS"></a>

[S3SseKmsKeyId](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html#DDB-Type-OutputS3Configuration-S3SseKmsKeyId) is required when [S3SseAlgorithm](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html#DDB-Type-OutputS3Configuration-S3SseAlgorithm) is `KMS`, and is rejected when `S3SseAlgorithm` is `AES256`. `S3SseAlgorithm` is required whenever you supply a key ID. For a table encrypted with a customer managed key, the caller needs `kms:Decrypt` on that key. If the caller does not have it, `StartBulkPutItems` returns an `AccessDeniedException` and no operation starts.

## CloudTrail
<a name="BulkPutItems.Considerations.CloudTrail"></a>

AWS CloudTrail logs the `StartBulkPutItems` call with the event name `StartBulkOperation` and resource type `AWS::DynamoDB::BulkOperation`. Individual item writes are not logged.

## DynamoDB Accelerator (DAX)
<a name="BulkPutItems.Considerations.DAX"></a>

Bulk writes bypass DAX, so items cached in DAX stay stale until their DAX TTL expires. Plan for this if the table is fronted by DAX.

## IAM permissions
<a name="BulkPutItems.Considerations.IAM"></a>

Bulk put items requires the following IAM actions. A minimum policy must include all five, because a policy that grants only the start actions can start an operation but cannot monitor or cancel it. The following table lists these actions.


| Action | Scope | Description | 
| --- | --- | --- | 
| dynamodb:StartBulkOperation | bulk-operation/\* | Required to start a bulk put items operation. The start call also evaluates the target table's tags and resource-based policy. | 
| dynamodb:BulkPutItems | The target table | Required to write items to the target table during a bulk put items operation. | 
| dynamodb:DescribeBulkOperation | The operation ARN | Required to monitor an operation. | 
| dynamodb:CancelBulkOperation | The operation ARN | Required to cancel an operation. | 
| dynamodb:ListBulkOperations | bulk-operation/\* | Required to list operations. | 

In addition to the DynamoDB actions, the IAM principal that calls `StartBulkPutItems` needs the Amazon S3 permissions in the example policy. For buckets in another account, see [Cross-account access](#BulkPutItems.Considerations.CrossAccount). The input bucket can also be in a different Region from the table.

DynamoDB checks the caller's permissions again while the operation runs. If the caller loses `dynamodb:BulkPutItems` on the table, or AWS KMS access to the table's customer managed key, the operation ends `FAILED` with `DynamoDBAccessDeniedException` or `KmsAccessDeniedException`. Items already written stay in the table. Keep the caller's permissions in place until the operation ends.

DynamoDB supports bulk operations on encrypted tables, and also supports reading from encrypted data sources and delivering the error output to encrypted Amazon S3 buckets.

### Example IAM policy
<a name="BulkPutItems.Considerations.IAM.Example"></a>

The following IAM policy grants the minimum permissions required to run a bulk put items operation. Replace the placeholder values with your account ID, Region, table name, and bucket names.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowStartBulkOperation",
            "Effect": "Allow",
            "Action": "dynamodb:StartBulkOperation",
            "Resource": "arn:aws:dynamodb:us-east-1:111122223333:bulk-operation/*"
        },
        {
            "Sid": "AllowBulkPutItems",
            "Effect": "Allow",
            "Action": "dynamodb:BulkPutItems",
            "Resource": "arn:aws:dynamodb:us-east-1:111122223333:table/MyTable"
        },
        {
            "Sid": "AllowManageBulkOperations",
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeBulkOperation",
                "dynamodb:CancelBulkOperation",
                "dynamodb:ListBulkOperations"
            ],
            "Resource": "arn:aws:dynamodb:us-east-1:111122223333:bulk-operation/*"
        },
        {
            "Sid": "AllowS3ReadInput",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket",
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ]
        },
        {
            "Sid": "AllowS3WriteOutput",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:AbortMultipartUpload"
            ],
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*"
        }
    ]
}
```

If you use AWS KMS encryption on the Amazon S3 objects or the DynamoDB table, add the following permissions to the policy. For reading from or writing to an encrypted table, the caller needs the same AWS KMS permissions documented for `PutItem` on encrypted tables. Replace {{your-kms-key-id}} with the ID of your AWS KMS key:

```
{
    "Sid": "AllowKMSAccess",
    "Effect": "Allow",
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "arn:aws:kms:us-east-1:111122223333:key/your-kms-key-id"
}
```