

# How AWS CodeCommit works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to CodeCommit, you should understand what IAM features are available to use with CodeCommit. To get a high-level view of how CodeCommit and other AWS services work with IAM, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [Condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys)
+ [Examples](#security_iam_service-with-iam-id-based-policies-examples)

## Condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

CodeCommit defines its own set of condition keys and also supports using some global condition keys. To see all AWS global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

 Some CodeCommit actions support the `codecommit:References` condition key. For an example policy that uses this key, see [Example 4: Deny or allow actions on branches](customer-managed-policies.md#identity-based-policies-example-4). 

To see a list of CodeCommit condition keys, see [Condition Keys for AWS CodeCommit](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscodecommit.html#awscodecommit-policy-keys) in the *IAM User Guide*. To learn with which actions and resources you can use a condition key, see [Actions Defined by AWS CodeCommit](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awscodecommit.html#awscodecommit-actions-as-permissions).

## Examples
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>



To view examples of CodeCommit identity-based policies, see [AWS CodeCommit identity-based policy examples](security-iam.md#security_iam_id-based-policy-examples).