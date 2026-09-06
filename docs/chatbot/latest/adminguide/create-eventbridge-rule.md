

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Tutorial: Creating an Amazon EventBridge rule that sends notifications to Amazon Q Developer in chat applications
<a name="create-eventbridge-rule"></a>

Amazon Q Developer in chat applications currently supports notifications for most service events that are handled by Amazon EventBridge. When you create a rule for events, you tell EventBridge what action to take for events that match the rule. In this tutorial, you create a rule to use Amazon Q Developer in chat applications to generate an Amazon SNS topic notification that will appear in your Microsoft Teams channel, Slack channel or Amazon Chime chatroom.

**Tip**  
You might create an EventBridge rule that unintentionally sends too many notifications to your chat channels. This typically happens with EventBridge rules that trigger on API calls via AWS CloudTrail. To better control the number of notifications you generate, write your EventBridge rules with event pattern based filtering. For more information about EventBridge event patterns, see [Content-based filtering in Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.html) in the *EventBridge User Guide*.

## Prerequisites
<a name="prerequisites"></a>

For this tutorial, you need a Amazon Chime, Microsoft Teams, or Slack client for Amazon Q Developer in chat applications. For more information, see [Getting started with Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

You also need to set up Amazon Simple Notification Service. Your Amazon SNS topic is used in the creation of your EventBridge rule and should be identical to the Amazon SNS topic used in your Amazon Q Developer in chat applications configuration. If you don't have any Amazon SNS topics yet, follow the steps in [Getting Started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the *Amazon Simple Notification Service Developer Guide*.

 For more information about EventBridge, see [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) in the *EventBridge User Guide*. 

## Step 1: Create an Amazon EventBridge Rule
<a name="creating-ebrule"></a>

Receiving notifications about events of interest in your Amazon Chime chat room, Microsoft Teams channel, or Slack channel is a convenient way to monitor service processes. In this tutorial, you create an EventBridge rule to use Amazon Q Developer in chat applications to generate an Amazon SNS topic notification that will appear in your chat channel or chat room. It is important to note that you only receive notifications from Amazon SNS topics that are used in your Amazon Q Developer in chat applications configuration.

**To create an EventBridge rule**

1. Open the [EventBridge console.](https://console.aws.amazon.com/events/)

1. In the navigation pane, choose **Rules**.

1. Choose ** Create rule**.

1. Enter a name and description for the rule. A rule must have a unique name from other rules in the same Region.

1. Choose **Next**.

1. For **Event source**, choose **AWS events or EventBridge partner events**.

1. For **Creation method**, choose **Use pattern form**.

1. In **Event Pattern**, for **Event source**, choose **AWS services**.

1. For **AWS service**, select the service that emits the event.

1. For **Event type**, select the event you're interested in.
**Important**  
Choosing **All Events** as your service provider can result in increased costs and notifications. 
**Tip**  
You can edit event patterns by choosing **Edit pattern** and then choosing **Save**.
**Note**  
Currently only AWS Services are supported.

1. Choose **Next**.

1. In **Target types**, select **AWS service**.

1. In **Select a target**, select **SNS Topic**.

1. For **Topic**, choose the appropriate topic.
**Note**  
This topic should be the same topic used in your Amazon Q Developer in chat applications configuration.

1. 

**(Optional) To create a custom notification**

   1. Choose **Additional settings**.

   1. In **Configure target input**, select **Input transformer**.

   1. Choose **Configure input transformer**.

   1.  (Optional) In **Sample events**, search for an event type of interest and note the parameter names. 

   1. In **Target input transformer**, enter your key-value pairs.

   1. In **Template**, enter a JSON object using the custom notifications event schema.

   1. (Optional) Choose **Generate output** to see what your custom notification will look like.

   1. Choose **Confirm**.
**Note**  
For more information on input transformers, see [Amazon EventBridge input transformation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html) in the *Amazon EventBridge User Guide*.

1. (Optional) To add additional targets, choose **Add target**.

1. Choose **Next**.

1. (Optional) Add tags.

1. Choose **Next**.

1. Choose **Create rule**.

After the rule is created, you can view, edit, or delete it in the console under **Rules**. When an event occurs that matches the rule, you receive a notification in your chat channel or Amazon Chime chat room from Amazon Q Developer in chat applications.

For information about testing your rule, see [Test notifications from AWS services to chat channels using CloudWatch](chime-setup.md#test-notifications).

## Step 2: Receive Amazon EventBridge event notifications between AWS accounts and Regions
<a name="cross-account-ebrule"></a>

You can receive EventBridge event notifications between AWS accounts and Regions in your chat channels and chat rooms using one Amazon Q Developer in chat applications and one Amazon SNS topic. To do this, use the Amazon SNS topic in your Amazon Q Developer in chat applications configuration as the target for your *receiver* account's EventBridge rule. With this mechanism, you don’t have to configure Amazon Q Developer in chat applications in each AWS account you want to receive notifications from. If you have multiple accounts with multiple resources you want to monitor, you can configure Amazon Q Developer in chat applications in one account and have all other accounts send their events to the account with Amazon Q Developer in chat applications using EventBridge. For more information about sending and receiving events across accounts and Regions, see [Sending and receiving EventBridge events between AWS accounts and Regions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html) in the *Amazon EventBridge User Guide*. 

## (Optional) Step 3: Delete an Amazon EventBridge rule
<a name="deleting-ebrule"></a>

You can remove any resources created for this tutorial by navigating to the EventBridge console and deleting the resource.

**To delete or disable an EventBridge rule**
+ To delete or disable an EventBridge rule, see [Deleting or Disabling a Rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/delete-or-disable-rule.html) in the *EventBridge User Guide*.