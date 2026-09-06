

# Delete IAM policies (AWS API)
<a name="access_policies_manage-delete-api"></a>

You can use the AWS API to delete *customer managed policies* and *inline policies* in IAM. The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md).

**Note**  
Deletion of IAM policies is permanent. After the policy is deleted it cannot be recovered.

For more information about IAM policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md) and the [IAM JSON policy element reference](reference_policies_elements.md).

For more information about the difference between managed and inline policies, see [Managed policies and inline policies](access_policies_managed-vs-inline.md). 

## Prerequisites
<a name="delete-policy-prerequisites-api"></a>

Before you delete a policy, you should review its recent service-level activity. This is important because you don't want to remove access from a principal (person or application) who is using it. For more information about viewing last accessed information, see [Refine permissions in AWS using last accessed information](access_policies_last-accessed.md).

## Deleting customer managed policies (AWS API)
<a name="delete-customer-managed-policy-api"></a>

You can delete a customer managed policy using the AWS API.

**To delete a customer managed policy (AWS API)**

1. (Optional) To view information about a policy, call the following operations:
   + To list managed policies: [ListPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html)
   + To retrieve detailed information about a managed policy: [GetPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicy.html)

1. (Optional) To find out about the relationships between the policies and identities, call the following operations:
   + To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy is attached, call the following operation: 
     + [ListEntitiesForPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListEntitiesForPolicy.html)
   + To list the managed policies attached to an identity (a user, user group, or role), call one of the following operations:
     + [ListAttachedUserPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedUserPolicies.html)
     + [ListAttachedGroupPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedGroupPolicies.html)
     + [ListAttachedRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedRolePolicies.html)

1. To delete a customer managed policy, call the following operation:
   + [DeletePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeletePolicy.html)

## Deleting inline policies (AWS API)
<a name="delete-inline-policy-api"></a>

You can delete an inline policy using the AWS API.

**To delete an inline policy (AWS API)**

1. (Optional) To list all inline policies that are attached to an identity (user, user group, role), call one of the following operations:
   + [ListUserPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUserPolicies.html)
   + [ListGroupPolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroupPolicies.html)
   + [ListRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRolePolicies.html)

1. (Optional) To retrieve an inline policy document that is embedded in an identity (user, user group, or role), call one of the following operations:
   + [GetUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetUserPolicy.html)
   + [GetGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroupPolicy.html)
   + [GetRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRolePolicy.html)

1. To delete an inline policy from an identity (user, user group, or role that is not a *[service-linked role](id_roles.md#iam-term-service-linked-role)*), call one of the following operations:
   + [DeleteUserPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteUserPolicy.html)
   + [DeleteGroupPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteGroupPolicy.html)
   + [DeleteRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteRolePolicy.html)