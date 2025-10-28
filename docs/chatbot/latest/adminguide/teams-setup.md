AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Tutorial: Get started with Microsoft Teams

To get started using Amazon Q Developer in chat applications to help manage your AWS infrastructure, follow the steps below to set up Amazon Q Developer in chat applications with chat channels and Amazon SNS topic subscriptions. Note that Amazon Q Developer in chat applications is approved by your Microsoft Teams administrator.

###### Topics

- [Prerequisites](#getting-started-prerequisites-teams "#getting-started-prerequisites-teams")
- [Step 1: Configure a Microsoft Teams client](#teams-client-setup "#teams-client-setup")
- [Step 2: Configure a Microsoft Teams channel](#teams-client-setup-2 "#teams-client-setup-2")
- [(Optional) Step 3: Test notifications from AWS services to Microsoft Teams](#test-notifications-teams "#test-notifications-teams")
- [Configuring Microsoft Teams channels using AWS CloudFormation](#cfn-teams "#cfn-teams")
- [Next steps](#next-steps-teams "#next-steps-teams")

## Prerequisites

Before you get started, make sure you've completed the tasks in [Setting up Amazon Q Developer in chat applications](getting-started.md#setting-up "getting-started.md#setting-up"). You should also ensure Microsoft Teams is installed and approved by your organization administrator. You will need to choose a permissions scheme in the following procedure.
This scheme determines the permissions your channel members will have and what Amazon Q Developer in chat applications can do on your behalf. For more information about Amazon Q Developer in chat applications permissions, see [Understanding permissions](understanding-permissions.md "understanding-permissions.md")
You must also create or choose a channel to be used in your Amazon Q Developer in chat applications configuration. This channel is used to monitor and operate your AWS resources.

###### Note

The following IAM permissions are required to create a Microsoft Teams configuration:

- GetMicrosoftTeamsOauthParameters
- RedeemMicrosoftTeamsOauthCode
- CreateMicrosoftTeamsChannelConfiguration
  If you have less than administrative permissions, ensure you have the aforementioned permissions to create a configuration.

## Step 1: Configure a Microsoft Teams client

To allow Amazon Q Developer in chat applications to send notifications or run commands in your Microsoft Teams channel, you must configure
Amazon Q Developer in chat applications with Microsoft Teams.

###### To configure a Microsoft Teams client

1. Add Amazon Q Developer in chat applications to your team:
   1. In Microsoft Teams, find your team name and choose **...**, then choose **Manage team**.
   2. Choose **Apps**, then choose **More apps**.
   3. Enter `Amazon Q Developer` in the search bar to find Amazon Q Developer in chat applications.
   4. Select the bot.
   5. Choose **Add to a team** and complete the prompt.

2. Open the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
3. Under **Configure a chat client**, choose **Microsoft Teams**, then choose **Configure client**.
4. Copy and paste your Microsoft Teams channel URL.

###### Tip

Your channel URL contains your tenant, team, and channel IDs. You can find your channel URL by right clicking on the channel in your Microsoft Teams channel list and copying the link. Your channel ID is the portion of your channel URL after the path `/channel/`,
starting with `19%3` and likely ending with either `thread.tacv2` or `thread.skype`.

For example, the bolded portion of the following channel URL is its channel ID: `https://teams.microsoft.com/l/channel/**19%3Ae5eace25j32023jga835103358eapge3t8235%40thread.tacv2**/ChannelName?groupId=0d36500a-6023-419c-8c36-7e21f19b0135&tenantId=5fe61832-9f46-403b-a7db-cf9cf2e38199`. 5. Choose **Configure**.

###### Note

After choosing **Configure**, you're redirected to Microsoft Team's authorization page to request permission for Amazon Q Developer in chat applications to access your information. For more information, see [Chat client application permissions for Amazon Q Developer in chat applications](app-permissions.md "app-permissions.md"). 6. On the Microsoft Teams authorization page, choose **Accept**.

## Step 2: Configure a Microsoft Teams channel

To allow Amazon Q Developer in chat applications to send notifications or run commands in your Microsoft Teams channel, you must also configure
Amazon Q Developer in chat applications with a Microsoft Teams channel. Channel configuration consists of:

- Associating a channel with the configuration
- Defining user permissions, which dictate what tasks users can perform in a channel
- (Optional) Adding Amazon SNS topics, which Amazon Q Developer in chat applications uses to send notifications to your channel

###### Note

Microsoft Teams doesn't currently support Amazon Q Developer in chat applications in private channels.
For more information, see [Private channel limitations](https://learn.microsoft.com/en-us/microsoftteams/private-channels#private-channel-limitations "https://learn.microsoft.com/en-us/microsoftteams/private-channels#private-channel-limitations").

###### To configure a Microsoft Teams channel

1.  Associate a channel with your configuration:
    1. On the **Team details** page in the Amazon Q Developer in chat applications console, choose **Configure new channel**.
    2. Under **Configuration details**, enter a name for your configuration. The name must be unique across your account and can't be edited later.
    3. If you want to enable logging for this configuration, choose **Publish logs to Amazon CloudWatch Logs**. For more information, see [Amazon CloudWatch Logs for Amazon Q Developer in chat applications](cloudwatch-logs.md "cloudwatch-logs.md").

    ###### Note

    There is an extra charge for using CloudWatch Logs. 4. For **Team channel**, paste your Microsoft Teams channel URL.

2.  Define user permissions:
    1. Choose your **Role Setting**.

    ###### Tip

    Your role setting dictates what permissions your channel members have. A channel role gives all members the same permissions.
    This is useful if your channel members typically perform the same actions in Microsoft Teams.
    A user role requires your channel members to choose their own roles. As such, different users in your channels can have different permissions.
    This is useful if your channel members are diverse or you don’t want new channel members to perform actions as soon as they join the channel. For more information, see [Role setting](understanding-permissions.md#role-settings "understanding-permissions.md#role-settings").

    Channel role

        1. For **Role setting**, choose **Channel role**.
        2. For **Channel role**, choose **Create an IAM role using a template**. If you want to use an existing role instead, choose **Use an existing IAM role**.
         To use an existing IAM role, you will
         need to modify it for use with Amazon Q Developer in chat applications. For more information, see [Configuring an IAM Role
         for Amazon Q Developer in chat applications](editing-iam-roles-for-chatbot.md "editing-iam-roles-for-chatbot.md").
        3. For **Role name**, enter a name. Valid characters: a-z, A-Z,
         0-9, .\w+=,.@-\_.
        4. (Optional) For **Policy template**, select **Amazon Q permissions** and any other templates you wish to use.


        ###### Note

        The **Amazon Q permissions** template allows you to chat with Amazon Q Developer in natural language. For more information, see [Chatting with Amazon Q Developer in chat channels](asking-questions.md "asking-questions.md").

        You can also use AWS software development kits (SDKs) to configure channels with Amazon Q permissions.

    User roles

        1. For **Role setting**, choose **User roles**.

    2. Select the policies that will make up your [channel guardrails](understanding-permissions.md#channel-guardrails "understanding-permissions.md#channel-guardrails"). Your channel guardrails control what actions are available to your channel members.
    3. (Optional) Add [AmazonQDeveloperAccess](../../../amazonq/latest/qdeveloper-ug/managed-policy.md#amazonq-policy-developeraccess "../../../amazonq/latest/qdeveloper-ug/managed-policy.md#amazonq-policy-developeraccess") as a channel guardrail to allow your users to chat with Amazon Q Developer in natural language from your Microsoft Teams channel.

3.  (Optional) Add Amazon SNS topics:

###### Note

If you want to receive notifications in your Microsoft Teams channel, complete these steps.

    1. Choose your notification settings:


    	1. For **SNS Region**, choose the AWS Region that hosts the SNS
    	 topics for this Amazon Q Developer in chat applications subscription.
    	2. For **SNS topic**, choose the Amazon SNS topic for the client
    	 subscription. This topic determines the content that's sent to the Microsoft Teams channel. If
    	 the region has additional SNS topics, you can choose them from the same dropdown
    	 list. The SNS topics you choose must be configured in the services for which you want to
    	 receive notifications. For more information, see [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md "related-services.md").
    	3. To add an Amazon SNS topic from another AWS Region to the notification
    	 subscription, choose **Add another Region**.


    	###### Note

    	For a tutorial on subscribing existing Amazon SNS topics to Amazon Q Developer in chat applications, see [Tutorial: Subscribing an Amazon SNS topic to Amazon Q Developer in chat applications](subscribe-sns-topic.md "subscribe-sns-topic.md").


    	Notifications from supported services that publish to the chosen Amazon SNS topics will now
    	 appear in the Microsoft Teams channel.

4. Choose **Configure**.

###### Note

You can configure a Microsoft Teams channel to run commands to your AWS account. For more
information, see [Running AWS CLI commands from chat
channels](chatbot-cli-commands.md "chatbot-cli-commands.md").

You can configure as many channels with as many topics as you need.

## (Optional) Step 3: Test notifications from AWS services to Microsoft Teams

To verify that an Amazon Simple Notification Service (Amazon SNS) topic sends notifications to your Microsoft Teams
channel, you can test your setup by sending a notification. Ensure your
Amazon Q Developer in chat applications configuration is subscribed to at least one Amazon SNS topic and that your topics are assigned to a service supported by Amazon Q Developer in chat applications. For a list of supported
services, see [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md "related-services.md"). You can
also test notifications by using CloudWatch. For more information, see [Test notifications from AWS services to Microsoft Teams
using CloudWatch](test-notifications-cw.md "test-notifications-cw.md").

###### Testing notifications with configured clients

1. Open the [Amazon Q Developer in chat applications
   console](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. Choose the configured client you want to test.
3. In the configured client, choose the channel to send a test notification to.
4. Choose **Send test message**.
5. View the confirmation message at the top of the screen that shows a message was sent to your
   Amazon SNS topic.
6. Confirm the test message in your Microsoft Teams channel.

## Configuring Microsoft Teams channels using AWS CloudFormation

You can automate Microsoft Teams channel configuration by using an AWS CloudFormation template. To use an AWS CloudFormation template, you need the **Team ID** and **Tenant ID** found under **Team details** in the Amazon Q Developer in chat applications console.
For more information, see [AWS::Chatbot::MicrosoftTeamsChannelConfiguration](../../../AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.md")
in the _AWS CloudFormation User Guide_.

## Next steps

After you configure your chat clients and test that your notifications are working, you might want to explore some of the following topics:

- Learn about which other AWS services you can integrate with Amazon Q Developer in chat applications in [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md "related-services.md").
- Learn about what you can customize using Amazon Q Developer in chat applications in [Customizing Amazon Q Developer in chat applications](customizing-chatbot.md "customizing-chatbot.md").
- Learn about what actions you can perform using Amazon Q Developer in chat applications in [Performing actions using Amazon Q Developer in chat applications](performing-actions.md "performing-actions.md").
- Learn what questions you can ask Amazon Q Developer in chat applications in [Chatting with Amazon Q Developer in chat channels](asking-questions.md "asking-questions.md").
- Learn how to receive AWS CodeStar notifications in your channels in [Tutorial: Receive Developer Tools notifications in Microsoft Teams](teams-codestar.md#teams-codestar.title "teams-codestar.md#teams-codestar.title").
