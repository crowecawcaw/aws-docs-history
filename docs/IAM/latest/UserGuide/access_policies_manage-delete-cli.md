# Delete IAM policies (AWS CLI)

You can use the AWS Command Line Interface (AWS CLI) to delete _customer managed
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

## Deleting customer managed policies

(AWS CLI)

You can delete a customer managed policy from the AWS Command Line Interface.

###### To delete a customer managed policy (AWS CLI)

1. (Optional) To view information about a policy, run the following commands:
   - To list managed policies: [list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md")
   - To retrieve detailed information about a managed policy: [get-policy](../../../cli/latest/reference/iam/get-policy.md "../../../cli/latest/reference/iam/get-policy.md")

2. (Optional) To find out about the relationships between the policies and identities,
   run the following commands:
   - To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy
     is attached, run the following command:
     - [list-entities-for-policy](../../../cli/latest/reference/iam/list-entities-for-policy.md "../../../cli/latest/reference/iam/list-entities-for-policy.md")

   - To list the managed policies attached to an identity (a user, user group, or
     role), run one of the following commands:
     - [list-attached-user-policies](../../../cli/latest/reference/iam/list-attached-user-policies.md "../../../cli/latest/reference/iam/list-attached-user-policies.md")
     - [list-attached-group-policies](../../../cli/latest/reference/iam/list-attached-group-policies.md "../../../cli/latest/reference/iam/list-attached-group-policies.md")
     - [list-attached-role-policies](../../../cli/latest/reference/iam/list-attached-role-policies.md "../../../cli/latest/reference/iam/list-attached-role-policies.md")

3. To delete a customer managed policy, run the following command:
   - [delete-policy](../../../cli/latest/reference/iam/delete-policy.md "../../../cli/latest/reference/iam/delete-policy.md")

## Deleting inline policies (AWS CLI)

You can delete an inline policy from the AWS CLI.

###### To delete an inline policy (AWS CLI)

1. (Optional) To list all inline policies that are attached to an identity (user, user
   group, role), use one of the following commands:
   - [aws iam
     list-user-policies](../../../cli/latest/reference/iam/list-user-policies.md "../../../cli/latest/reference/iam/list-user-policies.md")
   - [aws iam
     list-group-policies](../../../cli/latest/reference/iam/list-group-policies.md "../../../cli/latest/reference/iam/list-group-policies.md")
   - [aws iam
     list-role-policies](../../../cli/latest/reference/iam/list-role-policies.md "../../../cli/latest/reference/iam/list-role-policies.md")

2. (Optional) To retrieve an inline policy document that is embedded in an identity
   (user, user group, or role), use one of the following commands:
   - [aws iam
     get-user-policy](../../../cli/latest/reference/iam/get-user-policy.md "../../../cli/latest/reference/iam/get-user-policy.md")
   - [aws iam
     get-group-policy](../../../cli/latest/reference/iam/get-group-policy.md "../../../cli/latest/reference/iam/get-group-policy.md")
   - [aws iam
     get-role-policy](../../../cli/latest/reference/iam/get-role-policy.md "../../../cli/latest/reference/iam/get-role-policy.md")

3. To delete an inline policy from an identity (user, user group, or role that is not a
   _[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_),
   use one of the following commands:
   - [aws iam
     delete-user-policy](../../../cli/latest/reference/iam/delete-user-policy.md "../../../cli/latest/reference/iam/delete-user-policy.md")
   - [aws iam
     delete-group-policy](../../../cli/latest/reference/iam/delete-group-policy.md "../../../cli/latest/reference/iam/delete-group-policy.md")
   - [aws iam
     delete-role-policy](../../../cli/latest/reference/iam/delete-role-policy.md "../../../cli/latest/reference/iam/delete-role-policy.md")
