# Configuring how to handle files, objects, and

metadata

You can configure how AWS DataSync handles your files, objects, and their associated
metadata when transferring between locations.

For example, with recurring transfers, you might want to overwrite files in your
destination with changes in the source to keep the locations in sync. You can copy
properties such as POSIX permissions for files and folders, tags associated with
objects, and access control lists (ACLs).

## Transfer mode options

You can configure whether DataSync transfers only the data (including metadata)
that's changed following an initial copy or all data every time you run the
task. If you're planning on recurring transfers, you might only want to transfer
what's changed since your previous task execution.

| Option in console                          | Option in API                                                                                                                             | Description                                                                                                                                  |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Transfer only data that has<br>changed** | [TransferMode](API_Options.md#DataSync-Type-Options-TransferMode "API_Options.md#DataSync-Type-Options-TransferMode") set to<br>`CHANGED` | After your initial full transfer, DataSync copies only the data<br>and metadata that differs between the source and destination<br>location. |
| **Transfer all data**                      | [TransferMode](API_Options.md#DataSync-Type-Options-TransferMode "API_Options.md#DataSync-Type-Options-TransferMode") set to<br>`ALL`     | DataSync copies everything in the source to the destination<br>without comparing differences between the locations.                          |

## File and object handling

options

You can control some aspects of how DataSync treats your files or objects in the
destination location. For example, DataSync can delete files in the destination
that aren't in the source.

| Option in console      | Option in API                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Keep deleted files** | [PreserveDeletedFiles](API_Options.md#DataSync-Type-Options-PreserveDeletedFiles "API_Options.md#DataSync-Type-Options-PreserveDeletedFiles") | Specifies whether DataSync maintains files or objects in the<br>destination location that don't exist in the<br>source.<br>If you configure your task to delete objects from your<br>Amazon S3 bucket, you might incur minimum storage duration<br>charges for certain storage classes. For detailed<br>information, see [Storage class considerations with Amazon S3<br>transfers](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes").<br>WarningYou can't configure your task to delete data in the<br>destination and also [transfer all<br>data](#task-option-transfer-mode "#task-option-transfer-mode"). When you transfer all data, DataSync<br>doesn't scan your destination location and doesn't know<br>what to delete. |
| **Overwrite files**    | [OverwriteMode](API_Options.md#DataSync-Type-Options-OverwriteMode "API_Options.md#DataSync-Type-Options-OverwriteMode")                      | Specifies whether DataSync modifies data in the destination<br>location when the source data or metadata has changed. If<br>you don't configure your task to overwrite data, the<br>destination data isn't overwritten even if the source data<br>differs.<br>If your task overwrites objects, you might incur<br>additional charges for certain storage classes (for example,<br>for retrieval or early deletion). For detailed information,<br>see [Storage class considerations with Amazon S3<br>transfers](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes").                                                                                                                                                               |

## Metadata handling

options

DataSync can preserve file and object metadata during a transfer. The metadata
that DataSync can preserve depends on the storage systems involved and whether
those systems use a similar metadata structure.

Before configuring your task, make sure that you understand how DataSync handles
[metadata](metadata-copied.md "metadata-copied.md") and [special files](special-files-copied.md "special-files-copied.md") when transferring
between your source and destination locations.

###### Important

DataSync supports transfers to and from certain third-party cloud storage
systems, such as Google Cloud Storage and IBM Cloud Object Storage, which
handle system metadata in a way that is not fully S3-compatible. For these
transfers, DataSync attempts to copy metadata attributes such as
`ContentType`, `ContentEncoding`,
`ContentLanguage`, and `CacheControl` on a
best-effort basis. If the destination storage system does not apply these
attributes, they will be ignored during task verification.

| Option in console                    | Option in API                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Copy ownership**                   | [Gid](API_Options.md#DataSync-Type-Options-Gid "API_Options.md#DataSync-Type-Options-Gid") and [Uid](API_Options.md#DataSync-Type-Options-Uid "API_Options.md#DataSync-Type-Options-Uid")             | Specifies whether DataSync copies POSIX file and folder<br>ownership, such as the group ID of the file's owners and the<br>user ID of the file's owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Copy permissions**                 | [PosixPermissions](API_Options.md#DataSync-Type-Options-PosixPermissions "API_Options.md#DataSync-Type-Options-PosixPermissions")                                                                     | Specifies whether DataSync copies POSIX permissions for files<br>and folders from the source to the destination.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Copy timestamps**                  | [Atime](API_Options.md#DataSync-Type-Options-Atime "API_Options.md#DataSync-Type-Options-Atime") and [Mtime](API_Options.md#DataSync-Type-Options-Mtime "API_Options.md#DataSync-Type-Options-Mtime") | Specifies whether DataSync copies the timestamp metadata from<br>the source to the destination. Required when you need to run a task more than once.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Copy object tags**                 | [ObjectTags](API_Options.md#DataSync-Type-Options-ObjectTags "API_Options.md#DataSync-Type-Options-ObjectTags")                                                                                       | Specifies whether DataSync preserves the tags associated with<br>your objects when transferring between object storage<br>systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Copy ownership, DACLs, and SACLs** | [SecurityDescriptorCopyFlags](API_Options.md#DataSync-Type-Options-SecurityDescriptorCopyFlags "API_Options.md#DataSync-Type-Options-SecurityDescriptorCopyFlags")<br>set to `OWNER_DACL_SACL`        | DataSync copies the following:<br>• The object owner.<br>• NTFS discretionary access lists (DACLs), which<br>determine whether to grant access to an<br>object.<br>• NTFS system access control lists (SACLs), which<br>are used by administrators to log attempts to access<br>a secured object.<br>**Note**: SACLs are<br>not copied if you use SMB version 1.0.<br>Copying DACLs and SACLs requires granting specific<br>permissions to the Windows user that DataSync uses to<br>access your location using SMB. For more<br>information, see creating a location for [SMB](create-smb-location.md#configuring-smb "create-smb-location.md#configuring-smb"), [FSx for Windows File Server](create-fsx-location.md "create-fsx-location.md"),<br>or [FSx for ONTAP](create-ontap-location.md "create-ontap-location.md") (depending on the type of<br>location in your transfer). |
| **Copy ownership and DACLs**         | [SecurityDescriptorCopyFlags](API_Options.md#DataSync-Type-Options-SecurityDescriptorCopyFlags "API_Options.md#DataSync-Type-Options-SecurityDescriptorCopyFlags")<br>set to `OWNER_DACL`             | DataSync copies the following:<br>• The object owner.<br>• DACLs, which determine whether to grant access to<br>an object.<br>DataSync won't copy SACLs when you choose this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Do not copy ownership or ACLs**    | [SecurityDescriptorCopyFlags](API_Options.md#DataSync-Type-Options-SecurityDescriptorCopyFlags "API_Options.md#DataSync-Type-Options-SecurityDescriptorCopyFlags")<br>set to `NONE`                   | DataSync doesn't copy any ownership or permissions data. The<br>objects that DataSync writes to your destination location are<br>owned by the user whose credentials are provided for DataSync<br>to access the destination. Destination object permissions<br>are determined based on the permissions configured on the<br>destination server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Configuring file, object, and

metadata handling options

You can configure how DataSync handles files, objects, and metadata when
creating, editing, or starting your transfer task.

The following instructions describe how to configure file, object, and
metadata handling options when creating a task.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and
   then choose **Create task**.
3. Configure your task's source and destination locations.

For more information, see [Where can I transfer my data with
AWS DataSync?](working-with-locations.md "working-with-locations.md") 4. For **Transfer mode**, choose one of the
following options:

    * **Transfer only data that has
     changed**
    * **Transfer all data**

For more information about these options, see [Transfer mode options](#task-option-transfer-mode "#task-option-transfer-mode"). 5. Select **Keep deleted files** if you want
DataSync to maintain files or objects in the destination location
that don't exist in the source.

If you don't choose this option and your task deletes objects
from your Amazon S3 bucket, you might incur minimum storage duration
charges for certain storage classes. For detailed information,
see [Storage class considerations with Amazon S3
transfers](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes").

###### Warning

You can't deselect this option and enable
**Transfer all data**. When you
transfer all data, DataSync doesn't scan your destination
location and doesn't know what to delete. 6. Select **Overwrite files** if you want DataSync
to modify data in the destination location when the source data
or metadata has changed.

If your task overwrites objects, you might incur additional
charges for certain storage classes (for example, for retrieval
or early deletion). For detailed information, see [Storage class considerations with Amazon S3
transfers](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes").

If you don't choose this option, the destination data isn't
overwritten even if the source data differs. 7. Under **Transfer options**, select how you
want DataSync to handle metadata. For more information about the
options, see [Metadata handling
options](#task-option-metadata-handling "#task-option-metadata-handling").

###### Important

The options you see in the console depend on your task's
source and destination locations. You might have to expand
**Additional settings** to see some of
these options.

    * **Copy ownership**
    * **Copy permissions**
    * **Copy timestamps**
    * **Copy object tags**
    * **Copy ownership, DACLs, and
     SACLs**
    * **Copy ownership and DACLs**
    * **Do not copy ownership or
     ACLs**

You can configure file, object, and metadata handling options by using
the `Options` parameter with any of the following
operations:

- [CreateTask](API_CreateTask.md "API_CreateTask.md")
- [StartTaskExecution](API_StartTaskExecution.md "API_StartTaskExecution.md")
- [UpdateTask](API_UpdateTask.md "API_UpdateTask.md")
