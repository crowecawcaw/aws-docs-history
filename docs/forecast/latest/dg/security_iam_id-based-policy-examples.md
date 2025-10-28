Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Identity-based policy

examples for Amazon Forecast

By default, users and roles don't have permission to create or modify Forecast
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Forecast, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Forecast](../../../service-authorization/latest/reference/list_amazonforecast.md "../../../service-authorization/latest/reference/list_amazonforecast.md") in the _Service Authorization Reference_.

Whenever an operation is invoked, Amazon Forecast performs a set of authentication checks on the caller's permissions. These checks include the following:

- The caller's permission to invoke the operation is validated.
- If a role is provided within an operation, Amazon Forecast validates the PassRole permission for the role.
- If a KMS key is provided in the encryption configuration, then kms:Decrypt and kms:GenerateDataKey validation is performed on the caller's permissions. This key can differ for each operation performed in Amazon Forecast. You will receive an AccessDeniedException in the event that you do not have the relevant permissions. The key policy should resemble the following code:

```
"Effect": "Allow",
"Principal": {
    "AWS": “`AWS Invoking Identity`”
},
"Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey”
    ],
    "Resource": "*"
}
```

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Forecast
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [AWS Managed (Predefined)
  Policies for Amazon Forecast](#access-policy-aws-managed-policies "#access-policy-aws-managed-policies")
- [Customer Managed Policy
  Examples](#access-policy-customer-managed-examples "#access-policy-customer-managed-examples")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Forecast resources in your
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

## Using the Forecast

console

To access the Amazon Forecast console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Forecast resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the Forecast console, also
attach the following AWS managed policy to the entities. For more information, see
[Adding Permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_:

```
AWSForecastFullAccess
```

The following policy grants full access to all Amazon Forecast actions when using the
console:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "forecast:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "forecast.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Allow users

to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## AWS Managed (Predefined)

Policies for Amazon Forecast

AWS addresses many common use cases by providing standalone IAM policies that
are created and administered by AWS. These AWS managed policies grant necessary
permissions for common use cases so that you can avoid having to investigate which
permissions are needed. For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your account,
are specific to Amazon Forecast:

- **AmazonForecastFullAccess** – Grants
  full access to Amazon Forecast resources and all of the supported
  operations.

You can review these permissions policies by signing in to the IAM console and
searching for them.

You can also create your own custom IAM policies to allow permissions for
Amazon Forecast actions and resources. You can attach these custom policies to the IAM
users or groups that require them.

## Customer Managed Policy

Examples

In this section, you can find example user policies that grant permissions for
various Amazon Forecast actions. These policies work when you are using the AWS SDKs or
the AWS CLI. When you are using the console, see [Using the Forecast
console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console").

###### Examples

- [Example 1: Grant Account
  Administrator Permissions](#example-managed-policy-full-admin "#example-managed-policy-full-admin")
- [Example 2: Allow All
  Amazon Forecast and IAM PassRole Actions](#example-managed-policy-all-actions "#example-managed-policy-all-actions")
- [Example 3: Allow All
  Amazon Forecast actions while limiting IAM PassRole Actions](#example-managed-policy-limit-passrole "#example-managed-policy-limit-passrole")
- [Example 4:
  Action-based Policy: Amazon Forecast Read-Only Access](#example-managed-policy-read-only-access "#example-managed-policy-read-only-access")
- [Example 5: Allow all Amazon Forecast Actions with Pass Role and KMS Actions](#example-managed-policy-allow-all-forecast-actions "#example-managed-policy-allow-all-forecast-actions")

### Example 1: Grant Account

Administrator Permissions

After you set up an account (see [Sign Up for AWS](aws-forecast-set-up-aws-account.md "aws-forecast-set-up-aws-account.md")), you create an
administrator user to manage your account. The administrator user can create
users and manage their permissions.

To grant the administrator user all of the permissions available for your
account, attach the following permissions policy to that user:

### Example 2: Allow All

Amazon Forecast and IAM PassRole Actions

You might choose to create a user who has permissions for all Amazon Forecast
actions but not for any of your other services (think of this user as a
service-specific administrator). Attach the following permissions policy to this
user:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "forecast:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "forecast.amazonaws.com"
 }
 }
 }
 ]
}`

```

### Example 3: Allow All

Amazon Forecast actions while limiting IAM PassRole Actions

You might choose to create a user who has permissions for all Amazon Forecast
actions while limiting their IAM PassRole actions. Attach the following
permissions policy to this user:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "forecast:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/EXAMPLE_ROLE_TO_ALLOW_TO_PASS",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "forecast.amazonaws.com"
 }
 }
 }
 ]
}`

```

### Example 4:

Action-based Policy: Amazon Forecast Read-Only Access

The following policy grants permissions to Amazon Forecast actions that allow a user
to list and describe resources:

### Example 5: Allow all Amazon Forecast Actions with Pass Role and KMS Actions

You can create a user who has permissions for all Amazon Forecast actions, but does not have permissions for any other services, using a cross account Customer Managed Key for Encryption in Amazon Forecast. For more information, see [AWS Cross Account Key policy](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the AWS Key Management Service Developer Guide.
