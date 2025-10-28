# Create IAM policies (AWS CLI)

A [policy](access_policies.md "access_policies.md") is an entity that, when attached to an
identity or resource, defines their permissions. You can use the AWS CLI to create _customer managed policies_ in IAM. Customer managed policies are
standalone policies that you administer in your own AWS account.
As a [best practice](best-practices.md "best-practices.md"), we
recommend that you use IAM Access Analyzer to validate your IAM policies to ensure secure and
functional permissions. By [validating your
policies](access_policies_policy-validator.md "access_policies_policy-validator.md") you can address any errors or recommendations before you attach the policies
to identities (users, groups, and roles) in your AWS account.

The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

## Creating IAM policies (AWS CLI)

You can create an IAM customer managed policy or an inline policy using the AWS Command Line Interface
(AWS CLI).

###### To create a customer managed policy (AWS CLI)

Use the following command:

- [create-policy](../../../cli/latest/reference/iam/create-policy.md "../../../cli/latest/reference/iam/create-policy.md")

###### To create an inline policy for an IAM identity (group, user or role) (AWS CLI)

Use one of the following commands:

- [put-group-policy](../../../cli/latest/reference/iam/put-group-policy.md "../../../cli/latest/reference/iam/put-group-policy.md")
- [put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md")
- [put-user-policy](../../../cli/latest/reference/iam/put-user-policy.md "../../../cli/latest/reference/iam/put-user-policy.md")

###### Note

You can't use IAM to embed an inline policy for a _[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_.

###### To validate a customer managed policy (AWS CLI)

Use the following IAM Access Analyzer command:

- [validate-policy](../../../cli/latest/reference/accessanalyzer/validate-policy.md "../../../cli/latest/reference/accessanalyzer/validate-policy.md")
