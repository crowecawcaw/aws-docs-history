# Identity-based policy examples for

Amazon Q Business

By default, users and roles don't have permission to create or modify Amazon Q
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon Q, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for Amazon Q Business](../../../IAM/latest/UserGuide/list_your_service.md "../../../IAM/latest/UserGuide/list_your_service.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon Q console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Allow a user to
  converse with Amazon Q Business](#security_iam_id-based-policy-examples-application-1 "#security_iam_id-based-policy-examples-application-1")
- [Allow an admin to
  manage plugins in an application](#security_iam_id-based-policy-examples-plugins-1 "#security_iam_id-based-policy-examples-plugins-1")
- [Allow an admin to
  manage a specific plugin](#security_iam_id-based-policy-examples-plugins-2 "#security_iam_id-based-policy-examples-plugins-2")
- [Tag-based policy examples](#examples-tagging "#examples-tagging")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Q resources in your
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

## Using the Amazon Q console

To access the Amazon Q Business console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon Q resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the Amazon Q Business console,
also attach the
[`ReadOnlyAcess`AWS
managed policy](../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md") to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

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

## Allow a user to

converse with Amazon Q Business

This example allows a user to start conversations with Amazon Q Business, view
past conversations, and delete their conversation history for a specific Amazon Q Business application. The IAM context key
`qbusiness:userId` is used to restrict permissions to a
specific user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "qbusiness:ChatSync",
 "qbusiness:ListMessages",
 "qbusiness:ListConversations",
 "qbusiness:GetWebExperience",
 "qbusiness:DeleteConversation",
 "qbusiness:GetMedia"
 ],
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 ],
 "Effect": "Allow",
 "Sid": "QBusinessChatPermissions"
 }
 ]
}`

```

## Allow an admin to

manage plugins in an application

This example allows an Amazon Q Business admin to manage plugins in a chat
application.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "qbusiness:CreatePlugin",
 "qbusiness:ListPlugins",
 "qbusiness:GetPlugin",
 "qbusiness:UpdatePlugin",
 "qbusiness:DeletePlugin"
 ],
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 ],
 "Effect": "Allow",
 "Sid": "QBusinessListPermissions"
 }
 ]
}`

```

## Allow an admin to

manage a specific plugin

This example allows an Amazon Q Business admin to manage a specific
plugin.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "qbusiness:GetPlugin",
 "qbusiness:UpdatePlugin",
 "qbusiness:DeletePlugin"
 ],
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/plugin/`plugin-id`"
 ],
 "Effect": "Allow",
 "Sid": "QBusinessGetPermissions"
 }
 ]
}`

```

## Tag-based policy examples

Tag-based policies are JSON policy documents that specify the actions that a
principal can perform on tagged resources.

### Example: Use a tag to access a

resource

This example policy grants a user or role in your AWS account permission to use
the `ChatSync` operation with any resource tagged with the key
`department` and the value
`finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "qbusiness:ChatSync"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": "finance"
 }
 },
 "Sid": "QBusinessChatPermissions"
 }
 ]
}`

```

### Example: Use a tag to activate

operations

This example policy grants a user or role in your AWS account permission to use
any Amazon Q Business operation except the `TagResource` operation
with any resource tagged with the key `department` and the value
`finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessFullAccessPermissions",
 "Effect": "Allow",
 "Action": "qbusiness:*",
 "Resource": "*"
 },
 {
 "Sid": "QBusinessPermissions",
 "Effect": "Deny",
 "Action": [
 "qbusiness:TagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": "finance"
 }
 }
 }
 ]
}`

```

### Example: Use a tag to restrict

access to an operation

This example policy restricts access for a user or role in your AWS account to
use the `ChatSync` operation unless the user provides the
`department` tag and it has the allowed values
`finance` and `IT`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "qbusiness:ChatSync",
 "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "Effect": "Allow",
 "Sid": "QBusinessChatSyncPermissions"
 },
 {
 "Action": "qbusiness:ChatSync",
 "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "Effect": "Deny",
 "Condition": {
 "Null": {
 "aws:ResourceTag/department": "true"
 }
 },
 "Sid": "DenyChatSyncWithoutDepartmentTag"
 },
 {
 "Action": "qbusiness:ChatSync",
 "Resource": "*",
 "Effect": "Deny",
 "Condition": {
 "ForAnyValue:StringNotEquals": {
 "aws:ResourceTag/department": [
 "finance",
 "IT"
 ]
 }
 },
 "Sid": "DenyChatSyncForUnauthorizedDepts"
 }
 ]
}`

```
