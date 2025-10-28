# Edit IAM policies (AWS CLI)

A [policy](access_policies.md "access_policies.md") is an entity that, when attached to an
identity or resource, defines their permissions. You can use the AWS Command Line Interface (AWS CLI) to edit
_customer managed policies_ and _inline policies_ in IAM. AWS managed policies cannot be edited.
The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

For more information about policy structure and syntax, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md") and the [IAM JSON policy element reference](reference_policies_elements.md "reference_policies_elements.md").

## Prerequisites

Before you change the permissions for a policy, you should review its recent service-level
activity. This is important because you don't want to remove access from a principal (person
or application) who is using it. For more information about viewing last accessed information,
see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Editing customer managed policies

(AWS CLI)

You can edit a customer managed policy from the AWS CLI.

###### Note

A managed policy can have up to five versions. If you need to make changes to a customer
managed policy beyond five versions, you must first delete one or more existing
versions.

###### To edit a customer managed policy (AWS CLI)

1. (Optional) To view information about a policy, run the following commands:
   - To list managed policies: [list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md")
   - To retrieve detailed information about a managed policy: [get-policy](../../../cli/latest/reference/iam/get-policy.md "../../../cli/latest/reference/iam/get-policy.md")

2. (Optional) To find out about the relationships between the policies and identities,
   run the following commands:
   - To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy
     is attached:
     - [list-entities-for-policy](../../../cli/latest/reference/iam/list-entities-for-policy.md "../../../cli/latest/reference/iam/list-entities-for-policy.md")

   - To list the managed policies attached to an identity (a user, user group, or
     role):
     - [list-attached-user-policies](../../../cli/latest/reference/iam/list-attached-user-policies.md "../../../cli/latest/reference/iam/list-attached-user-policies.md")
     - [list-attached-group-policies](../../../cli/latest/reference/iam/list-attached-group-policies.md "../../../cli/latest/reference/iam/list-attached-group-policies.md")
     - [list-attached-role-policies](../../../cli/latest/reference/iam/list-attached-role-policies.md "../../../cli/latest/reference/iam/list-attached-role-policies.md")

3. To edit a customer managed policy, run the following command:
   - [create-policy-version](../../../cli/latest/reference/iam/create-policy-version.md "../../../cli/latest/reference/iam/create-policy-version.md")

4. (Optional) To validate a customer managed policy, run the following IAM Access Analyzer
   command:
   - [validate-policy](../../../cli/latest/reference/accessanalyzer/validate-policy.md "../../../cli/latest/reference/accessanalyzer/validate-policy.md")

## Setting the

default version of a customer managed policy (AWS CLI)

You can set a default version of a customer managed policy from the AWS CLI.

###### To set the default version of a customer managed policy (AWS CLI)

1. (Optional) To list managed policies, run the following command:
   - [list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md")

2. To set the default version of a customer managed policy, run the following
   command:
   - [set-default-policy-version](../../../cli/latest/reference/iam/set-default-policy-version.md "../../../cli/latest/reference/iam/set-default-policy-version.md")

## Deleting a version of

a customer managed policy (AWS CLI)

You can delete a version of a customer managed policy from the AWS CLI.

###### To delete a version of a customer managed policy (AWS CLI)

1. (Optional) To list managed policies, run the following command:
   - [list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md")

2. To delete a customer managed policy, run the following command:
   - [delete-policy-version](../../../cli/latest/reference/iam/delete-policy-version.md "../../../cli/latest/reference/iam/delete-policy-version.md")

## Editing inline policies (AWS CLI)

You can edit an inline policy from the AWS CLI.

###### To edit an inline policy (AWS CLI)

1. (Optional) To view information about a policy, run the following commands:
   - To list inline policies associated to an identity (a user, user group, or role):
     - [list-user-policies](../../../cli/latest/reference/iam/list-user-policies.md "../../../cli/latest/reference/iam/list-user-policies.md")
     - [list-role-policies](../../../cli/latest/reference/iam/list-role-policies.md "../../../cli/latest/reference/iam/list-role-policies.md")
     - [list-group-policies](../../../cli/latest/reference/iam/list-group-policies.md "../../../cli/latest/reference/iam/list-group-policies.md")

   - To retrieve detailed information about a inline policy:
     - [get-user-policy](../../../cli/latest/reference/iam/get-user-policy.md "../../../cli/latest/reference/iam/get-user-policy.md")
     - [get-role-policy](../../../cli/latest/reference/iam/get-role-policy.md "../../../cli/latest/reference/iam/get-role-policy.md")
     - [get-group-policy](../../../cli/latest/reference/iam/get-group-policy.md "../../../cli/latest/reference/iam/get-group-policy.md")

2. To edit an inline policy, run the following command:
   - [put-user-policy](../../../cli/latest/reference/iam/put-user-policy.md "../../../cli/latest/reference/iam/put-user-policy.md")
   - [put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md")
   - [put-group-policy](../../../cli/latest/reference/iam/put-group-policy.md "../../../cli/latest/reference/iam/put-group-policy.md")

3. (Optional) To validate an inline policy, run the following IAM Access Analyzer
   command:
   - [validate-policy](../../../cli/latest/reference/accessanalyzer/validate-policy.md "../../../cli/latest/reference/accessanalyzer/validate-policy.md")
