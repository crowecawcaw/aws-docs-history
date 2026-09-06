

# Delete IAM policies (AWS CLI)
<a name="access_policies_manage-delete-cli"></a>

You can use the AWS Command Line Interface (AWS CLI) to delete *customer managed policies* and *inline policies* in IAM. The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md).

**Note**  
Deletion of IAM policies is permanent. After the policy is deleted it cannot be recovered.

For more information about IAM policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md) and the [IAM JSON policy element reference](reference_policies_elements.md).

For more information about the difference between managed and inline policies, see [Managed policies and inline policies](access_policies_managed-vs-inline.md). 

## Prerequisites
<a name="delete-policy-prerequisites-cli"></a>

Before you delete a policy, you should review its recent service-level activity. This is important because you don't want to remove access from a principal (person or application) who is using it. For more information about viewing last accessed information, see [Refine permissions in AWS using last accessed information](access_policies_last-accessed.md).

## Deleting customer managed policies (AWS CLI)
<a name="delete-customer-managed-policy-cli"></a>

You can delete a customer managed policy from the AWS Command Line Interface.

**To delete a customer managed policy (AWS CLI)**

1. (Optional) To view information about a policy, run the following commands:
   + To list managed policies: [list-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-policies.html)
   + To retrieve detailed information about a managed policy: [get-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/get-policy.html)

1. (Optional) To find out about the relationships between the policies and identities, run the following commands:
   + To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy is attached, run the following command: 
     + [list-entities-for-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/list-entities-for-policy.html)
   + To list the managed policies attached to an identity (a user, user group, or role), run one of the following commands:
     + [list-attached-user-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-attached-user-policies.html)
     + [list-attached-group-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-attached-group-policies.html)
     + [list-attached-role-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-attached-role-policies.html)

1. To delete a customer managed policy, run the following command:
   + [delete-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-policy.html)

## Deleting inline policies (AWS CLI)
<a name="delete-inline-policy-cli"></a>

You can delete an inline policy from the AWS CLI.

**To delete an inline policy (AWS CLI)**

1. (Optional) To list all inline policies that are attached to an identity (user, user group, role), use one of the following commands:
   + [aws iam list-user-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-user-policies.html)
   + [aws iam list-group-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-group-policies.html)
   + [aws iam list-role-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-role-policies.html)

1. (Optional) To retrieve an inline policy document that is embedded in an identity (user, user group, or role), use one of the following commands:
   + [aws iam get-user-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/get-user-policy.html)
   + [aws iam get-group-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/get-group-policy.html)
   + [aws iam get-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/get-role-policy.html)

1. To delete an inline policy from an identity (user, user group, or role that is not a *[service-linked role](id_roles.md#iam-term-service-linked-role)*), use one of the following commands:
   + [aws iam delete-user-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-user-policy.html)
   + [aws iam delete-group-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-group-policy.html)
   + [aws iam delete-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-role-policy.html)