# Identity-based policy

examples for AWS CodeArtifact

By default, users and roles don't have permission to create or modify CodeArtifact
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by CodeArtifact, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS CodeArtifact](../../../service-authorization/latest/reference/list_awscodeartifact.md "../../../service-authorization/latest/reference/list_awscodeartifact.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the CodeArtifact
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [AWS managed (predefined) policies for
  AWS CodeArtifact](#managed-policies "#managed-policies")
- [Allow a user to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Allow a user to get information about repositories and domains](#security_iam_id-based-policy-examples-repos-and-domains "#security_iam_id-based-policy-examples-repos-and-domains")
- [Allow a user to get information about specific domains](#security_iam_id-based-policy-examples-specific-domains "#security_iam_id-based-policy-examples-specific-domains")
- [Allow a user to get information about specific repositories](#security_iam_id-based-policy-examples-specific-repos "#security_iam_id-based-policy-examples-specific-repos")
- [Limit authorization token duration](#limit-token-duration "#limit-token-duration")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete CodeArtifact resources in your
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

## Using the CodeArtifact

console

To access the AWS CodeArtifact console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the CodeArtifact resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the CodeArtifact console, also attach the
`AWSCodeArtifactAdminAccess` or `AWSCodeArtifactReadOnlyAccess` AWS
managed policy to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

## AWS managed (predefined) policies for

AWS CodeArtifact

AWS addresses many common use cases by providing standalone IAM policies that
are created and administered by AWS. These AWS managed policies grant necessary
permissions for common use cases so you can avoid having to investigate what
permissions are needed. For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

The following AWS managed policies, which you can attach to users in your
account, are specific to AWS CodeArtifact.

- `AWSCodeArtifactAdminAccess` – Provides full
  access to CodeArtifact including permissions to administrate CodeArtifact domains.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeartifact:*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "sts:GetServiceBearerToken",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sts:AWSServiceName": "codeartifact.amazonaws.com"
 }
 }
 }
 ]
}`

```

- `AWSCodeArtifactReadOnlyAccess` – Provides
  read-only access to CodeArtifact.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeartifact:Describe*",
 "codeartifact:Get*",
 "codeartifact:List*",
 "codeartifact:ReadFromRepository"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "sts:GetServiceBearerToken",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sts:AWSServiceName": "codeartifact.amazonaws.com"
 }
 }
 }
 ]
}`

```

To create and manage CodeArtifact service roles, you must also attach the AWS managed
policy named `IAMFullAccess`.

You can also create your own custom IAM policies to allow permissions for CodeArtifact
actions and resources. You can attach these custom policies to the IAM users or
groups that require those permissions.

## Allow a user to view their own permissions

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

## Allow a user to get information about repositories and domains

The following policy allows an IAM user or role to list and describe any type of CodeArtifact resource, including domains,
repositories, packages, and assets. The policy also includes the `codeArtifact:ReadFromRepository` permission,
which allows the principal to fetch packages from a CodeArtifact repository.
It does not allow creating new domains or repositories and does not allow publishing new packages.

The `codeartifact:GetAuthorizationToken` and `sts:GetServiceBearerToken` permissions are required to call the
`GetAuthorizationToken` API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codeartifact:List*",
 "codeartifact:Describe*",
 "codeartifact:Get*",
 "codeartifact:Read*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "sts:GetServiceBearerToken",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sts:AWSServiceName": "codeartifact.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Allow a user to get information about specific domains

The following shows an example of a permissions policy that allows a user to list
domains only in the `us-east-2` region for account
`123456789012` for any domain that starts with the name
`my`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codeartifact:ListDomains",
 "Resource": "arn:aws:codeartifact:us-east-2:`111122223333`:domain/my*"
 }
 ]
}`

```

## Allow a user to get information about specific repositories

The following shows an example of a permissions policy that allows a user to get
information about repositories that end with `test`, including information about the packages in them. The
user will not be able to publish, create, or delete resources.

The `codeartifact:GetAuthorizationToken` and `sts:GetServiceBearerToken` permissions are required to call the
`GetAuthorizationToken` API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codeartifact:List*",
 "codeartifact:Describe*",
 "codeartifact:Get*",
 "codeartifact:Read*"
 ],
 "Resource": "arn:aws:codeartifact:*:*:repository/*/*test"
 },
 {
 "Effect": "Allow",
 "Action": [
 "codeartifact:List*",
 "codeartifact:Describe*"
 ],
 "Resource": "arn:aws:codeartifact:*:*:package/*/*test/*/*/*"
 },
 {
 "Effect": "Allow",
 "Action": "sts:GetServiceBearerToken",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sts:AWSServiceName": "codeartifact.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "codeartifact:GetAuthorizationToken",
 "Resource": "*"
 }
 ]
}`

```

## Limit authorization token duration

Users must authenticate to CodeArtifact with authorization tokens to publish or consume package versions.
Authorization tokens are valid only during their configured lifetime. Tokens have a default lifetime of 12 hours.
For more information on authorization tokens, see
[AWS CodeArtifact authentication and tokens](tokens-authentication.md "tokens-authentication.md").

When fetching a token, users can configure the lifetime of the token. Valid values for the lifetime of an authorization token are `0`,
and any number between `900` (15 minutes) and `43200` (12 hours). A value of `0` will create a
token with a duration equal to the user's role's temporary credentials.

Administrators can limit the valid values for the lifetime of an authorization token
by using the `sts:DurationSeconds` condition key in the permissions policy attached to
the user or group. If the user attempts to create an authorization token with a lifetime outside of the valid values,
the token creation will fail.

The following example policies limit the possible durations of an authorization token created by CodeArtifact users.

**Example policy: Limit token lifetime to exactly 12 hours (43200 seconds)**

With this policy, users will only be able to create authorization tokens with a lifetime of 12 hours.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codeartifact:*",
 "Resource": "*"
 },
 {
 "Sid": "sts",
 "Effect": "Allow",
 "Action": "sts:GetServiceBearerToken",
 "Resource": "*",
 "Condition": {
 "NumericEquals": {
 "sts:DurationSeconds": 43200
 },
 "StringEquals": {
 "sts:AWSServiceName": "codeartifact.amazonaws.com"
 }
 }
 }
 ]
}`

```

**Example policy: Limit token lifetime between 15 minutes and 1 hour, or equal to the user's temporary credentials period**

With this policy, users will be able to create tokens that are valid between 15 minutes and 1 hour. Users will also be able to create a
token that lasts the duration of their role's temporary credentials by specifying `0` for `--durationSeconds`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codeartifact:*",
 "Resource": "*"
 },
 {
 "Sid": "sts",
 "Effect": "Allow",
 "Action": "sts:GetServiceBearerToken",
 "Resource": "*",
 "Condition": {
 "NumericLessThanEquals": {
 "sts:DurationSeconds": 3600
 },
 "StringEquals": {
 "sts:AWSServiceName": "codeartifact.amazonaws.com"
 }
 }
 }
 ]
}`

```
