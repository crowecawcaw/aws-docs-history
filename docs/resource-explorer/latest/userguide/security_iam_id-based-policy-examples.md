AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# AWS Resource Explorer identity-based policy

examples

By default, AWS Identity and Access Management (IAM) principals, such as roles, groups, and users, don't have
permission to create or modify Resource Explorer resources. They also can't perform tasks using the
AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS API. An IAM administrator must create IAM
policies that grant principals permission to perform specific API operations on the
specified resources they need. Then, the administrator must assign those policies to the
IAM principals that require those permissions.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:

      + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
      + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

  To learn how to create an IAM identity-based policy using these example JSON policy
  documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
  _IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Resource Explorer
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Granting access to a
  view based on tags](#security_iam_id-based-policy-examples-abac-views "#security_iam_id-based-policy-examples-abac-views")
- [Granting access
  to create a view based on tags](#security_iam_id-based-policy-examples-abac-createview "#security_iam_id-based-policy-examples-abac-createview")
- [Allow
  principals to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Resource Explorer resources in your
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

## Using the Resource Explorer

console

For principals to search in the AWS Resource Explorer console, they must have a minimum set of
permissions. If you don't create an identity-based policy with the minimum required
permissions, then the Resource Explorer console doesn't function as intended for principals in the
account.

You can use the AWS managed policy named `AWSResourceExplorerReadOnlyAccess` to
grant the ability to use the Resource Explorer console to search using any view in the account. To
grant permissions to search with only a single view, see [Granting access to Resource Explorer views for
search](configure-views-grant-access.md "configure-views-grant-access.md"), and the examples in the following two sections.

You don't need to allow minimum console permissions for principals that are making
calls only to the AWS CLI or the AWS API. Instead, you can choose to grant access to
only those actions that match the API operations that the principals need to
perform.

## Granting access to a

view based on tags

In this example, you want to grant access to a Resource Explorer view in your AWS account to
principals in the account. To do this you assign IAM identity-based policies to the
principals that you want to be able to search in Resource Explorer. The following example IAM
policy grants access to any request where the `Search-Group` tag attached to
the calling principal exactly matches the value for that same tag attached to the view
used in the request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "resource-explorer-2:GetView",
 "resource-explorer-2:Search"
 ],
 "Resource": "arn:aws:resource-explorer-2:*:*:view/*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/Search-Group": "${aws:PrincipalTag/Search-Group}"}
 }
 }
 ]
}`

```

You can assign this policy to the IAM principals in your account. If a principal
with the tag `Search-Group=A` attempts to search using a Resource Explorer view, the
view must also be tagged `Search-Group=A`. If it's not, then the principal is
denied access. The condition tag key `Search-Group` matches both
`Search-group` and `search-group` because condition key names
are not case-sensitive. For more information, see [IAM JSON Policy
Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.

###### Important

To see your resources in [Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md") results in the AWS Management Console,
principals must have both `GetView` and `Search` permissions
for the default view in the AWS Region that contains the aggregator index. The
simplest way to grant those permissions is to leave the default resource-based
permission that was attached to the view when you turned on Resource Explorer using Quick or
Advanced setup.

For this scenario, you could consider setting the default view to filter out
sensitive resources and then setting up additional views to which you grant
tag-based access as described in the previous example.

## Granting access

to create a view based on tags

In this example, you want to allow only principals that are tagged the same as the
index to be able to create views in the AWS Region that contains the index. To do
this, create identity-based permissions to allow the principals to search with
views.

Now you're ready to grant permissions to create a view. You can add the statements in
this example to the same permission policy that you use to grant `Search`
permissions to appropriate principals. The actions are allowed or denied based on the
tags attached to the principals calling the operations and index that the view is to be
associated with. The following example IAM policy denies any request to create a view
when the value of the `Allow-Create-View` tag attached to the caller's
principal doesn't exactly match the value for that same tag attached to the index in the
Region in which the view is created.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "resource-explorer-2:CreateView",
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {"aws:ResourceTag/Allow-Create-View": "${aws:PrincipalTag/Allow-Create-View}"}
 }
 }
 ]
}`

```

## Allow

principals to view their own permissions

JSON

```
`{
 "Version":"2012-10-17",
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
}`

```
