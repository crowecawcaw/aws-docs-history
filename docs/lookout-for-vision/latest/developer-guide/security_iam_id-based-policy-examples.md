End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Amazon Lookout for Vision identity-based

policy examples

By default, users and roles don't have permission to create or modify Lookout for Vision
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Lookout for Vision, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Lookout for Vision](../../../service-authorization/latest/reference/list_your_service.md "../../../service-authorization/latest/reference/list_your_service.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Accessing a single Amazon Lookout for Vision project](#security_iam_id-based-policy-examples-project "#security_iam_id-based-policy-examples-project")
- [Tag-based policy examples](#tag-based-policy-examples "#tag-based-policy-examples")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Lookout for Vision resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Accessing a single Amazon Lookout for Vision project

In this example, you want to grant a user in your AWS account
access to one of your Amazon Lookout for Vision projects.

```
{
    "Sid": "SpecificProjectOnly",
    "Effect": "Allow",
    "Action": [
        "lookoutvision:DetectAnomalies"
    ],
    "Resource": "arn:aws:lookoutvision:us-east-1:123456789012:model/myproject/*"
}

```

## Tag-based policy examples

Tag-based policies are JSON policy documents that specify the actions that a
principal can perform on tagged resources.

### Use a tag to access a resource

This example policy grants a user or role in your AWS account permission to use the
`DetectAnomalies` operation
with any model tagged with the key `stage` and the value `production`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "LookoutVision:DetectAnomalies"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/stage": "production"
 }
 }
 }
 ]
}`

```

#### Use a tag to deny access to specific Amazon Lookout for Vision operations

This example policy denies permission for a user or role in your AWS account
to call the `DeleteModel` or `StopModel` operations with any model tagged
with the key `stage` and the value `production`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "LookoutVision:DeleteModel",
 "LookoutVision:StopModel"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/stage": "production"
 }
 }
 }
 ]
}`

```
