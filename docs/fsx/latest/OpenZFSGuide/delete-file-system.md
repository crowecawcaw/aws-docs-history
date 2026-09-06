

# Deleting an Amazon FSx for OpenZFS file system
<a name="delete-file-system"></a>

This section contains instructions on how to delete a file system using the AWS CLI and the Amazon FSx API. For information on how to delete a file system using the Amazon FSx console, see [Step 3: Clean up your resources](getting-started.md#getting-started-step3).

**Note**  
Before deleting a file system, make sure there are no Amazon S3 access points attached to any volume. For information on how to list S3 access points attached to FSx for OpenZFS volumes, see [Listing S3 access point attachments](access-points-list.md). For information on how to delete S3 access points, see [Deleting an S3 access point attachment](delete-access-point.md).

**Topics**
+ [Deleting a file system](#delete-a-file-system-cli-api)

## Deleting a file system
<a name="delete-a-file-system-cli-api"></a>

**To delete a file system (AWS CLI and Amazon FSx API)**
+ Use the [delete-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/delete-file-system.html) CLI command or the [DeleteFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteFileSystem.html) API operation. The following is an example using the CLI to delete 
**Note**  
To delete a file system which still has child volumes present, you must include `DELETE_CHILD_VOLUMES_AND_SNAPSHOTS` in the `Options` property, otherwise the delete request will fail.

  ```
  aws fsx delete-file-system \
      --file-system-id fs-1234567890abcdef0
      --open-zfs-configuration '{ 
        "FinalBackupTags": [ 
           { 
              "Key": "string",
              "Value": "string"
           }
        ],
        "Options": [ "DELETE_CHILD_VOLUMES_AND_SNAPSHOTS" ],
        "SkipFinalBackup": boolean
     }'
  ```