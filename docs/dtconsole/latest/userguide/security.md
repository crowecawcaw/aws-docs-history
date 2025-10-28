# Security for features of the Developer Tools console

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that is built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes
this as security _of_ the cloud and security _in_ the
cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also
  provides you with services that you can use securely. Third-party auditors regularly test
  and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the
  compliance programs that apply to AWS CodeStar Notifications and AWS CodeConnections, see [AWS Services in Scope by Compliance
  Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors
  including the sensitivity of your data, your company’s requirements, and applicable laws and
  regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using AWS CodeStar Notifications and AWS CodeConnections. The following topics show you how to configure AWS CodeStar Notifications and AWS CodeConnections to meet your
  security and compliance objectives. You also learn how to use other AWS services that help you
  to monitor and secure your AWS CodeStar Notifications and AWS CodeConnections resources.

For more information about security for the services in the Developer Tools console, see the
following:

- [CodeBuild Security](../../../codebuild/latest/userguide/security.md "../../../codebuild/latest/userguide/security.md")
- [CodeCommit Security](../../../codecommit/latest/userguide/security.md "../../../codecommit/latest/userguide/security.md")
- [CodeDeploy Security](../../../codedeploy/latest/userguide/security.md "../../../codedeploy/latest/userguide/security.md")
- [CodePipeline Security](../../../codepipeline/latest/userguide/security.md "../../../codepipeline/latest/userguide/security.md")

## Understanding notification contents and

security

Notifications provide information about resources to users who are subscribed to the
notification rule targets that you configure. This information can include details about your
developer tool resources, including repository contents, build statuses, deployment statuses,
and pipeline executions.

For example, you can configure a notification rule for a repository in CodeCommit to include
comments on commits or pull requests. If so, the notifications sent in response to that rule
might contain the line or lines of code referenced in that comment. Similarly, you can
configure a notification rule for a build project in CodeBuild to include successes or failures
for build states and phases. Notifications sent in response to that rule will contain that
information.

You can configure a notification rule for a pipeline in CodePipeline to include information about
manual approvals, and notifications sent in response to that rule might contain the name of
the person providing that approval. You can configure a notification rule for an application
in CodeDeploy to indicate deployment success, and notifications sent in response to that rule might
contain information about the deployment target.

Notifications can include project-specific information such as build statuses, lines of
code that have comments, deployment states, and pipeline approvals. So to help ensure the
security of your project, make sure that you regularly review both the targets of notification
rules and the list of subscribers of the Amazon SNS topics specified as targets. Additionally, the
content of notifications sent in response to events might change as additional features are
added to the underlying services. This change can happen without notice to already-existing
notification rules. Consider reviewing the contents of notification messages periodically to
help ensure that you understand what is being sent, as well as to whom it is being
sent.

For more information about the event types available for notification rules, see [Notification concepts](concepts.md "concepts.md").

You can choose to limit the details included in notifications to only what is included in
an event. This is referred to as the **Basic** detail type. These events
contain exactly the same information as is sent to Amazon EventBridge and Amazon CloudWatch Events.

Developer Tools console services, such as CodeCommit, might choose to add information about some or all of
their event types in notification messages beyond what is available in an event. This
supplemental information could be added at any time to enhance current event types or
supplement future event types. You can choose to include any supplemental information about
the event, if available, in the notification by choosing the **Full** detail
type. For more information, see [Detail types](concepts.md#detail-type "concepts.md#detail-type").
