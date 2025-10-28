# Edit IAM policies (AWS API)

A [policy](access_policies.md "access_policies.md") is an entity that, when attached to an
identity or resource, defines their permissions. You can use the AWS API to edit _customer managed policies_ and _inline
policies_ in IAM. AWS managed policies cannot be edited.
The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

For more information about policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md") and the [IAM JSON policy element reference](reference_policies_elements.md "reference_policies_elements.md").

## Prerequisites

Before you change the permissions for a policy, you should review its recent service-level
activity. This is important because you don't want to remove access from a principal (person
or application) who is using it. For more information about viewing last accessed information,
see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Editing customer managed policies (AWS

API)

You can edit a customer managed policy using the AWS API.

###### Note

A managed policy can have up to five versions. If you need to make changes to a customer
managed policy beyond five versions, you must first delete one or more existing
versions.

###### To edit a customer managed policy (AWS API)

1. (Optional) To view information about a policy, call the following operations:
   - To list managed policies: [ListPolicies](../APIReference/API_ListPolicies.md "../APIReference/API_ListPolicies.md")
   - To retrieve detailed information about a managed policy: [GetPolicy](../APIReference/API_GetPolicy.md "../APIReference/API_GetPolicy.md")

2. (Optional) To find out about the relationships between the policies and identities,
   call the following operations:
   - To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy
     is attached:
     - [ListEntitiesForPolicy](../APIReference/API_ListEntitiesForPolicy.md "../APIReference/API_ListEntitiesForPolicy.md")

   - To list the managed policies attached to an identity (a user, user group, or
     role):
     - [ListAttachedUserPolicies](../APIReference/API_ListAttachedUserPolicies.md "../APIReference/API_ListAttachedUserPolicies.md")
     - [ListAttachedGroupPolicies](../APIReference/API_ListAttachedGroupPolicies.md "../APIReference/API_ListAttachedGroupPolicies.md")
     - [ListAttachedRolePolicies](../APIReference/API_ListAttachedRolePolicies.md "../APIReference/API_ListAttachedRolePolicies.md")

3. To edit a customer managed policy, call the following operation:
   - [CreatePolicyVersion](../APIReference/API_CreatePolicyVersion.md "../APIReference/API_CreatePolicyVersion.md")

4. (Optional) To validate a customer managed policy, call the following IAM Access Analyzer
   operation:
   - [ValidatePolicy](../../../access-analyzer/latest/APIReference/API_ValidatePolicy.md "../../../access-analyzer/latest/APIReference/API_ValidatePolicy.md")

## Setting the

default version of a customer managed policy (AWS API)

You can set a default version of a customer managed policy from the AWS API.

###### To set the default version of a customer managed policy (AWS API)

1. (Optional) To list managed policies, call the following operation:
   - [ListPolicies](../APIReference/API_ListPolicies.md "../APIReference/API_ListPolicies.md")

2. To set the default version of a customer managed policy, call the following
   operation:
   - [SetDefaultPolicyVersion](../APIReference/API_SetDefaultPolicyVersion.md "../APIReference/API_SetDefaultPolicyVersion.md")

## Deleting a version of

a customer managed policy (AWS API)

You can delete a version of a customer managed policy from the AWS API.

###### To delete a version of a customer managed policy (AWS API)

1. (Optional) To list managed policies, call the following operation:
   - [ListPolicies](../APIReference/API_ListPolicies.md "../APIReference/API_ListPolicies.md")

2. To delete a customer managed policy, call the following operation:
   - [DeletePolicyVersion](../APIReference/API_DeletePolicyVersion.md "../APIReference/API_DeletePolicyVersion.md")

## Editing inline policies (AWS API)

You can edit an inline policy from the AWS API.

###### To edit an inline policy (AWS API)

1. (Optional) To view information about an inline policy, run the following
   operations:
   - To list inline policies associated to an identity (a user, user group, or role):
     - [ListUserPolicies](../APIReference/API_ListUserPolicies.md "../APIReference/API_ListUserPolicies.md")
     - [ListRolePolicies](../APIReference/API_ListRolePolicies.md "../APIReference/API_ListRolePolicies.md")
     - [ListGroupPolicies](../APIReference/API_ListGroupPolicies.md "../APIReference/API_ListGroupPolicies.md")

   - To retrieve detailed information about an inline policy:
     - [GetUserPolicy](../APIReference/API_GetUserPolicy.md "../APIReference/API_GetUserPolicy.md")
     - [GetRolePolicy](../APIReference/API_GetRolePolicy.md "../APIReference/API_GetRolePolicy.md")
     - [GetGroupPolicy](../APIReference/API_GetGroupPolicy.md "../APIReference/API_GetGroupPolicy.md")

2. To edit an inline policy, run the following operations:
   - [PutUserPolicy](../APIReference/API_PutUserPolicy.md "../APIReference/API_PutUserPolicy.md")
   - [PutRolePolicy](../APIReference/API_PutRolePolicy.md "../APIReference/API_PutRolePolicy.md")
   - [PutGroupPolicy](../APIReference/API_PutGroupPolicy.md "../APIReference/API_PutGroupPolicy.md")

3. (Optional) To validate an inline policy, run the following IAM Access Analyzer
   operation:
   - [ValidatePolicy](../../../access-analyzer/latest/APIReference/API_ValidatePolicy.md "../../../access-analyzer/latest/APIReference/API_ValidatePolicy.md")
