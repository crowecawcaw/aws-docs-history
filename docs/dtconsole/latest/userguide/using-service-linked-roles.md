# Using service-linked roles for

AWS CodeStar Notifications

AWS CodeStar Notifications uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role
that is linked directly to AWS CodeStar Notifications. Service-linked roles are predefined by
AWS CodeStar Notifications and include all the permissions that the service requires to call other
AWS services on your behalf. This role is created for you the first time you create a
notification rule. You don't have to create the role.

A service-linked role makes setting up AWS CodeStar Notifications easier because you don’t have to add
permissions manually. AWS CodeStar Notifications defines the permissions of its service-linked roles, and
unless defined otherwise, only AWS CodeStar Notifications can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy cannot be
attached to any other IAM entity.

To delete a service-linked role, you must first delete its related resources. This
protects your AWS CodeStar Notifications resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md").

## Service-linked role permissions for

AWS CodeStar Notifications

AWS CodeStar Notifications uses the AWSServiceRoleForCodeStarNotifications service-linked role to retrieve information about
events that occur in your toolchain and send notifications to the targets you specify.

The AWSServiceRoleForCodeStarNotifications service-linked role trusts the following services to assume the
role:

- `codestar-notifications.amazonaws.com`

The role permissions policy allows AWS CodeStar Notifications to complete the following actions on
the specified resources:

- Action: `PutRule` on
  `CloudWatch Event rules that are named awscodestar-notifications-*`
- Action: `DescribeRule` on
  `CloudWatch Event rules that are named awscodestar-notifications-*`
- Action: `PutTargets` on
  `CloudWatch Event rules that are named awscodestar-notifications-*`
- Action: `CreateTopic` to `create Amazon SNS topics for use with
AWS CodeStar Notifications with the prefix CodeStarNotifications-`
- Action: `GetCommentsForPullRequests` on `all comments on all
pull requests in all CodeCommit repositories in the AWS account`
- Action: `GetCommentsForComparedCommit` on `all comments on all
commits in all CodeCommit repositories in the AWS account`
- Action: `GetDifferences` on `all commits in all CodeCommit
repositories in the AWS account`
- Action: `GetCommentsForComparedCommit` on `all comments on all
commits in all CodeCommit repositories in the AWS account`
- Action: `GetDifferences` on `all commits in all CodeCommit
repositories in the AWS account`
- Action: `DescribeSlackChannelConfigurations` on `all AWS Chatbot
clients in the AWS account`
- Action: `UpdateSlackChannelConfiguration` on `all AWS Chatbot
clients in the AWS account`
- Action: `ListActionExecutions` on `all actions in all
pipelines in the AWS account`
- Action: `GetFile` on `all files in all CodeCommit repositories in
the AWS account unless otherwise tagged`

You can see these actions in the policy statement for the AWSServiceRoleForCodeStarNotifications service-linked
role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "events:PutTargets",
 "events:PutRule",
 "events:DescribeRule"
 ],
 "Resource": "arn:aws:events:*:*:rule/awscodestarnotifications-*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "sns:CreateTopic"
 ],
 "Resource": "arn:aws:sns:*:*:CodeStarNotifications-*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "codecommit:GetCommentsForPullRequest",
 "codecommit:GetCommentsForComparedCommit",
 "codecommit:GetDifferences",
 "chatbot:DescribeSlackChannelConfigurations",
 "chatbot:UpdateSlackChannelConfiguration",
 "codepipeline:ListActionExecutions"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "codecommit:GetFile"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:ResourceTag/ExcludeFileContentFromNotifications": "true"
 }
 },
 "Effect": "Allow"
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for AWS CodeStar Notifications

You don't need to manually create a service-linked role. You can use the Developer Tools console or the CreateNotificationRule API from the AWS CLI or SDKs to create a notification rule. You can also directly call the API. No matter which method you use, the service-linked role is created for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. You can use the Developer Tools console or the CreateNotificationRule API from the AWS CLI or SDKs to create a notification rule. You can also directly call the API. No matter which method you use, the service-linked role is created for you.

## Editing a service-linked role for AWS CodeStar Notifications

After you create a service-linked role, you cannot change its name because various
entities might reference the role. However, you can use IAM to edit the role
description. For more information, see [Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for AWS CodeStar Notifications

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete the role. That way, you don’t have an unused entity that is
not actively monitored or maintained. You must clean up the resources for your
service-linked role before you can delete it. For AWS CodeStar Notifications, this means deleting all
notification rules that use the service role in your AWS account.

###### Note

If the AWS CodeStar Notifications service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few minutes and
try the operation again.

###### To delete AWS CodeStar Notifications resources used by AWSServiceRoleForCodeStarNotifications

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/ "https://console.aws.amazon.com/codesuite/settings/notifications/").

###### Note

Notification rules apply to the AWS Region where they are created. If
you have notification rules in more than one AWS Region, use the Region
selector to change the AWS Region. 2. Choose all notification rules that appear in the list, and then choose
**Delete**. 3. Repeat these steps in all AWS Regions where you created notification
rules.

**To **use IAM** to delete the
service-linked role**

Use the IAM console, AWS CLI, or AWS Identity and Access Management API to delete the AWSServiceRoleForCodeStarNotifications service-linked
role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported regions for AWS CodeStar Notifications service-linked

roles

AWS CodeStar Notifications supports using service-linked roles in all of the AWS Regions where the
service is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") and [AWS CodeStar Notifications](../../../general/latest/gr/codestar_notifications.md "../../../general/latest/gr/codestar_notifications.md").
