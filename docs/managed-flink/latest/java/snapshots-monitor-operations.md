

# Monitor enhanced snapshot operations
<a name="snapshots-monitor-operations"></a>

In Amazon Managed Service for Apache Flink, [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html), [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html), [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html), and [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) run asynchronously. Each call returns a `SnapshotOperationId`. This page shows how to use the ID to track the operation until the operation succeeds or fails.

## Check the status of snapshot operations
<a name="snapshots-monitor-operations-describesnapshotoperation-and-listsnapshotoperations"></a>

Use the following actions to monitor enhanced snapshot operations:
+ [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html): Returns the details of one operation on one enhanced snapshot.
+ [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html): Returns a summary of the operations on one enhanced snapshot.

Both actions take the name of one enhanced snapshot. No action lists the operations of every enhanced snapshot in your account.

IAM authorizes both actions on the enhanced snapshot ARN. For more information, see [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions).

### `DescribeSnapshotOperation` request
<a name="snapshots-monitor-operations-describe-request"></a>

A `DescribeSnapshotOperation` request has the following members:
+ `SnapshotName`: The name of the enhanced snapshot.
+ `SnapshotOperationId`: The ID that the asynchronous action returned. The ID has 1 to 64 characters.

```
{
    "SnapshotName": "MyApplication-snapshot-1",
    "SnapshotOperationId": "s9T0u1V2w3X4"
}
```

### `DescribeSnapshotOperation` response
<a name="snapshots-monitor-operations-describe-response"></a>

The response contains one `SnapshotOperationInfoDetails` object. The following table describes its members.


| Member | When present | Description | 
| --- | --- | --- | 
| SnapshotOperationId | Always | The ID of the operation. | 
| SnapshotOperation | Always | The type of operation: CreateSnapshot, DeleteSnapshot, ImportSnapshot, ExportSnapshot, or SystemCreateSnapshot. | 
| SnapshotOperationStatus | Always | The status of the operation. For the values, see [Operation status and snapshot status](#snapshots-monitor-operations-operation-status-and-snapshot-status). | 
| SnapshotArn | Always | The ARN of the enhanced snapshot. | 
| StartTime | Always | The start time of the operation, in epoch seconds. | 
| EndTime | After the operation ends | The end time of the operation, in epoch seconds. | 
| SourceEncryptionConfigurationDescription | Import and export | The KeyId and KeyType of the source data. | 
| DestinationEncryptionConfigurationDescription | Import and export | The KeyId and KeyType of the destination data. | 
| SnapshotSourceLocationDescription | Import | The Amazon S3 source: LocationType (S3) and S3PrefixLocation with BucketARN and KeyPrefix. | 
| SnapshotDestinationLocationDescription | Export, after the export ends | The Amazon S3 destination: LocationType and S3PrefixLocation. After an export ends, successful or failed, S3PrefixLocation includes ExportedPrefix, the Amazon S3 prefix that the export writes to. | 
| ApplicationOperationDescription | SystemCreateSnapshot operations | The ApplicationOperationId and ApplicationName of the related application operation. | 
| SnapshotOperationFailureDetails | FAILED operations | ErrorInfo with ErrorCode and ErrorString. For more information, see [Failure reasons](#snapshots-monitor-operations-failure-reasons). | 

### `ListSnapshotOperations` request
<a name="snapshots-monitor-operations-list-request"></a>

A `ListSnapshotOperations` request has the following members:
+ `SnapshotName` (required): The name of the enhanced snapshot.
+ `SnapshotOperation` (optional): A filter on the type of operation. The filter matches the value exactly. For example, the `CreateSnapshot` filter does not return `SystemCreateSnapshot` operations.
+ `SnapshotOperationStatus` (optional): A filter on the status of the operation.
+ `Limit` (optional): The maximum number of results in one response. Valid values are 1 to 50. If you omit `Limit`, the response has up to 50 results.
+ `NextToken` (optional): The token from the previous response. Use it to get the next page of results.

Each request accepts at most one filter. To filter on both type and status, filter on one member and check the other member in the results.

```
{
    "SnapshotName": "MyApplication-snapshot-1",
    "SnapshotOperationStatus": "FAILED",
    "Limit": 50
}
```

### `ListSnapshotOperations` response
<a name="snapshots-monitor-operations-list-response"></a>

The response has the following members:
+ `SnapshotOperationInfoList`: A list of operations, newest first. Each entry has `SnapshotOperationId`, `SnapshotOperation`, `SnapshotOperationStatus`, `StartTime`, and `EndTime`.
+ `NextToken`: A token for the next page. The response omits `NextToken` on the last page.

An entry in the list does not include location, encryption, or failure details. To get those details, call `DescribeSnapshotOperation` with the `SnapshotOperationId` of the entry.

For an example response, see [List the operations of an enhanced snapshot](snapshots-api-examples.md#snapshots-api-examples-listsnapshotoperations).

### Troubleshoot operation API errors
<a name="snapshots-monitor-operations-errors"></a>

The following table lists the exceptions that `DescribeSnapshotOperation` and `ListSnapshotOperations` can return.


| Exception | Cause | 
| --- | --- | 
| ResourceNotFoundException | The enhanced snapshot does not exist, or the operation record has expired. An unknown snapshot name returns this exception, not an empty list. | 
| InvalidArgumentException | A request member has a value that is not valid. | 
| ValidationException | The Limit value in the ListSnapshotOperations request is out of range. Valid values are 1 to 50. | 
| AccessDeniedException | IAM denies the action on the enhanced snapshot ARN. | 

## Operation status and snapshot status
<a name="snapshots-monitor-operations-operation-status-and-snapshot-status"></a>

`SnapshotOperationStatus` has the following values:
+ `IN_PROGRESS`: The operation has started and has not ended. Every operation starts in this status.
+ `SUCCESSFUL`: The operation completed.
+ `FAILED`: The operation did not complete. The response includes `SnapshotOperationFailureDetails`.
+ `CANCELLED`: Managed Service for Apache Flink stopped the operation before it captured the state. For example, the application was not `RUNNING`, an update changed the application version, or another application operation stopped the snapshot creation. The response includes no failure details. For more information, see [Failure reasons](#snapshots-monitor-operations-failure-reasons).

Managed Service for Apache Flink has no queued status for operations.

The following table shows the `SnapshotStatus` of the enhanced snapshot for each operation status.


| Operation | `IN_PROGRESS` | `SUCCESSFUL` | `FAILED` | `CANCELLED` | 
| --- | --- | --- | --- | --- | 
| CreateSnapshot | CREATING | READY | FAILED | FAILED | 
| ImportSnapshot | CREATING | READY | FAILED | Not applicable | 
| ExportSnapshot | READY | READY | READY | Not applicable | 
| DeleteSnapshot | DELETING | The enhanced snapshot no longer exists. | Not applicable. A DeleteSnapshot operation does not end in FAILED. | Not applicable | 
| SystemCreateSnapshot | Not applicable | READY | Not applicable | Not applicable | 

An enhanced snapshot never has a status of `CANCELLED`. If a `CreateSnapshot` operation ends in `CANCELLED`, the enhanced snapshot ends in `FAILED`.

After a delete succeeds, you get `ResourceNotFoundException` when you call [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html), `DescribeSnapshotOperation`, or `ListSnapshotOperations` with the name of the deleted enhanced snapshot. If you create a new enhanced snapshot with the same name, you do not see the old operations. To confirm a delete, poll `DescribeSnapshot` until the call returns `ResourceNotFoundException`.

You can see a `SystemCreateSnapshot` operation in the `ListSnapshotOperations` results only after the system snapshot succeeds. A system snapshot has no operation record while it runs or after it fails.

### Poll for status changes
<a name="snapshots-monitor-operations-poll"></a>

To wait for an operation, call `DescribeSnapshotOperation` in a loop. Stop the loop when `SnapshotOperationStatus` is no longer `IN_PROGRESS`. For a runnable example, see [Wait for an operation to complete](#snapshots-monitor-operations-poll-procedure).

Wait between calls. Each call counts toward the API request rate of your account. A call over the request rate returns `ThrottlingException`.

## Failure reasons
<a name="snapshots-monitor-operations-failure-reasons"></a>

If an operation fails, the `DescribeSnapshotOperation` response includes `SnapshotOperationFailureDetails.ErrorInfo`. `ErrorInfo` has an `ErrorCode` and an `ErrorString` that describes the failure.

A `CreateSnapshot` operation fails only when the state capture fails. The operation ends in `CANCELLED` instead of `FAILED` in the following cases:
+ The application is not `RUNNING` when the state capture starts.
+ An application update changes the application version before the state capture starts.
+ Another application operation stops the snapshot creation.

A `CANCELLED` operation has no `ErrorCode` and no `ErrorString`. Retry the request after the application is `RUNNING` and no other application operation is in progress.

A failed `CreateSnapshot` operation has one of the following `ErrorCode` values. A `DeleteSnapshot` operation does not end in `FAILED`. A failed system snapshot has no operation record.


| `ErrorCode` | Meaning | What to do | 
| --- | --- | --- | 
| ApplicationStateCaptureFailed | The Apache Flink job did not complete the savepoint. | If logging is enabled, check the CloudWatch logs of the application for details. Then retry the request. | 
| ApplicationStateCaptureTimedOut | The savepoint timed out before the Apache Flink job completed it. | If logging is enabled, check the CloudWatch logs of the application for slow or blocked operators. Then retry the request. | 
| KMSAccessDenied | The key policy of the application key does not allow Managed Service for Apache Flink to use the key. | Update the key policy to allow the Managed Service for Apache Flink service principal to use the key. Then retry the request. | 

A failed import or export operation has one of the values in the following table. For an Amazon S3, AWS Security Token Service (AWS STS), or AWS KMS error, the `ErrorString` names the error code, the resource, and the role.


| `ErrorCode` | Meaning | What to do | 
| --- | --- | --- | 
| S3AccessDenied | A bucket policy or an IAM policy denies the role access to the Amazon S3 objects. For an import, the bucket is the source bucket. For an export, the bucket is the destination bucket. | Fix the role policy or the bucket policy. | 
| S3NoSuchBucket | The bucket does not exist. | Check the BucketARN value in the request. | 
| S3NoSuchKey | Import only: you or another process deleted a source object during the import. | Do not delete source objects until the import ends. Then import again. | 
| S3PreconditionFailed | For an import, you or another process changed a source object during the import. For an export, an object in the destination prefix changed during the export. | For an import, do not write to the source prefix until the import ends. For an export, use an empty destination prefix and do not write to it until the export ends. Then try again. | 
| S3InvalidObjectState | Import only: a source object is in an archive storage class. | Restore the object from the archive storage class. Then retry the operation. | 
| S3NoSuchUpload | Export only: a process outside Managed Service for Apache Flink aborted an upload. For example, an Amazon S3 lifecycle rule aborted the upload. | Change the process or the lifecycle rule. Then export again. | 
| STSAccessDenied | The trust policy of the role rejects Managed Service for Apache Flink. | Check that the trust policy lets kinesisanalytics.amazonaws.com assume the role. | 
| KMSConfigError | A AWS KMS key that the operation uses is missing, disabled, or pending deletion. Or the key policy of that key denies the access that the operation needs. | Use an enabled key. Check the key policy. | 
| InvalidSnapshotContent | Import only: the source prefix has no objects. | Check the KeyPrefix value in the request. | 
| MissingObjectChecksum | Import only: a source object has no Amazon S3 full-object checksum that uses the CRC64NVME algorithm. | Upload the object again with a full-object CRC64NVME checksum. | 
| InvalidSnapshotMetadata | Import only: the savepoint has metadata that Managed Service for Apache Flink cannot read. For example, the files are not a savepoint, the savepoint holds absolute paths, or Managed Service for Apache Flink does not support the format version of the savepoint. | Import an Apache Flink savepoint that uses relative paths and a format version that Managed Service for Apache Flink supports. | 
| DestinationKeyTooLong | Import only: a destination key is longer than 1,024 bytes. A destination key is KeyPrefix plus the path of a savepoint file. | Use a shorter KeyPrefix. | 

`ErrorCode` is a string, not an enumeration. Managed Service for Apache Flink can add new values without an API change. Make your code handle an `ErrorCode` value that it does not recognize.

A failed operation affects the enhanced snapshot as follows:
+ **Failed import**: The enhanced snapshot stays in `FAILED`. No other enhanced snapshot can use the name of the failed enhanced snapshot. To import again with the same name, first delete the failed enhanced snapshot.
+ **Failed export**: The enhanced snapshot stays in `READY`. You can call `ExportSnapshot` again.

After a failed export, Managed Service for Apache Flink does not delete the files that it already wrote. The completed files stay in your bucket under the `ExportedPrefix` path. Delete these files yourself.

For more information about import and export, see [Import and export enhanced snapshots](snapshots-import-export.md).

## How long operation records are kept
<a name="snapshots-monitor-operations-retention"></a>

Managed Service for Apache Flink keeps the record of an operation for 90 days after the operation ends. The following rules apply:
+ After 90 days, `DescribeSnapshotOperation` returns `ResourceNotFoundException` for the operation.
+ The record of an operation in `IN_PROGRESS` does not expire.
+ After you delete an enhanced snapshot, you cannot get the records of its operations.

The response does not include the expiry time of a record. To keep a record longer than 90 days, save the response yourself.

## Operations that CloudTrail does not log
<a name="snapshots-monitor-operations-cloudtrail"></a>

CloudTrail logs the enhanced snapshot API calls that you make. CloudTrail does not log operations that Managed Service for Apache Flink starts, such as system snapshots.

To trace a system snapshot, do the following:

1. Call `ListSnapshotOperations`, and set `SnapshotOperation` to `SystemCreateSnapshot`.

1. Pass the `SnapshotOperationId` from the results to `DescribeSnapshotOperation`. Read `ApplicationOperationDescription` in the response.

1. Pass the `ApplicationName` and `ApplicationOperationId` values from `ApplicationOperationDescription` to [`DescribeApplicationOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationOperation.html).

## Wait for an operation to complete
<a name="snapshots-monitor-operations-poll-procedure"></a>

The following procedure polls an export of `MyApplication-snapshot-1` until the export ends. To poll an import, use the name of the imported enhanced snapshot and the `SnapshotOperationId` from the `ImportSnapshot` response.

Before you begin, install and configure the AWS CLI. Make sure that your credentials allow `ExportSnapshot` or `ImportSnapshot`, and `DescribeSnapshotOperation`, on the enhanced snapshot.

**To poll an import or export operation to completion**

1. Start the import or export. Save the `SnapshotOperationId` from the response. For more information, see [Import and export enhanced snapshots](snapshots-import-export.md).

   In this example, the `ExportSnapshot` response returns the `SnapshotOperationId` `s9T0u1V2w3X4`.

1. Describe the operation with `DescribeSnapshotOperation`. Use the snapshot name and the `SnapshotOperationId`.

   Run the following AWS CLI command:

   ```
   PROMPT> aws kinesisanalyticsv2 describe-snapshot-operation \
       --snapshot-name MyApplication-snapshot-1 \
       --snapshot-operation-id s9T0u1V2w3X4
   ```

   The following example shows the JSON request for the `DescribeSnapshotOperation` API:

   ```
   {
       "SnapshotName": "MyApplication-snapshot-1",
       "SnapshotOperationId": "s9T0u1V2w3X4"
   }
   ```

   The following example shows the JSON response while the export runs:

   ```
   {
       "SnapshotOperationInfoDetails": {
           "SnapshotOperationId": "s9T0u1V2w3X4",
           "SnapshotOperation": "ExportSnapshot",
           "SnapshotOperationStatus": "IN_PROGRESS",
           "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
           "DestinationEncryptionConfigurationDescription": {
               "KeyType": "AWS_OWNED_KEY"
           },
           "StartTime": 1767229200
       }
   }
   ```

1. Read `SnapshotOperationStatus` in the response. If the value is `IN_PROGRESS`, wait about 30 seconds, and then repeat the previous step. An import or export can take several minutes, depending on the size of the data. For the polling rules, see [Poll for status changes](#snapshots-monitor-operations-poll).

   The following AWS CLI script repeats the call until the operation ends:

   ```
   while true; do
       STATUS=$(aws kinesisanalyticsv2 describe-snapshot-operation \
           --snapshot-name MyApplication-snapshot-1 \
           --snapshot-operation-id s9T0u1V2w3X4 \
           --query 'SnapshotOperationInfoDetails.SnapshotOperationStatus' \
           --output text)
       echo "Status: $STATUS"
       if [ "$STATUS" != "IN_PROGRESS" ]; then
           break
       fi
       sleep 30
   done
   ```

1. Read the result of the operation if the status is `SUCCESSFUL`. For an export, read `ExportedPrefix` to find the exported files in Amazon S3. For an import, call `DescribeSnapshot` to confirm that the enhanced snapshot is `READY`.

   For an export, `ExportedPrefix` is in `SnapshotOperationInfoDetails.SnapshotDestinationLocationDescription.S3PrefixLocation`. For a full example response, see [Describe an enhanced snapshot operation](snapshots-api-examples.md#snapshots-api-examples-describesnapshotoperation).

1. Read `SnapshotOperationFailureDetails.ErrorInfo.ErrorCode` if the status is `FAILED`. For information about the action for that code, see [Failure reasons](#snapshots-monitor-operations-failure-reasons).

   The following example shows the failure details of a failed export:

   ```
   {
       "SnapshotOperationFailureDetails": {
           "ErrorInfo": {
               "ErrorCode": "S3AccessDenied",
               "ErrorString": "..."
           }
       }
   }
   ```