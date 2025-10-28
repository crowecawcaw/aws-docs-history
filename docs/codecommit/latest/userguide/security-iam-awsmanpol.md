AWS CodeCommit is no longer available to new customers. Existing customers of
AWS CodeCommit can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider")

# AWS managed policies for

CodeCommit

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

AWS addresses many common use cases by providing standalone IAM policies that
are created and administered by AWS. These AWS managed policies grant required
permissions for common use cases. The managed policies for CodeCommit also provide
permissions to perform operations in other services, such as IAM, Amazon SNS, and
Amazon CloudWatch Events, as required for the responsibilities for the users who have been granted
the policy in question. For example, the AWSCodeCommitFullAccess policy is an
administrative-level user policy that allows users with this policy to create and
manage CloudWatch Events rules for repositories (rules whose names are prefixed with
`codecommit`) and Amazon SNS topics for notifications about
repository-related events (topics whose names are prefixed with
`codecommit`), as well as administer repositories in CodeCommit.

The following AWS managed policies, which you can attach to users in your
account, are specific to CodeCommit.

###### Topics

- [AWS managed policy: AWSCodeCommitFullAccess](#managed-policies-full "#managed-policies-full")
- [AWS managed policy: AWSCodeCommitPowerUser](#managed-policies-poweruser "#managed-policies-poweruser")
- [AWS managed policy: AWSCodeCommitReadOnly](#managed-policies-read "#managed-policies-read")
- [CodeCommit managed policies and
  notifications](#notifications-permissions "#notifications-permissions")
- [AWS CodeCommit managed policies and
  Amazon CodeGuru Reviewer](#codeguru-permissions "#codeguru-permissions")
- [CodeCommit updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy: AWSCodeCommitFullAccess

You can attach the `AWSCodeCommitFullAccess` policy to your IAM identities.
This policy grants full access to CodeCommit. Apply this policy only to administrative-level users to whom you
want to grant full control over CodeCommit repositories and related resources in your
Amazon Web Services account, including the ability to delete repositories.

The AWSCodeCommitFullAccess policy contains the following policy
statement:

JSON

```
 `{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchEventsCodeCommitRulesAccess",
 "Effect": "Allow",
 "Action": [
 "events:DeleteRule",
 "events:DescribeRule",
 "events:DisableRule",
 "events:EnableRule",
 "events:PutRule",
 "events:PutTargets",
 "events:RemoveTargets",
 "events:ListTargetsByRule"
 ],
 "Resource": "arn:aws:events:*:*:rule/codecommit*"
 },
 {
 "Sid": "SNSTopicAndSubscriptionAccess",
 "Effect": "Allow",
 "Action": [
 "sns:CreateTopic",
 "sns:DeleteTopic",
 "sns:Subscribe",
 "sns:Unsubscribe",
 "sns:SetTopicAttributes"
 ],
 "Resource": "arn:aws:sns:*:*:codecommit*"
 },
 {
 "Sid": "SNSTopicAndSubscriptionReadAccess",
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics",
 "sns:ListSubscriptionsByTopic",
 "sns:GetTopicAttributes"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LambdaReadOnlyListAccess",
 "Effect": "Allow",
 "Action": [
 "lambda:ListFunctions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMReadOnlyListAccess",
 "Effect": "Allow",
 "Action": [
 "iam:ListUsers"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMReadOnlyConsoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:ListAccessKeys",
 "iam:ListSSHPublicKeys",
 "iam:ListServiceSpecificCredentials"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 },
 {
 "Sid": "IAMUserSSHKeys",
 "Effect": "Allow",
 "Action": [
 "iam:DeleteSSHPublicKey",
 "iam:GetSSHPublicKey",
 "iam:ListSSHPublicKeys",
 "iam:UpdateSSHPublicKey",
 "iam:UploadSSHPublicKey"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 },
 {
 "Sid": "IAMSelfManageServiceSpecificCredentials",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceSpecificCredential",
 "iam:UpdateServiceSpecificCredential",
 "iam:DeleteServiceSpecificCredential",
 "iam:ResetServiceSpecificCredential"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 },
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
 "Condition": {
 "ArnLike": {
 "codestar-notifications:NotificationsForResource": "`arn:aws:iam::*:role/Service*`"
 }
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
 "Sid": "AmazonCodeGuruReviewerFullAccess",
 "Effect": "Allow",
 "Action": [
 "codeguru-reviewer:AssociateRepository",
 "codeguru-reviewer:DescribeRepositoryAssociation",
 "codeguru-reviewer:ListRepositoryAssociations",
 "codeguru-reviewer:DisassociateRepository",
 "codeguru-reviewer:DescribeCodeReview",
 "codeguru-reviewer:ListCodeReviews"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonCodeGuruReviewerSLRCreation",
 "Action": "iam:CreateServiceLinkedRole",
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/aws-service-role/codeguru-reviewer.amazonaws.com/AWSServiceRoleForAmazonCodeGuruReviewer",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "codeguru-reviewer.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudWatchEventsManagedRules",
 "Effect": "Allow",
 "Action": [
 "events:PutRule",
 "events:PutTargets",
 "events:DeleteRule",
 "events:RemoveTargets"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "events:ManagedBy": "codeguru-reviewer.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CodeStarNotificationsChatbotAccess",
 "Effect": "Allow",
 "Action": [
 "chatbot:DescribeSlackChannelConfigurations",
 "chatbot:ListMicrosoftTeamsChannelConfigurations"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeStarConnectionsReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "codestar-connections:ListConnections",
 "codestar-connections:GetConnection"
 ],
 "Resource": "arn:aws:codestar-connections:*:*:connection/*"
 }
 ]
 }`

```

## AWS managed policy: AWSCodeCommitPowerUser

You can attach the `AWSCodeCommitPowerUser` policy to your IAM identities. This policy allows users access to all of
the functionality of CodeCommit and repository-related resources, except it does not
allow them to delete CodeCommit repositories or create or delete repository-related
resources in other AWS services, such as Amazon CloudWatch Events. We recommend that you
apply this policy to most users.

The AWSCodeCommitPowerUser policy contains the following policy statement:

JSON

```
 `{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:AssociateApprovalRuleTemplateWithRepository",
 "codecommit:BatchAssociateApprovalRuleTemplateWithRepositories",
 "codecommit:BatchDisassociateApprovalRuleTemplateFromRepositories",
 "codecommit:BatchGet*",
 "codecommit:BatchDescribe*",
 "codecommit:Create*",
 "codecommit:DeleteBranch",
 "codecommit:DeleteFile",
 "codecommit:Describe*",
 "codecommit:DisassociateApprovalRuleTemplateFromRepository",
 "codecommit:EvaluatePullRequestApprovalRules",
 "codecommit:Get*",
 "codecommit:List*",
 "codecommit:Merge*",
 "codecommit:OverridePullRequestApprovalRules",
 "codecommit:Put*",
 "codecommit:Post*",
 "codecommit:TagResource",
 "codecommit:Test*",
 "codecommit:UntagResource",
 "codecommit:Update*",
 "codecommit:GitPull",
 "codecommit:GitPush"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchEventsCodeCommitRulesAccess",
 "Effect": "Allow",
 "Action": [
 "events:DeleteRule",
 "events:DescribeRule",
 "events:DisableRule",
 "events:EnableRule",
 "events:PutRule",
 "events:PutTargets",
 "events:RemoveTargets",
 "events:ListTargetsByRule"
 ],
 "Resource": "arn:aws:events:*:*:rule/codecommit*"
 },
 {
 "Sid": "SNSTopicAndSubscriptionAccess",
 "Effect": "Allow",
 "Action": [
 "sns:Subscribe",
 "sns:Unsubscribe"
 ],
 "Resource": "arn:aws:sns:*:*:codecommit*"
 },
 {
 "Sid": "SNSTopicAndSubscriptionReadAccess",
 "Effect": "Allow",
 "Action": [
 "sns:ListTopics",
 "sns:ListSubscriptionsByTopic",
 "sns:GetTopicAttributes"
 ],
 "Resource": "*"
 },
 {
 "Sid": "LambdaReadOnlyListAccess",
 "Effect": "Allow",
 "Action": [
 "lambda:ListFunctions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMReadOnlyListAccess",
 "Effect": "Allow",
 "Action": [
 "iam:ListUsers"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMReadOnlyConsoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:ListAccessKeys",
 "iam:ListSSHPublicKeys",
 "iam:ListServiceSpecificCredentials"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 },
 {
 "Sid": "IAMUserSSHKeys",
 "Effect": "Allow",
 "Action": [
 "iam:DeleteSSHPublicKey",
 "iam:GetSSHPublicKey",
 "iam:ListSSHPublicKeys",
 "iam:UpdateSSHPublicKey",
 "iam:UploadSSHPublicKey"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 },
 {
 "Sid": "IAMSelfManageServiceSpecificCredentials",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceSpecificCredential",
 "iam:UpdateServiceSpecificCredential",
 "iam:DeleteServiceSpecificCredential",
 "iam:ResetServiceSpecificCredential"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 },
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
 "Condition": {
 "ArnLike": {
 "codestar-notifications:NotificationsForResource": "`arn:aws:iam::*:role/Service*`"
 }
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
 "Sid": "AmazonCodeGuruReviewerFullAccess",
 "Effect": "Allow",
 "Action": [
 "codeguru-reviewer:AssociateRepository",
 "codeguru-reviewer:DescribeRepositoryAssociation",
 "codeguru-reviewer:ListRepositoryAssociations",
 "codeguru-reviewer:DisassociateRepository",
 "codeguru-reviewer:DescribeCodeReview",
 "codeguru-reviewer:ListCodeReviews"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonCodeGuruReviewerSLRCreation",
 "Action": "iam:CreateServiceLinkedRole",
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/aws-service-role/codeguru-reviewer.amazonaws.com/AWSServiceRoleForAmazonCodeGuruReviewer",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "codeguru-reviewer.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudWatchEventsManagedRules",
 "Effect": "Allow",
 "Action": [
 "events:PutRule",
 "events:PutTargets",
 "events:DeleteRule",
 "events:RemoveTargets"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "events:ManagedBy": "codeguru-reviewer.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CodeStarNotificationsChatbotAccess",
 "Effect": "Allow",
 "Action": [
 "chatbot:DescribeSlackChannelConfigurations",
 "chatbot:ListMicrosoftTeamsChannelConfigurations"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeStarConnectionsReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "codestar-connections:ListConnections",
 "codestar-connections:GetConnection"
 ],
 "Resource": "arn:aws:codestar-connections:*:*:connection/*"
 }
 ]
 }`

```

## AWS managed policy: AWSCodeCommitReadOnly

You can attach the `AWSCodeCommitReadOnly` policy to your IAM identities. This policy grants read-only access to
CodeCommit and repository-related resources in other AWS services, as well
as the ability to create and manage their own CodeCommit-related resources (such as
Git credentials and SSH keys for their IAM user to use when accessing
repositories). Apply this policy to users to whom you want to grant the ability
to read the contents of a repository, but not make any changes to its
contents.

The AWSCodeCommitReadOnly policy contains the following policy
statement:

JSON

```
 `{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "codecommit:BatchGet*",
 "codecommit:BatchDescribe*",
 "codecommit:Describe*",
 "codecommit:EvaluatePullRequestApprovalRules",
 "codecommit:Get*",
 "codecommit:List*",
 "codecommit:GitPull"
 ],
 "Resource":"*"
 },
 {
 "Sid":"CloudWatchEventsCodeCommitRulesReadOnlyAccess",
 "Effect":"Allow",
 "Action":[
 "events:DescribeRule",
 "events:ListTargetsByRule"
 ],
 "Resource":"arn:aws:events:*:*:rule/codecommit*"
 },
 {
 "Sid":"SNSSubscriptionAccess",
 "Effect":"Allow",
 "Action":[
 "sns:ListTopics",
 "sns:ListSubscriptionsByTopic",
 "sns:GetTopicAttributes"
 ],
 "Resource":"*"
 },
 {
 "Sid":"LambdaReadOnlyListAccess",
 "Effect":"Allow",
 "Action":[
 "lambda:ListFunctions"
 ],
 "Resource":"*"
 },
 {
 "Sid":"IAMReadOnlyListAccess",
 "Effect":"Allow",
 "Action":[
 "iam:ListUsers"
 ],
 "Resource":"*"
 },
 {
 "Sid":"IAMReadOnlyConsoleAccess",
 "Effect":"Allow",
 "Action":[
 "iam:ListAccessKeys",
 "iam:ListSSHPublicKeys",
 "iam:ListServiceSpecificCredentials",
 "iam:GetSSHPublicKey"
 ],
 "Resource":"arn:aws:iam::*:user/${aws:username}"
 },
 {
 "Sid":"CodeStarNotificationsReadOnlyAccess",
 "Effect":"Allow",
 "Action":[
 "codestar-notifications:DescribeNotificationRule"
 ],
 "Resource":"*",
 "Condition":{
 "ArnLike":{
 "codestar-notifications:NotificationsForResource":"arn:aws:codecommit:us-east-2:`111122223333`:*"
 }
 }
 },
 {
 "Sid":"CodeStarNotificationsListAccess",
 "Effect":"Allow",
 "Action":[
 "codestar-notifications:ListNotificationRules",
 "codestar-notifications:ListEventTypes",
 "codestar-notifications:ListTargets"
 ],
 "Resource":"*"
 },
 {
 "Sid": "AmazonCodeGuruReviewerReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "codeguru-reviewer:DescribeRepositoryAssociation",
 "codeguru-reviewer:ListRepositoryAssociations",
 "codeguru-reviewer:DescribeCodeReview",
 "codeguru-reviewer:ListCodeReviews"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeStarConnectionsReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "codestar-connections:ListConnections",
 "codestar-connections:GetConnection"
 ],
 "Resource": "arn:aws:codestar-connections:*:*:connection/*"
 }
 ]
}`

```

## CodeCommit managed policies and

notifications

AWS CodeCommit supports notifications, which can notify users of important changes to
repositories.
Managed policies for CodeCommit include policy statements for notification
functionality. For more information, see [What are
notifications?](../../../codestar-notifications/latest/userguide/welcome.md "../../../codestar-notifications/latest/userguide/welcome.md").

### Permissions related to notifications in full access

managed policies

The `AWSCodeCommitFullAccess` managed policy includes the following statements
to allow full access to notifications. Users with this managed policy applied can also
create and manage Amazon SNS topics for notifications, subscribe and unsubscribe users to
topics, list topics to choose as targets for notification rules, and list Amazon Q Developer in chat applications
clients configured for Slack.

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
            "StringLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:codecommit:*"}
        }
    },
    {
        "Sid": "CodeStarNotificationsListAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:ListNotificationRules",
            "codestar-notifications:ListTargets",
            "codestar-notifications:ListTagsforResource,"
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

The `AWSCodeCommitReadOnlyAccess` managed policy includes the following
statements to allow read-only access to notifications. Users with this managed policy
applied can view notifications for resources, but cannot create, manage, or subscribe to
them.

```
   {
        "Sid": "CodeStarNotificationsPowerUserAccess",
        "Effect": "Allow",
        "Action": [
            "codestar-notifications:DescribeNotificationRule"
        ],
        "Resource": "*",
        "Condition" : {
            "StringLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:codecommit:*"}
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

### Permissions related to notifications in other managed

policies

The `AWSCodeCommitPowerUser` managed policy includes the following statements
to allow users to create, edit, and subscribe to notifications. Users cannot delete
notification rules or manage tags for resources.

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
            "StringLike" : {"codestar-notifications:NotificationsForResource" : "arn:aws:codecommit*"}
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

For more information about IAM and notifications, see [Identity and Access Management for AWS CodeStar Notifications](../../../codestar-notifications/latest/userguide/security-iam.md "../../../codestar-notifications/latest/userguide/security-iam.md").

## AWS CodeCommit managed policies and

Amazon CodeGuru Reviewer

CodeCommit supports Amazon CodeGuru Reviewer, an automated code review service that uses program analysis and
machine learning to detect common issues and recommend fixes in your Java or Python code. Managed
policies for CodeCommit include policy statements for CodeGuru Reviewer functionality. For more information,
see [What Is Amazon CodeGuru Reviewer](../../../codeguru/latest/reviewer-ug/welcome.md "../../../codeguru/latest/reviewer-ug/welcome.md").

### Permissions related to CodeGuru Reviewer in

AWSCodeCommitFullAccess

The `AWSCodeCommitFullAccess` managed policy includes the following statements
to allow CodeGuru Reviewer to be associated and disassociated with CodeCommit repositories. Users with
this managed policy applied can also view the association status between CodeCommit
repositories and CodeGuru Reviewer and view the status of review jobs for pull requests.

```
    {
      "Sid": "AmazonCodeGuruReviewerFullAccess",
      "Effect": "Allow",
      "Action": [
        "codeguru-reviewer:AssociateRepository",
        "codeguru-reviewer:DescribeRepositoryAssociation",
        "codeguru-reviewer:ListRepositoryAssociations",
        "codeguru-reviewer:DisassociateRepository",
        "codeguru-reviewer:DescribeCodeReview",
        "codeguru-reviewer:ListCodeReviews"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AmazonCodeGuruReviewerSLRCreation",
      "Action": "iam:CreateServiceLinkedRole",
      "Effect": "Allow",
      "Resource": "arn:aws:iam::*:role/aws-service-role/codeguru-reviewer.amazonaws.com/AWSServiceRoleForAmazonCodeGuruReviewer",
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": "codeguru-reviewer.amazonaws.com"
        }
      }
    },
    {
      "Sid": "CloudWatchEventsManagedRules",
      "Effect": "Allow",
      "Action": [
        "events:PutRule",
        "events:PutTargets",
        "events:DeleteRule",
        "events:RemoveTargets"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "events:ManagedBy": "codeguru-reviewer.amazonaws.com"
        }
      }
    }
```

### Permissions related to CodeGuru Reviewer in AWSCodeCommitPowerUser

The `AWSCodeCommitPowerUser` managed policy includes the following
statements to allow users to associate and disassociate repositories with CodeGuru Reviewer, view
association status, and view the status of review jobs for pull requests.

```
    {
      "Sid": "AmazonCodeGuruReviewerFullAccess",
      "Effect": "Allow",
      "Action": [
        "codeguru-reviewer:AssociateRepository",
        "codeguru-reviewer:DescribeRepositoryAssociation",
        "codeguru-reviewer:ListRepositoryAssociations",
        "codeguru-reviewer:DisassociateRepository",
        "codeguru-reviewer:DescribeCodeReview",
        "codeguru-reviewer:ListCodeReviews"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AmazonCodeGuruReviewerSLRCreation",
      "Action": "iam:CreateServiceLinkedRole",
      "Effect": "Allow",
      "Resource": "arn:aws:iam::*:role/aws-service-role/codeguru-reviewer.amazonaws.com/AWSServiceRoleForAmazonCodeGuruReviewer",
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": "codeguru-reviewer.amazonaws.com"
        }
      }
    },
    {
      "Sid": "CloudWatchEventsManagedRules",
      "Effect": "Allow",
      "Action": [
        "events:PutRule",
        "events:PutTargets",
        "events:DeleteRule",
        "events:RemoveTargets"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "events:ManagedBy": "codeguru-reviewer.amazonaws.com"
        }
      }
    }
```

### Permissions related to CodeGuru Reviewer in AWSCodeCommitReadOnly

The `AWSCodeCommitReadOnlyAccess` managed policy includes the following
statements to allow read-only access to CodeGuru Reviewer association status and view the status of
review jobs for pull requests. Users with this managed policy applied cannot associate
or disassociate repositories.

```
     {
      "Sid": "AmazonCodeGuruReviewerReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
            "codeguru-reviewer:DescribeRepositoryAssociation",
            "codeguru-reviewer:ListRepositoryAssociations",
            "codeguru-reviewer:DescribeCodeReview",
            "codeguru-reviewer:ListCodeReviews"
      ],
      "Resource": "*"
    }
```

### Amazon CodeGuru Reviewer service-linked role

When you associate a repository with CodeGuru Reviewer, a service-linked role is created so that
CodeGuru Reviewer can detect issues and recommend fixes for Java or Python code in pull requests. The
service-linked role is named AWSServiceRoleForAmazonCodeGuruReviewer. For more information, see [Using Service-Linked Roles for Amazon CodeGuru Reviewer](../../../codeguru/latest/reviewer-ug/using-service-linked-roles.md "../../../codeguru/latest/reviewer-ug/using-service-linked-roles.md").

For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## CodeCommit updates to AWS managed

policies

View details about updates to AWS managed policies for CodeCommit since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on [AWS CodeCommit User Guide document history](history.md "history.md").

| Change                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                         | Date            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [AWS managed policy: AWSCodeCommitFullAccess](#managed-policies-full "#managed-policies-full") and [AWS managed policy: AWSCodeCommitPowerUser](#managed-policies-poweruser "#managed-policies-poweruser") – Update to existing policies | CodeCommit added a permission to these policies to support an additional notification type using Amazon Q Developer in chat applications. The AWSCodeCommitPowerUser and AWSCodeCommitFullAccess policies have been changed to add a permission, `chatbot:ListMicrosoftTeamsChannelConfigurations`. | May 16, 2023    |
| [AWS managed policy: AWSCodeCommitReadOnly](#managed-policies-read "#managed-policies-read") – Update to an existing policy                                                                                                              | CodeCommit removed a duplicate permission from the policy. The AWSCodeCommitReadOnly has been changed to remove a duplicate permission, `"iam:ListAccessKeys"`.                                                                                                                                     | August 18, 2021 |
| CodeCommit started tracking changes                                                                                                                                                                                                      | CodeCommit started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                   | August 18, 2021 |
