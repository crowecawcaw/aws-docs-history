AWS CodeCommit is no longer available to new customers. Existing customers of
AWS CodeCommit can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider")

# How AWS CodeCommit works with

IAM

Before you use IAM to manage access to CodeCommit, you should understand what
IAM features are available to use with CodeCommit. To get a high-level view of how
CodeCommit and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys")
- [Examples](#security_iam_service-with-iam-id-based-policies-examples "#security_iam_service-with-iam-id-based-policies-examples")

## Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

CodeCommit defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

Some CodeCommit actions support the `codecommit:References` condition key. For an example
policy that uses this key, see [Example 4: Deny or allow
actions on branches](customer-managed-policies.md#identity-based-policies-example-4 "customer-managed-policies.md#identity-based-policies-example-4").

To see a list of CodeCommit condition keys, see [Condition Keys for AWS CodeCommit](../../../IAM/latest/UserGuide/list_awscodecommit.md#awscodecommit-policy-keys "../../../IAM/latest/UserGuide/list_awscodecommit.md#awscodecommit-policy-keys")
in the _IAM User Guide_. To learn with which actions and
resources you can use a condition key, see [Actions Defined by AWS CodeCommit](../../../IAM/latest/UserGuide/list_awscodecommit.md#awscodecommit-actions-as-permissions "../../../IAM/latest/UserGuide/list_awscodecommit.md#awscodecommit-actions-as-permissions").

## Examples

To view examples of CodeCommit identity-based policies, see [AWS CodeCommit identity-based
policy examples](security-iam.md#security_iam_id-based-policy-examples "security-iam.md#security_iam_id-based-policy-examples").
