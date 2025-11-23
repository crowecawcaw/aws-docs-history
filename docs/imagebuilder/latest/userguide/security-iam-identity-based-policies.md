# Image Builder identity-based policies

###### Topics

- [Identity-based policy best
  practices](#security-iam-service-policy-best-practices "#security-iam-service-policy-best-practices")
- [Using the Image Builder
  console](#sec-iam-id-based-policies-using-console "#sec-iam-id-based-policies-using-console")

## Identity-based policy best

practices

Identity-based policies determine whether someone can create, access, or delete Image Builder resources in your
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
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
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

## Using the Image Builder

console

To access the EC2 Image Builder console, you must have a minimum set of permissions. These
permissions allow you to list and view details about the Image Builder resources in your
AWS account. If you create an identity-based policy that is more restrictive than
the minimum required permissions, the console won't function as intended for
entities (IAM users or roles) with that policy.

To ensure that your IAM entities can use the Image Builder console, you must attach one of
the following AWS managed policies to them:

- [AWSImageBuilderReadOnlyAccess policy](security-iam-awsmanpol.md#sec-iam-manpol-AWSImageBuilderReadOnlyAccess "security-iam-awsmanpol.md#sec-iam-manpol-AWSImageBuilderReadOnlyAccess")
- [AWSImageBuilderFullAccess policy](security-iam-awsmanpol.md#sec-iam-manpol-AWSImageBuilderFullAccess "security-iam-awsmanpol.md#sec-iam-manpol-AWSImageBuilderFullAccess")

For more information about Image Builder managed policies, see
[Use AWS managed policies for EC2 Image Builder](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

###### Important

The **AWSImageBuilderFullAccess** policy is
required to create the Image Builder service-linked role. When you attach this policy
to an IAM entity, you must also attach the following custom policy and include the
resources you want to use that do not have `imagebuilder` in the resource
name:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sns:Publish"
 ],
 "Resource": "arn:aws:sns:*:*:*imagebuilder*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetInstanceProfile"
 ],
 "Resource": "arn:aws:iam::*:instance-profile/*imagebuilder*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::*:instance-profile/*imagebuilder*",
 "arn:aws:iam::*:role/*imagebuilder*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "ec2.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3::*:*imagebuilder*"
 }
 ]
}`

```

You don't need to allow minimum console permissions for users that are making
calls to only the AWS CLI or the AWS API. Instead, allow access to only the actions
that match the API operation that you're trying to perform.
