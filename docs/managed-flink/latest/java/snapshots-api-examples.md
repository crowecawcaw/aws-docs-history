

# Enhanced snapshot API examples

Use the following examples to call the enhanced snapshot API actions. Each snapshot action example shows the full request and response. The `CreateApplication` and `UpdateApplication` examples show only the request. For information about how to use a JSON file for input for an API action, see [Managed Service for Apache Flink API example code](api-examples.md).

The examples use the account `111122223333`, the Region `aa-example-1`, the application `MyApplication`, and the enhanced snapshot `MyApplication-snapshot-1`. Timestamps are in epoch seconds.

## Request examples
<a name="snapshots-api-examples-request-examples"></a>

Each of the following sections shows one API action.

### Create an enhanced snapshot
<a name="snapshots-api-examples-createsnapshot"></a>

The following example request for the [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) action creates an enhanced snapshot of a running application:

```json
{
    "ApplicationName": "MyApplication",
    "SnapshotName": "MyApplication-snapshot-1",
    "SnapshotDescription": "Before code update",
    "Tags": [ { "Key": "Environment", "Value": "prod" } ]
}
```

The following example shows the response:

```json
{
    "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
    "SnapshotStatus": "CREATING",
    "SnapshotOperationId": "a1B2c3D4e5F6",
    "SnapshotOperationStatus": "IN_PROGRESS"
}
```

### Describe an enhanced snapshot
<a name="snapshots-api-examples-describesnapshot"></a>

The following example request for the [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html) action returns the details of an enhanced snapshot:

```json
{
    "SnapshotName": "MyApplication-snapshot-1"
}
```

The following example shows the response:

```json
{
    "SnapshotInfoDetails": {
        "SnapshotName": "MyApplication-snapshot-1",
        "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
        "SnapshotDescription": "Before code update",
        "SnapshotStatus": "READY",
        "SnapshotCreationTimestamp": 1767225600,
        "RuntimeEnvironment": "FLINK-1_20",
        "SnapshotSizeInBytes": 104857600,
        "SnapshotEncryptionConfigurationDescription": {
            "KeyType": "AWS_OWNED_KEY"
        },
        "SnapshotInitiator": "USER",
        "SnapshotInitiatorOperation": "CreateSnapshot",
        "SnapshotSourceDescription": {
            "SourceApplicationDescription": {
                "ApplicationName": "MyApplication",
                "ApplicationCreationTimestamp": 1764547200,
                "ApplicationVersionId": 3
            }
        },
        "SnapshotFormat": "CANONICAL"
    }
}
```

### List the enhanced snapshots in an account
<a name="snapshots-api-examples-listsnapshots"></a>

The following example request for the [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) action lists the enhanced snapshots in the account and Region.

All filter fields are optional. The request accepts at most one of these filter fields: `SourceApplicationName`, `SnapshotInitiator`, `SnapshotInitiatorOperation`, or `SnapshotStatus`.

```json
{
    "Limit": 50
}
```

The following example shows the response. The newest enhanced snapshot comes first.

```json
{
    "SnapshotInfoList": [
        {
            "SnapshotName": "SYSTEMSNAPSHOT-STOP-MyApplication-1767312000000",
            "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/SYSTEMSNAPSHOT-STOP-MyApplication-1767312000000",
            "SnapshotStatus": "READY",
            "SnapshotCreationTimestamp": 1767312000,
            "SnapshotInitiator": "SYSTEM",
            "SnapshotInitiatorOperation": "SystemCreateSnapshot",
            "SourceApplicationName": "MyApplication",
            "SnapshotFormat": "CANONICAL"
        },
        {
            "SnapshotName": "MyApplication-snapshot-1",
            "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
            "SnapshotStatus": "READY",
            "SnapshotCreationTimestamp": 1767225600,
            "SnapshotInitiator": "USER",
            "SnapshotInitiatorOperation": "CreateSnapshot",
            "SourceApplicationName": "MyApplication",
            "SnapshotFormat": "CANONICAL"
        }
    ]
}
```

### Delete an enhanced snapshot
<a name="snapshots-api-examples-deletesnapshot"></a>

The following example request for the [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html) action deletes an enhanced snapshot. Copy the `SnapshotCreationTimestamp` value from the `DescribeSnapshot` response.

```json
{
    "SnapshotName": "MyApplication-snapshot-1",
    "SnapshotCreationTimestamp": 1767225600
}
```

The following example shows the response:

```json
{
    "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
    "SnapshotStatus": "DELETING",
    "SnapshotOperationId": "g7H8i9J0k1L2",
    "SnapshotOperationStatus": "IN_PROGRESS"
}
```

### Import an enhanced snapshot
<a name="snapshots-api-examples-importsnapshot"></a>

The following example request for the [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html) action imports an Apache Flink savepoint from Amazon S3 as a new enhanced snapshot:

```json
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

The following example shows the response:

```json
{
    "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-imported",
    "SnapshotStatus": "CREATING",
    "SnapshotOperationId": "m3N4o5P6q7R8",
    "SnapshotOperationStatus": "IN_PROGRESS"
}
```

### Export an enhanced snapshot
<a name="snapshots-api-examples-exportsnapshot"></a>

The following example request for the [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) action exports an enhanced snapshot to an Amazon S3 bucket. `DestinationEncryptionConfiguration` is optional. If you omit it, Managed Service for Apache Flink uses `AWS_OWNED_KEY`.

```json
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

The following example shows the response. The response has no snapshot ARN or snapshot status.

```json
{
    "SnapshotOperationId": "s9T0u1V2w3X4",
    "SnapshotOperationStatus": "IN_PROGRESS"
}
```

### Describe an enhanced snapshot operation
<a name="snapshots-api-examples-describesnapshotoperation"></a>

The following example request for the [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html) action returns the details of an export operation:

```json
{
    "SnapshotName": "MyApplication-snapshot-1",
    "SnapshotOperationId": "s9T0u1V2w3X4"
}
```

The following example shows the response for a successful export. The `ExportedPrefix` field holds the full path of the exported files.

```json
{
    "SnapshotOperationInfoDetails": {
        "SnapshotOperationId": "s9T0u1V2w3X4",
        "SnapshotOperation": "ExportSnapshot",
        "SnapshotOperationStatus": "SUCCESSFUL",
        "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
        "DestinationEncryptionConfigurationDescription": {
            "KeyType": "AWS_OWNED_KEY"
        },
        "SnapshotDestinationLocationDescription": {
            "LocationType": "S3",
            "S3PrefixLocation": {
                "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
                "KeyPrefix": "exports/my-app/",
                "ExportedPrefix": "exports/my-app/s9T0u1V2w3X4/data/"
            }
        },
        "StartTime": 1767229200,
        "EndTime": 1767229800
    }
}
```

The following example shows the response for a failed export. The response adds `SnapshotOperationFailureDetails`. `S3PrefixLocation` also includes `ExportedPrefix` for a failed export.

```json
{
    "SnapshotOperationInfoDetails": {
        "SnapshotOperationId": "y5Z6a7B8c9D0",
        "SnapshotOperation": "ExportSnapshot",
        "SnapshotOperationStatus": "FAILED",
        "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
        "DestinationEncryptionConfigurationDescription": {
            "KeyType": "AWS_OWNED_KEY"
        },
        "SnapshotDestinationLocationDescription": {
            "LocationType": "S3",
            "S3PrefixLocation": {
                "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
                "KeyPrefix": "exports/my-app/",
                "ExportedPrefix": "exports/my-app/y5Z6a7B8c9D0/data/"
            }
        },
        "StartTime": 1767232800,
        "EndTime": 1767233100,
        "SnapshotOperationFailureDetails": {
            "ErrorInfo": {
                "ErrorCode": "S3AccessDenied",
                "ErrorString": "..."
            }
        }
    }
}
```

### List the operations of an enhanced snapshot
<a name="snapshots-api-examples-listsnapshotoperations"></a>

The following example request for the [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html) action lists the failed operations of an enhanced snapshot. The request accepts at most one of these filter fields: `SnapshotOperation` or `SnapshotOperationStatus`.

```json
{
    "SnapshotName": "MyApplication-snapshot-1",
    "SnapshotOperationStatus": "FAILED",
    "Limit": 50
}
```

The following example shows the response:

```json
{
    "SnapshotOperationInfoList": [
        {
            "SnapshotOperationId": "y5Z6a7B8c9D0",
            "SnapshotOperation": "ExportSnapshot",
            "SnapshotOperationStatus": "FAILED",
            "StartTime": 1767232800,
            "EndTime": 1767233100
        }
    ]
}
```

### Create an application in enhanced snapshot mode
<a name="snapshots-api-examples-createapplication"></a>

The following example request for the [`CreateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html) action creates an application in enhanced snapshot mode. Set `SnapshotMode` to `ENHANCED_SNAPSHOTS`. The request must include `SnapshotsEnabled`. Set `SnapshotsEnabled` to `true` to turn on system snapshots.

```json
{
    "ApplicationName": "MyApplication",
    "RuntimeEnvironment": "FLINK-1_20",
    "ServiceExecutionRole": "arn:aws:iam::111122223333:role/MyApplicationServiceRole",
    "ApplicationConfiguration": {
        "ApplicationCodeConfiguration": {
            "CodeContent": {
                "S3ContentLocation": {
                    "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
                    "FileKey": "my-flink-app.jar"
                }
            },
            "CodeContentType": "ZIPFILE"
        },
        "ApplicationSnapshotConfiguration": {
            "SnapshotsEnabled": true,
            "SnapshotMode": "ENHANCED_SNAPSHOTS"
        }
    }
}
```

### Upgrade an existing application to enhanced snapshot mode
<a name="snapshots-api-examples-opt-in"></a>

The following example request for the [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) action upgrades an application to enhanced snapshot mode. The request must include `SnapshotsEnabledUpdate` together with `SnapshotModeUpdate`.

**Note**  
You cannot set `SnapshotModeUpdate` back to `APPLICATION_SNAPSHOTS_LEGACY`. That request returns `InvalidArgumentException`. To return to application snapshots (legacy), call `RollbackApplication` when the upgrade is still the most recent update. For more information, see [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md).

```json
{
    "ApplicationName": "MyApplication",
    "CurrentApplicationVersionId": 3,
    "ApplicationConfigurationUpdate": {
        "ApplicationSnapshotConfigurationUpdate": {
            "SnapshotsEnabledUpdate": true,
            "SnapshotModeUpdate": "ENHANCED_SNAPSHOTS"
        }
    }
}
```

### Start an application from an enhanced snapshot
<a name="snapshots-api-examples-startapplication"></a>

The following example request for the [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html) action starts an application from an enhanced snapshot. Set `ApplicationRestoreType` to `RESTORE_FROM_CUSTOM_SNAPSHOT`. Identify the enhanced snapshot with `SnapshotArn`, not `SnapshotName`.

```json
{
    "ApplicationName": "MyApplication",
    "RunConfiguration": {
        "ApplicationRestoreConfiguration": {
            "ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT",
            "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
        }
    }
}
```

The following example shows the response:

```json
{
    "OperationId": "Abc123Def456"
}
```

### Update an application and restore from an enhanced snapshot
<a name="snapshots-api-examples-updateapplication-restore"></a>

The following example request for the `UpdateApplication` action restores a running application from an enhanced snapshot. The application must be in the `RUNNING` status.

```json
{
    "ApplicationName": "MyApplication",
    "CurrentApplicationVersionId": 4,
    "RunConfigurationUpdate": {
        "ApplicationRestoreConfiguration": {
            "ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT",
            "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
        }
    }
}
```

For more information, see [Restore an application from an enhanced snapshot](snapshots-restore.md).