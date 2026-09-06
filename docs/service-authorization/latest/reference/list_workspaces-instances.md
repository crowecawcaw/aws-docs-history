

# Actions, resources, and condition keys for AWS WorkSpaces Managed Instances
<a name="list_workspaces-instances"></a>

AWS WorkSpaces Managed Instances (service prefix: `workspaces-instances`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/workspaces/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/workspaces/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/workspaces/latest/userguide/workspaces-instances-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/workspaces-instances/workspaces-instances.json) for this service.

**Topics**
+ [API operations defined by AWS WorkSpaces Managed Instances](#list_workspaces-instances-operations)
+ [Actions defined by AWS WorkSpaces Managed Instances](#list_workspaces-instances-actions-as-permissions)
+ [Resource types defined by AWS WorkSpaces Managed Instances](#list_workspaces-instances-resources-for-iam-policies)
+ [Condition keys for AWS WorkSpaces Managed Instances](#list_workspaces-instances-policy-keys)

## API operations defined by AWS WorkSpaces Managed Instances
<a name="list_workspaces-instances-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_workspaces-instances-actions-as-permissions).




- **   AssociateVolume  **
  - **IAM action:**  [workspaces-instances:AssociateVolume](#list_workspaces-instances-action-AssociateVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateVolume  **
  - **IAM action:**  [workspaces-instances:CreateVolume](#list_workspaces-instances-action-CreateVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkspaceInstance  **
  - **IAM action:**  [workspaces-instances:CreateWorkspaceInstance](#list_workspaces-instances-action-CreateWorkspaceInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [workspaces-instances:TagResource](#list_workspaces-instances-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteVolume  **
  - **IAM action:**  [workspaces-instances:DeleteVolume](#list_workspaces-instances-action-DeleteVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkspaceInstance  **
  - **IAM action:**  [workspaces-instances:DeleteWorkspaceInstance](#list_workspaces-instances-action-DeleteWorkspaceInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateVolume  **
  - **IAM action:**  [workspaces-instances:DisassociateVolume](#list_workspaces-instances-action-DisassociateVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetWorkspaceInstance  **
  - **IAM action:**  [workspaces-instances:GetWorkspaceInstance](#list_workspaces-instances-action-GetWorkspaceInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListInstanceTypes  **
  - **IAM action:**  [workspaces-instances:ListInstanceTypes](#list_workspaces-instances-action-ListInstanceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegions  **
  - **IAM action:**  [workspaces-instances:ListRegions](#list_workspaces-instances-action-ListRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [workspaces-instances:ListTagsForResource](#list_workspaces-instances-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkspaceInstances  **
  - **IAM action:**  [workspaces-instances:ListWorkspaceInstances](#list_workspaces-instances-action-ListWorkspaceInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [workspaces-instances:TagResource](#list_workspaces-instances-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [workspaces-instances:UntagResource](#list_workspaces-instances-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS WorkSpaces Managed Instances
<a name="list_workspaces-instances-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateVolume](https://docs.aws.amazon.com/workspaces/latest/api/API_AssociateVolume.html)  **
  - **Description:** Grants permission to associate a workspace managed volume to a workspace managed instance in your account
  - **Resource types (\*required):** [WorkspaceInstanceId\*](#list_workspaces-instances-resource-WorkspaceInstanceId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateVolume](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateVolume.html)  **
  - **Description:** Grants permission to create a workspace managed volume in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateWorkspaceInstance](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceInstance.html)  **
  - **Description:** Grants permission to create a workspace managed instance in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-instances-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-instances-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteVolume](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteVolume.html)  **
  - **Description:** Grants permission to delete a workspace managed volume in your account
  - **Resource types (\*required):** [VolumeId\*](#list_workspaces-instances-resource-VolumeId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkspaceInstance](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceInstance.html)  **
  - **Description:** Grants permission to delete a workspace managed instance in your account
  - **Resource types (\*required):** [WorkspaceInstanceId\*](#list_workspaces-instances-resource-WorkspaceInstanceId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateVolume](https://docs.aws.amazon.com/workspaces/latest/api/API_DisassociateVolume.html)  **
  - **Description:** Grants permission to disassociate a workspace managed volume from a workspace managed instance in your account
  - **Resource types (\*required):** [WorkspaceInstanceId\*](#list_workspaces-instances-resource-WorkspaceInstanceId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetWorkspaceInstance](https://docs.aws.amazon.com/workspaces/latest/api/API_GetWorkspaceInstance.html)  **
  - **Description:** Grants permission to get details for a specific workspace managed instance in your account
  - **Resource types (\*required):** [WorkspaceInstanceId\*](#list_workspaces-instances-resource-WorkspaceInstanceId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListInstanceTypes](https://docs.aws.amazon.com/workspaces/latest/api/API_ListInstanceTypes.html)  **
  - **Description:** Grants permission to list all supported instance types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegions](https://docs.aws.amazon.com/workspaces/latest/api/API_ListRegions.html)  **
  - **Description:** Grants permission to list all supported AWS regions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/workspaces/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list user tags for resources in your account
  - **Resource types (\*required):** [WorkspaceInstanceId\*](#list_workspaces-instances-resource-WorkspaceInstanceId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkspaceInstances](https://docs.aws.amazon.com/workspaces/latest/api/API_ListWorkspaceInstances.html)  **
  - **Description:** Grants permission to list workspace managed instances in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/workspaces/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add user tags to resources in your account
  - **Resource types (\*required):** [WorkspaceInstanceId\*](#list_workspaces-instances-resource-WorkspaceInstanceId)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-instances-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-instances-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/workspaces/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove user tags from resources in your account
  - **Resource types (\*required):** [WorkspaceInstanceId\*](#list_workspaces-instances-resource-WorkspaceInstanceId)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-instances-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS WorkSpaces Managed Instances
<a name="list_workspaces-instances-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [VolumeId](https://docs.aws.amazon.com/workspaces/latest/api/managed-workspaces-volumes.html)  | arn:${Partition}:ec2:${Region}:${Account}:volume/${VolumeId} | [aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_) | 
|  [WorkspaceInstanceId](https://docs.aws.amazon.com/workspaces/latest/api/managed-workspaces-instances.html)  | arn:${Partition}:workspaces-instances:${Region}:${Account}:workspaceinstance/${WorkspaceInstanceId} | [aws:ResourceTag/${TagKey}](#list_workspaces-instances-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS WorkSpaces Managed Instances
<a name="list_workspaces-instances-policy-keys"></a>

AWS WorkSpaces Managed Instances defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 