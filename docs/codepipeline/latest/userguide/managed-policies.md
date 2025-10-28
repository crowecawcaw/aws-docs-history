# AWS managed policies for AWS CodePipeline

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

###### Important

The AWS managed policies `AWSCodePipelineFullAccess` and
`AWSCodePipelineReadOnlyAccess` have been replaced. Use the
`AWSCodePipeline_FullAccess` and `AWSCodePipeline_ReadOnlyAccess` policies.

## AWS managed

policy: `AWSCodePipeline_FullAccess`

This is a policy that grants full access to CodePipeline. To view the JSON policy
document in the IAM console, see [AWSCodePipeline_FullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCodePipeline_FullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCodePipeline_FullAccess").

**Permissions details**

This policy includes the following permissions.

- `codepipeline` – Grants permissions to CodePipeline.
- `chatbot` – Grants permissions to allow principals to manage
  resources in Amazon Q Developer in chat applications.
- `cloudformation` – Grants permissions to allow principals to
  manage resource stacks in AWS CloudFormation.
- `cloudtrail` – Grants permissions to allow principals to
  manage logging resources in CloudTrail.
- `codebuild` – Grants permissions to allow principals to
  access build resources in CodeBuild.
- `codecommit` – Grants permissions to allow principals to
  access source resources in CodeCommit.
- `codedeploy` – Grants permissions to allow principals to
  access deployment resources in CodeDeploy.
- `codestar-notifications` – Grants permissions to allow
  principals to access resources in AWS CodeStar Notifications.
- `ec2` – Grants permissions to allow deployments in CodeCatalyst to
  manage elastic load balancing in Amazon EC2.
- `ecr` – Grants permissions to allow access to resources in
  Amazon ECR.
- `elasticbeanstalk` – Grants permissions to allow principals
  to access resources in Elastic Beanstalk.
- `iam` – Grants permissions to allow principals to manage
  roles and policies in IAM.
- `lambda` – Grants permissions to allow principals to manage
  resources in Lambda.
- `events` – Grants permissions to allow principals to manage
  resources in CloudWatch Events.
- `opsworks` – Grants permissions to allow principals to
  manage resources in AWS OpsWorks.
- `s3` – Grants permissions to allow principals to manage
  resources in Amazon S3.
- `sns` – Grants permissions to allow principals to manage
  notification resources in Amazon SNS.
- `states` – Grants permissions to allow principals to view
  state machines in AWS Step Functions. A state machine consists of a collection of states
  that manage tasks and transition between states.

For the policy, see [AWSCodePipeline_FullAccess](../../../aws-managed-policy/latest/reference/AWSCodePipeline_FullAccess.md "../../../aws-managed-policy/latest/reference/AWSCodePipeline_FullAccess.md").

## AWS managed

policy: `AWSCodePipeline_ReadOnlyAccess`

This is a policy that grants read-only access to CodePipeline. To view the JSON
policy document in the IAM console, see [AWSCodePipeline_ReadOnlyAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCodePipeline_ReadOnlyAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCodePipeline_ReadOnlyAccess").

**Permissions details**

This policy includes the following permissions.

- `codepipeline` – Grants permissions to actions in
  CodePipeline.
- `codestar-notifications` – Grants permissions to allow
  principals to access resources in AWS CodeStar Notifications.
- `s3` – Grants permissions to allow principals to manage
  resources in Amazon S3.
- `sns` – Grants permissions to allow principals to manage
  notification resources in Amazon SNS.

For the policy, see [AWSCodePipeline_ReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSCodePipeline_ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSCodePipeline_ReadOnlyAccess.md").

## AWS managed policy:

`AWSCodePipelineApproverAccess`

This is a policy that grants permission to approve or reject a manual approval action.
To view the JSON policy document in the IAM console, see [AWSCodePipelineApproverAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCodePipelineApproverAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCodePipelineApproverAccess").

**Permissions details**

This policy includes the following permissions.

- `codepipeline` – Grants permissions to actions in
  CodePipeline.

For the policy, see [AWSCodePipelineApproverAccess](../../../aws-managed-policy/latest/reference/AWSCodePipelineApproverAccess.md "../../../aws-managed-policy/latest/reference/AWSCodePipelineApproverAccess.md").

## AWS managed

policy: `AWSCodePipelineCustomActionAccess`

This is a policy that grants permission to to create custom actions in CodePipeline
or integrate Jenkins resources for build or test actions. To view the JSON policy
document in the IAM console, see [AWSCodePipelineCustomActionAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCodePipelineCustomActionAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSCodePipelineCustomActionAccess").

**Permissions details**

This policy includes the following permissions.

- `codepipeline` – Grants permissions to actions in
  CodePipeline.

For the policy, see [AWSCodePipelineCustomActionAccess](../../../aws-managed-policy/latest/reference/AWSCodePipelineCustomActionAccess.md "../../../aws-managed-policy/latest/reference/AWSCodePipelineCustomActionAccess.md").

## CodePipeline managed policies and

notifications

CodePipeline supports notifications, which can notify users of important changes to
pipelines.
Managed policies for CodePipeline include policy statements for notification
functionality. For more information, see [What are
notifications?](../../../codestar-notifications/latest/userguide/welcome.md "../../../codestar-notifications/latest/userguide/welcome.md").

### Permissions related to notifications in full access

managed policies

This managed policy grants permissions for CodePipeline along with the related services
CodeCommit, CodeBuild, CodeDeploy, and AWS CodeStar Notifications. The policy also grants permissions that
you need for working with other services that integrate with your pipelines, such as
Amazon S3, Elastic Beanstalk, CloudTrail, Amazon EC2, and AWS CloudFormation. Users with this managed policy applied can also
create and manage Amazon SNS topics for notifications, subscribe and unsubscribe users to
topics, list topics to choose as targets for notification rules, and list Amazon Q Developer in chat applications
clients configured for Slack.

The `AWSCodePipeline_FullAccess` managed policy includes the following
statements to allow full access to notifications.

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
            "StringLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:codepipeline:us-west-2:111222333444:MyFirstPipeline"}
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

### Permissions related to notifications in read-only managed

policies

The
`AWSCodePipeline_ReadOnlyAccess` managed policy includes the following
statements to allow read-only access to notifications. Users with this policy applied
can view notifications for resources, but cannot create, manage, or subscribe to them.

```
   {
        "Sid": "CodeStarNotificationsPowerUserAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:DescribeNotificationRule"
        ],
        "Resource": "*",
        "Condition" : {
            "StringLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:codepipeline:us-west-2:111222333444:MyFirstPipeline"}
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

For more information about IAM and notifications, see [Identity and Access Management for AWS CodeStar Notifications](../../../codestar-notifications/latest/userguide/security-iam.md "../../../codestar-notifications/latest/userguide/security-iam.md").

## AWS CodePipeline updates to AWS managed

policies

View details about updates to AWS managed policies for CodePipeline since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the CodePipeline [Document
history](history.md "history.md") page.

| Change                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                       | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSCodePipeline_FullAccess](#security-iam-awsmanpol-AWSCodePipeline_FullAccess "#security-iam-awsmanpol-AWSCodePipeline_FullAccess") – Updates to existing policy                                                                                                                                                                        | CodePipeline added a permission to this policy to support `ListStacks` in AWS CloudFormation.                                                                                                                                                                                     | March 15, 2024    |
| [AWSCodePipeline_FullAccess](#security-iam-awsmanpol-AWSCodePipeline_FullAccess "#security-iam-awsmanpol-AWSCodePipeline_FullAccess") – Updates to existing policy                                                                                                                                                                        | This policy was updated to add permissions for Amazon Q Developer in chat applications. For more information, see [CodePipeline managed policies and notifications](#notifications-permissions "#notifications-permissions").                                                     | June 21, 2023     |
| [AWSCodePipeline_FullAccess](#security-iam-awsmanpol-AWSCodePipeline_FullAccess "#security-iam-awsmanpol-AWSCodePipeline_FullAccess") and [AWSCodePipeline_ReadOnlyAccess](#security-iam-awsmanpol-AWSCodePipeline_ReadOnlyAccess "#security-iam-awsmanpol-AWSCodePipeline_ReadOnlyAccess") managed policies – Updates to existing policy | CodePipeline added a permission to these policies to support an additional notification type using Amazon Q Developer in chat applications, `chatbot:ListMicrosoftTeamsChannelConfigurations`.                                                                                    | May 16, 2023      |
| **AWSCodePipelineFullAccess** – Deprecated                                                                                                                                                                                                                                                                                                | This policy has been replaced by `AWSCodePipeline_FullAccess`. After November 17, 2022, this policy can not be attached to any new users, groups, or roles. For more information, see [AWS managed policies for AWS CodePipeline](managed-policies.md "managed-policies.md").     | November 17, 2022 |
| **AWSCodePipelineReadOnlyAccess** – Deprecated                                                                                                                                                                                                                                                                                            | This policy has been replaced by `AWSCodePipeline_ReadOnlyAccess`. After November 17, 2022, this policy can not be attached to any new users, groups, or roles. For more information, see [AWS managed policies for AWS CodePipeline](managed-policies.md "managed-policies.md"). | November 17, 2022 |
| CodePipeline started tracking changes                                                                                                                                                                                                                                                                                                     | CodePipeline started tracking changes for its AWS managed policies.                                                                                                                                                                                                               | March 12, 2021    |
