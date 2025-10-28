# Monitoring your data transfers with task reports

_Task reports_ provide detailed information about what AWS DataSync
attempts to transfer, skip, verify, and delete during a task execution. For more
information, see [How DataSync transfers files, objects, and
directories](how-datasync-transfer-works.md#transferring-files "how-datasync-transfer-works.md#transferring-files").

Task reports are generated in JSON format. You can customize the level of detail in your
reports:

- [Summary only task reports](#task-report-types-summary "#task-report-types-summary") give
  you the necessary details about your task execution, such as how many files
  transferred and whether DataSync could verify the data integrity of those files.
- [Standard task reports](#task-report-types-standard "#task-report-types-standard") include a
  summary plus detailed reports that list each file, object, or folder that DataSync
  attempts to transfer, skip, verify, and delete. With a standard task report, you can
  also specify the [report level](#task-report-level "#task-report-level") to show only
  the task execution's errors or its successes and errors.

## Use cases

Here are some situations where task reports can help you monitor and audit your data
transfers:

- When migrating millions of files, quickly identify files that DataSync has issues
  transferring.
- Verify chain-of-custody processes for your files.

## Summary only task reports

A report that's only a summary of a task execution includes the following
details:

- The AWS account that ran the task execution
- The source and destination locations
- The total number of files, objects, and folders that were skipped,
  transferred, verified, and deleted
- The total bytes (logical and physical) that were transferred
- If the task execution was completed, canceled, or encountered an error
- The start and end times (including the total time of the transfer)
- The task's settings (such as bandwidth limits, data integrity verification,
  and other options for your DataSync transfer)

## Standard task reports

A standard task report includes a [summary](#task-report-types-summary "#task-report-types-summary") of your task execution plus detailed reports of what DataSync attempts
to transfer, skip, verify, and delete.

###### Topics

- [Report level](#task-report-level "#task-report-level")
- [Transferred reports](#task-report-types-transferred "#task-report-types-transferred")
- [Skipped reports](#task-report-types-skipped "#task-report-types-skipped")
- [Verified reports](#task-report-types-verified "#task-report-types-verified")
- [Deleted reports](#task-report-types-deleted "#task-report-types-deleted")

### Report level

With standard task reports, you can choose one of the following report
levels:

- Errors only
- Successes and errors (essentially a list of everything that happened
  during your task execution)

For example, you might want to see which files DataSync skipped successfully during
your transfer and which ones it didn't. Files that DataSync skipped successfully might
be ones that you purposely want DataSync to exclude because they already exist in your
destination location. However, a skipped error for instance might indicate that
DataSync doesn't have the right permissions to read a file.

### Transferred reports

A list of files, objects, and directories that DataSync attempted to transfer during
your task execution. A transferred report includes the following details:

- The paths for the transferred data
- What was transferred (content, metadata, or both)
- The metadata, which includes the data type, content size (objects and
  files only), and more
- The time when an item was transferred
- The object version (if the destination is an Amazon S3 bucket that has
  versioning enabled)
- If something was overwritten in the destination
- Whether an item transferred successfully

###### Note

When moving data between S3 buckets, the prefix that you specify in your [source location](create-s3-location.md "create-s3-location.md") can show up in your
report (or in Amazon CloudWatch logs), even if that prefix doesn't exist as an object in
your destination location. (In the DataSync console, you might also notice this
prefix showing up as skipped or verified data.)

### Skipped reports

A list of files, objects, and directories that DataSync finds in your source location
but didn't attempt to transfer.
The
reasons DataSync skips data can depend on several factors, such as how you configure
your task and storage system permissions. Here are some examples:

- There's a file that exists in your source and destination locations. The
  file in the source hasn't been modified since the previous task execution.
  Since you're [only transferring data that
  has changed](configure-metadata.md#task-option-transfer-mode "configure-metadata.md#task-option-transfer-mode"), DataSync doesn't transfer that file next time you run
  your task.
- An object that exists in both of your locations changes in your source.
  When you run your task, DataSync skips this object in your destination because
  your task doesn't [overwrite
  data in the destination](configure-metadata.md#task-option-file-object-handling "configure-metadata.md#task-option-file-object-handling").
- DataSync skips an object in your source that's using an [archival storage class](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes") and isn't
  restored. You must restore an archived object for DataSync to read it.
- DataSync skips a file, object, or directory in your source location because
  it can't read it. If this happens and isn't expected, check your storage's
  access permissions and make sure that DataSync can read what was
  skipped.

A skipped report includes the following details:

- The paths for skipped data
- The time when an item was skipped
- The reason it was skipped
- Whether an item was skipped successfully

###### Note

Skipped reports can be large when they include successes and errors, you
configure your task to [transfer only the data
that has changed](configure-metadata.md "configure-metadata.md"), and source data already exists in the
destination.

### Verified reports

A list of files, objects, and directories that DataSync attempted to verify the
integrity of during your task execution. A verified data report includes the
following details:

- The paths for verified data
- The time when an item was verified
- The reason for the verification error (if any)
- The source and destination SHA256 checksums (files only)
- Whether an item was successfully verified

Note the following about verified reports:

- When you configure your task to [verify only transferred
  data](configure-data-verification-options.md "configure-data-verification-options.md"), DataSync doesn't verify directories in some situations or
  files or objects that fail to transfer. In either case, DataSync doesn't
  include unverified data in this report.
- If you're using [Enhanced mode](choosing-task-mode.md "choosing-task-mode.md"),
  verification might take longer than usual if you're transferring large
  objects.

### Deleted reports

A list of files, directories, and objects that were deleted during your task
execution. DataSync generates this report only if you [configure your task](configure-metadata.md "configure-metadata.md") to delete data in the
destination location that isn't in the source. A deleted data report includes the
following details:

- The paths for deleted data
- Whether an item was successfully deleted
- The time when an item was deleted

## Example task reports

The level of detail in your task report is up to you. Here are some example
transferred data reports with the following configuration:

- **Report type** – Standard
- **Report level** – Successes and errors

###### Note

Reports use the ISO-8601 standard for the timestamp format. Times are in UTC and
measured in nanoseconds. This behavior differs from how some other task report
metrics are measured. For example, [task
execution details](API_TaskExecutionResultDetail.md "API_TaskExecutionResultDetail.md"), such as `TransferDuration` and
`VerifyDuration`, are measured in milliseconds.

Enhanced mode
task reports use a somewhat different schema than Basic mode task reports. The
following examples can help you know what to expect from your reports depending on the
[task mode](choosing-task-mode.md "choosing-task-mode.md") you
use.

**Example transferred data reports with success status**

The following reports show successful transfers for an object named
`object1.txt`.

Enhanced mode

```
{
    "TaskExecutionId": "exec-abcdefgh12345678",
    "Transferred": [{
        "RelativePath": "object1.txt",
        "SourceMetadata": {
            "Type": "Object",
            "ContentSize": 6,
            "LastModified": "2024-10-04T14:40:55Z",
            "SystemMetadata": {
                "ContentType": "binary/octet-stream",
                "ETag": "\"9b2d7e1f8054c3a2041905d0378e6f14\"",
                "ServerSideEncryption": "AES256"
            },
            "UserMetadata": {},
            "Tags": []
        },
        "Overwrite": "False",
        "DstS3VersionId": "jtqRtX3jN4J2G8k0sFSGYK1f35KqpAVP",
        "TransferTimestamp": "2024-10-04T14:48:39.748862183Z",
        "TransferType": "CONTENT_AND_METADATA",
        "TransferStatus": "SUCCESS"
    }]
}
```

Basic mode

```
{
    "TaskExecutionId": "exec-abcdefgh12345678",
    "Transferred": [{
        "RelativePath": "/object1.txt",
        "SrcMetadata": {
            "Type": "Regular",
            "ContentSize": 6,
            "Mtime": "2022-01-07T16:59:26.136114671Z",
            "Atime": "2022-01-07T16:59:26.136114671Z",
            "Uid": 0,
            "Gid": 0,
            "Mode": "0644"
        },
        "Overwrite": "False",
        "DstS3VersionId": "jtqRtX3jN4J2G8k0sFSGYK1f35KqpAVP",
        "TransferTimestamp": "2022-01-07T16:59:45.747270957Z",
        "TransferType": "CONTENT_AND_METADATA",
        "TransferStatus": "SUCCESS"
    }]
}
```

**Example transferred data reports with error status**

The following reports provide examples of when DataSync can't transfer an
object named `object1.txt`.

Enhanced mode
This report shows that DataSync can't access an object named
`object1.txt` because of an AWS KMS
permissions issue. (If you get an error like this, see [Accessing S3 buckets using
server-side encryption](create-s3-location.md#create-s3-location-encryption "create-s3-location.md#create-s3-location-encryption").)

```
{
    "TaskExecutionId": "exec-abcdefgh12345678",
    "Transferred": [{
        "RelativePath": "object1.txt",
        "SourceMetadata": {
            "Type": "Object",
            "ContentSize": 6,
            "LastModified": "2022-10-07T20:48:32Z",
            "SystemMetadata": {
                "ContentType": "binary/octet-stream",
                "ETag": "\"3a7c0b2f1d9e5c4a6f8b2e0d1c9f7a3b2\"",
                "ServerSideEncryption": "AES256"
            },
            "UserMetadata": {},
            "Tags": []
        },
        "Overwrite": "False",
        "TransferTimestamp": "2022-10-09T16:05:11.134040717Z",
        "TransferType": "CONTENT_AND_METADATA",
        "TransferStatus": "FAILED",
        "ErrorCode": "AccessDenied",
        "ErrorDetail": "User: arn:aws:sts::111222333444:assumed-role/AWSDataSyncS3Bucket/AwsSync-loc-0b3017fc4ba4a2d8d is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:kms:us-east-1:111222333444:key/1111aaaa-22bb-33cc-44d-5555eeee6666 because no identity-based policy allows the kms:GenerateDataKey action"
    }]
}
```

Basic mode
This report shows that an object named
`object1.txt` didn't transfer because of
an S3 bucket permissions issue. (If you get an error like this,
see [Providing DataSync access to S3
buckets](create-s3-location.md#create-s3-location-access "create-s3-location.md#create-s3-location-access").)

```
{
    "TaskExecutionId": "exec-abcdefgh12345678",
    "Transferred": [{
        "RelativePath": "/object1.txt",
        "SrcMetadata": {
            "Type": "Regular",
            "ContentSize": 6,
            "Mtime": "2022-01-07T16:59:26.136114671Z",
            "Atime": "2022-01-07T16:59:26.136114671Z",
            "Uid": 0,
            "Gid": 0,
            "Mode": "0644"
        },
        "Overwrite": "False",
        "DstS3VersionId": "jtqRtX3jN4J2G8k0sFSGYK1f35KqpAVP",
        "TransferTimestamp": "2022-01-07T16:59:45.747270957Z",
        "TransferType": "CONTENT_AND_METADATA",
        "TransferStatus": "FAILED",
        "FailureReason": "S3 Get Object Failed",
        "FailureCode": 40974
    }]
}
```

## Limitations

- Individual task reports can't exceed 5 MB. If you're copying a large number of
  files, your task report might be split into multiple reports.
- There are situations when creating task reports can affect the performance of
  your data transfer. For example, you might notice this when your network
  connection has high latency and the files you're transferring are small or
  you're copying only metadata changes.
