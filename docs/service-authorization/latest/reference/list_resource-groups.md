

# Actions, resources, and condition keys for AWS Resource Groups
<a name="list_resource-groups"></a>

AWS Resource Groups (service prefix: `resource-groups`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ARG/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ARG/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ARG/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/resource-groups/resource-groups.json) for this service.

**Topics**
+ [API operations defined by AWS Resource Groups](#list_resource-groups-operations)
+ [Actions defined by AWS Resource Groups](#list_resource-groups-actions-as-permissions)
+ [Permission-only actions for AWS Resource Groups](#list_resource-groups-permission-only-actions)
+ [Resource types defined by AWS Resource Groups](#list_resource-groups-resources-for-iam-policies)
+ [Condition keys for AWS Resource Groups](#list_resource-groups-policy-keys)

## API operations defined by AWS Resource Groups
<a name="list_resource-groups-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_resource-groups-actions-as-permissions).




- **   CancelTagSyncTask  **
  - **IAM action:**  [resource-groups:CancelTagSyncTask](#list_resource-groups-action-CancelTagSyncTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resource-groups:DeleteGroup](#list_resource-groups-action-DeleteGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateGroup  **
  - **IAM action:**  [resource-groups:CreateGroup](#list_resource-groups-action-CreateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resource-groups:Tag](#list_resource-groups-action-Tag)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteGroup  **
  - **IAM action:**  [resource-groups:DeleteGroup](#list_resource-groups-action-DeleteGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountSettings  **
  - **IAM action:**  [resource-groups:GetAccountSettings](#list_resource-groups-action-GetAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroup  **
  - **IAM action:**  [resource-groups:GetGroup](#list_resource-groups-action-GetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroupConfiguration  **
  - **IAM action:**  [resource-groups:GetGroupConfiguration](#list_resource-groups-action-GetGroupConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGroupQuery  **
  - **IAM action:**  [resource-groups:GetGroupQuery](#list_resource-groups-action-GetGroupQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTagSyncTask  **
  - **IAM action:**  [resource-groups:GetTagSyncTask](#list_resource-groups-action-GetTagSyncTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTags  **
  - **IAM action:**  [resource-groups:GetTags](#list_resource-groups-action-GetTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GroupResources  **
  - **IAM action:**  [resource-groups:GroupResources](#list_resource-groups-action-GroupResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListGroupResources  **
  - **IAM action:**  [resource-groups:ListGroupResources](#list_resource-groups-action-ListGroupResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroupingStatuses  **
  - **IAM action:**  [resource-groups:ListGroupingStatuses](#list_resource-groups-action-ListGroupingStatuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroups  **
  - **IAM action:**  [resource-groups:ListGroups](#list_resource-groups-action-ListGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagSyncTasks  **
  - **IAM action:**  [resource-groups:ListTagSyncTasks](#list_resource-groups-action-ListTagSyncTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutGroupConfiguration  **
  - **IAM action:**  [resource-groups:PutGroupConfiguration](#list_resource-groups-action-PutGroupConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchResources  **
  - **IAM action:**  [resource-groups:SearchResources](#list_resource-groups-action-SearchResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartTagSyncTask  **
  - **IAM action:**  [resource-groups:CreateGroup](#list_resource-groups-action-CreateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [resource-groups:StartTagSyncTask](#list_resource-groups-action-StartTagSyncTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** resource-groups.amazonaws.com / **Access level:** Write

- **   Tag  **
  - **IAM action:**  [resource-groups:Tag](#list_resource-groups-action-Tag) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UngroupResources  **
  - **IAM action:**  [resource-groups:UngroupResources](#list_resource-groups-action-UngroupResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Untag  **
  - **IAM action:**  [resource-groups:Untag](#list_resource-groups-action-Untag) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountSettings  **
  - **IAM action:**  [resource-groups:UpdateAccountSettings](#list_resource-groups-action-UpdateAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGroup  **
  - **IAM action:**  [resource-groups:UpdateGroup](#list_resource-groups-action-UpdateGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGroupQuery  **
  - **IAM action:**  [resource-groups:UpdateGroupQuery](#list_resource-groups-action-UpdateGroupQuery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Resource Groups
<a name="list_resource-groups-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelTagSyncTask](https://docs.aws.amazon.com/ARG/latest/APIReference/API_CancelTagSyncTask.html)  **
  - **Description:** Grants permission to cancel a tag-sync task for an application group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGroup](https://docs.aws.amazon.com/ARG/latest/APIReference/API_CreateGroup.html)  **
  - **Description:** Grants permission to create a resource group with a specified name, description, and resource query
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resource-groups-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_resource-groups-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/ARG/latest/APIReference/API_DeleteGroup.html)  **
  - **Description:** Grants permission to delete a specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountSettings](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetAccountSettings.html)  **
  - **Description:** Grants permission to get the current status of optional features in Resource Groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGroup](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetGroup.html)  **
  - **Description:** Grants permission to get information of a specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGroupConfiguration](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetGroupConfiguration.html)  **
  - **Description:** Grants permission to get the service configuration associated with the specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGroupQuery](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetGroupQuery.html)  **
  - **Description:** Grants permission to get the query associated with a specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTagSyncTask](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetTagSyncTask.html)  **
  - **Description:** Grants permission to get information of a specified tag-sync task
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTags](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetTags.html)  **
  - **Description:** Grants permission to get the tags associated with a specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GroupResources](https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupResources.html)  **
  - **Description:** Grants permission to add the specified resources to the specified group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListGroupResources](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupResources.html)  **
  - **Description:** Grants permission to list the resources that are members of a specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGroupingStatuses](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupingStatuses.html)  **
  - **Description:** Grants permission to list grouping statuses for a specified application group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroups.html)  **
  - **Description:** Grants permission to list all resource groups in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagSyncTasks](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListTagSyncTasks.html)  **
  - **Description:** Grants permission to list all tag-sync tasks in your account
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutGroupConfiguration](https://docs.aws.amazon.com/ARG/latest/APIReference/API_PutGroupConfiguration.html)  **
  - **Description:** Grants permission to put the service configuration associated with the specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchResources](https://docs.aws.amazon.com/ARG/latest/APIReference/API_SearchResources.html)  **
  - **Description:** Grants permission to search for AWS resources matching the given query
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartTagSyncTask](https://docs.aws.amazon.com/ARG/latest/APIReference/API_StartTagSyncTask.html)  **
  - **Description:** Grants permission to create a tag-sync task for an application group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Tag](https://docs.aws.amazon.com/ARG/latest/APIReference/API_Tag.html)  **
  - **Description:** Grants permission to tag a specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_resource-groups-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resource-groups-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UngroupResources](https://docs.aws.amazon.com/ARG/latest/APIReference/API_UngroupResources.html)  **
  - **Description:** Grants permission to remove the specified resources from the specified group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Untag](https://docs.aws.amazon.com/ARG/latest/APIReference/API_Untag.html)  **
  - **Description:** Grants permission to remove tags associated with a specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_resource-groups-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountSettings](https://docs.aws.amazon.com/ARG/latest/APIReference/API_UpdateAccountSettings.html)  **
  - **Description:** Grants permission to update optional features in Resource Groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateGroup](https://docs.aws.amazon.com/ARG/latest/APIReference/API_UpdateGroup.html)  **
  - **Description:** Grants permission to update a specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGroupQuery](https://docs.aws.amazon.com/ARG/latest/APIReference/API_UpdateGroupQuery.html)  **
  - **Description:** Grants permission to update the query associated with a specified resource group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Resource Groups
<a name="list_resource-groups-permission-only-actions"></a>

The following actions are defined by AWS Resource Groups but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateResource](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-resources.html)  **
  - **Description:** Grants permission to associate a resource to an Application
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGroupPolicy](https://docs.aws.amazon.com/license-manager/latest/userguide/management-role.html#service-linked-role-permissions-management-role)  **
  - **Description:** Grants permission to delete a resource-based policy for the specified group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateResource](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-resources.html)  **
  - **Description:** Grants permission to disassociate a resource from an Application
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetGroupPolicy](https://docs.aws.amazon.com/license-manager/latest/userguide/management-role.html#service-linked-role-permissions-management-role)  **
  - **Description:** Grants permission to get a resource-based policy for the specified group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListResourceTypes](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html)  **
  - **Description:** Grants permission to list supported resource types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutGroupPolicy](https://docs.aws.amazon.com/license-manager/latest/userguide/management-role.html#service-linked-role-permissions-management-role)  **
  - **Description:** Grants permission to add a resource-based policy for the specified group
  - **Resource types (\*required):** [group\*](#list_resource-groups-resource-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Resource Groups
<a name="list_resource-groups-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [group](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html)  | arn:${Partition}:resource-groups:${Region}:${Account}:group/${GroupName} | [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_) | 
|  [tagSyncTask](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html)  | arn:${Partition}:resource-groups:${Region}:${Account}:group/${GroupName}/tag-sync-task/${TaskId} | [aws:ResourceTag/${TagKey}](#list_resource-groups-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Resource Groups
<a name="list_resource-groups-policy-keys"></a>

AWS Resource Groups defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 