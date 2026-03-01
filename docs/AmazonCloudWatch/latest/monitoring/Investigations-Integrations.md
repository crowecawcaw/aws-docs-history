# Integrations with other systems

###### Topics

- [Integration with AWS Systems Manager Automation](#Investigations-Integrations-SSM "#Investigations-Integrations-SSM")
- [Integration with third-party chat systems](#Investigations-Integrations-Chat "#Investigations-Integrations-Chat")

## Integration with AWS Systems Manager Automation

CloudWatch investigations is integrated with Automation, a capability of AWS Systems Manager. You don't need to
configure integration, but you might need to update AWS Identity and Access Management (IAM) permissions so
you can use Automation runbooks.

###### What is AWS Systems Manager?

Systems Manager helps you centrally view, manage, and operate _managed nodes_ at scale in AWS, on-premises, and multicloud
environments. In Systems Manager, a managed node is any machine configured for use with
Systems Manager. For information, see the [_AWS Systems Manager User Guide_.](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md")

###### What is Systems Manager Automation?

Automation performs common maintenance, deployment, troubleshooting, and
remediation tasks through the use of _runbooks_. Each runbook defines a number of steps for performing
tasks. Each step is associated with a particular _action_. The action determines the inputs, behavior, and outputs
of the step. For descriptions of the nearly two dozen actions that are supported
for runbooks, see the [Systems Manager
Automation actions reference](../../../systems-manager/latest/userguide/automation-actions.md "../../../systems-manager/latest/userguide/automation-actions.md") in the _AWS Systems Manager User Guide_.

Automation provides over 400 AWS managed runbooks. For details about each runbook,
including a step-by-step description of the actions performed when executed, see the
[Systems Manager Automation runbook reference](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md"). Customers can also design their own
runbooks to address specific scenarios in their environments. For information, see
[Creating your own runbooks](../../../systems-manager-automation-runbooks/latest/userguide/automation-documents.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-documents.md") in the _AWS Systems Manager User Guide_.

For information about working with runbooks in an investigation, see [Reviewing and executing suggested runbook remediations for CloudWatch investigations](suggested-investigation-actions.md "suggested-investigation-actions.md").

## Integration with third-party chat systems

By integrating CloudWatch investigations with CloudWatch investigations in chat applications, you can have updates from
investigations sent to third-party chat services, including Slack, and Microsoft
Teams. The integration is facilitated by Amazon Simple Notification Service.

The following topics describe the required steps in the recommended order:

###### Topics

- [Create and configure the Amazon SNS topic and access policy](#Investigations-Integrations-Chat-policy "#Investigations-Integrations-Chat-policy")
- [Configure CloudWatch investigations in your chat applications](#Investigations-Integrations-Chatbot-configure "#Investigations-Integrations-Chatbot-configure")
- [Add Amazon SNS topics to CloudWatch AI Operations](#Investigations-Integrations-Chat-configure "#Investigations-Integrations-Chat-configure")

### Create and configure the Amazon SNS topic and access policy

Create an Amazon SNS topic in the same region as your investigation. For more
information, see [Creating an Amazon Simple Notification Service
topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md").

To enable CloudWatch investigations to send notifications, you must add an the following access
policy to the Amazon SNS topic

```
{
    "Sid": "AIOPS-CHAT-PUBLISH",
    "Effect": "Allow",
    "Principal": {
        "Service": "aiops.amazonaws.com"
    },
    "Action": "sns:Publish",
    "Resource": "`SNS-TOPIC-ARN`",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "`account-Id`"
        }
    }
}
```

### Configure CloudWatch investigations in your chat applications

To configure CloudWatch investigations in chat applications for communication with a third-party
chat service, use the following tutorials:

- [Tutorial: Get
  started with Slack](../../../chatbot/latest/adminguide/slack-setup.md "../../../chatbot/latest/adminguide/slack-setup.md").
- [Tutorial: Get
  started with Microsoft Teams](../../../chatbot/latest/adminguide/teams-setup.md "../../../chatbot/latest/adminguide/teams-setup.md").

Then, to support using AI assistant actions within chat channels you must
provide the CloudWatch investigations in chat applications role with appropriate permissions. When
you create a new IAM channel role for the channel, select the
**Notifications** and **Amazon Q operations assistant
permissions** policy templates.

Attach the **AIOpsOperatorAccess** managed IAM policy to the
guardrail policies in CloudWatch investigations in chat applications. This grants permissions to CloudWatch investigations
in chat applications to interact with CloudWatch investigations and perform required actions on your
behalf.

In the channel configuration, you must also subscribe to the Amazon SNS topic that
you created in the previous procedure.

### Add Amazon SNS topics to CloudWatch AI Operations

You must use the CloudWatch console to configure CloudWatch investigations to integrate with Amazon SNS. You
can do this while you create the investigation group in your account, or
later.

If you have already created an investigation group and want to add chat
integration, follow these steps.

###### To add chat integration to an existing investigation group

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **AI Operations**,
   **Configuration**.
3. On the **Optional configuration** tab, in the
   **Chat integration** section, do the
   following:
   - If you have already integrated CloudWatch investigations in chat applications
     with a third-party chat system, you can choose
     **Select SNS topic** to choose the
     Amazon SNS topic to use to send updates to about investigations.
     This Amazon SNS topic will relay those updates to the chat
     client.
   - If you want to integrate CloudWatch investigations in chat applications with a
     third-party chat system, choose **Configure new chat
     client**. For more information about setting
     up this configuration, see [Getting started with CloudWatch investigations in chat
     applications](../../../chatbot/latest/adminguide/getting-started.md "../../../chatbot/latest/adminguide/getting-started.md").

When incident reports are generated, notifications can be sent to configured
chat channels to alert team members that new documentation is available. These
notifications include links to the generated reports and can be customized to
include key findings or action items.
