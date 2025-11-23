# Identity-based policy examples for

Security Lake

By default, users and roles don't have permission to create or modify Security Lake
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Security Lake, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Security Lake](../../../IAM/latest/UserGuide/list_amazonsecuritylake.md "../../../IAM/latest/UserGuide/list_amazonsecuritylake.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Security Lake
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Example:
  Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Example: Allow the
  organization management account to designate and remove a delegated
  administrator](#security_iam_id-based-policy-examples-orgs "#security_iam_id-based-policy-examples-orgs")
- [Example:
  Allow users to review subscribers based on tags](#security_iam_id-based-policy-examples-review-subscribers-tags "#security_iam_id-based-policy-examples-review-subscribers-tags")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Security Lake resources in your
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

## Using the Security Lake

console

To access the Amazon Security Lake console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Security Lake resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can use the Security Lake console, create IAM policies that provide them
with console access. For more information, see [IAM identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the
_IAM User Guide_.

If you create a policy that allows users or roles to use the Security Lake console, ensure that the policy includes the
appropriate actions for the resources that those users or roles need to access on the console. Otherwise, they won't
be able to navigate to or display details about those resources on the console.

For example, to add a custom source by using the console, a user must be allowed to
perform these actions:

- `glue:CreateCrawler`
- `glue:CreateDatabase`
- `glue:CreateTable`
- `glue:StartCrawlerSchedule`
- `iam:GetRole`
- `iam:PutRolePolicy`
- `iam:DeleteRolePolicy`
- `iam:PassRole`
- `lakeformation:RegisterResource`
- `lakeformation:GrantPermissions`
- `s3:ListBucket`
- `s3:PutObject`

## Example:

Allow users to view their own permissions

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

## Example: Allow the

organization management account to designate and remove a delegated
administrator

This example shows how you might create a policy that allows a user of an
AWS Organizations management account to designate and remove the delegated Security Lake administrator for their organization.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "securitylake:RegisterDataLakeDelegatedAdministrator",
 "securitylake:DeregisterDataLakeDelegatedAdministrator"
 ],
 "Resource": "arn:aws:securitylake:*:*:*"
 }
 ]
}`

```

## Example:

Allow users to review subscribers based on tags

In identity-based policies, you can use conditions to control access to Security Lake
resources based on tags. This example shows how you might create a policy that allows a
user to review subscribers by using the Security Lake console or the Security Lake API. However,
permission is granted only if the value for the `Owner` tag for a subscriber
is the user's username.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReviewSubscriberDetailsIfOwner",
 "Effect": "Allow",
 "Action": "securitylake:GetSubscriber",
 "Resource": "arn:aws:securitylake:*:*:subscriber/*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 },
 {
 "Sid": "ListSubscribersIfOwner",
 "Effect": "Allow",
 "Action": "securitylake:ListSubscribers",
 "Resource": "*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

In this example, if a user who has the username `richard-roe` attempts to
review the details of individual subscribers, a subscriber must be tagged
`Owner=richard-roe` or `owner=richard-roe`. Otherwise, the user
is denied access. The condition tag key `Owner` matches both
`Owner` and `owner` because condition key names are not case
sensitive. For more information about using condition keys, see [IAM JSON policy
elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_. For information about tagging Security Lake resources, see
[Tagging Security Lake resources](tagging-resources.md "tagging-resources.md").
