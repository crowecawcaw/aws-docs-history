# Define custom IAM permissions with customer managed

policies

[Policies](access_policies.md "access_policies.md") define permissions for identities or
resources in AWS. You can create _customer managed policies_
in IAM using the AWS Management Console, AWS CLI, or AWS API. Customer managed policies are standalone
policies that you manage in your own AWS account. You can then attach the policies to
identities (users, groups, and roles) in your AWS account.

An _identity-based policy_ is a policy attached to an
identity in IAM. Identity-based policies can include AWS managed policies, customer managed
policies, and inline policies. AWS managed policies are created and managed by AWS, and you
can use them but not manage them. An inline policy is one that you create and embed directly to
an IAM user group, user, or role. Inline policies can't be reused on other identities or
managed outside of the identity where they exist. For more information, see [Adding and removing IAM identity
permissions](access_policies_manage-attach-detach.md "access_policies_manage-attach-detach.md").

It's generally better to use customer managed policies instead of inline policies or
AWS managed policies. AWS managed policies usually provide broad administrative or read-only
permissions. For the greatest security, [grant the least
privilege](best-practices.md#grant-least-privilege "best-practices.md#grant-least-privilege"), which means granting only the permissions required to perform specific job
tasks.

When you create or edit IAM policies, AWS can automatically perform policy validation to
help you create an effective policy with least privilege in mind. In the AWS Management Console, IAM
identifies JSON syntax errors, while IAM Access Analyzer provides additional policy checks with
recommendations to help you further refine your policies. To learn more about policy validation,
see [IAM policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md"). To learn more about IAM Access Analyzer policy
checks and actionable recommendations, see [IAM Access Analyzer policy
validation](access-analyzer-policy-validation.md "access-analyzer-policy-validation.md").

You can use the AWS Management Console, AWS CLI, or AWS API to create customer managed policies in IAM.
For more information about using AWS CloudFormation templates to add or update policies, see [AWS Identity and Access Management resource
type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md") in the _AWS CloudFormation User Guide_.

###### Topics

- [Create IAM policies (console)](access_policies_create-console.md "access_policies_create-console.md")
- [Create IAM policies (AWS CLI)](access_policies_create-cli.md "access_policies_create-cli.md")
- [Create IAM policies (AWS API)](access_policies_create-api.md "access_policies_create-api.md")
