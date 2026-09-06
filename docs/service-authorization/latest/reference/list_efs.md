

# Actions, resources, and condition keys for Amazon Elastic File System
<a name="list_efs"></a>

Amazon Elastic File System (service prefix: `elasticfilesystem`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/efs/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/efs/latest/ug/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/efs/latest/ug/security-considerations.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elasticfilesystem/elasticfilesystem.json) for this service.

**Topics**
+ [API operations defined by Amazon Elastic File System](#list_efs-operations)
+ [Actions defined by Amazon Elastic File System](#list_efs-actions-as-permissions)
+ [Permission-only actions for Amazon Elastic File System](#list_efs-permission-only-actions)
+ [Resource types defined by Amazon Elastic File System](#list_efs-resources-for-iam-policies)
+ [Condition keys for Amazon Elastic File System](#list_efs-policy-keys)

## API operations defined by Amazon Elastic File System
<a name="list_efs-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_efs-actions-as-permissions).




- **   CreateAccessPoint  **
  - **IAM action:**  [elasticfilesystem:CreateAccessPoint](#list_efs-action-CreateAccessPoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elasticfilesystem:TagResource](#list_efs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFileSystem  **
  - **IAM action:**  [elasticfilesystem:CreateFileSystem](#list_efs-action-CreateFileSystem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elasticfilesystem:TagResource](#list_efs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMountTarget  **
  - **IAM action:**  [elasticfilesystem:CreateMountTarget](#list_efs-action-CreateMountTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateReplicationConfiguration  **
  - **IAM action:**  [elasticfilesystem:CreateReplicationConfiguration](#list_efs-action-CreateReplicationConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** elasticfilesystem.amazonaws.com / **Access level:** Write

- **   CreateTags  **
  - **IAM action:**  [elasticfilesystem:CreateTags](#list_efs-action-CreateTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteAccessPoint  **
  - **IAM action:**  [elasticfilesystem:DeleteAccessPoint](#list_efs-action-DeleteAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFileSystem  **
  - **IAM action:**  [elasticfilesystem:DeleteFileSystem](#list_efs-action-DeleteFileSystem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFileSystemPolicy  **
  - **IAM action:**  [elasticfilesystem:DeleteFileSystemPolicy](#list_efs-action-DeleteFileSystemPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteMountTarget  **
  - **IAM action:**  [elasticfilesystem:DeleteMountTarget](#list_efs-action-DeleteMountTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationConfiguration  **
  - **IAM action:**  [elasticfilesystem:DeleteReplicationConfiguration](#list_efs-action-DeleteReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTags  **
  - **IAM action:**  [elasticfilesystem:DeleteTags](#list_efs-action-DeleteTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DescribeAccessPoints  **
  - **IAM action:**  [elasticfilesystem:DescribeAccessPoints](#list_efs-action-DescribeAccessPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeAccountPreferences  **
  - **IAM action:**  [elasticfilesystem:DescribeAccountPreferences](#list_efs-action-DescribeAccountPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeBackupPolicy  **
  - **IAM action:**  [elasticfilesystem:DescribeBackupPolicy](#list_efs-action-DescribeBackupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFileSystemPolicy  **
  - **IAM action:**  [elasticfilesystem:DescribeFileSystemPolicy](#list_efs-action-DescribeFileSystemPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFileSystems  **
  - **IAM action:**  [elasticfilesystem:DescribeFileSystems](#list_efs-action-DescribeFileSystems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeLifecycleConfiguration  **
  - **IAM action:**  [elasticfilesystem:DescribeLifecycleConfiguration](#list_efs-action-DescribeLifecycleConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMountTargetSecurityGroups  **
  - **IAM action:**  [elasticfilesystem:DescribeMountTargetSecurityGroups](#list_efs-action-DescribeMountTargetSecurityGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMountTargets  **
  - **IAM action:**  [elasticfilesystem:DescribeMountTargets](#list_efs-action-DescribeMountTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationConfigurations  **
  - **IAM action:**  [elasticfilesystem:DescribeReplicationConfigurations](#list_efs-action-DescribeReplicationConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeTags  **
  - **IAM action:**  [elasticfilesystem:DescribeTags](#list_efs-action-DescribeTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [elasticfilesystem:ListTagsForResource](#list_efs-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ModifyMountTargetSecurityGroups  **
  - **IAM action:**  [elasticfilesystem:ModifyMountTargetSecurityGroups](#list_efs-action-ModifyMountTargetSecurityGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAccountPreferences  **
  - **IAM action:**  [elasticfilesystem:PutAccountPreferences](#list_efs-action-PutAccountPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBackupPolicy  **
  - **IAM action:**  [elasticfilesystem:PutBackupPolicy](#list_efs-action-PutBackupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutFileSystemPolicy  **
  - **IAM action:**  [elasticfilesystem:PutFileSystemPolicy](#list_efs-action-PutFileSystemPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutLifecycleConfiguration  **
  - **IAM action:**  [elasticfilesystem:PutLifecycleConfiguration](#list_efs-action-PutLifecycleConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [elasticfilesystem:TagResource](#list_efs-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [elasticfilesystem:UntagResource](#list_efs-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateFileSystem  **
  - **IAM action:**  [elasticfilesystem:UpdateFileSystem](#list_efs-action-UpdateFileSystem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFileSystemProtection  **
  - **IAM action:**  [elasticfilesystem:UpdateFileSystemProtection](#list_efs-action-UpdateFileSystemProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Elastic File System
<a name="list_efs-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAccessPoint](https://docs.aws.amazon.com/efs/latest/ug/API_CreateAccessPoint.html)  **
  - **Description:** Grants permission to create an access point for the specified file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_efs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_efs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFileSystem](https://docs.aws.amazon.com/efs/latest/ug/API_CreateFileSystem.html)  **
  - **Description:** Grants permission to create a new, empty file system
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_efs-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_efs-aws_TagKeys)<br />[elasticfilesystem:Encrypted](#list_efs-elasticfilesystem_Encrypted)
  - **Access level:** Write

- **   [CreateMountTarget](https://docs.aws.amazon.com/efs/latest/ug/API_CreateMountTarget.html)  **
  - **Description:** Grants permission to create a mount target for a file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateReplicationConfiguration](https://docs.aws.amazon.com/efs/latest/ug/API_CreateReplicationConfiguration.html)  **
  - **Description:** Grants permission to create a new replication configuration
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTags](https://docs.aws.amazon.com/efs/latest/ug/API_CreateTags.html)  **
  - **Description:** Grants permission to create or overwrite tags associated with a file system; deprecated, see TagResource
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_efs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_efs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [DeleteAccessPoint](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteAccessPoint.html)  **
  - **Description:** Grants permission to delete the specified access point
  - **Resource types (\*required):** [access-point\*](#list_efs-resource-access-point)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFileSystem](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteFileSystem.html)  **
  - **Description:** Grants permission to delete a file system, permanently severing access to its contents
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFileSystemPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteFileSystemPolicy.html)  **
  - **Description:** Grants permission to delete the resource-level policy for a file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteMountTarget](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteMountTarget.html)  **
  - **Description:** Grants permission to delete the specified mount target
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReplicationConfiguration](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteReplicationConfiguration.html)  **
  - **Description:** Grants permission to delete a replication configuration
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTags](https://docs.aws.amazon.com/efs/latest/ug/API_DeleteTags.html)  **
  - **Description:** Grants permission to delete the specified tags from a file system; deprecated, see UntagResource
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_efs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [DescribeAccessPoints](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeAccessPoints.html)  **
  - **Description:** Grants permission to view the descriptions of Amazon EFS access points
  - **Resource types (\*required):** [access-point](#list_efs-resource-access-point) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [file-system](#list_efs-resource-file-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeAccountPreferences](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeAccountPreferences.html)  **
  - **Description:** Grants permission to view the account preferences in effect for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeBackupPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeBackupPolicy.html)  **
  - **Description:** Grants permission to view the BackupPolicy object for an Amazon EFS file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFileSystemPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeFileSystemPolicy.html)  **
  - **Description:** Grants permission to view the resource-level policy for an Amazon EFS file system
  - **Resource types (\*required):** [file-system](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFileSystems](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeFileSystems.html)  **
  - **Description:** Grants permission to view the description of an Amazon EFS file system specified by file system CreationToken or FileSystemId; or to view the description of all file systems owned by the caller's AWS account in the AWS region of the endpoint that is being called
  - **Resource types (\*required):** [file-system](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeLifecycleConfiguration](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeLifecycleConfiguration.html)  **
  - **Description:** Grants permission to view the LifecycleConfiguration object for an Amazon EFS file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMountTargetSecurityGroups](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeMountTargetSecurityGroups.html)  **
  - **Description:** Grants permission to view the security groups in effect for a mount target
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMountTargets](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeMountTargets.html)  **
  - **Description:** Grants permission to view the descriptions of all mount targets, or a specific mount target, for a file system
  - **Resource types (\*required):** [access-point](#list_efs-resource-access-point) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeReplicationConfigurations](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeReplicationConfigurations.html)  **
  - **Description:** Grants permission to view the description of an Amazon EFS replication configuration specified by FileSystemId; or to view the description of all replication configurations owned by the caller's AWS account in the AWS region of the endpoint that is being called
  - **Resource types (\*required):** [file-system](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeTags](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeTags.html)  **
  - **Description:** Grants permission to view the tags associated with a file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/efs/latest/ug/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to view the tags associated with the specified Amazon EFS resource
  - **Resource types (\*required):** [access-point](#list_efs-resource-access-point) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [file-system](#list_efs-resource-file-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ModifyMountTargetSecurityGroups](https://docs.aws.amazon.com/efs/latest/ug/API_ModifyMountTargetSecurityGroups.html)  **
  - **Description:** Grants permission to modify the set of security groups in effect for a mount target
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutAccountPreferences](https://docs.aws.amazon.com/efs/latest/ug/API_PutAccountPreferences.html)  **
  - **Description:** Grants permission to set the account preferences of an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutBackupPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_PutBackupPolicy.html)  **
  - **Description:** Grants permission to enable or disable automatic backups with AWS Backup by creating a new BackupPolicy object
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutFileSystemPolicy](https://docs.aws.amazon.com/efs/latest/ug/API_PutFileSystemPolicy.html)  **
  - **Description:** Grants permission to apply a resource-level policy that defines the actions allowed or denied from given actors for the specified file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutLifecycleConfiguration](https://docs.aws.amazon.com/efs/latest/ug/API_PutLifecycleConfiguration.html)  **
  - **Description:** Grants permission to enable lifecycle management by creating a new LifecycleConfiguration object
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/efs/latest/ug/API_TagResource.html)  **
  - **Description:** Grants permission to create or overwrite tags associated with the specified Amazon EFS resource
  - **Resource types (\*required):** [access-point](#list_efs-resource-access-point) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_efs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_efs-aws_TagKeys)<br />[elasticfilesystem:CreateAction](#list_efs-elasticfilesystem_CreateAction)
  - **Resource types (\*required):** [file-system](#list_efs-resource-file-system) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_efs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_efs-aws_TagKeys)<br />[elasticfilesystem:CreateAction](#list_efs-elasticfilesystem_CreateAction)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/efs/latest/ug/API_UntagResource.html)  **
  - **Description:** Grants permission to delete the specified tags from an Amazon EFS resource
  - **Resource types (\*required):** [access-point](#list_efs-resource-access-point) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_efs-aws_TagKeys)
  - **Resource types (\*required):** [file-system](#list_efs-resource-file-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_efs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateFileSystem](https://docs.aws.amazon.com/efs/latest/ug/API_UpdateFileSystem.html)  **
  - **Description:** Grants permission to update the throughput mode or the amount of provisioned throughput of an existing file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFileSystemProtection](https://docs.aws.amazon.com/efs/latest/ug/API_UpdateFileSystemProtection.html)  **
  - **Description:** Grants permission to update the file system protection of an existing file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Elastic File System
<a name="list_efs-permission-only-actions"></a>

The following actions are defined by Amazon Elastic File System but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [Backup](https://docs.aws.amazon.com/efs/latest/ug/efs-backup-solutions.html)  **
  - **Description:** Grants permission to start a backup job for an existing file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ClientMount](https://docs.aws.amazon.com/efs/latest/ug/efs-client-authorization.html)  **
  - **Description:** Grants permission to allow an NFS client read-access to a file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[elasticfilesystem:AccessedViaMountTarget](#list_efs-elasticfilesystem_AccessedViaMountTarget)<br />[elasticfilesystem:AccessPointArn](#list_efs-elasticfilesystem_AccessPointArn)
  - **Access level:** Read

- **   [ClientRootAccess](https://docs.aws.amazon.com/efs/latest/ug/efs-client-authorization.html)  **
  - **Description:** Grants permission to allow an NFS client root-access to a file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[elasticfilesystem:AccessedViaMountTarget](#list_efs-elasticfilesystem_AccessedViaMountTarget)<br />[elasticfilesystem:AccessPointArn](#list_efs-elasticfilesystem_AccessPointArn)
  - **Access level:** Write

- **   [ClientWrite](https://docs.aws.amazon.com/efs/latest/ug/efs-client-authorization.html)  **
  - **Description:** Grants permission to allow an NFS client write-access to a file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)<br />[elasticfilesystem:AccessedViaMountTarget](#list_efs-elasticfilesystem_AccessedViaMountTarget)<br />[elasticfilesystem:AccessPointArn](#list_efs-elasticfilesystem_AccessPointArn)
  - **Access level:** Write

- **   [ReplicationRead](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html)  **
  - **Description:** Grants permission to read file system data for replication
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ReplicationWrite](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html)  **
  - **Description:** Grants permission to replicate data to a file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Restore](https://docs.aws.amazon.com/efs/latest/ug/efs-backup-solutions.html)  **
  - **Description:** Grants permission to start a restore job for a backup of a file system
  - **Resource types (\*required):** [file-system\*](#list_efs-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Elastic File System
<a name="list_efs-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [access-point](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html)  | arn:${Partition}:elasticfilesystem:${Region}:${Account}:access-point/${AccessPointId} | [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_) | 
|  [file-system](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html)  | arn:${Partition}:elasticfilesystem:${Region}:${Account}:file-system/${FileSystemId} | [aws:ResourceTag/${TagKey}](#list_efs-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Elastic File System
<a name="list_efs-policy-keys"></a>

Amazon Elastic File System defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [elasticfilesystem:AccessPointArn](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html)  | Filters access by the ARN of the access point used to mount the file system | ARN | 
|   [elasticfilesystem:AccessedViaMountTarget](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs.html)  | Filters access by whether the file system is accessed via mount targets | Bool | 
|   [elasticfilesystem:CreateAction](https://docs.aws.amazon.com/efs/latest/ug/using-tags-efs.html)  | Filters access by the name of a resource-creating API action | String | 
|   [elasticfilesystem:Encrypted](https://docs.aws.amazon.com/efs/latest/ug/encryption.html)  | Filters access by whether users can create only encrypted or unencrypted file systems | Bool | 