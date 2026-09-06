

# Actions, resources, and condition keys for AWS rePost Private
<a name="list_repostspace"></a>

AWS rePost Private (service prefix: `repostspace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/repostprivate/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/repostprivate/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/repostprivate/latest/caguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/repostspace/repostspace.json) for this service.

**Topics**
+ [API operations defined by AWS rePost Private](#list_repostspace-operations)
+ [Actions defined by AWS rePost Private](#list_repostspace-actions-as-permissions)
+ [Resource types defined by AWS rePost Private](#list_repostspace-resources-for-iam-policies)
+ [Condition keys for AWS rePost Private](#list_repostspace-policy-keys)

## API operations defined by AWS rePost Private
<a name="list_repostspace-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_repostspace-actions-as-permissions).




- **   BatchAddChannelRoleToAccessors  **
  - **IAM action:**  [repostspace:BatchAddChannelRoleToAccessors](#list_repostspace-action-BatchAddChannelRoleToAccessors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAddRole  **
  - **IAM action:**  [repostspace:BatchAddRole](#list_repostspace-action-BatchAddRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchRemoveChannelRoleFromAccessors  **
  - **IAM action:**  [repostspace:BatchRemoveChannelRoleFromAccessors](#list_repostspace-action-BatchRemoveChannelRoleFromAccessors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchRemoveRole  **
  - **IAM action:**  [repostspace:BatchRemoveRole](#list_repostspace-action-BatchRemoveRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChannel  **
  - **IAM action:**  [repostspace:CreateChannel](#list_repostspace-action-CreateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSpace  **
  - **IAM action:**  [repostspace:CreateSpace](#list_repostspace-action-CreateSpace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [repostspace:TagResource](#list_repostspace-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** repostspace.amazonaws.com / **Access level:** Write

- **   DeleteSpace  **
  - **IAM action:**  [repostspace:DeleteSpace](#list_repostspace-action-DeleteSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterAdmin  **
  - **IAM action:**  [repostspace:DeregisterAdmin](#list_repostspace-action-DeregisterAdmin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetChannel  **
  - **IAM action:**  [repostspace:GetChannel](#list_repostspace-action-GetChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSpace  **
  - **IAM action:**  [repostspace:GetSpace](#list_repostspace-action-GetSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListChannels  **
  - **IAM action:**  [repostspace:ListChannels](#list_repostspace-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSpaces  **
  - **IAM action:**  [repostspace:ListSpaces](#list_repostspace-action-ListSpaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [repostspace:ListTagsForResource](#list_repostspace-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterAdmin  **
  - **IAM action:**  [repostspace:RegisterAdmin](#list_repostspace-action-RegisterAdmin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendInvites  **
  - **IAM action:**  [repostspace:SendInvites](#list_repostspace-action-SendInvites) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [repostspace:TagResource](#list_repostspace-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [repostspace:UntagResource](#list_repostspace-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateChannel  **
  - **IAM action:**  [repostspace:UpdateChannel](#list_repostspace-action-UpdateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSpace  **
  - **IAM action:**  [repostspace:UpdateSpace](#list_repostspace-action-UpdateSpace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** repostspace.amazonaws.com / **Access level:** Write



## Actions defined by AWS rePost Private
<a name="list_repostspace-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchAddChannelRoleToAccessors](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchAddChannelRoleToAccessors.html)  **
  - **Description:** Grants permission to add a role to users and groups in a private re:Post channel in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAddRole](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchAddRole.html)  **
  - **Description:** Grants permission to add a role to users and groups in a private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchRemoveChannelRoleFromAccessors](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchRemoveChannelRoleFromAccessors.html)  **
  - **Description:** Grants permission to remove a role from users and groups in a private re:Post channel in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchRemoveRole](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_BatchRemoveRole.html)  **
  - **Description:** Grants permission to remove a role from users and groups in a private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_CreateChannel.html)  **
  - **Description:** Grants permission to create a new channel in private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSpace](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_CreateSpace.html)  **
  - **Description:** Grants permission to create a new private re:Post in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_repostspace-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_repostspace-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteSpace](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_DeleteSpace.html)  **
  - **Description:** Grants permission to delete a private re:Post from your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterAdmin](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_DeregisterAdmin.html)  **
  - **Description:** Grants permission to remove an administrator to a private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetChannel](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_GetChannel.html)  **
  - **Description:** Grants permission to get the description for a channel in private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSpace](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_GetSpace.html)  **
  - **Description:** Grants permission to get the description for a private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListChannels](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_ListChannels.html)  **
  - **Description:** Grants permission to list all channels in a private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSpaces](API_ListSpaces.html)  **
  - **Description:** Grants permission to list all private re:Posts in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags associated with a resource
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_repostspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_repostspace-aws_TagKeys)
  - **Access level:** Read

- **   [RegisterAdmin](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_RegisterAdmin.html)  **
  - **Description:** Grants permission to add an administrator to a private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendInvites](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_SendInvites.html)  **
  - **Description:** Grants permission to send invites to users of a private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_repostspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_repostspace-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_repostspace-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateChannel](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_UpdateChannel.html)  **
  - **Description:** Grants permission to update a channel in private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSpace](https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_UpdateSpace.html)  **
  - **Description:** Grants permission to update a private re:Post in your account
  - **Resource types (\*required):** [space\*](#list_repostspace-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS rePost Private
<a name="list_repostspace-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [space](https://docs.aws.amazon.com/repostprivate/latest/userguide/)  | arn:${Partition}:repostspace:${Region}:${Account}:space/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_repostspace-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS rePost Private
<a name="list_repostspace-policy-keys"></a>

AWS rePost Private defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 