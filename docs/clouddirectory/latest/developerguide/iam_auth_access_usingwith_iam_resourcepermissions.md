

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/). 

# Amazon Cloud Directory API Permissions: Actions, Resources, and Conditions Reference
<a name="iam_auth_access_usingwith_iam_resourcepermissions"></a>

When you are setting up [Access Control](iam_auth_access.md#iam_auth_access_accesscontrol) and writing permissions policies that you can attach to an IAM identity (identity-based policies), you can use the following table as a reference. The table lists each Amazon Cloud Directory API operation, the corresponding actions for which you can grant permissions to perform the action, the AWS resource for which you can grant the permissions. You specify the actions in the policy's `Action` field and the resource value in the policy's `Resource` field. 

You can use AWS-wide condition keys in your Amazon Cloud Directory policies to express conditions. For a complete list of AWS-wide keys, see [Available Global Condition Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#AvailableKeys) in the *IAM User Guide*. 

**Note**  
To specify an action, use the `clouddirectory:` prefix followed by the API operation name (for example, `clouddirectory:CreateDirectory`).


**Amazon Cloud Directory API and Required Permissions for Actions**  

| Amazon Cloud Directory API Operations | Required Permissions (API Actions) | Resources | 
| --- | --- | --- | 
| [AddFacetToObject](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_AddFacetToObject.html) | `clouddirectory:AddFacetToObject` | \* | 
| [ApplySchema](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ApplySchema.html) | clouddirectory:ApplySchema | \* | 
| [AttachObject](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_AttachObject.html)  | clouddirectory:AttachObject | \* | 
|  [AttachPolicy](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_AttachPolicy.html)  | `clouddirectory:AttachPolicy` | \* | 
|  [AttachToIndex](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_AttachToIndex.html)  | `clouddirectory:AttachToIndex` | \* | 
|  [AttachTypedLink](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_AttachTypedLink.html)  | `clouddirectory:AttachTypedLink` | \* | 
|  [BatchRead](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchRead.html)  | `clouddirectory:BatchRead` | \* | 
|  [BatchWrite](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchWrite.html)  | `clouddirectory:BatchWrite` | \* | 
|  [CreateDirectory](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_CreateDirectory.html)  | `clouddirectory:CreateDirectory` | \* | 
|  [CreateFacet](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_CreateFacet.html)  | `clouddirectory:CreateFacet` | \* | 
|  [CreateIndex](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_CreateIndex.html)  | `clouddirectory:CreateIndex` | \* | 
|  [CreateObject](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_CreateObject.html)  | `clouddirectory:CreateObject` | \* | 
|  [CreateSchema](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_CreateSchema.html)  | `clouddirectory:CreateSchema` | \* | 
|  [CreateTypedLinkFacet](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_CreateTypedLinkFacet.html)  | `clouddirectory:CreateTypedLinkFacet` | \* | 
|  [DeleteDirectory](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DeleteDirectory.html)  | `clouddirectory:DeleteDirectory` | \* | 
|  [DeleteFacet](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DeleteFacet.html)  | `clouddirectory:DeleteFacet` | \* | 
|  [DeleteObject](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DeleteObject.html)  | `clouddirectory:DeleteObject` | \* | 
|  [DeleteSchema](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DeleteSchema.html)  | `clouddirectory:DeleteSchema` | \* | 
|  [DeleteTypedLinkFacet](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DeleteTypedLinkFacet.html)  | `clouddirectory:DeleteTypedLinkFacet` | \* | 
|  [DetachFromIndex](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DetachFromIndex.html)  | `clouddirectory:DetachFromIndex` | \* | 
|  [DetachObject](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DetachObject.html)  | `clouddirectory:DetachObject` | \* | 
|  [DetachPolicy](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DetachPolicy.html)  | `clouddirectory:DetachPolicy` | \* | 
|  [DetachedTypedLink](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DetachTypedLink.html)  | `clouddirectory:DetachTypedLink` | \* | 
|  [DisableDirectory](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_DisableDirectory.html)  | `clouddirectory:DisableDirectory` | \* | 
|  [EnableDirectory](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_EnableDirectory.html)  | `clouddirectory:EnableDirectory` | \* | 
|  [GetAppliedSchemaVersion](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetAppliedSchemaVersion.html)  | `clouddirectory:GetAppliedSchemaVersion` | \* | 
|  [GetDirectory](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetDirectory.html)  | `clouddirectory:GetDirectory` | \* | 
|  [GetFacet](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetFacet.html)  | `clouddirectory:GetFacet` | \* | 
|  [GetObjectAttributes](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetObjectAttributes.html)  | `clouddirectory:GetObjectAttributes` | \* | 
|  [GetObjectInformation](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetObjectInformation.html)  | `clouddirectory:GetObjectInformation` | \* | 
|  [GetSchemaAsJson](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetSchemaAsJson.html)  | `clouddirectory:GetSchemaAsJson` | \* | 
|  [GetTypedLinkFacetInformation](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_GetTypedLinkFacetInformation.html)  | `clouddirectory:GetTypedLinkFacetInformation` | \* | 
|  [ListAppliedSchemaArns](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListAppliedSchemaArns.html)  | `clouddirectory:ListAppliedSchemaArns` | \* | 
| [ListAttachedIndices](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListAttachedIndices.html) | `clouddirectory:ListAttachedIndices` | \* | 
| [ListDevelopmentSchemaArns](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListDevelopmentSchemaArns.html) | `clouddirectory:ListDevelopmentSchemaArns` | \* | 
| [ListDirectories](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListDirectories.html) | `clouddirectory:ListDirectories` | \* | 
|  [ListFacetAttributes](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListFacetAttributes.html)  | `clouddirectory:ListFacetAttributes` | \* | 
| [ListFacetNames](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListFacetNames.html) | `clouddirectory:ListFacetNames` | \* | 
|  [ListIncomingTypedLinks](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListIncomingTypedLinks.html)  | `clouddirectory:ListIncomingTypedLinks` | \* | 
| [ListIndex](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListIndex.html) | `clouddirectory:ListIndex` | \* | 
|  [ListObjectAttributes](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListObjectAttributes.html)  | `clouddirectory:ListObjectAttributes` | \* | 
| [ListObjectChildren](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListObjectChildren.html) | `clouddirectory:ListObjectChildren` | \* | 
|  [ListObjectParentPaths](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListObjectParentPaths.html)  | `clouddirectory:ListObjectParentPaths` | \* | 
|  [ListObjectParents](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListObjectParents.html)  | `clouddirectory:ListObjectParents` | \* | 
|  [ListObjectPolicies](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListObjectPolicies.html)  | `clouddirectory:ListObjectPolicies` | \* | 
|  [ListOutgoingTypedLinks](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListOutgoingTypedLinks.html)  | `clouddirectory:ListOutgoingTypedLinks` | \* | 
|  [ListPolicyAttachments](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListPolicyAttachments.html)  | `clouddirectory:ListPolicyAttachments` | \* | 
|  [ListPublishedSchemaArns](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListPublishedSchemaArns.html)  | `clouddirectory:ListPublishedSchemaArns` | \* | 
|  [ListTagsForResource](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListTagsForResource.html)  | `clouddirectory:ListTagsForResource` | \* | 
|  [ListTypedLinkFacetAttributes](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListTypedLinkFacetAttributes.html)  | `clouddirectory:ListTypedLinkFacetAttributes` | \* | 
|  [ListTypedLinkFacetNames](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListTypedLinkFacetNames.html)  | `clouddirectory:ListTypedLinkFacetNames` | \* | 
|  [LookupPolicy](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_LookupPolicy.html)  | `clouddirectory:LookupPolicy` | \* | 
|  [PublishSchema](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_PublishSchema.html)  | `clouddirectory:PublishSchema` | \* | 
|  [PutSchemaFromJson](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_PutSchemaFromJson.html)  | `clouddirectory:PutSchemaFromJson` | \* | 
|  [RemoveFacetFromObject](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_RemoveFacetFromObject.html)  | `clouddirectory:RemoveFacetFromObject` | \* | 
|  [TagResource](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_TagResource.html)  | `clouddirectory:TagResource` | \* | 
|  [UntagResource](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_UntagResource.html)  | `clouddirectory:UntagResource` | \* | 
|  [UpdateFacet](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_UpdateFacet.html)  | `clouddirectory:UpdateFacet` | \* | 
|  [UpdateObjectAttributes](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_UpdateObjectAttributes.html)  | `clouddirectory:UpdateObjectAttributes` | \* | 
|  [UpdateSchema](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_UpdateSchema.html)  | `clouddirectory:UpdateSchema` | \* | 
|  [UpdateTypedLinkFacet](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_UpdateTypedLinkFacet.html)  | `clouddirectory:UpdateTypedLinkFacet` | \* | 
|  [UpgradeAppliedSchema](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_UpgradeAppliedSchema.html)  | `clouddirectory:UpgradeAppliedSchema` | \* | 
|  [UpgradePublishedSchema](http://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_UpgradePublishedSchema.html)  | `clouddirectory:UpgradePublishedSchema` | \* | 