

# Import and export enhanced snapshots
<a name="snapshots-import-export"></a>

You can export an enhanced snapshot to an Amazon S3 bucket. You can also import an Apache Flink savepoint from an Amazon S3 bucket as a new enhanced snapshot.

For example, you can import a savepoint that a self-managed Apache Flink cluster wrote. Then you can restore a Managed Service for Apache Flink application from the new enhanced snapshot that the import creates.

Import and export work within one account and one AWS Region. The Amazon S3 bucket must be in the same account and Region as the enhanced snapshot.

The `KeyPrefix` of the Amazon S3 location has 1 to 200 characters. For an export, end the `KeyPrefix` with a slash (`/`). Managed Service for Apache Flink adds the operation ID directly after the prefix.

The [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) and [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html) actions run asynchronously. Each call returns a `SnapshotOperationId` that you use to track the operation. You cannot cancel an import or an export. Import and export work whether or not an application uses enhanced snapshot mode.

## Set up the import and export role
<a name="snapshots-import-export-set-up-the-role"></a>

Managed Service for Apache Flink assumes an AWS Identity and Access Management (IAM) role that you supply to read from or write to your bucket. You pass the role in `ImportRoleArn` or `ExportRoleArn`. The role needs a trust policy and a permissions policy.

This procedure sets up the IAM role that Managed Service for Apache Flink assumes to read from or write to your Amazon S3 bucket during an import or an export.

**To set up the import or export role**

1. Open the [IAM console](https://console.aws.amazon.com/iam/home).

1. Create a role in the IAM console with the trust policy in [Trust policy](security-iam-snapshots.md#security-iam-snapshots-transfer-role-trust).

1. Attach one of the following permissions policies to the role in the IAM console:
   + For an import of source objects without a customer managed key, use [Import permissions policy](security-iam-snapshots.md#security-iam-snapshots-transfer-role-import).
   + For an import of source objects that a customer managed key encrypts, use [Import KMS permissions policy](security-iam-snapshots.md#security-iam-snapshots-transfer-role-import-kms).
   + For an export with `KeyType` set to `AWS_OWNED_KEY`, to a bucket whose default encryption does not use a customer managed key, use [Export permissions policy](security-iam-snapshots.md#security-iam-snapshots-transfer-role-export).
   + For an export with `KeyType` set to `CUSTOMER_MANAGED_KEY`, use [Export KMS permissions policy](security-iam-snapshots.md#security-iam-snapshots-transfer-role-export-kms).
   + For an export with `KeyType` set to `AWS_OWNED_KEY`, to a bucket whose default encryption uses a customer managed key, use [Export permissions policy](security-iam-snapshots.md#security-iam-snapshots-transfer-role-export). Also give the role permissions on the key of the bucket. For more information, see [Export an enhanced snapshot to Amazon S3](#snapshots-import-export-export-a-snapshot-to-amazon-s3).

1. Give the IAM principal that calls `ExportSnapshot` or `ImportSnapshot` the `iam:PassRole` permission on the role in the caller policy.

1. Give the same principal `kinesisanalytics:ImportSnapshot` on the ARN of the enhanced snapshot that the import creates. Add this permission to the caller policy for an import.

1. Give the same principal `kinesisanalytics:ExportSnapshot` on the ARN of the enhanced snapshot to export. Add this permission to the caller policy for an export.

The IAM principal that calls `ImportSnapshot` or `ExportSnapshot` needs a caller policy. The following caller policy allows an import and an export. It also allows `iam:PassRole` on both roles with the `iam:PassedToService` condition.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "kinesisanalytics:ImportSnapshot",
            "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-imported"
        },
        {
            "Effect": "Allow",
            "Action": "kinesisanalytics:TagResource",
            "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-imported"
        },
        {
            "Effect": "Allow",
            "Action": "kinesisanalytics:ExportSnapshot",
            "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": [
                "arn:aws:iam::111122223333:role/MSFSnapshotImportRole",
                "arn:aws:iam::111122223333:role/MSFSnapshotExportRole"
            ],
            "Condition": {
                "StringEquals": { "iam:PassedToService": "kinesisanalytics.amazonaws.com" }
            }
        }
    ]
}
```

The IAM principal that calls `ImportSnapshot` with `Tags` also needs `kinesisanalytics:TagResource` on the ARN of the new enhanced snapshot. If the caller does not have this permission, the request returns `AccessDeniedException`.

For the encryption keys that each import and export uses, see [Encryption for imported and exported snapshots](#snapshots-import-export-encryption-for-imported-and-exported-snapshots).

## Export an enhanced snapshot to Amazon S3
<a name="snapshots-import-export-export-a-snapshot-to-amazon-s3"></a>

Export an enhanced snapshot to keep a copy of the application state in your own Amazon S3 bucket. You can then process the state with your own Apache Flink tools or import it again later.

The AWS CLI examples on this page assume that the AWS CLI is configured with your credentials and a default AWS Region.

Before you export an enhanced snapshot, check the following requirements:
+ The enhanced snapshot status is `READY`. For any other status, `ExportSnapshot` returns `ResourceInUseException`.
+ No other export of the same enhanced snapshot is in progress. You can export an enhanced snapshot to only one destination at a time. While one export of the enhanced snapshot is in progress, `ExportSnapshot` returns `LimitExceededException` for a new export of it.
+ Your account has fewer than 10 imports and exports combined in progress in the Region. When 10 are in progress, a new import or export request returns `LimitExceededException`.
+ The snapshot is an enhanced snapshot. You cannot export an application snapshot (legacy).
+ The export role exists, and you have `iam:PassRole` on it. You also have `kinesisanalytics:ExportSnapshot` on the enhanced snapshot ARN.

The request needs `SnapshotName` and `ExportDestinationConfiguration`. In `ExportDestinationConfiguration`, set the following members:
+ `DestinationType`
+ `ExportRoleArn`
+ `DestinationS3PrefixLocation`

`DestinationEncryptionConfiguration` is optional. If you omit it, Managed Service for Apache Flink uses `AWS_OWNED_KEY`.

**To export an enhanced snapshot to Amazon S3**

1. Save the following request as `export.json`.

   ```
   {
       "SnapshotName": "MyApplication-snapshot-1",
       "ExportDestinationConfiguration": {
           "DestinationType": "S3",
           "ExportRoleArn": "arn:aws:iam::111122223333:role/MSFSnapshotExportRole",
           "DestinationEncryptionConfiguration": {
               "KeyType": "AWS_OWNED_KEY"
           },
           "DestinationS3PrefixLocation": {
               "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
               "KeyPrefix": "exports/my-app/"
           }
       }
   }
   ```

   Replace the snapshot name, the role ARN, the bucket ARN, and the key prefix with your own values.

1. Run the following AWS CLI command.

   ```
   PROMPT> aws kinesisanalyticsv2 export-snapshot --cli-input-json file://export.json
   ```

1. Save the `SnapshotOperationId` value from the response. For the full response, see [Export an enhanced snapshot](snapshots-api-examples.md#snapshots-api-examples-exportsnapshot).

If `KeyType` is `AWS_OWNED_KEY`, or if you omit `DestinationEncryptionConfiguration`, Managed Service for Apache Flink does not set an encryption header on the exported objects. Amazon S3 applies the default encryption of the bucket.

If the bucket default encryption uses a customer managed key, give the export role `kms:GenerateDataKey` and `kms:Decrypt` on that key. Use the condition `kms:ViaService` = `s3.{{region}}.amazonaws.com`. Do not add a `kms:EncryptionContext:aws:kinesisanalytics:arn` condition, because Managed Service for Apache Flink sends no encryption context in this case.

Managed Service for Apache Flink does not check the default encryption key of the bucket when it validates the request. If the export role cannot use that key, the export operation fails with the `KMSConfigError` error code.

Managed Service for Apache Flink writes the savepoint files under `{{KeyPrefix}}{{SnapshotOperationId}}/data/`. The `ExportedPrefix` field holds this path.

After an export ends, you can export the enhanced snapshot to the same location again.

**To track an export to completion**

1. Call [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html) with the `SnapshotName` and the `SnapshotOperationId`. In the following example, replace `MyApplication-snapshot-1` with the name of your enhanced snapshot. Replace `s9T0u1V2w3X4` with your `SnapshotOperationId`.

   Run the following AWS CLI command.

   ```
   PROMPT> aws kinesisanalyticsv2 describe-snapshot-operation \
       --snapshot-name MyApplication-snapshot-1 \
       --snapshot-operation-id s9T0u1V2w3X4
   ```

   The response is similar to the following:

   ```
   {
       "SnapshotOperationInfoDetails": {
           "SnapshotOperationId": "s9T0u1V2w3X4",
           "SnapshotOperation": "ExportSnapshot",
           "SnapshotOperationStatus": "IN_PROGRESS",
           "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
           "StartTime": 1767225600,
           "DestinationEncryptionConfigurationDescription": {
               "KeyType": "AWS_OWNED_KEY"
           }
       }
   }
   ```

1. Repeat the call until `SnapshotOperationStatus` is `SUCCESSFUL` or `FAILED`. An export can take several minutes, depending on the size of the enhanced snapshot.

1. Read `SnapshotDestinationLocationDescription.S3PrefixLocation.ExportedPrefix` for a `SUCCESSFUL` export. This value is the full path of the exported files.

During the export, the response omits `SnapshotDestinationLocationDescription`. After the export ends, `ExportedPrefix` holds the export path for a successful export and for a failed export. A failed export does not change the enhanced snapshot. The enhanced snapshot status stays `READY`.

After a failed export, Managed Service for Apache Flink does not delete the files that it already wrote. The completed files stay in your bucket under the `ExportedPrefix` path. Delete these files yourself.

A failed export can also leave incomplete multipart uploads in the bucket. Amazon S3 charges for the storage of incomplete uploads. To remove them, add an Amazon S3 lifecycle rule that aborts incomplete multipart uploads. Set the number of days in the rule to more than the duration of your longest export. If the rule aborts an upload during an export, the export fails with the `S3NoSuchUpload` error code. For more information, see [Configuring a bucket lifecycle configuration to delete incomplete multipart uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.html) in the *Amazon S3 User Guide*.

To list the exports of an enhanced snapshot, call [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html) with `SnapshotOperation` set to `ExportSnapshot`. For more information, see [Monitor enhanced snapshot operations](snapshots-monitor-operations.md).

## Import an enhanced snapshot from Amazon S3
<a name="snapshots-import-export-import-a-snapshot-from-amazon-s3"></a>

Import a savepoint to move application state from a self-managed Apache Flink cluster into Managed Service for Apache Flink.

The import source is an Apache Flink savepoint under a prefix in your Amazon S3 bucket. The prefix must hold the savepoint `_metadata` file. The import role must be able to read that file. If Managed Service for Apache Flink cannot find the file, `ImportSnapshot` returns `InvalidArgumentException`.

The savepoint must be relocatable. A relocatable savepoint holds no absolute paths to its original storage location, so you can move it to a new location. Managed Service for Apache Flink validates the savepoint metadata after it accepts the request. If the metadata is not valid, the import operation fails with the `InvalidSnapshotMetadata` error code.

The source must be a savepoint. You cannot import an Apache Flink checkpoint. A checkpoint is the recovery state that Apache Flink writes automatically. For more information, see the [comparison of checkpoints and savepoints](https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/state/checkpoints_vs_savepoints/) in the Apache Flink documentation.

Do not change or delete the source objects during the import. If a source object changes, the import fails with the `S3PreconditionFailed` error code. If you delete a source object, the import fails with the `S3NoSuchKey` error code.

Every source object must have a full-object CRC64NVME checksum. Files that `ExportSnapshot` writes meet this requirement.

The savepoint must use the canonical format. The canonical format is the same for all Apache Flink state backends. Managed Service for Apache Flink cannot import a savepoint in the native format, which is specific to one state backend. For more information, see [Savepoint format](https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/state/savepoints/#savepoint-format) in the Apache Flink documentation.

The `SnapshotName` must not match an existing enhanced snapshot in the account and Region. If the name is already in use, `ImportSnapshot` returns `ResourceInUseException`.

The `SnapshotName` must not start with `SYSTEMSNAPSHOT`, in any combination of uppercase and lowercase letters. This prefix is reserved for system snapshots. A name with this prefix returns `InvalidArgumentException`.

The request needs `SnapshotName` and `ImportSourceConfiguration`. In `ImportSourceConfiguration`, set `SourceType`, `ImportRoleArn`, and `SourceS3PrefixLocation`. `SourceEncryptionConfiguration` is an optional member of `ImportSourceConfiguration`. `DestinationEncryptionConfiguration`, `SnapshotDescription`, and `Tags` are optional top-level members of the request.

**To import an enhanced snapshot from Amazon S3**

1. Save the following request as `import.json`.

   ```
   {
       "SnapshotName": "MyApplication-snapshot-imported",
       "ImportSourceConfiguration": {
           "SourceType": "S3",
           "ImportRoleArn": "arn:aws:iam::111122223333:role/MSFSnapshotImportRole",
           "SourceS3PrefixLocation": {
               "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
               "KeyPrefix": "imports/my-app/"
           }
       },
       "DestinationEncryptionConfiguration": {
           "KeyId": "arn:aws:kms:aa-example-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
           "KeyType": "CUSTOMER_MANAGED_KEY"
       },
       "SnapshotDescription": "Imported from self-managed Apache Flink",
       "Tags": [ { "Key": "Environment", "Value": "prod" } ]
   }
   ```

   Replace the snapshot name, the role ARN, the bucket ARN, the key prefix, and the key ARN with your own values.

1. Run the following AWS CLI command.

   ```
   PROMPT> aws kinesisanalyticsv2 import-snapshot --cli-input-json file://import.json
   ```

1. Save the `SnapshotArn` and the `SnapshotOperationId` values from the response. For the full response, see [Import an enhanced snapshot](snapshots-api-examples.md#snapshots-api-examples-importsnapshot).

1. Call `DescribeSnapshotOperation` until `SnapshotOperationStatus` is `SUCCESSFUL` or `FAILED`. An import can take several minutes, depending on the size of the savepoint.

If the request fails, the AWS CLI shows the exception name and message. For each exception and its fix, see [Troubleshoot import and export errors](#snapshots-import-export-troubleshoot).

The new enhanced snapshot starts in the `CREATING` status. After a successful import, its status is `READY`. After a failed import, its status is `FAILED`. A `FAILED` enhanced snapshot keeps its name until you delete it.

An imported enhanced snapshot has no `RuntimeEnvironment` and no source application. A [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) request with a `SourceApplicationName` filter does not return imported enhanced snapshots.

You can restore an application from the imported enhanced snapshot after its status is `READY`. The restoring application must use enhanced snapshot mode. Managed Service for Apache Flink does not compare the runtime of the imported savepoint with the runtime of the application. Make sure that the Apache Flink version of the restoring application can read the saved state.

**Note**  
Do not restore an imported enhanced snapshot to an application that uses an older Apache Flink version than the application that created the snapshot. The older version might not read the saved state correctly. The restore can lose or corrupt application data.

The restoring application must have the same operator IDs as the job that wrote the savepoint.

For more information, see the following topics:
+ [Restore an application from an enhanced snapshot](snapshots-restore.md)
+ [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md)
+ [Monitor enhanced snapshot operations](snapshots-monitor-operations.md)

## Encryption for imported and exported snapshots
<a name="snapshots-import-export-encryption-for-imported-and-exported-snapshots"></a>

Managed Service for Apache Flink uses AWS KMS keys to encrypt enhanced snapshots and the Amazon S3 objects that an import reads or an export writes. This section describes which key each import and export uses and the format of the key in the request.

In an import or export request, `KeyId` must hold a full AWS KMS key ARN. Managed Service for Apache Flink rejects a key ID or an alias with `InvalidArgumentException`.

Each import or export uses a source key and a destination key. The Managed Service for Apache Flink service principal uses the key of the enhanced snapshot. The import or export role uses the key of the Amazon S3 objects.

The following table lists the source key and the destination key of each operation.


| Operation | Source key | Destination key | 
| --- | --- | --- | 
| ImportSnapshot | The key of the Amazon S3 objects. Set it in SourceEncryptionConfiguration. The import role uses it. | The key of the new enhanced snapshot. Set it in DestinationEncryptionConfiguration. The Managed Service for Apache Flink service principal uses it. | 
| ExportSnapshot | The key of the enhanced snapshot. The Managed Service for Apache Flink service principal uses it. | The key of the exported Amazon S3 objects. Set it in DestinationEncryptionConfiguration. The export role uses it. | 

On import, `DestinationEncryptionConfiguration` is optional. If you omit it, Managed Service for Apache Flink encrypts the new enhanced snapshot with an AWS owned key.

On export, `DestinationEncryptionConfiguration` is also optional. If you omit it, Managed Service for Apache Flink uses `AWS_OWNED_KEY`. The `DescribeSnapshotOperation` response then shows `AWS_OWNED_KEY` as the destination key type.

If a customer managed key encrypts the Amazon S3 objects, attach a permissions policy that grants access to that key to the import or export role. For the import and export permissions policies, see [IAM role for import and export](security-iam-snapshots.md#security-iam-snapshots-transfer-role).

An encryption context is a key-value pair that AWS KMS binds to each key operation. Managed Service for Apache Flink uses the encryption context key `aws:kinesisanalytics:arn`. Its value depends on the operation and the key:
+ **Import**: The ARN of the new enhanced snapshot.
+ **Export, destination key**: The ARN of the enhanced snapshot that you export.
+ **Export, key of the enhanced snapshot**: The ARN of the application that created the enhanced snapshot. For an imported enhanced snapshot, the snapshot ARN.

If a customer managed key in `DestinationEncryptionConfiguration` or `SourceEncryptionConfiguration` encrypts the Amazon S3 objects, the role permissions policies already include a `kms:EncryptionContext:aws:kinesisanalytics:arn` condition. The condition value is the enhanced snapshot ARN.

In the key policy of the enhanced snapshot key, allow the following actions for the principal that calls the request:
+ `ExportSnapshot`: `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey`.
+ `ImportSnapshot`: `kms:Decrypt` and `kms:GenerateDataKey`.

Add the condition `kms:ViaService` = `kinesisanalytics.{{region}}.amazonaws.com`, with your Region in place of {{region}}. The key policy must also allow the Managed Service for Apache Flink service principals. On import, use the ARN of the new enhanced snapshot. On export, use the ARN of the application that created the enhanced snapshot, or the snapshot ARN for an imported enhanced snapshot. For the key policy statements, see [Key policy for enhanced snapshot import and export](manage-cmk-api.md#create-cmk-kms-key-policy-snapshot-transfer). For more information about key policy constraints, see [KMS encryption context and constraints](key-management-flink.md#kms-encryption-context-constraints).

Managed Service for Apache Flink does not require a specific key policy design for the import or export role. Managed Service for Apache Flink checks only that the role can use the key.

Managed Service for Apache Flink checks customer managed keys when it validates the request. If the caller cannot use a customer managed key in the request, the call returns `AccessDeniedException`.

If you omit `SourceEncryptionConfiguration` on import, Managed Service for Apache Flink cannot validate the source key with the request. A key failure then appears later, on the import operation.

For more information about keys in Managed Service for Apache Flink, see [Key management in Amazon Managed Service for Apache Flink](key-management-flink.md).

## Troubleshoot import and export errors
<a name="snapshots-import-export-troubleshoot"></a>

A request that Managed Service for Apache Flink rejects returns an exception. The following table lists the exceptions that `ImportSnapshot` and `ExportSnapshot` can return.


| Exception | Cause | Fix | 
| --- | --- | --- | 
| InvalidArgumentException | A role, key, or bucket ARN is not valid, the source prefix has no \_metadata file, or the bucket is in another account or Region. | Use full ARNs. Check that the prefix holds the savepoint and that the role can read it. Use a bucket in the same account and Region as the enhanced snapshot. | 
| ResourceInUseException | An import uses a name that is already in use. An export targets an enhanced snapshot whose status is not READY. | Use a new name, or delete the old enhanced snapshot, before you import. Wait until the status is READY before you export. | 
| LimitExceededException | Your account already has 10 imports and exports in progress in the Region. For an export, another export of the enhanced snapshot might be in progress. For an import, the account might have the maximum number of enhanced snapshots. | Wait for an import or export to end. Wait for the other export of the enhanced snapshot to end before you export it again. Delete the enhanced snapshots that you do not need before you import. | 
| ResourceNotFoundException | An export names an enhanced snapshot that does not exist. | Check the SnapshotName in the request. | 
| ConcurrentModificationException | Another change to the resource is in progress. | Send the request again after the other change completes. | 
| TooManyTagsException | An import request has 51 to 200 tags. | Send 50 tags or fewer in the request. | 
| UnsupportedOperationException | Enhanced snapshots are not available for your account in the Region of the request. | Contact AWS Support. | 
| AccessDeniedException | The caller does not have permission for the action or for iam:PassRole. Or the caller cannot use a customer managed key in the request. | Add the permissions to the caller policy. Check the key policy and the role policy if the failure is for a key. | 

A failure after Managed Service for Apache Flink accepts the request does not return an exception. Instead, the operation status becomes `FAILED`. Call `DescribeSnapshotOperation` and read `SnapshotOperationFailureDetails.ErrorInfo`. The `ErrorCode` field holds a free-form string. Managed Service for Apache Flink can add new values without an API change.

Common causes of a failed import or export include the following:
+ `S3AccessDenied`: A bucket policy or an IAM policy denies the role access to the Amazon S3 objects. For an import, the bucket is the source bucket. For an export, the bucket is the destination bucket.
+ `STSAccessDenied`: The trust policy of the role rejects Managed Service for Apache Flink.
+ `KMSConfigError`: The AWS KMS key is missing, disabled, or pending deletion. Or the key policy denies the access that the operation needs.
+ `S3NoSuchKey`: You or another process deleted a source object during the import.
+ `MissingObjectChecksum`: A source object has no full-object CRC64NVME checksum.
+ `InvalidSnapshotMetadata`: The savepoint metadata is not valid or not supported.

For each `ErrorCode` value and its fix, see [Failure reasons](snapshots-monitor-operations.md#snapshots-monitor-operations-failure-reasons).