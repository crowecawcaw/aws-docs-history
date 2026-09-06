

# Edit IAM policies (AWS CLI)
<a name="access_policies_manage-edit-cli"></a>

A [policy](access_policies.md) is an entity that, when attached to an identity or resource, defines their permissions. You can use the AWS Command Line Interface (AWS CLI) to edit *customer managed policies* and *inline policies* in IAM. AWS managed policies cannot be edited. The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md).

For more information about policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md) and the [IAM JSON policy element reference](reference_policies_elements.md).

## Prerequisites
<a name="edit-customer-managed-policy-cli-prerequisites"></a>

Before you change the permissions for a policy, you should review its recent service-level activity. This is important because you don't want to remove access from a principal (person or application) who is using it. For more information about viewing last accessed information, see [Refine permissions in AWS using last accessed information](access_policies_last-accessed.md).

## Editing customer managed policies (AWS CLI)
<a name="edit-customer-managed-policy-cli"></a>

You can edit a customer managed policy from the AWS CLI.

**Note**  
A managed policy can have up to five versions. If you need to make changes to a customer managed policy beyond five versions, you must first delete one or more existing versions.

**To edit a customer managed policy (AWS CLI)**

1. (Optional) To view information about a policy, run the following commands:
   + To list managed policies: [list-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-policies.html)
   + To retrieve detailed information about a managed policy: [get-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/get-policy.html)

1. (Optional) To find out about the relationships between the policies and identities, run the following commands:
   + To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy is attached: 
     + [list-entities-for-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/list-entities-for-policy.html)
   + To list the managed policies attached to an identity (a user, user group, or role):
     + [list-attached-user-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-attached-user-policies.html)
     + [list-attached-group-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-attached-group-policies.html)
     + [list-attached-role-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-attached-role-policies.html)

1. To edit a customer managed policy, run the following command:
   + [create-policy-version](https://docs.aws.amazon.com/cli/latest/reference/iam/create-policy-version.html)

1. (Optional) To validate a customer managed policy, run the following IAM Access Analyzer command:
   + [validate-policy](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/validate-policy.html)

## Setting the default version of a customer managed policy (AWS CLI)
<a name="edit-customer-managed-policy-cli-set-default-policy-version"></a>

You can set a default version of a customer managed policy from the AWS CLI.

**To set the default version of a customer managed policy (AWS CLI)**

1. (Optional) To list managed policies, run the following command:
   + [list-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-policies.html)

1. To set the default version of a customer managed policy, run the following command:
   + [set-default-policy-version](https://docs.aws.amazon.com/cli/latest/reference/iam/set-default-policy-version.html)

## Deleting a version of a customer managed policy (AWS CLI)
<a name="edit-customer-managed-policy-cli-delete-policy-version"></a>

You can delete a version of a customer managed policy from the AWS CLI.

**To delete a version of a customer managed policy (AWS CLI)**

1. (Optional) To list managed policies, run the following command:
   + [list-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-policies.html)

1. To delete a customer managed policy, run the following command:
   + [delete-policy-version](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-policy-version.html)

## Editing inline policies (AWS CLI)
<a name="edit-inline-policy-cli"></a>

You can edit an inline policy from the AWS CLI.

**To edit an inline policy (AWS CLI)**

1. (Optional) To view information about a policy, run the following commands:
   + To list inline policies associated to an identity (a user, user group, or role): 
     + [list-user-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-user-policies.html)
     + [list-role-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-role-policies.html)
     + [list-group-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-group-policies.html)
   + To retrieve detailed information about an inline policy: 
     + [get-user-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/get-user-policy.html)
     + [get-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/get-role-policy.html)
     + [get-group-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/get-group-policy.html)

1. To edit an inline policy, run the following command:
   + [put-user-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/put-user-policy.html)
   + [put-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-policy.html)
   + [put-group-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/put-group-policy.html)

1. (Optional) To validate an inline policy, run the following IAM Access Analyzer command:
   + [validate-policy](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/validate-policy.html)