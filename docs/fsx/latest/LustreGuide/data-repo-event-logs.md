

# Data repository event logs
<a name="data-repo-event-logs"></a>

You can turn on logging to CloudWatch Logs to log information about any failures experienced while importing or exporting files using import, export, data repository tasks and restore events. For more information, see [Logging with Amazon CloudWatch Logs](cw-event-logging.md).

**Note**  
When a data repository task fails, Amazon FSx also writes failure information to the task completion report. For more information about failure information in completion reports, see [Troubleshooting data repository task failures](failed-tasks.md).

**Topics**
+ [Import events](#import-event-logging)
+ [Export events](#export-event-logging)
+ [HSM restore events](#hsm-restore-event-logging)

## Import events
<a name="import-event-logging"></a>


| Error type | Log level | Log message | Root cause | Error code in completion report | 
| --- | --- | --- | --- | --- | 
| List objects failure | ERROR | Failed to list S3 objects in S3 bucket {{bucket\_name}} with prefix {{prefix}}. | Amazon FSx failed to list S3 objects in the S3 bucket. This can happen if the S3 bucket policy does not provide sufficient permissions to Amazon FSx. | N/A | 
| Unsupported S3 storage class | WARN | Failed to import S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} due to an S3 object in an unsupported tier {{S3\_tier\_name}}. | Amazon FSx was unable to import an S3 object because it's in an Amazon S3 storage class that is not supported, such as S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage class. | S3ObjectInUnsupportedTier | 
| Unsupported symlink storage class | ERROR | Failed to import S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} due to an S3 symlink object in an unsupported tier {{S3\_tier\_name}}. | Amazon FSx was unable to import a symlink object because it's in an Amazon S3 storage class that is not supported, such as S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage class. | S3SymlinkInUnsupportedTier | 
| S3 access denied | ERROR | Failed to import S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} because access to the S3 object was denied. | Access was denied to Amazon S3 for a data repository export import task.<br />For import tasks, the Amazon FSx file system must have permission to perform the `s3:HeadObject` and `s3:GetObject` operations to import from a linked data repository on S3.<br />For import tasks, if your S3 bucket uses server-side encryption with customer managed keys stored in AWS Key Management Service (SSE-KMS), you must follow the policy configurations in [Working with server-side encrypted Amazon S3 buckets](s3-server-side-encryption-support.md). | S3AccessDenied | 
| Delete access denied | ERROR | Failed to delete local file for S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} because access to the S3 object was denied. | Automatic import was denied access to an S3 object. | N/A | 
| Non-POSIX compliant object | ERROR | Failed to import S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} because S3 object is not POSIX compliant. | The Amazon S3 object exists but can't be imported because it isn't a POSIX-compliant object. For information about supported POSIX metadata, see [POSIX metadata support for data repositories](posix-metadata-support.md). | S3ObjectPathNotPosixCompliant | 
| Object type mismatch | ERROR | Failed to import S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} because an S3 object with the same name has already been imported into the file system. | The S3 object being imported is of a different type (file or directory) than an existing object with the same name in the file system. | S3ObjectTypeMismatch | 
| Directory metadata update failure | ERROR | Failed to update local directory metadata due to an internal error. | Directory metadata could not be imported due to an internal error. | N/A | 
| S3 object not found | ERROR | Failed to import S3 object with key {{key\_value}} because it was not found in S3 bucket {{bucket\_name}}. | Amazon FSx was unable to import file metadata because the corresponding object doesn't exist in the data repository. | S3FileDeleted | 
| S3 bucket not found | ERROR | Failed to import S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} due to bucket does not exist. | Amazon FSx cannot automatically import an S3 object to the file system because the S3 bucket no longer exists. | N/A | 
| S3 bucket not found | ERROR | Failed to delete local file for S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} due to bucket does not exist. | Amazon FSx cannot delete a file linked to an S3 object on the file system because the S3 bucket no longer exists. | N/A | 
| Directory creation failure | ERROR | Failed to create local directory due to an internal error. | Amazon FSx failed to automatically import a directory creation on the file system due to an internal error. | N/A | 
| Disk space full | ERROR | Failed to import S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} because the file system is full. | File system ran out of disk space on the metadata server(s) while creating file or directory. | N/A | 
| File name too long | ERROR | Failed to import S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} because the file exceeds the maximum supported file name length (255). | Amazon FSx was unable to import the S3 object because its file name exceeds the maximum supported file name length of 255 bytes. | N/A | 

## Export events
<a name="export-event-logging"></a>


| Error type | Log level | Log message | Root cause | Error code in completion report | 
| --- | --- | --- | --- | --- | 
| Access denied | ERROR | Failed to export file because access was denied to S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}}. | Access was denied to Amazon S3 for a data repository export task.<br />For export tasks, the Amazon FSx file system must have permission to perform the `s3:PutObject` operation to export to a linked data repository on S3. This permission is granted in the `AWSServiceRoleForFSxS3Access_{{fs-0123456789abcdef0}}` service-linked role. For more information, see [Using service-linked roles for Amazon FSx](using-service-linked-roles.md).<br />Because the export task requires data to flow outside a file system's VPC, this error can occur if the target repository has a bucket policy that contains one of the `aws:SourceVpc` or `aws:SourceVpce` IAM global condition keys.<br />If your S3 bucket contains objects uploaded from a different AWS account than your file system linked S3 bucket account, you can ensure that your data repository tasks can modify S3 metadata or overwrite S3 objects regardless of which account uploaded them. We recommend that you enable the S3 Object Ownership feature for your S3 bucket. This feature enables you to take ownership of new objects that other AWS accounts upload to your bucket, by forcing uploads to provide the `--acl bucket-owner-full-control` canned ACL. You enable S3 Object Ownership by choosing the **Bucket owner preferred** option in your S3 bucket. For more information, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide*. | S3AccessDenied | 
| Export path too long | ERROR | Failed to export file because the local file path size exceeds the maximum object key length supported by S3. | The export path is too long. The maximum object key length supported by S3 is 1,024 characters. | PathSizeTooLong | 
| File too large | ERROR | Failed to export file because the file size exceeds the maximum supported S3 objects size. | The maximum object size supported by Amazon S3 is 5 TiB. | FileSizeTooLarge | 
| KMS key not found | ERROR | Failed to export file for S3 object with key {{key\_value}} in S3 bucket {{bucket\_name}} because the bucket's KMS key was not found. | Amazon FSx was unable to export the file because the AWS KMS key couldn't be found. Be sure to use a key that's in the same AWS Region as the S3 bucket. For more information on creating KMS keys, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the AWS Key Management Service Developer Guide. | N/A | 
| Resource busy | ERROR | Failed to export file because it is being used by another process. | Amazon FSx was unable to export the file because it was being modified by another client on the file system. You can retry the task after your workflow has finished writing to the file. | ResourceBusy | 
| File released | WARN | Export skipped: Local file is in released state and a linked S3 object with key {{key\_value}} was not found in bucket {{bucket\_name}}. | Amazon FSx was unable to export the file because it was in a released state on the file system. | N/A | 
| Data repository path mismatch | WARN | Export skipped: local file does not belong to a data repository linked file system path. | Amazon FSx was unable to export because the object doesn't belong to a file system path that is linked to a data repository. | N/A | 
| Internal failure | ERROR | Automatic export encountered an internal error while exporting a file system object | The export failed because of an internal (auto-export- or lustre-level) error. | N/A | 
| Completion report upload failure | ERROR | Failed to upload data repository task completion report into {{bucket\_name}} | Amazon FSx was unable to upload the completion report. | N/A | 
| Completion report validation failure | ERROR | Failed to upload data repository task completion report into bucket {{bucket\_name}} because the completion report path {{report\_path}} does not belong to a data repository associated with this file system | Amazon FSx was unable to upload the completion report because the customer-provided S3 path does not belong to a linked data repository. | N/A | 

## HSM restore events
<a name="hsm-restore-event-logging"></a>


| Error type | Log level | Log message | Root cause | 
| --- | --- | --- | --- | 
| Access denied | ERROR | Failed to restore file because access was denied to S3 object {{object\_name}} in S3 bucket {{bucket\_name}}. | Access was denied to Amazon S3 when attempting to restore a file using HSM commands. The file system must have permission to perform the `s3:HeadObject` and `s3:GetObject` operations to restore from the linked data repository on S3. | 
| Unsupported S3 storage class | WARN | Failed to restore file because S3 object {{object\_name}} in bucket {{bucket\_name}} was in an unsupported {{S3\_storage\_class \_name}}. | Amazon FSx was unable to restore the file because the corresponding S3 object is in an S3 unsupported storage class, such as S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive. You must first restore the object from the Glacier storage class before using `hsm_restore`. | 
| S3 object not found | ERROR | Failed to restore file because S3 object with key {{key\_value}} was not found in S3 bucket {{bucket\_name}}. | Amazon FSx was unable to restore the file because the corresponding S3 object doesn't exist in the data repository. | 
| S3 bucket not found | ERROR | Failed to restore file because S3 bucket {{bucket\_name}} does not exist. | Amazon FSx cannot restore the file because the linked S3 bucket no longer exists. | 
| Disk space full | ERROR | Failed to restore file because there was no available storage space on the file system. | The file system ran out of available storage space while attempting to restore the file data from S3. Consider increasing the file system's storage capacity or releasing files to free up space. | 