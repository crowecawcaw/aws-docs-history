Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").
 

# Amazon Cloud Directory API Permissions: Actions, Resources, and Conditions
 Reference

When you are setting up [Access Control](iam_auth_access.md#iam_auth_access_accesscontrol "iam_auth_access.md#iam_auth_access_accesscontrol") and writing permissions policies that you
 can attach to an IAM identity (identity-based policies), you can use the following table as
 a reference. The table lists
 each Amazon Cloud Directory API operation, the corresponding actions for which you can grant permissions to
 perform the action, the AWS resource for which you can grant the permissions.
 
 You specify the actions in the policy's `Action` field and the resource value in
 the policy's `Resource` field. 

You can use AWS-wide condition keys in your Amazon Cloud Directory policies to express
 conditions. For a complete list of AWS-wide keys, see [Available Global Condition Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#AvailableKeys "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#AvailableKeys") in
 the *IAM User Guide*. 

###### Note

To specify an action, use the `clouddirectory:` prefix followed by the API
 operation name (for example, `clouddirectory:CreateDirectory`).



Amazon Cloud Directory API and Required Permissions for Actions | Amazon Cloud Directory API Operations | Required Permissions (API Actions) | Resources |
| --- | --- | --- |
| [AddFacetToObject](../APIReference/API_AddFacetToObject.md "../APIReference/API_AddFacetToObject.md") | `clouddirectory:AddFacetToObject` | \* |
| [ApplySchema](../APIReference/API_ApplySchema.md "../APIReference/API_ApplySchema.md") | `clouddirectory:ApplySchema` | \* |
| [AttachObject](../APIReference/API_AttachObject.md "../APIReference/API_AttachObject.md") | `clouddirectory:AttachObject` | \* |
| [AttachPolicy](../APIReference/API_AttachPolicy.md "../APIReference/API_AttachPolicy.md") | `clouddirectory:AttachPolicy` | \* |
| [AttachToIndex](../APIReference/API_AttachToIndex.md "../APIReference/API_AttachToIndex.md") | `clouddirectory:AttachToIndex` | \* |
| [AttachTypedLink](../APIReference/API_AttachTypedLink.md "../APIReference/API_AttachTypedLink.md") | `clouddirectory:AttachTypedLink` | \* |
| [BatchRead](../APIReference/API_BatchRead.md "../APIReference/API_BatchRead.md") | `clouddirectory:BatchRead` | \* |
| [BatchWrite](../APIReference/API_BatchWrite.md "../APIReference/API_BatchWrite.md") | `clouddirectory:BatchWrite` | \* |
| [CreateDirectory](../APIReference/API_CreateDirectory.md "../APIReference/API_CreateDirectory.md") | `clouddirectory:CreateDirectory` | \* |
| [CreateFacet](../APIReference/API_CreateFacet.md "../APIReference/API_CreateFacet.md") | `clouddirectory:CreateFacet` | \* |
| [CreateIndex](../APIReference/API_CreateIndex.md "../APIReference/API_CreateIndex.md") | `clouddirectory:CreateIndex` | \* |
| [CreateObject](../APIReference/API_CreateObject.md "../APIReference/API_CreateObject.md") | `clouddirectory:CreateObject` | \* |
| [CreateSchema](../APIReference/API_CreateSchema.md "../APIReference/API_CreateSchema.md") | `clouddirectory:CreateSchema` | \* |
| [CreateTypedLinkFacet](../APIReference/API_CreateTypedLinkFacet.md "../APIReference/API_CreateTypedLinkFacet.md") | `clouddirectory:CreateTypedLinkFacet` | \* |
| [DeleteDirectory](../APIReference/API_DeleteDirectory.md "../APIReference/API_DeleteDirectory.md") | `clouddirectory:DeleteDirectory` | \* |
| [DeleteFacet](../APIReference/API_DeleteFacet.md "../APIReference/API_DeleteFacet.md") | `clouddirectory:DeleteFacet` | \* |
| [DeleteObject](../APIReference/API_DeleteObject.md "../APIReference/API_DeleteObject.md") | `clouddirectory:DeleteObject` | \* |
| [DeleteSchema](../APIReference/API_DeleteSchema.md "../APIReference/API_DeleteSchema.md") | `clouddirectory:DeleteSchema` | \* |
| [DeleteTypedLinkFacet](../APIReference/API_DeleteTypedLinkFacet.md "../APIReference/API_DeleteTypedLinkFacet.md") | `clouddirectory:DeleteTypedLinkFacet` | \* |
| [DetachFromIndex](../APIReference/API_DetachFromIndex.md "../APIReference/API_DetachFromIndex.md") | `clouddirectory:DetachFromIndex` | \* |
| [DetachObject](../APIReference/API_DetachObject.md "../APIReference/API_DetachObject.md") | `clouddirectory:DetachObject` | \* |
| [DetachPolicy](../APIReference/API_DetachPolicy.md "../APIReference/API_DetachPolicy.md") | `clouddirectory:DetachPolicy` | \* |
| [DetachedTypedLink](../APIReference/API_DetachTypedLink.md "../APIReference/API_DetachTypedLink.md") | `clouddirectory:DetachTypedLink` | \* |
| [DisableDirectory](../APIReference/API_DisableDirectory.md "../APIReference/API_DisableDirectory.md") | `clouddirectory:DisableDirectory` | \* |
| [EnableDirectory](../APIReference/API_EnableDirectory.md "../APIReference/API_EnableDirectory.md") | `clouddirectory:EnableDirectory` | \* |
| [GetAppliedSchemaVersion](../APIReference/API_GetAppliedSchemaVersion.md "../APIReference/API_GetAppliedSchemaVersion.md") | `clouddirectory:GetAppliedSchemaVersion` | \* |
| [GetDirectory](../APIReference/API_GetDirectory.md "../APIReference/API_GetDirectory.md") | `clouddirectory:GetDirectory` | \* |
| [GetFacet](../APIReference/API_GetFacet.md "../APIReference/API_GetFacet.md") | `clouddirectory:GetFacet` | \* |
| [GetObjectAttributes](../APIReference/API_GetObjectAttributes.md "../APIReference/API_GetObjectAttributes.md") | `clouddirectory:GetObjectAttributes` | \* |
| [GetObjectInformation](../APIReference/API_GetObjectInformation.md "../APIReference/API_GetObjectInformation.md") | `clouddirectory:GetObjectInformation` | \* |
| [GetSchemaAsJson](../APIReference/API_GetSchemaAsJson.md "../APIReference/API_GetSchemaAsJson.md") | `clouddirectory:GetSchemaAsJson` | \* |
| [GetTypedLinkFacetInformation](../APIReference/API_GetTypedLinkFacetInformation.md "../APIReference/API_GetTypedLinkFacetInformation.md") | `clouddirectory:GetTypedLinkFacetInformation` | \* |
| [ListAppliedSchemaArns](../APIReference/API_ListAppliedSchemaArns.md "../APIReference/API_ListAppliedSchemaArns.md") | `clouddirectory:ListAppliedSchemaArns` | \* |
| [ListAttachedIndices](../APIReference/API_ListAttachedIndices.md "../APIReference/API_ListAttachedIndices.md") | `clouddirectory:ListAttachedIndices` | \* |
| [ListDevelopmentSchemaArns](../APIReference/API_ListDevelopmentSchemaArns.md "../APIReference/API_ListDevelopmentSchemaArns.md") | `clouddirectory:ListDevelopmentSchemaArns` | \* |
| [ListDirectories](../APIReference/API_ListDirectories.md "../APIReference/API_ListDirectories.md") | `clouddirectory:ListDirectories` | \* |
| [ListFacetAttributes](../APIReference/API_ListFacetAttributes.md "../APIReference/API_ListFacetAttributes.md") | `clouddirectory:ListFacetAttributes` | \* |
| [ListFacetNames](../APIReference/API_ListFacetNames.md "../APIReference/API_ListFacetNames.md") | `clouddirectory:ListFacetNames` | \* |
| [ListIncomingTypedLinks](../APIReference/API_ListIncomingTypedLinks.md "../APIReference/API_ListIncomingTypedLinks.md") | `clouddirectory:ListIncomingTypedLinks` | \* |
| [ListIndex](../APIReference/API_ListIndex.md "../APIReference/API_ListIndex.md") | `clouddirectory:ListIndex` | \* |
| [ListObjectAttributes](../APIReference/API_ListObjectAttributes.md "../APIReference/API_ListObjectAttributes.md") | `clouddirectory:ListObjectAttributes` | \* |
| [ListObjectChildren](../APIReference/API_ListObjectChildren.md "../APIReference/API_ListObjectChildren.md") | `clouddirectory:ListObjectChildren` | \* |
| [ListObjectParentPaths](../APIReference/API_ListObjectParentPaths.md "../APIReference/API_ListObjectParentPaths.md") | `clouddirectory:ListObjectParentPaths` | \* |
| [ListObjectParents](../APIReference/API_ListObjectParents.md "../APIReference/API_ListObjectParents.md") | `clouddirectory:ListObjectParents` | \* |
| [ListObjectPolicies](../APIReference/API_ListObjectPolicies.md "../APIReference/API_ListObjectPolicies.md") | `clouddirectory:ListObjectPolicies` | \* |
| [ListOutgoingTypedLinks](../APIReference/API_ListOutgoingTypedLinks.md "../APIReference/API_ListOutgoingTypedLinks.md") | `clouddirectory:ListOutgoingTypedLinks` | \* |
| [ListPolicyAttachments](../APIReference/API_ListPolicyAttachments.md "../APIReference/API_ListPolicyAttachments.md") | `clouddirectory:ListPolicyAttachments` | \* |
| [ListPublishedSchemaArns](../APIReference/API_ListPublishedSchemaArns.md "../APIReference/API_ListPublishedSchemaArns.md") | `clouddirectory:ListPublishedSchemaArns` | \* |
| [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") | `clouddirectory:ListTagsForResource` | \* |
| [ListTypedLinkFacetAttributes](../APIReference/API_ListTypedLinkFacetAttributes.md "../APIReference/API_ListTypedLinkFacetAttributes.md") | `clouddirectory:ListTypedLinkFacetAttributes` | \* |
| [ListTypedLinkFacetNames](../APIReference/API_ListTypedLinkFacetNames.md "../APIReference/API_ListTypedLinkFacetNames.md") | `clouddirectory:ListTypedLinkFacetNames` | \* |
| [LookupPolicy](../APIReference/API_LookupPolicy.md "../APIReference/API_LookupPolicy.md") | `clouddirectory:LookupPolicy` | \* |
| [PublishSchema](../APIReference/API_PublishSchema.md "../APIReference/API_PublishSchema.md") | `clouddirectory:PublishSchema` | \* |
| [PutSchemaFromJson](../APIReference/API_PutSchemaFromJson.md "../APIReference/API_PutSchemaFromJson.md") | `clouddirectory:PutSchemaFromJson` | \* |
| [RemoveFacetFromObject](../APIReference/API_RemoveFacetFromObject.md "../APIReference/API_RemoveFacetFromObject.md") | `clouddirectory:RemoveFacetFromObject` | \* |
| [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") | `clouddirectory:TagResource` | \* |
| [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") | `clouddirectory:UntagResource` | \* |
| [UpdateFacet](../APIReference/API_UpdateFacet.md "../APIReference/API_UpdateFacet.md") | `clouddirectory:UpdateFacet` | \* |
| [UpdateObjectAttributes](../APIReference/API_UpdateObjectAttributes.md "../APIReference/API_UpdateObjectAttributes.md") | `clouddirectory:UpdateObjectAttributes` | \* |
| [UpdateSchema](../APIReference/API_UpdateSchema.md "../APIReference/API_UpdateSchema.md") | `clouddirectory:UpdateSchema` | \* |
| [UpdateTypedLinkFacet](../APIReference/API_UpdateTypedLinkFacet.md "../APIReference/API_UpdateTypedLinkFacet.md") | `clouddirectory:UpdateTypedLinkFacet` | \* |
| [UpgradeAppliedSchema](../APIReference/API_UpgradeAppliedSchema.md "../APIReference/API_UpgradeAppliedSchema.md") | `clouddirectory:UpgradeAppliedSchema` | \* |
| [UpgradePublishedSchema](../APIReference/API_UpgradePublishedSchema.md "../APIReference/API_UpgradePublishedSchema.md") | `clouddirectory:UpgradePublishedSchema` | \* |
