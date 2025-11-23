# Edit IAM policies

A [policy](access_policies.md "access_policies.md") is an entity that, when attached to an
identity or resource, defines their permissions. Policies are stored in AWS as JSON documents
and are attached to principals as _identity-based policies_ in IAM. You can
attach an identity-based policy to a principal (or identity), such as an IAM user group, user,
or role. Identity-based policies include AWS managed policies, customer managed policies, and
[inline policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md"). You can edit
customer managed policies and inline policies in IAM. AWS managed policies cannot be edited.
The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

It's generally better to use customer managed policies instead of inline policies or AWS
managed policies. AWS managed policies usually provide broad administrative or read-only
permissions. Inline policies can't be reused on other identities or managed outside of the
identity where they exist. For the greatest security, [grant the least privilege](best-practices.md#grant-least-privilege "best-practices.md#grant-least-privilege"), which means granting only the permissions required to
perform specific job tasks.

When you create or edit IAM policies, AWS can automatically perform policy validation to
help you create an effective policy with least privilege in mind. In the AWS Management Console, IAM
identifies JSON syntax errors, while IAM Access Analyzer provides additional policy checks with
recommendations to help you further refine your policies. To learn more about policy validation,
see [IAM policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md"). To learn more about IAM Access Analyzer policy
checks and actionable recommendations, see [IAM Access Analyzer policy
validation](access-analyzer-policy-validation.md "access-analyzer-policy-validation.md").

You can use the AWS Management Console, AWS CLI, or AWS API to edit customer managed policies and inline
policies in IAM. For more information about using CloudFormation templates to add or update policies,
see [AWS Identity and Access Management
resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md") in the _CloudFormation User Guide_.

###### Topics

- [Edit IAM policies (console)](access_policies_manage-edit-console.md "access_policies_manage-edit-console.md")
- [Edit IAM policies (AWS CLI)](access_policies_manage-edit-cli.md "access_policies_manage-edit-cli.md")
- [Edit IAM policies (AWS API)](access_policies_manage-edit-api.md "access_policies_manage-edit-api.md")
