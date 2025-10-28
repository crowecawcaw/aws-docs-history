AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Tutorial: Create or configure an Amazon Simple Notification Service topic as a notification target for Microsoft Teams and AWS CodeStar

The notifications feature in the Developer Tools console is a notifications manager for
subscribing to events in AWS CodeBuild, AWS CodeCommit,
AWS CodeDeploy, and AWS CodePipeline. It has its own API,
AWS CodeStar. Notification rule targets defined within AWS CodeStar are
currently Amazon SNS topics or Amazon Q Developer in chat applications clients configured for Slack channels, but not Amazon Q Developer in chat applications clients
configured for Microsoft Teams. However, to receive notifications about resources of interest
in Microsoft Teams, you can use an Amazon SNS topic as a target in both your Microsoft Teams
channel configuration and your AWS CodeStar notification rules. This tutorial
describes two methods to achieve this:

- [Configure an existing Amazon SNS topic to use as a notification target](#teams-codestar-configure-teams "#teams-codestar-configure-teams").
- [Create a new Amazon SNS topic as a target by
  editing notification rules](#teams-codestar-create-teams "#teams-codestar-create-teams").

## Prerequisites

This tutorial assumes you already have some familiarity with Amazon SNS topics, AWS CodeStar, and Amazon Q Developer in chat applications.
It also assumes that you've already created at least one notification rule in AWS CodeStar and that you've configured at least one Amazon Q Developer in chat applications client for Microsoft Teams.

For more information see the following topics:

- [Tutorial: Get started with Microsoft Teams](teams-setup.md "teams-setup.md")
- [What is the Developer Tools console?](../../../dtconsole/latest/userguide/what-is-dtconsole.md "../../../dtconsole/latest/userguide/what-is-dtconsole.md") in the _Developer Tools console User Guide_.
- [What are notifications?](../../../dtconsole/latest/userguide/welcome.md "../../../dtconsole/latest/userguide/welcome.md") in the _Developer Tools console User Guide_.

## Step 1: Configure or create an Amazon SNS topic

### Configure an existing Amazon SNS topic to use as a notification target

In this procedure you edit an existing Amazon SNS topic used in your Microsoft Teams channel configuration to be used as a notification rule target in AWS CodeStar.

###### To configure an existing Amazon SNS topic to use as a notification rule target

1. Open the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. Select
   your configured Microsoft Teams chat channel.
3. Choose the channel you want to receive notifications
   in.
4. Choose **Edit**.
5. In **Notifications**, identify the name of the Amazon SNS topic you
   want to use.
6. Follow the steps in [To configure an Amazon Simple Notification Service topic to
   use as a target for AWS CodeStar notification rules](../../../dtconsole/latest/userguide/set-up-sns.md "../../../dtconsole/latest/userguide/set-up-sns.md") in the
   _Developer Tools User Guide_.
7. The Amazon SNS topic is now associated with both AWS CodeStar and your
   chosen Microsoft Teams channel configuration.

### Create a new Amazon SNS topic as a target by

editing notification rules

In this procedure you create a new Amazon SNS topic by editing an existing notification rule. You then use this Amazon SNS topic in your Microsoft Teams channel configuration.

###### To create a new Amazon SNS topic to use as a notification rule target

1. Edit your notification rule:

###### Note

The Region in which this notification rule is created must be added as a notification Region
in your Microsoft Teams configuration.

    1. Open the [Developer Tools console](https://console.aws.amazon.com/codesuite/ "https://console.aws.amazon.com/codesuite/").
    2. In the navigation pane, choose **Settings** and then choose **Notification rules.**
    3. Select the appropriate rule and choose **Edit**.
    4. In **Targets**, choose **Create target**.
    5. Choose **Amazon SNS topic** as your target type.
    6. Enter a topic name.


    ###### Note

    This topic will be used in your Microsoft Teams configuration.

2. Edit your Microsoft Teams configuration:
   1. Open the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
   2. Select your configured Microsoft Teams chat client.
   3. Select the channel in which you want to receive notifications.
   4. Choose **Edit**.
   5. (Optional) If you have no Regions or you don't currently have the Region you used for Developer Tools added, choose **Add another Region** in **Notifications** and select the appropriate Region.
   6. In **Topics**, search for and select the Amazon SNS topic you created while editing your notification rule.
   7. Choose **Configure**.
