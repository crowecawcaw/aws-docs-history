

# Actions, resources, and condition keys for Amazon S3 Files
<a name="list_s3files"></a>

Amazon S3 Files (service prefix: `s3files`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonS3/latest/API/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Files.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/s3files/s3files.json) for this service.

**Topics**
+ [API operations defined by Amazon S3 Files](#list_s3files-operations)
+ [Actions defined by Amazon S3 Files](#list_s3files-actions-as-permissions)
+ [Permission-only actions for Amazon S3 Files](#list_s3files-permission-only-actions)
+ [Resource types defined by Amazon S3 Files](#list_s3files-resources-for-iam-policies)
+ [Condition keys for Amazon S3 Files](#list_s3files-policy-keys)

## API operations defined by Amazon S3 Files
<a name="list_s3files-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_s3files-actions-as-permissions).




- **   CreateAccessPoint  **
  - **IAM action:**  [s3files:CreateAccessPoint](#list_s3files-action-CreateAccessPoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3files:TagResource](#list_s3files-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFileSystem  **
  - **IAM action:**  [s3files:CreateFileSystem](#list_s3files-action-CreateFileSystem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [s3files:TagResource](#list_s3files-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** elasticfilesystem.amazonaws.com / **Access level:** Write

- **   CreateMountTarget  **
  - **IAM action:**  [s3files:CreateMountTarget](#list_s3files-action-CreateMountTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAccessPoint  **
  - **IAM action:**  [s3files:DeleteAccessPoint](#list_s3files-action-DeleteAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFileSystem  **
  - **IAM action:**  [s3files:DeleteFileSystem](#list_s3files-action-DeleteFileSystem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFileSystemPolicy  **
  - **IAM action:**  [s3files:DeleteFileSystemPolicy](#list_s3files-action-DeleteFileSystemPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteMountTarget  **
  - **IAM action:**  [s3files:DeleteMountTarget](#list_s3files-action-DeleteMountTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessPoint  **
  - **IAM action:**  [s3files:GetAccessPoint](#list_s3files-action-GetAccessPoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFileSystem  **
  - **IAM action:**  [s3files:GetFileSystem](#list_s3files-action-GetFileSystem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFileSystemPolicy  **
  - **IAM action:**  [s3files:GetFileSystemPolicy](#list_s3files-action-GetFileSystemPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMountTarget  **
  - **IAM action:**  [s3files:GetMountTarget](#list_s3files-action-GetMountTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSynchronizationConfiguration  **
  - **IAM action:**  [s3files:GetSynchronizationConfiguration](#list_s3files-action-GetSynchronizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessPoints  **
  - **IAM action:**  [s3files:ListAccessPoints](#list_s3files-action-ListAccessPoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFileSystems  **
  - **IAM action:**  [s3files:ListFileSystems](#list_s3files-action-ListFileSystems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMountTargets  **
  - **IAM action:**  [s3files:ListMountTargets](#list_s3files-action-ListMountTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [s3files:ListTagsForResource](#list_s3files-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutFileSystemPolicy  **
  - **IAM action:**  [s3files:PutFileSystemPolicy](#list_s3files-action-PutFileSystemPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutSynchronizationConfiguration  **
  - **IAM action:**  [s3files:PutSynchronizationConfiguration](#list_s3files-action-PutSynchronizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [s3files:TagResource](#list_s3files-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [s3files:UntagResource](#list_s3files-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateMountTarget  **
  - **IAM action:**  [s3files:UpdateMountTarget](#list_s3files-action-UpdateMountTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon S3 Files
<a name="list_s3files-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_CreateAccessPoint.html)  **
  - **Description:** Grants permission to create an access point for the specified file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3files-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3files-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFileSystem](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_CreateFileSystem.html)  **
  - **Description:** Grants permission to create a new file system
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3files-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_s3files-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMountTarget](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_CreateMountTarget.html)  **
  - **Description:** Grants permission to create a mount target for a file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_DeleteAccessPoint.html)  **
  - **Description:** Grants permission to delete a specified access point
  - **Resource types (\*required):** [access-point\*](#list_s3files-resource-access-point)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFileSystem](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_DeleteFileSystem.html)  **
  - **Description:** Grants permission to delete a specified file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFileSystemPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_DeleteFileSystemPolicy.html)  **
  - **Description:** Grants permission to delete the IAM resource policy for a specified file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteMountTarget](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_DeleteMountTarget.html)  **
  - **Description:** Grants permission to delete a specified mount target
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_GetAccessPoint.html)  **
  - **Description:** Grants permission to get resource information for a specified access point
  - **Resource types (\*required):** [access-point\*](#list_s3files-resource-access-point)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFileSystem](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_GetFileSystem.html)  **
  - **Description:** Grants permission to get resource information for a specified file system
  - **Resource types (\*required):** [file-system](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFileSystemPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_GetFileSystemPolicy.html)  **
  - **Description:** Grants permission to get the IAM resource policy for a specified file system
  - **Resource types (\*required):** [file-system](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMountTarget](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_GetMountTarget.html)  **
  - **Description:** Grants permission to get resource information for a specified mount target
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSynchronizationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_GetSynchronizationConfiguration.html)  **
  - **Description:** Grants permission to get a synchronization configuration for a specified file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListAccessPoints.html)  **
  - **Description:** Grants permission to get a paginated list of all access points in the account
  - **Resource types (\*required):** [access-point\*](#list_s3files-resource-access-point)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFileSystems](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListFileSystems.html)  **
  - **Description:** Grants permission to get a paginated list of all file systems in the account
  - **Resource types (\*required):** [file-system](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMountTargets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListMountTargets.html)  **
  - **Description:** Grants permission to get a paginated list of all mount targets in the account
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a specified S3 Files resource
  - **Resource types (\*required):** [access-point](#list_s3files-resource-access-point) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [file-system](#list_s3files-resource-file-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutFileSystemPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_PutFileSystemPolicy.html)  **
  - **Description:** Grants permission to add an IAM resource policy to a specified file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutSynchronizationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_PutSynchronizationConfiguration.html)  **
  - **Description:** Grants permission to add a synchronization configuration to a specified file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_TagResource.html)  **
  - **Description:** Grants permission to tag a specified S3 Files resource
  - **Resource types (\*required):** [access-point](#list_s3files-resource-access-point) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3files-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3files-aws_TagKeys)<br />[s3files:CreateAction](#list_s3files-s3files_CreateAction)
  - **Resource types (\*required):** [file-system](#list_s3files-resource-file-system) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_s3files-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3files-aws_TagKeys)<br />[s3files:CreateAction](#list_s3files-s3files_CreateAction)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_UntagResource.html)  **
  - **Description:** Grants permission to untag a specified S3 Files resource
  - **Resource types (\*required):** [access-point](#list_s3files-resource-access-point) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3files-aws_TagKeys)
  - **Resource types (\*required):** [file-system](#list_s3files-resource-file-system) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_s3files-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateMountTarget](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_UpdateMountTarget.html)  **
  - **Description:** Grants permission to update resource information for a specified mount target
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon S3 Files
<a name="list_s3files-permission-only-actions"></a>

The following actions are defined by Amazon S3 Files but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [ClientMount](https://docs.aws.amazon.com/AmazonS3/latest/API/s3files-client-authorization.html)  **
  - **Description:** Grants permission to allow an NFS client read-access to a file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)<br />[s3files:AccessPointArn](#list_s3files-s3files_AccessPointArn)
  - **Access level:** Read

- **   [ClientRootAccess](https://docs.aws.amazon.com/AmazonS3/latest/API/s3files-client-authorization.html)  **
  - **Description:** Grants permission to allow an NFS client root-access to a file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)<br />[s3files:AccessPointArn](#list_s3files-s3files_AccessPointArn)
  - **Access level:** Write

- **   [ClientWrite](https://docs.aws.amazon.com/AmazonS3/latest/API/s3files-client-authorization.html)  **
  - **Description:** Grants permission to allow an NFS client write-access to a file system
  - **Resource types (\*required):** [file-system\*](#list_s3files-resource-file-system)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_)<br />[s3files:AccessPointArn](#list_s3files-s3files_AccessPointArn)
  - **Access level:** Write



## Resource types defined by Amazon S3 Files
<a name="list_s3files-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [access-point](https://docs.aws.amazon.com/AmazonS3/latest/API/s3files-access-points.html)  | arn:${Partition}:s3files:${Region}:${Account}:file-system/${FileSystemId}/access-point/${AccessPointId} | [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_) | 
|  [file-system](https://docs.aws.amazon.com/AmazonS3/latest/API/creating-using-create-fs.html)  | arn:${Partition}:s3files:${Region}:${Account}:file-system/${FileSystemId} | [aws:ResourceTag/${TagKey}](#list_s3files-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon S3 Files
<a name="list_s3files-policy-keys"></a>

Amazon S3 Files defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [s3files:AccessPointArn](https://docs.aws.amazon.com/AmazonS3/latest/API/s3files-access-points.html)  | Filters access by the ARN of the access point used to mount the file system | ARN | 
|   [s3files:CreateAction](https://docs.aws.amazon.com/AmazonS3/latest/API/using-tags-s3files.html)  | Filters access by the name of a resource-creating API action | String | 