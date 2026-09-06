

# Actions, resources, and condition keys for AWS Resource Access Manager (RAM)
<a name="list_ram"></a>

AWS Resource Access Manager (RAM) (service prefix: `ram`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ram/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ram/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ram/ram.json) for this service.

**Topics**
+ [API operations defined by AWS Resource Access Manager (RAM)](#list_ram-operations)
+ [Actions defined by AWS Resource Access Manager (RAM)](#list_ram-actions-as-permissions)
+ [Resource types defined by AWS Resource Access Manager (RAM)](#list_ram-resources-for-iam-policies)
+ [Condition keys for AWS Resource Access Manager (RAM)](#list_ram-policy-keys)

## API operations defined by AWS Resource Access Manager (RAM)
<a name="list_ram-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ram-actions-as-permissions).




- **   AcceptResourceShareInvitation  **
  - **IAM action:**  [ram:AcceptResourceShareInvitation](#list_ram-action-AcceptResourceShareInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateResourceShare  **
  - **IAM action:**  [ram:AssociateResourceShare](#list_ram-action-AssociateResourceShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateResourceSharePermission  **
  - **IAM action:**  [ram:AssociateResourceSharePermission](#list_ram-action-AssociateResourceSharePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePermission  **
  - **IAM action:**  [ram:CreatePermission](#list_ram-action-CreatePermission)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ram:TagResource](#list_ram-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePermissionVersion  **
  - **IAM action:**  [ram:CreatePermissionVersion](#list_ram-action-CreatePermissionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateResourceShare  **
  - **IAM action:**  [ram:CreateResourceShare](#list_ram-action-CreateResourceShare)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ram:TagResource](#list_ram-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeletePermission  **
  - **IAM action:**  [ram:DeletePermission](#list_ram-action-DeletePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePermissionVersion  **
  - **IAM action:**  [ram:DeletePermissionVersion](#list_ram-action-DeletePermissionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceShare  **
  - **IAM action:**  [ram:DeleteResourceShare](#list_ram-action-DeleteResourceShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateResourceShare  **
  - **IAM action:**  [ram:DisassociateResourceShare](#list_ram-action-DisassociateResourceShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateResourceSharePermission  **
  - **IAM action:**  [ram:DisassociateResourceSharePermission](#list_ram-action-DisassociateResourceSharePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableSharingWithAwsOrganization  **
  - **IAM action:**  [ram:EnableSharingWithAwsOrganization](#list_ram-action-EnableSharingWithAwsOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   GetPermission  **
  - **IAM action:**  [ram:GetPermission](#list_ram-action-GetPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicies  **
  - **IAM action:**  [ram:GetResourcePolicies](#list_ram-action-GetResourcePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceShareAssociations  **
  - **IAM action:**  [ram:GetResourceShareAssociations](#list_ram-action-GetResourceShareAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceShareInvitations  **
  - **IAM action:**  [ram:GetResourceShareInvitations](#list_ram-action-GetResourceShareInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceShares  **
  - **IAM action:**  [ram:GetResourceShares](#list_ram-action-GetResourceShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPendingInvitationResources  **
  - **IAM action:**  [ram:ListPendingInvitationResources](#list_ram-action-ListPendingInvitationResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPermissionAssociations  **
  - **IAM action:**  [ram:ListPermissionAssociations](#list_ram-action-ListPermissionAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPermissionVersions  **
  - **IAM action:**  [ram:ListPermissionVersions](#list_ram-action-ListPermissionVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPermissions  **
  - **IAM action:**  [ram:ListPermissions](#list_ram-action-ListPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrincipals  **
  - **IAM action:**  [ram:ListPrincipals](#list_ram-action-ListPrincipals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReplacePermissionAssociationsWork  **
  - **IAM action:**  [ram:ListReplacePermissionAssociationsWork](#list_ram-action-ListReplacePermissionAssociationsWork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceSharePermissions  **
  - **IAM action:**  [ram:ListResourceSharePermissions](#list_ram-action-ListResourceSharePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceTypes  **
  - **IAM action:**  [ram:ListResourceTypes](#list_ram-action-ListResourceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResources  **
  - **IAM action:**  [ram:ListResources](#list_ram-action-ListResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSourceAssociations  **
  - **IAM action:**  [ram:ListSourceAssociations](#list_ram-action-ListSourceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PromotePermissionCreatedFromPolicy  **
  - **IAM action:**  [ram:PromotePermissionCreatedFromPolicy](#list_ram-action-PromotePermissionCreatedFromPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PromoteResourceShareCreatedFromPolicy  **
  - **IAM action:**  [ram:PromoteResourceShareCreatedFromPolicy](#list_ram-action-PromoteResourceShareCreatedFromPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectResourceShareInvitation  **
  - **IAM action:**  [ram:RejectResourceShareInvitation](#list_ram-action-RejectResourceShareInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReplacePermissionAssociations  **
  - **IAM action:**  [ram:ReplacePermissionAssociations](#list_ram-action-ReplacePermissionAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetDefaultPermissionVersion  **
  - **IAM action:**  [ram:SetDefaultPermissionVersion](#list_ram-action-SetDefaultPermissionVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ram:TagResource](#list_ram-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ram:UntagResource](#list_ram-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateResourceShare  **
  - **IAM action:**  [ram:UpdateResourceShare](#list_ram-action-UpdateResourceShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Resource Access Manager (RAM)
<a name="list_ram-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptResourceShareInvitation](https://docs.aws.amazon.com/ram/latest/APIReference/API_AcceptResourceShareInvitation.html)  **
  - **Description:** Grants permission to accept the specified resource share invitation
  - **Resource types (\*required):** [resource-share-invitation\*](#list_ram-resource-resource-share-invitation)
  - **Condition keys:** [ram:ResourceShareName](#list_ram-ram_ResourceShareName)<br />[ram:ShareOwnerAccountId](#list_ram-ram_ShareOwnerAccountId)
  - **Access level:** Write

- **   [AssociateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociateResourceShare.html)  **
  - **Description:** Grants permission to associate resource(s) and/or principal(s) to a resource share
  - **Resource types (\*required):** [resource-share\*](#list_ram-resource-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:Principal](#list_ram-ram_Principal)<br />[ram:RequestedResourceType](#list_ram-ram_RequestedResourceType)<br />[ram:ResourceArn](#list_ram-ram_ResourceArn)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)<br />[ram:ResourceTag/${TagKey}](#list_ram-ram_ResourceTag___TagKey_)<br />[ram:RetainSharingOnAccountLeaveOrganization](#list_ram-ram_RetainSharingOnAccountLeaveOrganization)
  - **Access level:** Write

- **   [AssociateResourceSharePermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociateResourceSharePermission.html)  **
  - **Description:** Grants permission to associate a Permission with a Resource Share
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Resource types (\*required):** [permission\*](#list_ram-resource-permission) / **Condition keys:** [ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Resource types (\*required):** [resource-share\*](#list_ram-resource-resource-share) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)
  - **Access level:** Write

- **   [CreatePermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreatePermission.html)  **
  - **Description:** Grants permission to create a Permission that can be associated to a Resource Share
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ram-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ram-aws_TagKeys)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Access level:** Write

- **   [CreatePermissionVersion](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreatePermissionVersion.html)  **
  - **Description:** Grants permission to create a new version of a Permission that can be associated to a Resource Share
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Access level:** Write

- **   [CreateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html)  **
  - **Description:** Grants permission to create a resource share with provided resource(s) and/or principal(s)
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ram-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ram-aws_TagKeys)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:Principal](#list_ram-ram_Principal)<br />[ram:RequestedAllowsExternalPrincipals](#list_ram-ram_RequestedAllowsExternalPrincipals)<br />[ram:RequestedResourceType](#list_ram-ram_RequestedResourceType)<br />[ram:ResourceArn](#list_ram-ram_ResourceArn)<br />[ram:RetainSharingOnAccountLeaveOrganization](#list_ram-ram_RetainSharingOnAccountLeaveOrganization)
  - **Access level:** Write

- **   [DeletePermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_DeletePermission.html)  **
  - **Description:** Grants permission to delete a specified Permission
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Access level:** Write

- **   [DeletePermissionVersion](https://docs.aws.amazon.com/ram/latest/APIReference/API_DeletePermissionVersion.html)  **
  - **Description:** Grants permission to delete a specified version of a permission
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Access level:** Write

- **   [DeleteResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_DeleteResourceShare.html)  **
  - **Description:** Grants permission to delete resource share
  - **Resource types (\*required):** [resource-share\*](#list_ram-resource-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)<br />[ram:ResourceTag/${TagKey}](#list_ram-ram_ResourceTag___TagKey_)<br />[ram:RetainSharingOnAccountLeaveOrganization](#list_ram-ram_RetainSharingOnAccountLeaveOrganization)
  - **Access level:** Write

- **   [DisassociateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_DisassociateResourceShare.html)  **
  - **Description:** Grants permission to disassociate resource(s) and/or principal(s) from a resource share
  - **Resource types (\*required):** [resource-share\*](#list_ram-resource-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:Principal](#list_ram-ram_Principal)<br />[ram:RequestedResourceType](#list_ram-ram_RequestedResourceType)<br />[ram:ResourceArn](#list_ram-ram_ResourceArn)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)<br />[ram:ResourceTag/${TagKey}](#list_ram-ram_ResourceTag___TagKey_)<br />[ram:RetainSharingOnAccountLeaveOrganization](#list_ram-ram_RetainSharingOnAccountLeaveOrganization)
  - **Access level:** Write

- **   [DisassociateResourceSharePermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_DisassociateResourceSharePermission.html)  **
  - **Description:** Grants permission to disassociate a Permission from a Resource Share
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Resource types (\*required):** [permission\*](#list_ram-resource-permission) / **Condition keys:** [ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Resource types (\*required):** [resource-share\*](#list_ram-resource-resource-share) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)
  - **Access level:** Write

- **   [EnableSharingWithAwsOrganization](https://docs.aws.amazon.com/ram/latest/APIReference/API_EnableSharingWithAwsOrganization.html)  **
  - **Description:** Grants permission to access customer's organization and create a SLR in the customer's account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetPermission](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetPermission.html)  **
  - **Description:** Grants permission to get the contents of an AWS RAM permission
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Resource types (\*required):** [permission\*](#list_ram-resource-permission) / **Condition keys:** [ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Access level:** Read

- **   [GetResourcePolicies](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourcePolicies.html)  **
  - **Description:** Grants permission to get the policies for the specified resources that you own and have shared
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceShareAssociations](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareAssociations.html)  **
  - **Description:** Grants permission to get a set of resource share associations from a provided list or with a specified status of the specified type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceShareInvitations](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareInvitations.html)  **
  - **Description:** Grants permission to get resource share invitations by the specified invitation arn or those for the resource share
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceShares](https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShares.html)  **
  - **Description:** Grants permission to get a set of resource shares from a provided list or with a specified status
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ram-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ram-aws_TagKeys)
  - **Access level:** Read

- **   [ListPendingInvitationResources](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html)  **
  - **Description:** Grants permission to list the resources in a resource share that is shared with you but that the invitation is still pending for
  - **Resource types (\*required):** [resource-share-invitation\*](#list_ram-resource-resource-share-invitation)
  - **Condition keys:** [ram:ResourceShareName](#list_ram-ram_ResourceShareName)<br />[ram:ShareOwnerAccountId](#list_ram-ram_ShareOwnerAccountId)
  - **Access level:** Read

- **   [ListPermissionAssociations](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPermissionAssociations.html)  **
  - **Description:** Grants permission to list information about the permission and any associations
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Resource types (\*required):** [permission\*](#list_ram-resource-permission) / **Condition keys:** [ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Access level:** List

- **   [ListPermissionVersions](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPermissionVersions.html)  **
  - **Description:** Grants permission to list the versions of an AWS RAM permission
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPermissions](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPermissions.html)  **
  - **Description:** Grants permission to list the AWS RAM permissions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPrincipals](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPrincipals.html)  **
  - **Description:** Grants permission to list the principals that you have shared resources with or that have shared resources with you
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReplacePermissionAssociationsWork](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListReplacePermissionAssociationsWork.html)  **
  - **Description:** Grants permission to retrieve the status of the asynchronous permission replacement
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceSharePermissions](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResourceSharePermissions.html)  **
  - **Description:** Grants permission to list the Permissions associated with a Resource Share
  - **Resource types (\*required):** [resource-share\*](#list_ram-resource-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)<br />[ram:RetainSharingOnAccountLeaveOrganization](#list_ram-ram_RetainSharingOnAccountLeaveOrganization)
  - **Access level:** List

- **   [ListResourceTypes](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResourceTypes.html)  **
  - **Description:** Grants permission to list the shareable resource types supported by AWS RAM
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResources](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResources.html)  **
  - **Description:** Grants permission to list the resources that you added to resource shares or the resources that are shared with you
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSourceAssociations](https://docs.aws.amazon.com/ram/latest/APIReference/API_ListSourceAssociations.html)  **
  - **Description:** Grants permission to list source associations for resource shares
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PromotePermissionCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromotePermissionCreatedFromPolicy.html)  **
  - **Description:** Grants permission to create a separate, fully manageable customer managed permission
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Access level:** Write

- **   [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html)  **
  - **Description:** Grants permission to promote the specified resource share
  - **Resource types (\*required):** [resource-share\*](#list_ram-resource-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)
  - **Access level:** Write

- **   [RejectResourceShareInvitation](https://docs.aws.amazon.com/ram/latest/APIReference/API_RejectResourceShareInvitation.html)  **
  - **Description:** Grants permission to reject the specified resource share invitation
  - **Resource types (\*required):** [resource-share-invitation\*](#list_ram-resource-resource-share-invitation)
  - **Condition keys:** [ram:ResourceShareName](#list_ram-ram_ResourceShareName)<br />[ram:ShareOwnerAccountId](#list_ram-ram_ShareOwnerAccountId)
  - **Access level:** Write

- **   [ReplacePermissionAssociations](https://docs.aws.amazon.com/ram/latest/APIReference/API_ReplacePermissionAssociations.html)  **
  - **Description:** Grants permission to update all resource shares to a new permission
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Resource types (\*required):** [permission\*](#list_ram-resource-permission) / **Condition keys:** [ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Access level:** Write

- **   [SetDefaultPermissionVersion](https://docs.aws.amazon.com/ram/latest/APIReference/API_SetDefaultPermissionVersion.html)  **
  - **Description:** Grants permission to specify a version number as the default version for the respective customer managed permission
  - **Resource types (\*required):** [customer-managed-permission\*](#list_ram-resource-customer-managed-permission)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/ram/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag the specified resource share or permission
  - **Resource types (\*required):** [customer-managed-permission](#list_ram-resource-customer-managed-permission) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ram-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ram-aws_TagKeys)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Resource types (\*required):** [resource-share](#list_ram-resource-resource-share) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ram-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ram-aws_TagKeys)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/ram/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag the specified resource share or permission
  - **Resource types (\*required):** [customer-managed-permission](#list_ram-resource-customer-managed-permission) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ram-aws_TagKeys)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType)
  - **Resource types (\*required):** [resource-share](#list_ram-resource-resource-share) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ram-aws_TagKeys)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)
  - **Access level:** Tagging, Write

- **   [UpdateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_UpdateResourceShare.html)  **
  - **Description:** Grants permission to update attributes of the resource share
  - **Resource types (\*required):** [resource-share\*](#list_ram-resource-resource-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:RequestedAllowsExternalPrincipals](#list_ram-ram_RequestedAllowsExternalPrincipals)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName)<br />[ram:ResourceTag/${TagKey}](#list_ram-ram_ResourceTag___TagKey_)<br />[ram:RetainSharingOnAccountLeaveOrganization](#list_ram-ram_RetainSharingOnAccountLeaveOrganization)
  - **Access level:** Write



## Resource types defined by AWS Resource Access Manager (RAM)
<a name="list_ram-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [customer-managed-permission](${ActionsDocRoot}API_ResourceSharePermissionDetail.html)  | arn:${Partition}:ram:${Region}:${Account}:permission/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType) | 
|  [permission](${ActionsDocRoot}API_ResourceSharePermissionDetail.html)  | arn:${Partition}:ram::${Account}:permission/${ResourcePath} | [ram:PermissionArn](#list_ram-ram_PermissionArn)<br />[ram:PermissionResourceType](#list_ram-ram_PermissionResourceType) | 
|  [resource-share](${ActionsDocRoot}API_ResourceShare.html)  | arn:${Partition}:ram:${Region}:${Account}:resource-share/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_ram-aws_ResourceTag___TagKey_)<br />[ram:AllowsExternalPrincipals](#list_ram-ram_AllowsExternalPrincipals)<br />[ram:ResourceShareName](#list_ram-ram_ResourceShareName) | 
|  [resource-share-invitation](${ActionsDocRoot}API_ResourceShareInvitation.html)  | arn:${Partition}:ram:${Region}:${Account}:resource-share-invitation/${ResourcePath} | [ram:ShareOwnerAccountId](#list_ram-ram_ShareOwnerAccountId) | 

## Condition keys for AWS Resource Access Manager (RAM)
<a name="list_ram-policy-keys"></a>

AWS Resource Access Manager (RAM) defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request when creating or tagging a resource share. If users don't pass these specific tags, or if they don't specify tags at all, the request fails | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed when creating or tagging a resource share | ArrayOfString | 
|   [ram:AllowsExternalPrincipals](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by resource shares that allow or deny sharing with external principals. For example, specify true if the action can only be performed on resource shares that allow sharing with external principals. External principals are AWS accounts that are outside of its AWS organization | Bool | 
|   [ram:PermissionArn](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by the specified Permission ARN | ARN | 
|   [ram:PermissionResourceType](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by permissions of specified resource type | String | 
|   [ram:Principal](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by format of the specified principal | String | 
|   [ram:RequestedAllowsExternalPrincipals](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by the specified value for 'allowExternalPrincipals'. External principals are AWS accounts that are outside of its AWS Organization | Bool | 
|   [ram:RequestedResourceType](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by the specified resource type | String | 
|   [ram:ResourceArn](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by the specified ARN | ARN | 
|   [ram:ResourceShareName](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by a resource share with the specified name | String | 
|   [ram:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [ram:RetainSharingOnAccountLeaveOrganization](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by RetainSharingOnAccountLeaveOrganization value within ResourceShareConfiguration that is set on resource share | Bool | 
|   [ram:ShareOwnerAccountId](https://docs.aws.amazon.com/ram/latest/userguide/iam-policies.html#iam-policies-condition)  | Filters access by resource shares owned by a specific account. For example, you can use this condition key to specify which resource share invitations can be accepted or rejected based on the resource share owner's account ID | String | 