# Permissions

and examples for AWS CodeStar Notifications

The following policy statements and examples can help you manage AWS CodeStar Notifications.

## Permissions related to notifications

in full access managed policies

The **AWSCodeCommitFullAccess**,
**AWSCodeBuildAdminAccess**,
**AWSCodeDeployFullAccess**, and
**AWSCodePipeline_FullAccess** managed policies include the
following statements to allow full access to notifications in the Developer Tools console.
Users with one of these managed policies applied can also create and manage
Amazon SNS topics for notifications, subscribe and unsubscribe users to topics, and
list topics to choose as targets for notification rules.

###### Note

In the managed policy, the condition key
`codestar-notifications:NotificationsForResource` will have a
value specific to the resource type for the service. For example, in the
full access policy for CodeCommit, the value is
`arn:aws:codecommit:*`.

```
    {
        "Sid": "CodeStarNotificationsReadWriteAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:CreateNotificationRule",
            "codestar-notifications:DescribeNotificationRule",
            "codestar-notifications:UpdateNotificationRule",
            "codestar-notifications:DeleteNotificationRule",
            "codestar-notifications:Subscribe",
            "codestar-notifications:Unsubscribe"
        ],
        "Resource": "*",
        "Condition" : {
            "StringLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:<vendor-code>:*"}
        }
    },
    {
        "Sid": "CodeStarNotificationsListAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:ListNotificationRules",
            "codestar-notifications:ListTargets",
            "codestar-notifications:ListTagsforResource",
            "codestar-notifications:ListEventTypes"
        ],
        "Resource": "*"
    },
    {
        "Sid": "CodeStarNotificationsSNSTopicCreateAccess",
        "Effect": "Allow",
        "Action": [
            "sns:CreateTopic",
            "sns:SetTopicAttributes"
        ],
        "Resource": "arn:aws:sns:*:*:codestar-notifications*"
    },
    {
        "Sid": "SNSTopicListAccess",
        "Effect": "Allow",
        "Action": [
            "sns:ListTopics"
        ],
        "Resource": "*"
    },
    {
        "Sid": "CodeStarNotificationsChatbotAccess",
        "Effect": "Allow",
        "Action": [
            "chatbot:DescribeSlackChannelConfigurations",
            "chatbot:ListMicrosoftTeamsChannelConfigurations"
          ],
       "Resource": "*"
    }
```

## Permissions related to notifications in

read-only managed policies

The **AWSCodeCommitReadOnlyAccess**,
**AWSCodeBuildReadOnlyAccess**,
**AWSCodeDeployReadOnlyAccess**, and **AWSCodePipeline_ReadOnlyAccess** managed policies include the
following statements to allow read-only access to notifications. For example,
they can view notifications for resources in the Developer Tools console, but cannot create,
manage, or subscribe to them.

###### Note

In the managed policy, the condition key
`codestar-notifications:NotificationsForResource` will have a
value specific to the resource type for the service. For example, in the
full access policy for CodeCommit, the value is
`arn:aws:codecommit:*`.

```
   {
        "Sid": "CodeStarNotificationsPowerUserAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:DescribeNotificationRule"
        ],
        "Resource": "*",
        "Condition" : {
            "StringLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:<vendor-code>:*"}
        }
    },
    {
        "Sid": "CodeStarNotificationsListAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:ListNotificationRules",
            "codestar-notifications:ListEventTypes",
            "codestar-notifications:ListTargets"
        ],
        "Resource": "*"
    }
```

## Permissions related to notifications

in other managed policies

The **AWSCodeCommitPowerUser**,
**AWSCodeBuildDeveloperAccess**, and **AWSCodeBuildDeveloperAccess** managed policies include the
following statements to allow developers with one of these managed policies
applied to create, edit, and subscribe to notifications. They cannot delete
notification rules or manage tags for resources.

###### Note

In the managed policy, the condition key
`codestar-notifications:NotificationsForResource` will have a
value specific to the resource type for the service. For example, in the
full access policy for CodeCommit, the value is
`arn:aws:codecommit:*`.

```
    {
        "Sid": "CodeStarNotificationsReadWriteAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:CreateNotificationRule",
            "codestar-notifications:DescribeNotificationRule",
            "codestar-notifications:UpdateNotificationRule",
            "codestar-notifications:Subscribe",
            "codestar-notifications:Unsubscribe"
        ],
        "Resource": "*",
        "Condition" : {
            "StringLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:<vendor-code>:*"}
        }
    },
    {
        "Sid": "CodeStarNotificationsListAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:ListNotificationRules",
            "codestar-notifications:ListTargets",
            "codestar-notifications:ListTagsforResource",
            "codestar-notifications:ListEventTypes"
        ],
        "Resource": "*"
    },
    {
        "Sid": "SNSTopicListAccess",
        "Effect": "Allow",
        "Action": [
            "sns:ListTopics"
        ],
        "Resource": "*"
    },
    {
        "Sid": "CodeStarNotificationsChatbotAccess",
        "Effect": "Allow",
        "Action": [
            "chatbot:DescribeSlackChannelConfigurations",
            "chatbot:ListMicrosoftTeamsChannelConfigurations"
          ],
       "Resource": "*"
    }
```

## Example: An administrator-level policy for managing AWS CodeStar Notifications

In this example, you want to grant an IAM user in your AWS account full
access to AWS CodeStar Notifications so that the user can review details of notification rules and
list notification rules, targets, and event types. You also want to allow the
user to add, update, and delete notification rules. This is a full access
policy, equivalent to the notification permissions included as part of the
**AWSCodeBuildAdminAccess**,
**AWSCodeCommitFullAccess**,
**AWSCodeDeployFullAccess**, and
**AWSCodePipeline_FullAccess** managed policies. Like those
managed policies, you should only attach this kind of policy statement to IAM
users, groups, or roles that require full administrative access to notifications
and notification rules across your AWS account.

###### Note

This policy contains allows `CreateNotificationRule`. Any user
with this policy applied to their IAM user or role will be able to create
notification rules for any and all resource types supported by AWS CodeStar Notifications in the
AWS account, even if that user does not have access to those resources
themselves. For example, a user with this policy could create a notification
rule for a CodeCommit repository without having permissions to access CodeCommit
itself.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSCodeStarNotificationsFullAccess",
 "Effect": "Allow",
 "Action": [
 "codestar-notifications:CreateNotificationRule",
 "codestar-notifications:DeleteNotificationRule",
 "codestar-notifications:DescribeNotificationRule",
 "codestar-notifications:ListNotificationRules",
 "codestar-notifications:UpdateNotificationRule",
 "codestar-notifications:Subscribe",
 "codestar-notifications:Unsubscribe",
 "codestar-notifications:DeleteTarget",
 "codestar-notifications:ListTargets",
 "codestar-notifications:ListTagsforResource",
 "codestar-notifications:TagResource",
 "codestar-notifications:UntagResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: A contributor-level policy for using AWS CodeStar Notifications

In this example, you want to grant access to the day-to-day usage of AWS CodeStar Notifications,
such as creating and subscribing to notifications, but not to more destructive
actions, such as deleting notification rules or targets. This is the equivalent
to the access provided in the **AWSCodeBuildDeveloperAccess**,
**AWSCodeDeployDeveloperAccess**, and
**AWSCodeCommitPowerUser** managed policies.

###### Note

This policy contains allows `CreateNotificationRule`. Any user
with this policy applied to their IAM user or role will be able to create
notification rules for any and all resource types supported by AWS CodeStar Notifications in the
AWS account, even if that user does not have access to those resources
themselves. For example, a user with this policy could create a notification
rule for a CodeCommit repository without having permissions to access CodeCommit
itself.

```
{
    "Version": "2012-10-17",
    "Sid": "AWSCodeStarNotificationsPowerUserAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:CreateNotificationRule",
            "codestar-notifications:DescribeNotificationRule",
            "codestar-notifications:ListNotificationRules",
            "codestar-notifications:UpdateNotificationRule",
            "codestar-notifications:Subscribe",
            "codestar-notifications:Unsubscribe",
            "codestar-notifications:ListTargets",
            "codestar-notifications:ListTagsforResource"
        ],
        "Resource": "*"
        }
    ]
}
```

## Example: A read-only-level policy for using AWS CodeStar Notifications

In this example, you want to grant an IAM user in your account read-only
access to the notification rules, targets, and event types in your AWS
account. This example shows how you might create a policy that allows viewing
these items. This is the equivalent to the permissions included as part of the
**AWSCodeBuildReadOnlyAccess**,
**AWSCodeCommitReadOnly**, and
**AWSCodePipeline_ReadOnlyAccess** managed policies.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "CodeNotificationforReadOnly",
 "Statement": [
 {
 "Sid": "ReadsAccess",
 "Effect": "Allow",
 "Action": [
 "codestar-notifications:DescribeNotificationRule",
 "codestar-notifications:ListNotificationRules",
 "codestar-notifications:ListTargets",
 "codestar-notifications:ListEventTypes"
 ],
 "Resource": "*"
 }
 ]
}`

```
