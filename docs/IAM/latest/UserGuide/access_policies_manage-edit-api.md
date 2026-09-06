

# Edit IAM policies (AWS API)
<a name="access_policies_manage-edit-api"></a>

A [policy](access_policies.md) is an entity that, when attached to an identity or resource, defines their permissions. You can use the AWS API to edit *customer managed policies* and *inline policies* in IAM. AWS managed policies cannot be edited. The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md).

For more information about policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md) and the [IAM JSON policy element reference](reference_policies_elements.md).

## Prerequisites
<a name="edit-customer-managed-policy-api-prerequisites"></a>

Before you change the permissions for a policy, you should review its recent service-level activity. This is important because you don't want to remove access from a principal (person or application) who is using it. For more information about viewing last accessed information, see [Refine permissions in AWS using last accessed information](access_policies_last-accessed.md).

## Editing customer managed policies (AWS API)
<a name="edit-customer-managed-policy-api"></a>

You can edit a customer managed policy using the AWS API.

**Note**  
A managed policy can have up to five versions. If you need to make changes to a customer managed policy beyond five versions, you must first delete one or more existing versions.

**To edit a customer managed policy (AWS API)**

1. (Optional) To view information about a policy, call the following operations:
   + To list managed policies: [ListPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html)
   + To retrieve detailed information about a managed policy: [GetPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicy.html)

1. (Optional) To find out about the relationships between the policies and identities, call the following operations:
   + To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy is attached: 
     + [ListEntitiesForPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListEntitiesForPolicy.html)
   + To list the managed policies attached to an identity (a user, user group, or role):
     + [ListAttachedUserPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedUserPolicies.html)
     + [ListAttachedGroupPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedGroupPolicies.html)
     + [ListAttachedRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedRolePolicies.html)

1. To edit a customer managed policy, call the following operation:
   + [CreatePolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicyVersion.html)

1. (Optional) To validate a customer managed policy, call the following IAM Access Analyzer operation:
   + [ValidatePolicy](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html)

## Setting the default version of a customer managed policy (AWS API)
<a name="edit-customer-managed-policy-api-set-default-policy-version"></a>

You can set a default version of a customer managed policy from the AWS API.

**To set the default version of a customer managed policy (AWS API)**

1. (Optional) To list managed policies, call the following operation:
   + [ListPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html)

1. To set the default version of a customer managed policy, call the following operation:
   + [SetDefaultPolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SetDefaultPolicyVersion.html)

## Deleting a version of a customer managed policy (AWS API)
<a name="edit-customer-managed-policy-api-delete-policy-version"></a>

You can delete a version of a customer managed policy from the AWS API.

**To delete a version of a customer managed policy (AWS API)**

1. (Optional) To list managed policies, call the following operation:
   + [ListPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html)

1. To delete a customer managed policy, call the following operation:
   + [DeletePolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeletePolicyVersion.html)

## Editing inline policies (AWS API)
<a name="edit-inline-policy-api"></a>

You can edit an inline policy from the AWS API.

**To edit an inline policy (AWS API)**

1. (Optional) To view information about an inline policy, call the following operations:
   + To list inline policies associated to an identity (a user, user group, or role): 
     + [ListUserPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUserPolicies.html)
     + [ListRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRolePolicies.html)
     + [ListGroupPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroupPolicies.html)
   + To retrieve detailed information about an inline policy: 
     + [GetUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUserPolicy.html)
     + [GetRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRolePolicy.html)
     + [GetGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroupPolicy.html)

1. To edit an inline policy, call the following operations:
   + [PutUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutUserPolicy.html)
   + [PutRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePolicy.html)
   + [PutGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutGroupPolicy.html)

1. (Optional) To validate an inline policy, run the following IAM Access Analyzer operation:
   + [ValidatePolicy](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html)