# Identity-based policy examples

for AWS Account Management

By default, users and roles don't have permission to create or modify Account Management
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Account Management, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Account Management](../../../service-authorization/latest/reference/list_awsaccountmanagement.md "../../../service-authorization/latest/reference/list_awsaccountmanagement.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Account
  page in the AWS Management Console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Providing read-only access to the Account page in the AWS Management Console](#security_iam_id-based-policy-examples-allow-ro-console-settings "#security_iam_id-based-policy-examples-allow-ro-console-settings")
- [Providing full access to the Account page in the AWS Management Console](#security_iam_id-based-policy-examples-allow-rw-console-settings "#security_iam_id-based-policy-examples-allow-rw-console-settings")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Account Management resources in your
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

## Using the Account

page in the AWS Management Console

To access the [**Account** page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account") in the AWS Management Console, you must have a
minimum set of permissions. These permissions must allow you to list and view
details about your AWS account. If you create an identity-based policy that is
more restrictive than the minimum required permissions, the console won't function
as intended for entities (IAM users or roles) with that policy.

To ensure that users and roles can use the Account Management console, you can choose to
attach either the `AWSAccountManagementReadOnlyAccess` or
`AWSAccountManagementFullAccess` AWS managed policy to the
entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

You don't need to allow minimum console permissions for users that are making
calls only to the AWS CLI or the AWS API. Instead, in many cases you can choose
to allow access to only the actions that match the API operations that you're trying
to perform.

## Providing read-only access to the Account page in the AWS Management Console

In the following example, you want to grant an IAM user in your AWS account
read-only access to the Account page in the AWS Management Console. Users with this policy
attached can't make any changes.

The `account:GetAccountInformation` action grants access to view most
of the settings on the Account page. However, to view the currently enabled AWS
Regions, you must also include the `account:ListRegions` action.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GrantReadOnlyAccessToAccountSettings",
 "Effect": "Allow",
 "Action": [
 "account:GetAccountInformation",
 "account:ListRegions"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Providing full access to the Account page in the AWS Management Console

In the following example, you want to grant an IAM user in your AWS account
full access to the Account page in the AWS Management Console. Users with this policy attached
can alter settings for the account.

This example policy builds on the preceding example policy by adding each of the
available write permissions (with the exception of CloseAccount), which allows the
user to change most of the settings for the account, including the
`account:EnableRegion` and `account:DisableRegion`
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GrantFullAccessToAccountSettings",
 "Effect": "Allow",
 "Action": [
 "account:GetAccountInformation",
 "account:ListRegions",
 "account:PutContactInformation",
 "account:PutAlternateContact",
 "account:DeleteAlternateContact",
 "account:EnableRegion",
 "account:DisableRegion"
 ],
 "Resource": "*"
 }
 ]
}`

```
