# Delete IAM policies (AWS API)

You can use the AWS API to delete _customer managed
policies_ and _inline policies_ in IAM.
The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

###### Note

Deletion of IAM policies is permanent. After the policy is deleted it cannot be
recovered.

For more information about IAM policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md") and the [IAM JSON policy element reference](reference_policies_elements.md "reference_policies_elements.md").

For more information about the difference between managed and inline policies, see [Managed policies and inline policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md").

## Prerequisites

Before you delete a policy, you should review its recent service-level activity. This is
important because you don't want to remove access from a principal (person or application) who
is using it. For more information about viewing last accessed information, see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Deleting customer managed policies (AWS

API)

You can delete a customer managed policy using the AWS API.

###### To delete a customer managed policy (AWS API)

1. (Optional) To view information about a policy, call the following operations:
   - To list managed policies: [ListPolicies](../APIReference/API_ListPolicies.md "../APIReference/API_ListPolicies.md")
   - To retrieve detailed information about a managed policy: [GetPolicy](../APIReference/API_GetPolicy.md "../APIReference/API_GetPolicy.md")

2. (Optional) To find out about the relationships between the policies and identities,
   call the following operations:
   - To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy
     is attached, call the following operation:
     - [ListEntitiesForPolicy](../APIReference/API_ListEntitiesForPolicy.md "../APIReference/API_ListEntitiesForPolicy.md")

   - To list the managed policies attached to an identity (a user, user group, or
     role), call one of the following operations:
     - [ListAttachedUserPolicies](../APIReference/API_ListAttachedUserPolicies.md "../APIReference/API_ListAttachedUserPolicies.md")
     - [ListAttachedGroupPolicies](../APIReference/API_ListAttachedGroupPolicies.md "../APIReference/API_ListAttachedGroupPolicies.md")
     - [ListAttachedRolePolicies](../APIReference/API_ListAttachedRolePolicies.md "../APIReference/API_ListAttachedRolePolicies.md")

3. To delete a customer managed policy, call the following operation:
   - [DeletePolicy](../APIReference/API_DeletePolicy.md "../APIReference/API_DeletePolicy.md")

## Deleting inline policies (AWS API)

You can delete an inline policy using the AWS API.

###### To delete an inline policy (AWS API)

1. (Optional) To list all inline policies that are attached to an identity (user, user
   group, role), call one of the following operations:
   - [ListUserPolicies](../APIReference/API_ListUserPolicies.md "../APIReference/API_ListUserPolicies.md")
   - [ListGroupPolicies](../APIReference/API_ListGroupPolicies.md "../APIReference/API_ListGroupPolicies.md")
   - [ListRolePolicies](../APIReference/API_ListRolePolicies.md "../APIReference/API_ListRolePolicies.md")

2. (Optional) To retrieve an inline policy document that is embedded in an identity
   (user, user group, or role), call one of the following operations:
   - [GetUserPolicy](../APIReference/API_GetUserPolicy.md "../APIReference/API_GetUserPolicy.md")
   - [GetGroupPolicy](../APIReference/API_GetGroupPolicy.md "../APIReference/API_GetGroupPolicy.md")
   - [GetRolePolicy](../APIReference/API_GetRolePolicy.md "../APIReference/API_GetRolePolicy.md")

3. To delete an inline policy from an identity (user, user group, or role that is not a
   _[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_),
   call one of the following operations:
   - [DeleteUserPolicy](../APIReference/API_DeleteUserPolicy.md "../APIReference/API_DeleteUserPolicy.md")
   - [DeleteGroupPolicy](../APIReference/API_DeleteGroupPolicy.md "../APIReference/API_DeleteGroupPolicy.md")
   - [DeleteRolePolicy](../APIReference/API_DeleteRolePolicy.md "../APIReference/API_DeleteRolePolicy.md")
