

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Tutorial: Get started with Slack
<a name="slack-setup"></a>

**Note**  
To install the Slack application, sign in to your AWS account in the AWS Management Console. Then navigate to the Amazon Q Developer in chat applications console and choose **Configure new client**. The following steps detail the full setup process.

To get started using Amazon Q Developer in chat applications to help manage your AWS infrastructure, use the following steps to set up Amazon Q Developer in chat applications with chat channels and Amazon SNS topic subscriptions.

**Topics**
+ [Prerequisites](#getting-started-prerequisites-slack)
+ [Step 1: Configure a Slack client](#slack-client-setup)
+ [Step 2: Configure a Slack channel](#slack-client-setup2)
+ [(Optional) Step 3: Test notifications from AWS services to Slack](#test-notifications-slack)
+ [Configuring Slack channels using AWS CloudFormation](#cfn-slack)
+ [Next steps](#next-steps-slack)

## Prerequisites
<a name="getting-started-prerequisites-slack"></a>

Before you get started, make sure you've completed the tasks in [Setting up Amazon Q Developer in chat applications](getting-started.md#setting-up). You will need to choose a permissions scheme in the following procedure. This scheme determines the permissions your channel members will have and what Amazon Q Developer in chat applications can do on your behalf. For more information about Amazon Q Developer in chat applications permissions, see [Understanding permissions](understanding-permissions.md). You must also create or choose a Slack channel to be used in your Amazon Q Developer in chat applications configuration. This channel is used to monitor and operate your AWS resources.

## Step 1: Configure a Slack client
<a name="slack-client-setup"></a>

To allow Amazon Q Developer in chat applications to send notifications or run commands, you must configure Amazon Q Developer in chat applications with Slack. Workspace administrators must approve the use of the Amazon Q Developer in chat applications app in the workspace. Members can request to install apps if app approval is turned on by the workspace administrator. For more information, see [Add apps to your Slack workspace](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace). 

**To configure a Slack client**

1. Add Amazon Q Developer in chat applications to the Slack workspace:

   1. In Slack, on the left navigation pane, choose **Automations**.
**Note**  
If you do not see **Automations** in the left navigation pane, choose **More**, then choose **Automations**.

   1. If Amazon Q Developer in chat applications is not listed, choose the **Browse Apps Directory** button.

   1. Browse the directory for the Amazon Q Developer in chat applications app and then choose **Add** to add Amazon Q Developer in chat applications to your workspace.

1. Open the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/).

1. Under **Configure a chat client**, choose **Slack**, then choose **Configure**.
**Note**  
After choosing **Configure**, you'll be redirected to Slack's authorization page to request permission for Amazon Q Developer in chat applications to access your information. For more information, see [Chat client application permissions for Amazon Q Developer in chat applications](app-permissions.md).

1. From the dropdown list at the top right, choose the Slack workspace that you want to use with Amazon Q Developer in chat applications.

   There's no limit to the number of workspaces that you can set up for Amazon Q Developer in chat applications, but you can set up only one at a time.

1. Choose **Allow**.

## Step 2: Configure a Slack channel
<a name="slack-client-setup2"></a>

To allow Amazon Q Developer in chat applications to send notifications or run commands in your Slack channel, you must also configure Amazon Q Developer in chat applications with a Slack channel. Configuring a channel consists of:
+ Adding Amazon Q Developer in chat applications to your Slack channel
+ Associating a channel with the configuration
+ Defining user permissions, which dictate what tasks users can perform in a channel
+ (Optional) Adding Amazon SNS topics, which Amazon Q Developer in chat applications uses to send notifications to your channel

**To configure a Slack channel**

1. Add Amazon Q Developer in chat applications to the Slack channel:

   1. In your Slack channel, enter **/invite @Amazon Q**.
**Note**  
If copying and pasting this command in Slack, ensure you have the correct formatting.

   1. Choose **Invite Them**.

1. Associate a channel with your configuration:

   1. On the **Workspace details** page in the Amazon Q Developer in chat applications console, choose **Configure new channel**.

   1. Under **Configuration details**, enter a name for your configuration. The name must be unique across your account and can't be edited later.

   1. If you want to enable logging for this configuration, choose **Publish logs to Amazon CloudWatch Logs**. For more information, see [Amazon CloudWatch Logs for Amazon Q Developer in chat applications](cloudwatch-logs.md).
**Note**  
There is an extra charge for using CloudWatch Logs.

   1. For **Slack channel**, choose the channel you used in step 1. Amazon Q Developer in chat applications supports both public and private channels.

      (Optional) To configure a private channel with Amazon Q Developer in chat applications:

      1. In Slack, copy the Channel ID of the private channel by right-clicking on the channel name in the left pane and choosing **Copy Link**. The Channel ID is the string at the end of the URL (for example, `AB3BBLZZ8YY`).

      1. In Amazon Q Developer in chat applications, paste the ID into the **Channel URL** field. (If you copy the URL of the private Slack channel, the Amazon Q Developer in chat applications console shows only the Channel ID value when you paste it into the field.)

1. Define user permissions:

   1. Choose your **Role Setting**.
**Tip**  
 Your role setting dictates what permissions your channel members have. A channel role gives all members the same permissions. This is useful if your channel members typically perform the same actions in Slack. A user role requires your channel members to choose their own roles. As such, different users in your channels can have different permissions. This is useful if your channel members are diverse or you don’t want new channel members to perform actions as soon as they join the channel. For more information, see [Role setting](understanding-permissions.md#role-settings). 

------
#### [ Channel role ]

      1. For **Role setting**, choose **Channel role**.

      1. For **Channel role**, choose **Create an IAM role using a template**. If you want to use an existing role instead, choose **Use an existing IAM role**. To use an existing IAM role, you will need to modify it for use with Amazon Q Developer in chat applications. For more information, see [Configuring an IAM Role for Amazon Q Developer in chat applications](editing-iam-roles-for-chatbot.md).

      1. For **Role name**, enter a name. Valid characters: a-z, A-Z, 0-9, .\\w\+=,.@-\_.

      1. (Optional) For **Policy template**, select **Amazon Q permissions** and any other templates you wish to use.
**Note**  
The **Amazon Q permissions** template allows you to chat with Amazon Q Developer in natural language. For more information, see [Chatting with Amazon Q Developer in chat channels](asking-questions.md).  
You can also use AWS software development kits (SDKs) to configure channels with Amazon Q permissions.

------
#### [ User roles ]

      1. For **Role setting**, choose **User roles**.

------

   1. Select the policies that will make up your [channel guardrails](understanding-permissions.md#channel-guardrails). Your channel guardrails control what actions are available to your channel members.

   1. (Optional) Add [AmazonQDeveloperAccess](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/managed-policy.html#amazonq-policy-developeraccess) as a channel guardrail to allow your users to chat with Amazon Q Developer from your Slack channel.

1. (Optional) Add Amazon SNS topics:
**Note**  
If you want to receive notifications in your Slack channel, complete these steps.

   1. Choose your notification settings:

     1. For **SNS Region**, choose the AWS Region that hosts the SNS topics for this Amazon Q Developer in chat applications subscription.

     1. For **SNS topic**, choose the Amazon SNS topic for the client subscription. This topic determines the content that's sent to the Slack channel. If the region has additional SNS topics, you can choose them from the same dropdown list. The SNS topics you choose must be configured in the services for which you want to receive notifications. For more information, see [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md).

     1. To add an Amazon SNS topic from another AWS Region to the notification subscription, choose **Add another Region**.
**Note**  
For a tutorial on subscribing existing Amazon SNS topics to Amazon Q Developer in chat applications, see [Tutorial: Subscribing an Amazon SNS topic to Amazon Q Developer in chat applications](subscribe-sns-topic.md).

        Notifications from supported services that publish to the chosen Amazon SNS topics will now appear in the Slack channel.

1. Choose **Save**. 

**Note**  
You can configure a Slack channel to run commands to your AWS account. For more information, see [Running AWS CLI commands from chat channels](chatbot-cli-commands.md).

You can configure as many channels with as many topics as you need.

## (Optional) Step 3: Test notifications from AWS services to Slack
<a name="test-notifications-slack"></a>

To verify that an Amazon Simple Notification Service (Amazon SNS) topic sends notifications to your Slack channel, you can test your setup by sending a notification. Ensure your Amazon Q Developer in chat applications configuration is subscribed to at least one Amazon SNS topic and that your topics are assigned to a service supported by Amazon Q Developer in chat applications. For a list of supported services, see [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md). You can also test notifications by using CloudWatch. For more information, see [Test notifications from AWS services to Amazon Chime or Slack using CloudWatch](test-notifications-cw.md).

**Testing notifications with configured clients**

1. Open the [Amazon Q Developer in chat applications console](https://console.aws.amazon.com/chatbot/).

1. Choose the configured client you want to test.

1. In the configured client, choose the channel to send a test notification to.

1. Choose **Send test message**.

1. View the confirmation message at the top of the screen that shows a message was sent to your Amazon SNS topic.

1. Confirm the test message in your Slack channel.

## Configuring Slack channels using AWS CloudFormation
<a name="cfn-slack"></a>

You can automate Slack channel configuration by using an CloudFormation template. To use an CloudFormation template, you need the **Workspace ID** found under **Workspace details** in the Amazon Q Developer in chat applications console. For more information, see [AWS::Chatbot::SlackChannelConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html) in the *AWS CloudFormation User Guide*.

## Next steps
<a name="next-steps-slack"></a>

After you configure your chat clients and test that your notifications are working, you might want to explore some of the following topics:
+ Learn about which other AWS services you can integrate with Amazon Q Developer in chat applications in [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md).
+ Learn about what you can customize using Amazon Q Developer in chat applications in [Customizing Amazon Q Developer in chat applications](customizing-chatbot.md).
+ Learn about what actions you can perform using Amazon Q Developer in chat applications in [Performing actions using Amazon Q Developer in chat applications](performing-actions.md).
+ Learn what questions you can ask Amazon Q Developer in chat applications in [Chatting with Amazon Q Developer in chat channels](asking-questions.md).