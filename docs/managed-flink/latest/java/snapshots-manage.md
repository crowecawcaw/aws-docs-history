

# Create and manage enhanced snapshots

Use the procedures on this page to create, describe, list, and delete enhanced snapshots in Amazon Managed Service for Apache Flink. The page also lists the errors that these operations return.

## Create an enhanced snapshot
<a name="snapshots-manage-create-a-snapshot"></a>

Use [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) to take a Flink savepoint of a running application. Managed Service for Apache Flink stores the savepoint as an enhanced snapshot with its own ARN.

Before you create an enhanced snapshot, make sure that the application meets these requirements:
+ The application uses enhanced snapshot mode. For more information, see [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md).
+ The application uses Apache Flink version 1.20 or later. For more information, see [Prerequisites](snapshots-setup.md#snapshots-setup-prerequisites).
+ The application status is `RUNNING`.
+ No other enhanced snapshot of the application is in the `CREATING` status. Each application allows one create at a time.

You can create an enhanced snapshot whether `SnapshotsEnabled` is `true` or `false`. `SnapshotsEnabled` controls only the system snapshots that Managed Service for Apache Flink creates for you. It does not affect `CreateSnapshot`.

**Snapshot names** – Each enhanced snapshot name is unique in the account and Region. For more information about the name rules, see [Enhanced snapshots as standalone resources](snapshots-how-it-works.md#snapshots-how-it-works-snapshots-as-standalone-resources).

After Managed Service for Apache Flink finishes deleting an enhanced snapshot, you can create a new enhanced snapshot with the same name. These rules apply to the new enhanced snapshot:
+ The snapshot ARN identifies the enhanced snapshot by name only, with no unique ID. The new enhanced snapshot has the same ARN as the deleted one.
+ An IAM policy that names that ARN applies to the new enhanced snapshot.
+ The tags of the deleted enhanced snapshot do not carry over.
+ `ListSnapshotOperations` shows only the operations of the new enhanced snapshot.
+ A delete request for the new enhanced snapshot needs the `SnapshotCreationTimestamp` value of the new enhanced snapshot.

**Description** – The optional `SnapshotDescription` value has 0–1,024 characters. The description cannot contain control characters.

**Tags** – The optional `Tags` list adds tags when Managed Service for Apache Flink creates the enhanced snapshot. These rules apply to tags:
+ To add tags on create, the caller needs `kinesisanalytics:TagResource` and `kinesisanalytics:CreateSnapshot`.
+ Tagging and creation succeed or fail together. If IAM denies the tags, the request returns `AccessDeniedException` and Managed Service for Apache Flink creates no snapshot.
+ An enhanced snapshot can have up to 50 tags. A request with 51 to 200 tags returns `TooManyTagsException`. A request with more than 200 tags returns `ValidationException`. A tag key has 1–128 characters. A tag value has 0–256 characters.
+ To create a snapshot without tags, omit `Tags`. An empty `Tags` list returns `ValidationException`.
+ A system snapshot inherits the tags of the application. Managed Service for Apache Flink copies the tags before the system snapshot appears in `ListSnapshots`. If the application has no tags, the system snapshot has no tags. An enhanced snapshot that you create with `CreateSnapshot` gets only the tags in the request.

**Encryption** – Your enhanced snapshot uses the encryption configuration of your application. If your application uses a customer managed key, Managed Service for Apache Flink encrypts the snapshot with that key. Otherwise, Managed Service for Apache Flink uses an AWS owned key. `CreateSnapshot` always uses the key of your application.

For an application with a customer managed key, the caller needs `kms:Decrypt` and `kms:GenerateDataKey` on the key. The key policy can use these conditions:
+ `kms:ViaService` equals `kinesisanalytics.{{region}}.amazonaws.com`.
+ The encryption context key `aws:kinesisanalytics:arn` equals the application ARN.

`CreateSnapshot` does not need `iam:PassRole`. For more information, see [Key management in Amazon Managed Service for Apache Flink](key-management-flink.md).

**To create an enhanced snapshot**

1. Call [`DescribeApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.html) for your application with the AWS CLI or an AWS SDK.

1. Confirm that `ApplicationStatus` in the response is `RUNNING`.

1. Confirm that `SnapshotMode` in the response is `ENHANCED_SNAPSHOTS`.

1. Send a `CreateSnapshot` request for your application. The response returns the snapshot ARN with the `CREATING` status.

   In the following example, replace `MyApplication` with your application name and `MyApplication-snapshot-1` with your snapshot name. The following example JSON `CreateSnapshot` request adds a description and one tag.

   ```json
   {
     "ApplicationName": "MyApplication",
     "SnapshotName": "MyApplication-snapshot-1",
     "SnapshotDescription": "Before code update",
     "Tags": [{ "Key": "Environment", "Value": "prod" }]
   }
   ```

   Run the following AWS CLI command to send the same request:

   ```bash
   PROMPT> aws kinesisanalyticsv2 create-snapshot \
       --application-name MyApplication \
       --snapshot-name MyApplication-snapshot-1 \
       --snapshot-description "Before code update" \
       --tags Key=Environment,Value=prod
   ```

1. Save the `SnapshotArn` and `SnapshotOperationId` values from the response. For an example response, see [Create an enhanced snapshot](snapshots-api-examples.md#snapshots-api-examples-createsnapshot).

1. Call [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html) with the snapshot name. Repeat the call until `SnapshotStatus` is `READY` or `FAILED`.

The `CreateSnapshot` call returns after Managed Service for Apache Flink accepts the request. A later failure does not return an exception. Instead, the snapshot status changes to `FAILED`.

To see the result of the operation, call [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html) with the snapshot name and the `SnapshotOperationId` value. For more information, see [Monitor enhanced snapshot operations](snapshots-monitor-operations.md).

A failed create operation has one of the `ErrorCode` values in the following table. `ErrorString` describes the cause.


| `ErrorCode` | `ErrorString` | 
| --- | --- | 
| ApplicationStateCaptureFailed | The application state could not be captured. If logging is enabled, check the application's CloudWatch logs for details, then retry. | 
| ApplicationStateCaptureTimedOut | The application state could not be captured before the snapshot timed out. If logging is enabled, check the application's CloudWatch logs for slow or blocked operators, then retry. | 
| KMSAccessDenied | The application state could not be captured because the service is not allowed to use the application's KMS key. Update the key policy to allow the service principal to use the key, then retry. | 

In some cases, the create operation ends in `CANCELLED` with no `ErrorCode`. For these cases, see [Failure reasons](snapshots-monitor-operations.md#snapshots-monitor-operations-failure-reasons).

**Note**  
Wait until the snapshot is `READY` before you update the application. If you update the application first, the create operation can end in `CANCELLED`.

## Describe and list enhanced snapshots
<a name="snapshots-manage-describe-and-list-snapshots"></a>

Use `DescribeSnapshot` to get the details of one enhanced snapshot. The only request member is `SnapshotName`. The response holds one `SnapshotInfoDetails` object with the members in the following table.


| Member | Description | 
| --- | --- | 
| SnapshotName | The name of the enhanced snapshot. Always present. | 
| SnapshotArn | The ARN of the enhanced snapshot. Always present. | 
| SnapshotDescription | The description from the create or import request, if any. | 
| SnapshotStatus | CREATING, READY, DELETING, or FAILED. Always present. | 
| SnapshotCreationTimestamp | The creation time in epoch seconds, with one-second precision. Always present. DeleteSnapshot requires this value. | 
| RuntimeEnvironment | The runtime of the source application, for example FLINK-1\_20. Absent for imported snapshots. | 
| SnapshotSizeInBytes | The size of the enhanced snapshot in bytes. | 
| SnapshotEncryptionConfigurationDescription | KeyType (AWS\_OWNED\_KEY or CUSTOMER\_MANAGED\_KEY) and, for a customer managed key, KeyId. | 
| SnapshotInitiator | USER for snapshots that you create or import. SYSTEM for system snapshots. Always present. | 
| SnapshotInitiatorOperation | CreateSnapshot, ImportSnapshot, or SystemCreateSnapshot. Always present. | 
| SnapshotSourceDescription | For an imported snapshot, S3PrefixLocation. For other snapshots, SourceApplicationDescription with ApplicationName, ApplicationCreationTimestamp, and ApplicationVersionId. Always present. | 
| SnapshotFormat | The format of the enhanced snapshot. The only value is CANONICAL. Always present. | 

The following example JSON request describes one enhanced snapshot. In the example, replace `MyApplication-snapshot-1` with your snapshot name.

```json
{ "SnapshotName": "MyApplication-snapshot-1" }
```

Run the following AWS CLI command to send the same request:

```bash
PROMPT> aws kinesisanalyticsv2 describe-snapshot --snapshot-name MyApplication-snapshot-1
```

For an example response, see [Describe an enhanced snapshot](snapshots-api-examples.md#snapshots-api-examples-describesnapshot).

Use [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) to list the enhanced snapshots in the account and Region. The request accepts these optional filters:
+ `SourceApplicationName`: enhanced snapshots from one application. Imported snapshots have no source application, so this filter never returns them.
+ `SnapshotInitiator`: `USER` or `SYSTEM`.
+ `SnapshotInitiatorOperation`: `CreateSnapshot`, `ImportSnapshot`, or `SystemCreateSnapshot`.
+ `SnapshotStatus`: `CREATING`, `READY`, `DELETING`, or `FAILED`.

Each `ListSnapshots` request accepts at most one filter. A request with two or more filters returns `InvalidArgumentException`. To combine conditions, filter the results in your code.

The filter member is `SourceApplicationName`, not `ApplicationName`. Managed Service for Apache Flink ignores an `ApplicationName` key and returns every snapshot in the account.

**Visibility** – Without a filter, the list includes these snapshots:
+ Enhanced snapshots that you create.
+ Enhanced snapshots that you import.
+ System snapshots that Managed Service for Apache Flink takes for you. For the operations that create a system snapshot, see [System snapshots](snapshots-how-it-works.md#snapshots-how-it-works-system-snapshots).

To list only the enhanced snapshots that you create or import, set `SnapshotInitiator` to `USER`.

**Order and pagination** – Results come newest first by `SnapshotCreationTimestamp`. No sort parameter exists. These rules apply to pages of results:
+ The optional `Limit` member accepts values from 1 through 50. If you omit `Limit`, the response has up to 50 results.
+ If more results exist, the response includes a `NextToken` value. Send that value in the next request to get the next page.
+ The last page has no `NextToken` value.
+ `NextToken` is opaque. A `NextToken` value that is not valid returns `InvalidArgumentException`.
+ A `Limit` value out of range returns `ValidationException`.

Each entry in `SnapshotInfoList` holds the members in the following table.


| Member | Description | 
| --- | --- | 
| SnapshotName | The name of the enhanced snapshot. | 
| SnapshotArn | The ARN of the enhanced snapshot. | 
| SnapshotStatus | The status of the enhanced snapshot. | 
| SnapshotCreationTimestamp | The creation time in epoch seconds. | 
| SnapshotInitiator | USER or SYSTEM. | 
| SnapshotInitiatorOperation | CreateSnapshot, ImportSnapshot, or SystemCreateSnapshot. | 
| SourceApplicationName | The application that created the enhanced snapshot. Absent for imported snapshots. | 
| SnapshotFormat | The format of the enhanced snapshot: CANONICAL. | 

The following example JSON request lists the enhanced snapshots in the account and Region.

```json
{ "Limit": 50 }
```

Run the following AWS CLI command to send the same request:

```bash
PROMPT> aws kinesisanalyticsv2 list-snapshots \
    --limit 50
```

To list the enhanced snapshots of one application, add `--source-application-name MyApplication`. In the example, replace `MyApplication` with your application name.

For an example response, see [List the enhanced snapshots in an account](snapshots-api-examples.md#snapshots-api-examples-listsnapshots).

The following example JSON request lists the failed enhanced snapshots in the account. The request passes a `NextToken` value from an earlier response. In the example, replace `token-from-previous-response` with the `NextToken` value from your earlier response.

```json
{ "SnapshotStatus": "FAILED", "Limit": 50, "NextToken": "token-from-previous-response" }
```

Run the following AWS CLI command to send the same request:

```bash
PROMPT> aws kinesisanalyticsv2 list-snapshots \
    --snapshot-status FAILED \
    --limit 50 \
    --next-token token-from-previous-response
```

## Delete an enhanced snapshot
<a name="snapshots-manage-delete-a-snapshot"></a>

Use [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html) to delete an enhanced snapshot. The request requires two members:
+ `SnapshotName`: the name of the enhanced snapshot.
+ `SnapshotCreationTimestamp`: the creation time of the enhanced snapshot, in epoch seconds. Copy this value from the `DescribeSnapshot` or `ListSnapshots` response.

A request whose timestamp does not match the enhanced snapshot returns `InvalidArgumentException`.

Billing for the enhanced snapshot stops when its status changes to `DELETING`. For more information, see [Billing for enhanced snapshots](snapshots-how-it-works.md#snapshots-how-it-works-billing-for-snapshots).

The caller needs `kinesisanalytics:DeleteSnapshot` on the snapshot ARN.

You can delete an enhanced snapshot in the `READY` or `FAILED` status. In any other status, the request returns `ResourceInUseException`.

**Asynchronous delete** – The `DeleteSnapshot` call returns after Managed Service for Apache Flink accepts the request. The response shows the following values:
+ `SnapshotStatus` is `DELETING`.
+ `SnapshotOperationStatus` is `IN_PROGRESS`.
+ `SnapshotOperationId` identifies the delete operation.

The delete can take some time to complete. No `DELETED` status exists. After the delete completes, `DescribeSnapshot` returns `ResourceNotFoundException`. `DescribeSnapshotOperation` and [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html) calls for the enhanced snapshot also return `ResourceNotFoundException`.

[`DeleteApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplication.html) does not delete the enhanced snapshots of the application. To remove those enhanced snapshots, call `DeleteSnapshot` for each one. For more information, see [Snapshot lifecycle](snapshots-how-it-works.md#snapshots-how-it-works-snapshot-lifecycle).

**Note**  
After the delete completes, you cannot recover the enhanced snapshot. To keep a copy of the state, export the snapshot to Amazon S3 before you delete it. For more information, see [Import and export enhanced snapshots](snapshots-import-export.md).

You can delete an enhanced snapshot even if a later [`RollbackApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_RollbackApplication.html) request might need it. If you delete that snapshot, the rollback uses the newest remaining `READY` enhanced snapshot that meets the rollback selection rules. To make sure that the rollback can proceed, keep at least one enhanced snapshot that meets these rules. For more information about the selection rules, see [Roll back an application](snapshots-restore.md#snapshots-restore-rollback).

**To delete an enhanced snapshot**

1. Call `DescribeSnapshot` with the snapshot name of the enhanced snapshot. Copy the `SnapshotCreationTimestamp` value from the response.

   Run the following AWS CLI command to send the same request:

   ```bash
   PROMPT> aws kinesisanalyticsv2 describe-snapshot \
       --snapshot-name MyApplication-snapshot-1 \
       --query 'SnapshotInfoDetails.SnapshotCreationTimestamp'
   ```

1. Send a `DeleteSnapshot` request with the name and the timestamp for the same enhanced snapshot.

   ```json
   { "SnapshotName": "MyApplication-snapshot-1", "SnapshotCreationTimestamp": 1767225600 }
   ```

   Run the following AWS CLI command to send the same request:

   ```bash
   PROMPT> aws kinesisanalyticsv2 delete-snapshot \
       --snapshot-name MyApplication-snapshot-1 \
       --snapshot-creation-timestamp 1767225600
   ```

1. Save the `SnapshotOperationId` value from the response. For an example response, see [Delete an enhanced snapshot](snapshots-api-examples.md#snapshots-api-examples-deletesnapshot).

1. Call `DescribeSnapshot` with the name of the enhanced snapshot. Repeat the call until it returns `ResourceNotFoundException`.

### Delete a snapshot while an operation uses it
<a name="snapshots-manage-delete-protection-for-snapshots-in-use"></a>

You can call `DeleteSnapshot` while an operation uses the enhanced snapshot, such as an export. Managed Service for Apache Flink accepts the request and waits for the operation to finish. Then Managed Service for Apache Flink deletes the enhanced snapshot. To track the delete, call `DescribeSnapshotOperation` with the `SnapshotOperationId` from the response.

`DeleteSnapshot` returns `ResourceInUseException` if the enhanced snapshot is not in the `READY` or `FAILED` status. For example, an imported snapshot is `CREATING` until the import completes. Wait until the enhanced snapshot is `READY` or `FAILED`, then send the request again.

You can delete an enhanced snapshot while the application is running. You can also delete an enhanced snapshot that an `ApplicationRestoreConfiguration` names.

**Note**  
After you delete an enhanced snapshot, a later `RESTORE_FROM_LATEST_SNAPSHOT` restore cannot use it. A later `RollbackApplication` request also cannot use it. Before you delete an enhanced snapshot, make sure that you do not need it for a restore or a rollback. For more information about restores, see [Restore an application from an enhanced snapshot](snapshots-restore.md).

## Manage enhanced snapshots with CloudFormation
<a name="snapshots-manage-cfn"></a>

Use the `AWS::KinesisAnalyticsV2::Snapshot` resource to create an enhanced snapshot from a CloudFormation template. When CloudFormation creates the resource, it calls `CreateSnapshot` or `ImportSnapshot`. CloudFormation then waits until the enhanced snapshot is `READY`. When CloudFormation deletes the resource, it calls `DeleteSnapshot`.

Specify one source for the enhanced snapshot, not both:
+ `ApplicationName`: CloudFormation calls `CreateSnapshot` on this application. The application must meet the conditions in [Create an enhanced snapshot](#snapshots-manage-create-a-snapshot).
+ `ImportSourceConfiguration`: CloudFormation calls `ImportSnapshot` on the savepoint files in Amazon S3. This property has the same members as the `ImportSnapshot` request: `SourceType`, `ImportRoleArn`, `SourceS3PrefixLocation`, and `SourceEncryptionConfiguration`. For the file, role, and bucket requirements, see [Import and export enhanced snapshots](snapshots-import-export.md).

The resource also has the following properties:
+ `SnapshotName` (required): The name of the enhanced snapshot.
+ `SnapshotDescription`: A description of the enhanced snapshot.
+ `SnapshotEncryptionConfigurationDescription`: The key that encrypts an imported enhanced snapshot. Set this property only with `ImportSourceConfiguration`. If you do not set it, Managed Service for Apache Flink uses an AWS owned key. An enhanced snapshot of an application uses the key of the application.
+ `SnapshotFormat`: The format of the enhanced snapshot. The only value is `CANONICAL`.

If you change any of these properties, CloudFormation replaces the enhanced snapshot. The resource does not support tags. To keep an enhanced snapshot after CloudFormation deletes the resource, set `DeletionPolicy` to `Retain`.

The following example template creates an enhanced snapshot of `MyApplication`. The template returns the ARN of the enhanced snapshot. Replace `MyApplication` and `MyApplication-snapshot-1` with your application name and snapshot name.

```yaml
Resources:
  MySnapshot:
    Type: AWS::KinesisAnalyticsV2::Snapshot
    DeletionPolicy: Retain
    Properties:
      ApplicationName: MyApplication
      SnapshotName: MyApplication-snapshot-1
      SnapshotDescription: Before code update
Outputs:
  SnapshotArn:
    Value: !GetAtt MySnapshot.SnapshotArn
```

The following example template imports an enhanced snapshot from Amazon S3. Replace the role ARN, bucket ARN, and key prefix with your own values.

```yaml
Resources:
  MyImportedSnapshot:
    Type: AWS::KinesisAnalyticsV2::Snapshot
    Properties:
      SnapshotName: MyApplication-snapshot-imported
      ImportSourceConfiguration:
        SourceType: S3
        ImportRoleArn: arn:aws:iam::111122223333:role/MSFSnapshotImportRole
        SourceS3PrefixLocation:
          BucketARN: arn:aws:s3:::amzn-s3-demo-bucket
          KeyPrefix: imports/my-app/
```

To create the resource, the CloudFormation role needs `kinesisanalytics:CreateSnapshot` and `kinesisanalytics:DescribeSnapshot`. For an import, the role needs `kinesisanalytics:ImportSnapshot` instead of `kinesisanalytics:CreateSnapshot`, and `iam:PassRole` on the import role. If a customer managed key encrypts the application or the imported enhanced snapshot, the role also needs `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey` on that key. To delete the resource, the role needs `kinesisanalytics:DescribeSnapshot` and `kinesisanalytics:DeleteSnapshot`.

To restore an application from this enhanced snapshot, set `SnapshotArn` in `ApplicationRestoreConfiguration`. For more information, see [Upgrade with CloudFormation](snapshots-upgrade.md#snapshots-upgrade-cfn).

## Troubleshoot snapshot API errors
<a name="snapshots-manage-errors"></a>

The following table lists the errors that `CreateSnapshot`, `DescribeSnapshot`, `ListSnapshots`, and `DeleteSnapshot` return, with the cause and the fix.


| Exception | Operation | Cause | Fix | 
| --- | --- | --- | --- | 
| ResourceInUseException | CreateSnapshot | An enhanced snapshot with this name exists in the account and Region, in any status. | Use a different name, or delete the enhanced snapshot that holds the name. | 
| ResourceInUseException | CreateSnapshot | Another enhanced snapshot of the application is in the CREATING status. | Wait until that enhanced snapshot is READY or FAILED, then retry. | 
| ResourceInUseException | DeleteSnapshot | The enhanced snapshot is not in the READY or FAILED status. | Wait until the enhanced snapshot is READY or FAILED, then retry. For more information, see [Delete a snapshot while an operation uses it](#snapshots-manage-delete-protection-for-snapshots-in-use). | 
| InvalidApplicationConfigurationException | CreateSnapshot | The application status is not RUNNING, or another operation on the application is in progress. | Start the application, or wait for the other operation to complete. Then retry. | 
| InvalidApplicationConfigurationException | CreateSnapshot | The application uses an Apache Flink version earlier than 1.20. The message is CreateSnapshot requires Flink runtime 1.20 or later. | Upgrade the application to Apache Flink version 1.20 or later. For more information, see [Prerequisites](snapshots-setup.md#snapshots-setup-prerequisites). | 
| UnsupportedOperationException | CreateSnapshot | The application does not use enhanced snapshot mode, or the application is a SQL application. | Upgrade the application to enhanced snapshot mode. For more information, see [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md). | 
| InvalidArgumentException | CreateSnapshot | No application with the name in ApplicationName exists in the account and Region. | Check the application name with [`ListApplications`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplications.html). | 
| InvalidArgumentException | CreateSnapshot | The enhanced snapshot name breaks the name rules. | Use a name that follows the name rules. For more information, see [Enhanced snapshots as standalone resources](snapshots-how-it-works.md#snapshots-how-it-works-snapshots-as-standalone-resources). | 
| AccessDeniedException | CreateSnapshot | The caller cannot use the customer managed key of the application. | Grant the caller kms:Decrypt and kms:GenerateDataKey on the key. | 
| InvalidArgumentException | ListSnapshots | The NextToken value is not valid. | Send the NextToken value from the previous response, or omit it to start again. | 
| InvalidArgumentException | ListSnapshots | The request has two or more filters. | Send at most one filter, and filter the results in your code. | 
| InvalidArgumentException | DeleteSnapshot | The SnapshotCreationTimestamp value does not match the snapshot. | Copy the timestamp from DescribeSnapshot, then retry. | 
| LimitExceededException | CreateSnapshot | The account has the maximum number of enhanced snapshots. | Delete the enhanced snapshots that you no longer need. Then retry the request. | 
| TooManyTagsException | CreateSnapshot | The request has 51 to 200 tags. | Send 50 tags or fewer. | 
| ValidationException | CreateSnapshot | The request has more than 200 tags. | Send 50 tags or fewer. | 
| ResourceNotFoundException | DescribeSnapshot, DeleteSnapshot | No enhanced snapshot with this name exists, or the delete of the snapshot completed. | Check the name with ListSnapshots. | 
| AccessDeniedException | All | IAM denies the caller the action on the resource. For CreateSnapshot with Tags, this cause includes a denied TagResource. | Grant the action to the caller. For more information, see [Identity and Access Management for Amazon Managed Service for Apache Flink](security-iam.md). | 
| ValidationException | CreateSnapshot, ListSnapshots | The request has an empty Tags list, or a Limit value out of range. | Omit Tags, or set Limit from 1 through 50. | 