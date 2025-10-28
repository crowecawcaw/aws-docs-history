# Setting up

If you have a managed policy for AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, or AWS CodePipeline applied to
your IAM user or role, you have the permissions required to work with notifications within
the limitations of the roles and permissions provided by the policy. For example, users who
have the `AWSCodeBuildAdminAccess`, `AWSCodeCommitFullAccess`,
`AWSCodeDeployFullAccess`, or `AWSCodePipeline_FullAccess` managed
policy applied have full administrative access to notifications.

For more information, including example policies, see [Identity-based
policies](security-iam.md#security_iam_access-manage-id-based-policies "security-iam.md#security_iam_access-manage-id-based-policies").

If you have one of these policies applied to your IAM user or role, and a build project
in CodeBuild, a repository in CodeCommit, a deployment application in CodeDeploy, or a pipeline in CodePipeline,
you are ready to create your first notification rule. Continue to [Getting started with notifications](getting-started.md "getting-started.md"). If not, see the following
topics:

- CodeBuild: [Getting started with
  CodeBuild](../../../codebuild/latest/userguide/getting-started.md "../../../codebuild/latest/userguide/getting-started.md")
- CodeCommit: [Getting started with
  CodeCommit](../../../codecommit/latest/userguide/getting-started-cc.md "../../../codecommit/latest/userguide/getting-started-cc.md")
- CodeDeploy: [Tutorials](../../../codedeploy/latest/userguide/tutorials.md "../../../codedeploy/latest/userguide/tutorials.md")
- CodePipeline: [Getting
  started with CodePipeline](../../../codepipeline/latest/userguide/getting-started-codepipeline.md "../../../codepipeline/latest/userguide/getting-started-codepipeline.md")
  If you want to manage administrative permissions for notifications for IAM users,
  groups, or roles yourself, follow the procedures in this topic to set up the permissions and
  resources you need to use the service.

If you want to use previously created Amazon SNS topics for notifications instead of creating
topics specifically for notifications, you must configure an Amazon SNS topic to use as the
target for a notification rule by applying a policy that allows events to be published to
that topic.

###### Note

To perform the following procedures, you must be signed in with an account that has
administrative permissions. For more information, see [Creating your first
IAM admin user and group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md").

###### Topics

- [Create and apply a policy for administrative access
  to notifications](#set-up-permissions "#set-up-permissions")
- [Configure Amazon SNS topics for notifications](set-up-sns.md "set-up-sns.md")
- [Subscribe users to Amazon SNS topics that are
  targets](subscribe-users-sns.md "subscribe-users-sns.md")

## Create and apply a policy for administrative access

to notifications

You can administer notifications by signing in with an IAM user or using a role that
has permissions to access the service and the services (AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy,
or AWS CodePipeline) for which you want to create notifications. You can also create your own
policies and apply them to users or groups.

The following procedure shows you how to configure an IAM group with permissions for
administering notifications and adding IAM users. If you do not want to set up a
group, you can apply this policy directly to IAM users or to an IAM role that can be
assumed by users. You can also use the managed policies for CodeBuild, CodeCommit, CodeDeploy, or
CodePipeline, which include policy-appropriate access to notification features depending on the
scope of the policy.

For the policy below, enter a name (for example,
`AWSCodeStarNotificationsFullAccess`) and an optional description for
this policy. The description helps you remember the purpose of the policy (for example,
`This policy provides full access to AWS CodeStar Notifications.`

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
 {
    "Version": "2012-10-17",
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
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.
