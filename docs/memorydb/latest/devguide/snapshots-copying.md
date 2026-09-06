

# Copying a snapshot
<a name="snapshots-copying"></a>

You can make a copy of any snapshot, whether it was created automatically or manually. When copying a snapshot, the same KMS encryption key as the source is used for the target unless specifically overridden. You can also export your snapshot so you can access it from outside MemoryDB. For guidance on exporting your snapshot, see [Exporting a snapshot](snapshots-exporting.md).

The following procedures show you how to copy a snapshot.

## Copying a snapshot (Console)
<a name="snapshots-copying-CON"></a>

**To copy a snapshot (console)**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. To see a list of your snapshots, from the left navigation pane choose **Snapshots**.

1. From the list of snapshots, choose the radio button to the left of the name of the snapshot you want to copy.

1. Choose **Actions** and then choose **Copy**.

1. In the **Copy snapshot** page, do the following:

   1. In the **New snapshot name** box, type a name for your new snapshot.

   1. Leave the optional **Target S3 Bucket** box blank. This field should only be used to export your snapshot and requires special S3 permissions. For information on exporting a snapshot, see [Exporting a snapshot](snapshots-exporting.md).

   1. Choose whether to use the default AWS KMS encryption key or a use a custom key. For more information, see [In-transit encryption (TLS) in MemoryDB](in-transit-encryption.md).

   1. Optionally, you can also add tags to the snapshot copy. 

   1. Choose **Copy**.

## Copying a snapshot (AWS CLI)
<a name="snapshots-copying-CLI"></a>

To copy a snapshot, use the `copy-snapshot` operation.

**Parameters**
+ `--source-snapshot-name` – Name of the snapshot to be copied.
+ `--target-snapshot-name` – Name of the snapshot's copy.
+ `--target-bucket` – Reserved for exporting a snapshot. Do not use this parameter when making a copy of a snapshot. For more information, see [Exporting a snapshot](snapshots-exporting.md).

The following example makes a copy of an automatic snapshot.

For Linux, macOS, or Unix:

```
aws memorydb copy-snapshot \
    --source-snapshot-name {{automatic.my-primary-2021-03-27-03-15}} \
    --target-snapshot-name {{my-snapshot-copy}}
```

For Windows:

```
aws memorydb copy-snapshot ^
    --source-snapshot-name {{automatic.my-primary-2021-03-27-03-15}} ^
    --target-snapshot-name {{my-snapshot-copy}}
```

For more information, see [copy-snapshot](https://docs.aws.amazon.com/cli/latest/reference/memorydb/copy-snapshot.html).

## Copying a snapshot (MemoryDB API)
<a name="snapshots-copying-API"></a>

To copy a snapshot, use the `copy-snapshot` operation with the following parameters:

**Parameters**
+ `SourceSnapshotName` – Name of the snapshot to be copied.
+ `TargetSnapshotName` – Name of the snapshot's copy.
+ `TargetBucket` – Reserved for exporting a snapshot. Do not use this parameter when making a copy of a snapshot. For more information, see [Exporting a snapshot](snapshots-exporting.md).

The following example makes a copy of an automatic snapshot.

**Example**  

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=CopySnapshot
    &SourceSnapshotName=automatic.my-primary-2021-03-27-03-15
    &TargetSnapshotName=my-snapshot-copy
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20210801T220302Z
    &Version=2021-01-01
    &X-Amz-Algorithm=Amazon4-HMAC-SHA256
    &X-Amz-Date=20210801T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Expires=20210801T220302Z
    &X-Amz-Credential=<credential>
    &X-Amz-Signature=<signature>
```

For more information, see [CopySnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CopySnapshot.html).