

# Actions, resources, and condition keys for Amazon FSx
<a name="list_fsx"></a>

Amazon FSx (service prefix: `fsx`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/fsx/latest/APIReference/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/fsx/fsx.json) for this service.

**Topics**
+ [API operations defined by Amazon FSx](#list_fsx-operations)
+ [Actions defined by Amazon FSx](#list_fsx-actions-as-permissions)
+ [Permission-only actions for Amazon FSx](#list_fsx-permission-only-actions)
+ [Resource types defined by Amazon FSx](#list_fsx-resources-for-iam-policies)
+ [Condition keys for Amazon FSx](#list_fsx-policy-keys)

## API operations defined by Amazon FSx
<a name="list_fsx-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_fsx-actions-as-permissions).




- **   AssociateFileSystemAliases  **
  - **IAM action:**  [fsx:AssociateFileSystemAliases](#list_fsx-action-AssociateFileSystemAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelDataRepositoryTask  **
  - **IAM action:**  [fsx:CancelDataRepositoryTask](#list_fsx-action-CancelDataRepositoryTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyBackup  **
  - **IAM action:**  [fsx:CopyBackup](#list_fsx-action-CopyBackup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CopySnapshotAndUpdateVolume  **
  - **IAM action:**  [fsx:CopySnapshotAndUpdateVolume](#list_fsx-action-CopySnapshotAndUpdateVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAndAttachS3AccessPoint  **
  - **IAM action:**  [fsx:CreateAndAttachS3AccessPoint](#list_fsx-action-CreateAndAttachS3AccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBackup  **
  - **IAM action:**  [fsx:CreateBackup](#list_fsx-action-CreateBackup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataRepositoryAssociation  **
  - **IAM action:**  [fsx:CreateDataRepositoryAssociation](#list_fsx-action-CreateDataRepositoryAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataRepositoryTask  **
  - **IAM action:**  [fsx:CreateDataRepositoryTask](#list_fsx-action-CreateDataRepositoryTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFileCache  **
  - **IAM action:**  [fsx:CreateDataRepositoryAssociation](#list_fsx-action-CreateDataRepositoryAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:CreateFileCache](#list_fsx-action-CreateFileCache)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFileSystem  **
  - **IAM action:**  [fsx:CreateFileSystem](#list_fsx-action-CreateFileSystem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFileSystemFromBackup  **
  - **IAM action:**  [fsx:CreateFileSystemFromBackup](#list_fsx-action-CreateFileSystemFromBackup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSnapshot  **
  - **IAM action:**  [fsx:CreateSnapshot](#list_fsx-action-CreateSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStorageVirtualMachine  **
  - **IAM action:**  [fsx:CreateStorageVirtualMachine](#list_fsx-action-CreateStorageVirtualMachine)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVolume  **
  - **IAM action:**  [fsx:CreateVolume](#list_fsx-action-CreateVolume)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVolumeFromBackup  **
  - **IAM action:**  [fsx:CreateVolumeFromBackup](#list_fsx-action-CreateVolumeFromBackup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteBackup  **
  - **IAM action:**  [fsx:DeleteBackup](#list_fsx-action-DeleteBackup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataRepositoryAssociation  **
  - **IAM action:**  [fsx:DeleteDataRepositoryAssociation](#list_fsx-action-DeleteDataRepositoryAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFileCache  **
  - **IAM action:**  [fsx:DeleteDataRepositoryAssociation](#list_fsx-action-DeleteDataRepositoryAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:DeleteFileCache](#list_fsx-action-DeleteFileCache)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteFileSystem  **
  - **IAM action:**  [fsx:CreateBackup](#list_fsx-action-CreateBackup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:DeleteFileSystem](#list_fsx-action-DeleteFileSystem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteSnapshot  **
  - **IAM action:**  [fsx:DeleteSnapshot](#list_fsx-action-DeleteSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStorageVirtualMachine  **
  - **IAM action:**  [fsx:DeleteStorageVirtualMachine](#list_fsx-action-DeleteStorageVirtualMachine) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVolume  **
  - **IAM action:**  [fsx:BypassSnaplockEnterpriseRetention](#list_fsx-action-BypassSnaplockEnterpriseRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [fsx:DeleteVolume](#list_fsx-action-DeleteVolume)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DescribeBackups  **
  - **IAM action:**  [fsx:DescribeBackups](#list_fsx-action-DescribeBackups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataRepositoryAssociations  **
  - **IAM action:**  [fsx:DescribeDataRepositoryAssociations](#list_fsx-action-DescribeDataRepositoryAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataRepositoryTasks  **
  - **IAM action:**  [fsx:DescribeDataRepositoryTasks](#list_fsx-action-DescribeDataRepositoryTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFileCaches  **
  - **IAM action:**  [fsx:DescribeFileCaches](#list_fsx-action-DescribeFileCaches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFileSystemAliases  **
  - **IAM action:**  [fsx:DescribeFileSystemAliases](#list_fsx-action-DescribeFileSystemAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFileSystems  **
  - **IAM action:**  [fsx:DescribeFileSystems](#list_fsx-action-DescribeFileSystems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeS3AccessPointAttachments  **
  - **IAM action:**  [fsx:DescribeS3AccessPointAttachments](#list_fsx-action-DescribeS3AccessPointAttachments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSharedVpcConfiguration  **
  - **IAM action:**  [fsx:DescribeSharedVpcConfiguration](#list_fsx-action-DescribeSharedVpcConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSnapshots  **
  - **IAM action:**  [fsx:DescribeSnapshots](#list_fsx-action-DescribeSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStorageVirtualMachines  **
  - **IAM action:**  [fsx:DescribeStorageVirtualMachines](#list_fsx-action-DescribeStorageVirtualMachines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVolumes  **
  - **IAM action:**  [fsx:DescribeVolumes](#list_fsx-action-DescribeVolumes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetachAndDeleteS3AccessPoint  **
  - **IAM action:**  [fsx:DetachAndDeleteS3AccessPoint](#list_fsx-action-DetachAndDeleteS3AccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFileSystemAliases  **
  - **IAM action:**  [fsx:DisassociateFileSystemAliases](#list_fsx-action-DisassociateFileSystemAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListTagsForResource  **
  - **IAM action:**  [fsx:ListTagsForResource](#list_fsx-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ReleaseFileSystemNfsV3Locks  **
  - **IAM action:**  [fsx:ReleaseFileSystemNfsV3Locks](#list_fsx-action-ReleaseFileSystemNfsV3Locks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreVolumeFromSnapshot  **
  - **IAM action:**  [fsx:RestoreVolumeFromSnapshot](#list_fsx-action-RestoreVolumeFromSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMisconfiguredStateRecovery  **
  - **IAM action:**  [fsx:StartMisconfiguredStateRecovery](#list_fsx-action-StartMisconfiguredStateRecovery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [fsx:TagResource](#list_fsx-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [fsx:UntagResource](#list_fsx-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDataRepositoryAssociation  **
  - **IAM action:**  [fsx:UpdateDataRepositoryAssociation](#list_fsx-action-UpdateDataRepositoryAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFileCache  **
  - **IAM action:**  [fsx:UpdateFileCache](#list_fsx-action-UpdateFileCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFileSystem  **
  - **IAM action:**  [fsx:UpdateFileSystem](#list_fsx-action-UpdateFileSystem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSharedVpcConfiguration  **
  - **IAM action:**  [fsx:UpdateSharedVpcConfiguration](#list_fsx-action-UpdateSharedVpcConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSnapshot  **
  - **IAM action:**  [fsx:UpdateSnapshot](#list_fsx-action-UpdateSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStorageVirtualMachine  **
  - **IAM action:**  [fsx:UpdateStorageVirtualMachine](#list_fsx-action-UpdateStorageVirtualMachine) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVolume  **
  - **IAM action:**  [fsx:UpdateVolume](#list_fsx-action-UpdateVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon FSx
<a name="list_fsx-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_AssociateFileSystemAliases.html)  **
  - **Description:** Grants permission to associate DNS aliases with an Amazon FSx for Windows File Server file system
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelDataRepositoryTask](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CancelDataRepositoryTask.html)  **
  - **Description:** Grants permission to cancel a data repository task
  - **Resource types (\*required):** [task\*](#list_fsx-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CopyBackup](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopyBackup.html)  **
  - **Description:** Grants permission to copy a backup
  - **Resource types (\*required):** [backup\*](#list_fsx-resource-backup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Write

- **   [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html)  **
  - **Description:** Grants permission to update an existing volume by using a snapshot from another Amazon FSx for OpenZFS file system
  - **Resource types (\*required):** [snapshot\*](#list_fsx-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAndAttachS3AccessPoint](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateAndAttachS3AccessPoint.html)  **
  - **Description:** Grants permission to create and attach a S3 Access Point to a FSx File System
  - **Resource types (\*required):** [volume](#list_fsx-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBackup](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateBackup.html)  **
  - **Description:** Grants permission to create a new backup of an Amazon FSx file system or an Amazon FSx volume
  - **Resource types (\*required):** [backup\*](#list_fsx-resource-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [file-system](#list_fsx-resource-file-system) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [volume](#list_fsx-resource-volume) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataRepositoryAssociation](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateDataRepositoryAssociation.html)  **
  - **Description:** Grants permission to create a new data respository association for an Amazon FSx for Lustre file system
  - **Resource types (\*required):** [association\*](#list_fsx-resource-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)<br />[fsx:NfsDataRepositoryAuthenticationEnabled](#list_fsx-fsx_NfsDataRepositoryAuthenticationEnabled)<br />[fsx:NfsDataRepositoryEncryptionInTransitEnabled](#list_fsx-fsx_NfsDataRepositoryEncryptionInTransitEnabled)
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataRepositoryTask](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateDataRepositoryTask.html)  **
  - **Description:** Grants permission to create a new data respository task for an Amazon FSx for Lustre file system
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [task\*](#list_fsx-resource-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFileCache](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileCache.html)  **
  - **Description:** Grants permission to create a new, empty, Amazon file cache
  - **Resource types (\*required):** [association](#list_fsx-resource-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)<br />[fsx:NfsDataRepositoryAuthenticationEnabled](#list_fsx-fsx_NfsDataRepositoryAuthenticationEnabled)<br />[fsx:NfsDataRepositoryEncryptionInTransitEnabled](#list_fsx-fsx_NfsDataRepositoryEncryptionInTransitEnabled)
  - **Resource types (\*required):** [file-cache\*](#list_fsx-resource-file-cache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileSystem.html)  **
  - **Description:** Grants permission to create a new, empty, Amazon FSx file system
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFileSystemFromBackup](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateFileSystemFromBackup.html)  **
  - **Description:** Grants permission to create a new Amazon FSx file system from an existing backup
  - **Resource types (\*required):** [backup\*](#list_fsx-resource-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSnapshot](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateSnapshot.html)  **
  - **Description:** Grants permission to create a new snapshot on a volume
  - **Resource types (\*required):** [snapshot\*](#list_fsx-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStorageVirtualMachine](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateStorageVirtualMachine.html)  **
  - **Description:** Grants permission to create a new storage virtual machine in an Amazon FSx for Ontap file system
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [storage-virtual-machine\*](#list_fsx-resource-storage-virtual-machine) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateVolume.html)  **
  - **Description:** Grants permission to create a new volume
  - **Resource types (\*required):** [snapshot](#list_fsx-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [storage-virtual-machine](#list_fsx-resource-storage-virtual-machine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)<br />[fsx:ParentVolumeId](#list_fsx-fsx_ParentVolumeId)<br />[fsx:StorageVirtualMachineId](#list_fsx-fsx_StorageVirtualMachineId)
  - **Access level:** Write

- **   [CreateVolumeFromBackup](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateVolumeFromBackup.html)  **
  - **Description:** Grants permission to create a new volume from backup
  - **Resource types (\*required):** [backup\*](#list_fsx-resource-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)<br />[fsx:StorageVirtualMachineId](#list_fsx-fsx_StorageVirtualMachineId)
  - **Resource types (\*required):** [storage-virtual-machine\*](#list_fsx-resource-storage-virtual-machine) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)<br />[fsx:StorageVirtualMachineId](#list_fsx-fsx_StorageVirtualMachineId)
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)<br />[fsx:StorageVirtualMachineId](#list_fsx-fsx_StorageVirtualMachineId)
  - **Access level:** Write

- **   [DeleteBackup](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteBackup.html)  **
  - **Description:** Grants permission to delete a backup, deleting its contents. After deletion, the backup no longer exists, and its data is no longer available
  - **Resource types (\*required):** [backup\*](#list_fsx-resource-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataRepositoryAssociation](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteDataRepositoryAssociation.html)  **
  - **Description:** Grants permission to delete a data repository association
  - **Resource types (\*required):** [association\*](#list_fsx-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFileCache](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteFileCache.html)  **
  - **Description:** Grants permission to delete a file cache, deleting its contents
  - **Resource types (\*required):** [association](#list_fsx-resource-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [file-cache\*](#list_fsx-resource-file-cache) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteFileSystem.html)  **
  - **Description:** Grants permission to delete a file system, deleting its contents and any existing automatic backups of the file system
  - **Resource types (\*required):** [backup](#list_fsx-resource-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSnapshot](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteSnapshot.html)  **
  - **Description:** Grants permission to delete a snapshot on a volume
  - **Resource types (\*required):** [snapshot\*](#list_fsx-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStorageVirtualMachine](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteStorageVirtualMachine.html)  **
  - **Description:** Grants permission to delete a storage virtual machine, deleting its contents
  - **Resource types (\*required):** [storage-virtual-machine\*](#list_fsx-resource-storage-virtual-machine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteVolume.html)  **
  - **Description:** Grants permission to delete a volume, deleting its contents and any existing automatic backups of the volume
  - **Resource types (\*required):** [backup](#list_fsx-resource-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[fsx:ParentVolumeId](#list_fsx-fsx_ParentVolumeId)<br />[fsx:StorageVirtualMachineId](#list_fsx-fsx_StorageVirtualMachineId)
  - **Access level:** Write

- **   [DescribeBackups](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeBackups.html)  **
  - **Description:** Grants permission to return the descriptions of all backups owned by your AWS account in the AWS Region of the endpoint that you're calling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDataRepositoryAssociations](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeDataRepositoryAssociations.html)  **
  - **Description:** Grants permission to return the descriptions of all data repository associations owned by your AWS account in the AWS Region of the endpoint that you're calling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDataRepositoryTasks](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeDataRepositoryTasks.html)  **
  - **Description:** Grants permission to return the descriptions of all data repository tasks owned by your AWS account in the AWS Region of the endpoint that you're calling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFileCaches](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileCaches.html)  **
  - **Description:** Grants permission to return the descriptions of all file caches owned by your AWS account in the AWS Region of the endpoint that you're calling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystemAliases.html)  **
  - **Description:** Grants permission to return the description of all DNS aliases owned by your Amazon FSx for Windows File Server file system
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFileSystems](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html)  **
  - **Description:** Grants permission to return the descriptions of all file systems owned by your AWS account in the AWS Region of the endpoint that you're calling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeS3AccessPointAttachments](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeS3AccessPointAttachments.html)  **
  - **Description:** Grants permission to return the descriptions of S3 Access Point Attachments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSharedVpcConfiguration](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeSharedVpcConfiguration.html)  **
  - **Description:** Grants permission to return the descriptions of whether FSx route table updates from participant accounts are allowed in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSnapshots](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeSnapshots.html)  **
  - **Description:** Grants permission to return the descriptions of all snapshots owned by your AWS account in the AWS Region of the endpoint you're calling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeStorageVirtualMachines](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeStorageVirtualMachines.html)  **
  - **Description:** Grants permission to return the descriptions of all storage virtual machines owned by your AWS account in the AWS Region of the endpoint that you're calling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVolumes](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeVolumes.html)  **
  - **Description:** Grants permission to return the descriptions of all volumes owned by your AWS account in the AWS Region of the endpoint that you're calling
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetachAndDeleteS3AccessPoint](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DetachAndDeleteS3AccessPoint.html)  **
  - **Description:** Grants permission to detach an S3 Access Point from an Amazon FSx File System and delete the S3 Access Point
  - **Resource types (\*required):** [volume](#list_fsx-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DisassociateFileSystemAliases.html)  **
  - **Description:** Grants permission to disassociate file system aliases with an Amazon FSx for Windows File Server file system
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListTagsForResource](https://docs.aws.amazon.com/fsx/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an Amazon FSx resource
  - **Resource types (\*required):** [association](#list_fsx-resource-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [backup](#list_fsx-resource-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [file-cache](#list_fsx-resource-file-cache) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [file-system](#list_fsx-resource-file-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [snapshot](#list_fsx-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [storage-virtual-machine](#list_fsx-resource-storage-virtual-machine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task](#list_fsx-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [volume](#list_fsx-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ReleaseFileSystemNfsV3Locks](https://docs.aws.amazon.com/fsx/latest/APIReference/API_ReleaseFileSystemNfsV3Locks.html)  **
  - **Description:** Grants permission to release file system NFS V3 locks
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreVolumeFromSnapshot](https://docs.aws.amazon.com/fsx/latest/APIReference/API_RestoreVolumeFromSnapshot.html)  **
  - **Description:** Grants permission to restore volume state from a snapshot
  - **Resource types (\*required):** [snapshot\*](#list_fsx-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMisconfiguredStateRecovery](https://docs.aws.amazon.com/fsx/latest/APIReference/API_StartMisconfiguredStateRecovery.html)  **
  - **Description:** Grants permission to start misconfigured state recovery
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/fsx/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an Amazon FSx resource
  - **Resource types (\*required):** [association](#list_fsx-resource-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)<br />[fsx:NfsDataRepositoryAuthenticationEnabled](#list_fsx-fsx_NfsDataRepositoryAuthenticationEnabled)<br />[fsx:NfsDataRepositoryEncryptionInTransitEnabled](#list_fsx-fsx_NfsDataRepositoryEncryptionInTransitEnabled)
  - **Resource types (\*required):** [backup](#list_fsx-resource-backup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [file-cache](#list_fsx-resource-file-cache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [file-system](#list_fsx-resource-file-system) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_fsx-resource-snapshot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [storage-virtual-machine](#list_fsx-resource-storage-virtual-machine) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [task](#list_fsx-resource-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [volume](#list_fsx-resource-volume) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fsx-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)<br />[fsx:ParentVolumeId](#list_fsx-fsx_ParentVolumeId)<br />[fsx:StorageVirtualMachineId](#list_fsx-fsx_StorageVirtualMachineId)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from an Amazon FSx resource
  - **Resource types (\*required):** [association](#list_fsx-resource-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [backup](#list_fsx-resource-backup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [file-cache](#list_fsx-resource-file-cache) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [file-system](#list_fsx-resource-file-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [snapshot](#list_fsx-resource-snapshot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [storage-virtual-machine](#list_fsx-resource-storage-virtual-machine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [task](#list_fsx-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Resource types (\*required):** [volume](#list_fsx-resource-volume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fsx-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDataRepositoryAssociation](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateDataRepositoryAssociation.html)  **
  - **Description:** Grants permission to update data repository association configuration
  - **Resource types (\*required):** [association\*](#list_fsx-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFileCache](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateFileCache.html)  **
  - **Description:** Grants permission to update file cache configuration
  - **Resource types (\*required):** [file-cache\*](#list_fsx-resource-file-cache)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateFileSystem.html)  **
  - **Description:** Grants permission to update file system configuration
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSharedVpcConfiguration](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateSharedVpcConfiguration.html)  **
  - **Description:** Grants permission to enable or disable FSx route table updates from participant accounts in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSnapshot](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateSnapshot.html)  **
  - **Description:** Grants permission to update snapshot configuration
  - **Resource types (\*required):** [snapshot\*](#list_fsx-resource-snapshot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStorageVirtualMachine](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateStorageVirtualMachine.html)  **
  - **Description:** Grants permission to update storage virtual machine configuration
  - **Resource types (\*required):** [storage-virtual-machine\*](#list_fsx-resource-storage-virtual-machine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateVolume.html)  **
  - **Description:** Grants permission to update volume configuration
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)<br />[fsx:ParentVolumeId](#list_fsx-fsx_ParentVolumeId)<br />[fsx:StorageVirtualMachineId](#list_fsx-fsx_StorageVirtualMachineId)
  - **Access level:** Write



## Permission-only actions for Amazon FSx
<a name="list_fsx-permission-only-actions"></a>

The following actions are defined by Amazon FSx but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateFileGateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html)  **
  - **Description:** Grants permission to associate a File Gateway instance with an Amazon FSx for Windows File Server file system
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BypassSnaplockEnterpriseRetention](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#bypass-enterprise)  **
  - **Description:** Grants permission to allow deletion of an FSx for ONTAP SnapLock Enterprise volume that contains WORM (write once, read many) files with active retention periods
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/on-demand-replication.html)  **
  - **Description:** Grants permission to manage cross-account sharing of FSx volumes through AWS Resource Access Manager (RAM). PutResourcePolicy and GetResourcePolicy are also required
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DescribeAssociatedFileGateways](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html)  **
  - **Description:** Grants permission to describe the File Gateway instances associated with an Amazon FSx for Windows File Server file system
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateFileGateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html)  **
  - **Description:** Grants permission to disassociate a File Gateway instance from an Amazon FSx for Windows File Server file system
  - **Resource types (\*required):** [file-system\*](#list_fsx-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetResourcePolicy](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/on-demand-replication.html)  **
  - **Description:** Grants permission to manage cross-account sharing of FSx volumes through AWS Resource Access Manager (RAM). PutResourcePolicy and DeleteResourcePolicy are also required
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [ManageBackupPrincipalAssociations](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopyBackup.html)  **
  - **Description:** Grants permission to manage backup principal associations through AWS Backup
  - **Resource types (\*required):** [backup\*](#list_fsx-resource-backup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/on-demand-replication.html)  **
  - **Description:** Grants permission to manage cross-account sharing of FSx volumes through AWS Resource Access Manager (RAM). DeleteResourcePolicy and GetResourcePolicy are also required
  - **Resource types (\*required):** [volume\*](#list_fsx-resource-volume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon FSx
<a name="list_fsx-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [association](https://docs.aws.amazon.com/fsx/latest/LustreGuide/access-control-overview.html#access-control-resources)  | arn:${Partition}:fsx:${Region}:${Account}:association/${FileSystemIdOrFileCacheId}/${DataRepositoryAssociationId} | [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_) | 
|  [backup](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/access-control-overview.html#access-control-resources)  | arn:${Partition}:fsx:${Region}:${Account}:backup/${BackupId} | [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_) | 
|  [file-cache](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/security-iam.html)  | arn:${Partition}:fsx:${Region}:${Account}:file-cache/${FileCacheId} | [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_) | 
|  [file-system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/access-control-overview.html#access-control-resources)  | arn:${Partition}:fsx:${Region}:${Account}:file-system/${FileSystemId} | [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_) | 
|  [snapshot](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-control-overview.html#access-control-resources)  | arn:${Partition}:fsx:${Region}:${Account}:snapshot/${VolumeId}/${SnapshotId} | [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_) | 
|  [storage-virtual-machine](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html)  | arn:${Partition}:fsx:${Region}:${Account}:storage-virtual-machine/${FileSystemId}/${StorageVirtualMachineId} | [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_) | 
|  [task](https://docs.aws.amazon.com/fsx/latest/LustreGuide/access-control-overview.html#access-control-resources)  | arn:${Partition}:fsx:${Region}:${Account}:task/${TaskId} | [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_) | 
|  [volume](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/security-iam.html)  | arn:${Partition}:fsx:${Region}:${Account}:volume/${FileSystemId}/${VolumeId} | [aws:ResourceTag/${TagKey}](#list_fsx-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon FSx
<a name="list_fsx-policy-keys"></a>

Amazon FSx defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [fsx:IsBackupCopyDestination](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html#copy-backups)  | Filters access by whether the backup is a destination backup for a CopyBackup operation | Bool | 
|   [fsx:IsBackupCopySource](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html#copy-backups)  | Filters access by whether the backup is a source backup for a CopyBackup operation | Bool | 
|   [fsx:NfsDataRepositoryAuthenticationEnabled](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/encryption-in-transit.html)  | Filters access by NFS data repositories which support authentication | Bool | 
|   [fsx:NfsDataRepositoryEncryptionInTransitEnabled](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/encryption-in-transit.html)  | Filters access by NFS data repositories which support encryption-in-transit | Bool | 
|   [fsx:ParentVolumeId](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/creating-volumes.html)  | Filters access by the containing parent volume for mutating volume operations | String | 
|   [fsx:StorageVirtualMachineId](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/creating-volumes.html)  | Filters access by the containing storage virtual machine for a volume for mutating volume operations | String | 