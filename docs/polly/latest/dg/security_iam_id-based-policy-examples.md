# Identity-based policy

examples for Amazon Polly

By default, users and roles don't have permission to create or modify Amazon Polly
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon Polly, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Polly](../../../service-authorization/latest/reference/list_amazonpolly.md "../../../service-authorization/latest/reference/list_amazonpolly.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon Polly
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [AWS managed (predefined) policies
  for Amazon Polly](#access-policy-aws-managed-policies "#access-policy-aws-managed-policies")
- [Customer-managed policy
  examples](#access-policy-customer-managed-examples "#access-policy-customer-managed-examples")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Polly resources in your
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

## Using the Amazon Polly

console

To access the Amazon Polly console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon Polly resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the Amazon Polly console, also attach the
Amazon Polly `ConsoleAccess` or `ReadOnly` AWS managed policy to
the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

To use the Amazon Polly console, grant permissions to all the Amazon Polly APIs. There are no
additional permissions needed. To get full console functionality you can use following
policy:.

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

## AWS managed (predefined) policies

for Amazon Polly

AWS addresses many common use cases by providing standalone IAM policies that are
created and administered by AWS. These AWS managed policies grant necessary
permissions for common use cases so that you can avoid having to investigate what
permissions are needed. For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your account,
are specific to Amazon Polly:

- **AmazonPollyReadOnlyAccess** – Grants
  read-only access to resources, allows listing lexicons, fetching lexicons, listing
  available voices and synthesizing speech (including, applying lexicons to the
  synthesized speech).
- **AmazonPollyFullAccess** –
  Grants full access to resources and all the supported operations.

###### Note

You can review these permissions policies by signing in to the IAM console
and searching for specific policies there.

You can also create your own custom IAM policies to allow permissions for
Amazon Polly actions and resources. You can attach these custom policies to the
IAM users or groups that require those permissions.

## Customer-managed policy

examples

In this section, you can find example user policies that grant permissions for
various Amazon Polly actions. These policies work when you're using AWS SDKs or the AWS CLI.
When you're using the console, grant permissions to all the Amazon Polly APIs.

###### Note

All examples use the us-east-2 Region and contain fictitious account
IDs.

###### Examples

- [Example 1: Allow All Amazon Polly Actions](#example-managed-policy-service-admin "#example-managed-policy-service-admin")
- [Example 2: Allow all Amazon Polly
  actions except DeleteLexicon](#example-managed-policy-full-permissions-no-delete "#example-managed-policy-full-permissions-no-delete")
- [Example 3: Allow DeleteLexicon](#example-managed-policy-delete-all-regions "#example-managed-policy-delete-all-regions")
- [Example 4: Allow Delete Lexicon in a specified Region](#example-managed-policy-delete-one-region "#example-managed-policy-delete-one-region")
- [Example 5: Allow DeleteLexicon for specified Lexicon](#example-managed-policy-delete-specific-lexicon "#example-managed-policy-delete-specific-lexicon")

### Example 1: Allow All Amazon Polly Actions

After you sign up (see [Getting started with Amazon Polly](getting-started.md "getting-started.md")) create an administrator user to manage your
account, including creating users and managing their permissions.

You might create a user who has permissions for all Amazon Polly actions. Think of
this user as a service-specific administrator for working with Amazon Polly. You can
attach the following permissions policy to this user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AllowAllPollyActions",
 "Effect": "Allow",
 "Action": [
 "polly:*"],
 "Resource": "*"
 }
 ]
}`

```

### Example 2: Allow all Amazon Polly

actions except DeleteLexicon

The following permissions policy grants the user permissions to perform all
actions except `DeleteLexicon`, with the permissions for delete explicitly
denied in all Regions.

### Example 3: Allow DeleteLexicon

The following permissions policy grants the user permissions to delete any
lexicon that you own regardless of the project or Region in which it is located.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AllowDeleteLexicon",
 "Effect": "Allow",
 "Action": [
 "polly:DeleteLexicon"],
 "Resource": "*"
 }
 ]
}`

```

### Example 4: Allow Delete Lexicon in a specified Region

The following permissions policy grants the user permissions to delete any
lexicon in any project that you own that is located in a single Region (in this case,
us-east-2).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AllowDeleteSpecifiedRegion",
 "Effect": "Allow",
 "Action": [
 "polly:DeleteLexicon"],
 "Resource": "arn:aws:polly:us-east-2:`111122223333`:lexicon/*"
 }
 ]
}`

```

### Example 5: Allow DeleteLexicon for specified Lexicon

The following permissions policy grants the user permissions to delete a
specific lexicon that you own (in this case, myLexicon) in a specific Region (in this
case, us-east-2).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AllowDeleteForSpecifiedLexicon",
 "Effect": "Allow",
 "Action": [
 "polly:DeleteLexicon"],
 "Resource": "arn:aws:polly:us-east-2:`111122223333`:lexicon/myLexicon"
 }
 ]
}`

```
