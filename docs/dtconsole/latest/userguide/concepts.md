# Notification concepts

Setting up and using notifications is easier if you understand the concepts and terms. Here are some concepts
to know about as you use notifications.

###### Topics

- [Notifications](#notifications "#notifications")
- [Notification rules](#rules "#rules")
- [Events](#events "#events")
- [Detail types](#detail-type "#detail-type")
- [Targets](#targets "#targets")
- [Notifications and AWS CodeStar Notifications](#concepts-api "#concepts-api")
- [Events for notification rules on repositories](#events-ref-repositories "#events-ref-repositories")
- [Events for notification rules on build projects](#events-ref-buildproject "#events-ref-buildproject")
- [Events for notification rules on deployment
  applications](#events-ref-deployapplication "#events-ref-deployapplication")
- [Events for notification rules on pipelines](#events-ref-pipeline "#events-ref-pipeline")

## Notifications

A _notification_ is a message that contains information about events that
occur in the resources you and your developers use. You can set up notifications so that users of a
resource, such as a build project, repository, deployment application, or pipeline, receive emails about the
event types you specify according to the notification rule you create.

Notifications for AWS CodeCommit can contain user identity information, such as a display
name or an email address, through the use of session tags. CodeCommit supports the use of
session tags, which are key-value pair attributes that you pass when you assume an IAM
role, use temporary credentials, or federate a user in AWS Security Token Service (AWS STS). You can also
associate tags with an
IAM user.
CodeCommit includes the values for `displayName` and `emailAddress` in
notification content if those tags are present. For more information, see [Using tags
to provide additional identity information in CodeCommit](../../../codecommit/latest/userguide/security-iam.md#security_iam_service-with-iam-tags "../../../codecommit/latest/userguide/security-iam.md#security_iam_service-with-iam-tags").

###### Important

Notifications include project-specific information such as build status,
deployment status, lines of code that have comments, and pipeline approvals.
Notification content might change as new features are added. As a security best
practice, you should regularly review the targets of notification rules and the
Amazon SNS topic subscribers. For more information, see [Understanding notification contents and
security](security.md#security-notifications "security.md#security-notifications").

## Notification rules

A _notification rule_ is an AWS resource that you create to specify when
and where notifications are sent. It defines:

- The conditions under which a notification is created. These conditions are
  based on events that you choose, which are specific to the resource type.
  Supported resource types include build projects in AWS CodeBuild, deployment
  applications in AWS CodeDeploy, pipelines in AWS CodePipeline, and repositories in
  AWS CodeCommit.
- The targets to which the notification is sent. You can specify up to 10 targets for a notification
  rule.

Notification rules are scoped to individual build projects, deployment applications, pipelines, and
repositories. Notification rules have both user-defined friendly names and Amazon Resource Names (ARNs).
Notification rules must be created in the same AWS Region where the resource exists. For example, if your
build project is in the US East (Ohio) Region, your notification rule must be created in the
US East (Ohio) Region, too.

You can define up to 10 notification rules for a resource.

## Events

An _event_ is a change of state on a resource that you want to monitor.
Each resource has a list of event types you can choose from. When you set up a notification rule on a
resource, you specify the events that cause notifications to be sent. For example, if you set up
notifications for a repository in CodeCommit, and you select **Created** for both **Pull
request** and **Branches and tags**, a notification is sent every time a user
in that repository creates a pull request, branch, or Git tag.

## Detail types

When you create a notification rule, you can choose the level of detail or _detail type_ included in notifications
(**Full** or **Basic**). The
**Full** setting (the default) includes all information available
for the event in the notification, including any enhanced information provided by
services for specific events. The **Basic** setting includes only a
subset of the available information.

The following table lists the enhanced information available for specific event types
and describes the differences between the detail types.

| Service      | Event                                                                          | Full includes                                                                                                                                                                            | Basic does not include                                                                                             |
| ------------ | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| CodeCommit   | Comments on commits<br>Comments on pull requests                               | All event details and the content of the comment, including any<br>replies or comment threads. It also includes the line number and the<br>line of code upon which the comment was made. | The content of the comment. line number, line of code, or any<br>comment threads.                                  |
| CodeCommit   | Pull request created                                                           | All event details and the number of files that were added,<br>modified, or deleted in the pull request in relation to the<br>destination branch.                                         | No list of files or details about whether the pull request source<br>branch has added, modified, or deleted files. |
| CodePipeline | Manual approval needed                                                         | All event details and custom data (if configured). The<br>notification also includes a link to the required approval in the<br>pipeline.                                                 | No custom data or link.                                                                                            |
| CodePipeline | Action execution failed<br>Pipeline execution failed<br>Stage execution failed | All event details and the content of the error message for the<br>failure.                                                                                                               | No error message content.                                                                                          |

## Targets

A _target_ is a location for receiving notifications
from notification rules. The allowed target types are Amazon SNS topics and AWS Chatbot clients
configured for Slack or Microsoft Teams channels. Any user subscribed to the target receives notifications
about the events that you specify in the notification rule.

If you want to extend the reach of notifications, you can manually configure
integration between notifications and AWS Chatbot so that notifications are sent to Amazon Chime
chatrooms. You can then choose the Amazon SNS topic that is configured for that AWS Chatbot client
as the target for the notification rule. For more information, see [To integrate notifications with AWS Chatbot
and Amazon Chime](notifications-chatbot.md#notifications-chatbot-chime "notifications-chatbot.md#notifications-chatbot-chime").

If you choose to use an AWS Chatbot client as a target, you must first create that client
in AWS Chatbot. When you choose an AWS Chatbot client as a target for a notification rule, an
Amazon SNS topic is configured for that AWS Chatbot client with all the policies required for
notifications to be sent to the Slack or Microsoft Teams channel. You don't have to configure any existing
Amazon SNS topics for the AWS Chatbot client.

You can choose to create an Amazon SNS topic as a target as part of creating a notification
rule (recommended). You can also choose an existing Amazon SNS topic in the same AWS Region
as the notification rule, but you must configure it with the required policy. The Amazon SNS
topic that you use for a target must be in your AWS account. It also must be in the
same AWS Region as the notification rule and the AWS resource for which the rule was
created.

For example, if you create a notification rule for a repository in the
US East (Ohio) Region, the Amazon SNS topic must also exist in that Region. If you create
an Amazon SNS topic as part of creating a notification rule, the topic is configured with the
policy required to allow the publication of events to the topic. This is the best method
for working with targets and notification rules. If you choose to use an
already-existing topic or create one manually, you must configure it with the required
permissions before users receive notifications. For more information, see [Configure Amazon SNS topics for notifications](set-up-sns.md "set-up-sns.md").

###### Note

If you want to use an existing Amazon SNS topic instead of creating a new one,
in **Targets**, choose its ARN. Make sure the topic has the
appropriate access policy, and that the subscriber list
contains only those users who are allowed to see information about the
resource. If the Amazon SNS topic is a topic that was used for
CodeCommit notifications before November 5, 2019, it will contain a policy that allows
CodeCommit to publish to it that contains different permissions than those required
for AWS CodeStar Notifications. Using these topics is not recommended. If you want to use one created
for that experience, you must add the required policy for AWS CodeStar Notifications in addition to the one
that already exists. For more information, see [Configure Amazon SNS topics for notifications](set-up-sns.md "set-up-sns.md") and [Understanding notification contents and
security](security.md#security-notifications "security.md#security-notifications").

## Notifications and AWS CodeStar Notifications

While a feature of the Developer Tools console, notifications has its own API, AWS CodeStar Notifications. It also has its own AWS
resource type (notification rules), permissions, and events. Events for notification rules are logged in
AWS CloudTrail. API actions can be allowed or denied through IAM policies.

## Events for notification rules on repositories

| Category          | Events                                                | Event IDs                                                                                                                                                                                                 |
| ----------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Comments          | On commits<br>On pull requests                        | `codecommit-repository-comments-on-commits`<br>`codecommit-repository-comments-on-pull-requests`                                                                                                          |
| Approvals         | Status changed<br>Rule override                       | `codecommit-repository-approvals-status-changed`<br>`codecommit-repository-approvals-rule-override`                                                                                                       |
| Pull request      | Created<br>Source updated<br>Status changed<br>Merged | `codecommit-repository-pull-request-created`<br>`codecommit-repository-pull-request-source-updated`<br>`codecommit-repository-pull-request-status-changed`<br>`codecommit-repository-pull-request-merged` |
| Branches and tags | Created<br>Deleted<br>Updated                         | `codecommit-repository-branches-and-tags-created``codecommit-repository-branches-and-tags-deleted``codecommit-repository-branches-and-tags-updated`                                                       |

## Events for notification rules on build projects

| Category    | Events                                        | Event IDs                                                                                                                                                                     |
| ----------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Build state | Failed<br>Succeeded<br>In-progress<br>Stopped | `codebuild-project-build-state-failed`<br>`codebuild-project-build-state-succeeded`<br>`codebuild-project-build-state-in-progress`<br>`codebuild-project-build-state-stopped` |
| Build phase | Failure<br>Success                            | `codebuild-project-build-phase-failure`<br>`codebuild-project-build-phase-success`                                                                                            |

## Events for notification rules on deployment

applications

| Category   | Events                         | Event IDs                                                                                                                          |
| ---------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Deployment | Failed<br>Succeeded<br>Started | `codedeploy-application-deployment-failed``codedeploy-application-deployment-succeeded``codedeploy-application-deployment-started` |

## Events for notification rules on pipelines

| Category           | Events                                                              | Event IDs                                                                                                                                                                                                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Action execution   | Succeeded<br>Failed<br>Canceled<br>Started                          | `codepipeline-pipeline-action-execution-succeeded`<br>`codepipeline-pipeline-action-execution-failed`<br>`codepipeline-pipeline-action-execution-canceled`<br>`codepipeline-pipeline-action-execution-started`                                                                                                                        |
| Stage execution    | Started<br>Succeeded<br>Resumed<br>Canceled<br>Failed               | `codepipeline-pipeline-stage-execution-started`<br>`codepipeline-pipeline-stage-execution-succeeded`<br>`codepipeline-pipeline-stage-execution-resumed`<br>`codepipeline-pipeline-stage-execution-canceled`<br>`codepipeline-pipeline-stage-execution-failed`                                                                         |
| Pipeline execution | Failed<br>Canceled<br>Started<br>Resumed<br>Succeeded<br>Superseded | `codepipeline-pipeline-pipeline-execution-failed`<br>`codepipeline-pipeline-pipeline-execution-canceled`<br>`codepipeline-pipeline-pipeline-execution-started`<br>`codepipeline-pipeline-pipeline-execution-resumed`<br>`codepipeline-pipeline-pipeline-execution-succeeded`<br>`codepipeline-pipeline-pipeline-execution-superseded` |
| Manual approval    | Failed<br>Needed<br>Succeeded                                       | `codepipeline-pipeline-manual-approval-failed``codepipeline-pipeline-manual-approval-needed``codepipeline-pipeline-manual-approval-succeeded`                                                                                                                                                                                         |
