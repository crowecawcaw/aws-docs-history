AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Tutorial: Creating an Amazon EventBridge rule that sends

notifications to Amazon Q Developer in chat applications

Amazon Q Developer in chat applications currently supports notifications for most service events that are handled by
Amazon EventBridge. When you create a rule for events, you tell EventBridge what action to take for events
that match the rule. In this tutorial, you create a rule to use Amazon Q Developer in chat applications to generate an Amazon SNS
topic notification that will appear in your Microsoft Teams channel, Slack channel or Amazon Chime chatroom.

###### Tip

You might create an EventBridge rule that unintentionally sends too many notifications to your chat channels.
This typically happens with EventBridge rules that trigger on API calls via AWS CloudTrail. To better control the number of notifications
you generate, write your EventBridge rules with event pattern based filtering. For more information about EventBridge event patterns, see
[Content-based filtering in Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.md "../../../eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.md")
in the _EventBridge User Guide_.

## Prerequisites

For this tutorial, you need a Amazon Chime, Microsoft Teams, or Slack client for Amazon Q Developer in chat applications. For more
information, see [Getting started with Amazon Q Developer in chat applications](getting-started.md "getting-started.md") in
the _Amazon Q Developer in chat applications Administrator Guide_.

You also need to set up Amazon Simple Notification Service. Your Amazon SNS topic is used in the creation of your EventBridge rule
and should be identical to the Amazon SNS topic used in your Amazon Q Developer in chat applications configuration. If you don't have any Amazon SNS topics yet, follow the steps
in [Getting Started with
Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the _Amazon Simple Notification Service Developer
Guide_.

For more information about EventBridge, see [What Is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the
_EventBridge User Guide_.

## Step 1: Create an Amazon EventBridge Rule

Receiving notifications about events of interest in your Amazon Chime chat room, Microsoft Teams channel, or Slack channel
is a convenient way to monitor service processes. In this tutorial, you create an EventBridge rule
to use Amazon Q Developer in chat applications to generate an Amazon SNS topic notification that will appear in your chat channel
or chat room. It is important to note that you only receive notifications from Amazon SNS topics that
are used in your Amazon Q Developer in chat applications configuration.

###### To create an EventBridge rule

1. Open the [EventBridge console.](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/")
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. A rule must have a unique name from other
   rules in the same Region.
5. Choose **Next**.
6. For **Event source**, choose **AWS events or EventBridge partner events**.
7. For **Creation method**, choose **Use pattern form**.
8. In **Event Pattern**, for **Event source**, choose **AWS
   services**.
9. For **AWS service**, select the service that emits the event.
10. For **Event type**, select the event you're interested in.

###### Important

Choosing **All Events** as your service provider can result in
increased costs and notifications.

###### Tip

You can edit event patterns by choosing **Edit pattern** and then choosing
**Save**.

###### Note

Currently only AWS Services are supported. 11. Choose **Next**. 12. In **Target types**, select **AWS service**. 13. In **Select a target**, select
**SNS Topic**. 14. For **Topic**, choose the appropriate topic.

###### Note

This topic should be the same topic used in your Amazon Q Developer in chat applications configuration. 15. ###### (Optional) To create a custom notification

    1. Choose **Additional settings**.
    2. In **Configure target input**, select **Input transformer**.
    3. Choose **Configure input transformer**.
    4. (Optional) In **Sample events**, search for an event type of interest and note the parameter names.
    5. In **Target input transformer**, enter your key-value pairs.
    6. In **Template**, enter a JSON object using the custom notifications event schema.
    7. (Optional) Choose **Generate output** to see what your custom notification will look like.
    8. Choose **Confirm**.


    ###### Note

    For more information on input transformers, see [Amazon EventBridge input transformation](../../../eventbridge/latest/userguide/eb-transform-target-input.md "../../../eventbridge/latest/userguide/eb-transform-target-input.md") in the *Amazon EventBridge User Guide*.

16. (Optional) To add additional targets, choose **Add target**.
17. Choose **Next**.
18. (Optional) Add tags.
19. Choose **Next**.
20. Choose **Create rule**.
    After the rule is created, you can view, edit, or delete it in the console
    under **Rules**. When an event occurs that matches the rule, you receive a
    notification in your chat channel or Amazon Chime chat room from Amazon Q Developer in chat applications.

For
information about testing your rule, see [Test notifications
from AWS services to chat channels using CloudWatch](chime-setup.md#test-notifications "chime-setup.md#test-notifications").

## Step 2: Receive Amazon EventBridge event notifications between AWS accounts and Regions

You can receive EventBridge event notifications between AWS accounts and Regions in your chat channels and chat rooms using one Amazon Q Developer in chat applications and one Amazon SNS topic.
To do this, use the Amazon SNS topic in your Amazon Q Developer in chat applications configuration as the target for your _receiver_ account's EventBridge rule. With this mechanism, you don’t have to configure Amazon Q Developer in chat applications in each AWS account you want to receive notifications from.
If you have multiple accounts with multiple resources you want to monitor, you can configure Amazon Q Developer in chat applications in one account and have all other accounts send their events to the account with Amazon Q Developer in chat applications using EventBridge.
For more information about sending and receiving events across accounts and Regions, see [Sending and receiving EventBridge events between AWS accounts and Regions](../../../eventbridge/latest/userguide/eb-cross-account.md "../../../eventbridge/latest/userguide/eb-cross-account.md") in the _Amazon EventBridge User Guide_.

## (Optional) Step 3: Delete an Amazon EventBridge rule

You can remove any resources created for this tutorial by navigating to the EventBridge
console and deleting the resource.

###### To delete or disable an EventBridge rule

- To delete or disable an EventBridge rule, see [Deleting or Disabling a
  Rule](../../../eventbridge/latest/userguide/delete-or-disable-rule.md "../../../eventbridge/latest/userguide/delete-or-disable-rule.md") in the _EventBridge User Guide_.
