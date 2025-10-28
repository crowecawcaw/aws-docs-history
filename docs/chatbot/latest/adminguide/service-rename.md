AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Amazon Q Developer in chat applications rename - Summary of changes

On February 19, 2025, we renamed AWS Chatbot to Amazon Q Developer.

If you are a current user, there is no change in functionality or impact to your current usage, pricing, and setup.

All features of AWS Chatbot are moving to Amazon Q Developer. Your code and Region availability will remain the same.

###### Note

Mentions of the name AWS Chatbot may persist in the AWS CloudFormation guide, AWS General Reference entry, and user guide page URLs.
Service principals, IAM permissions, console urls, organizations policy schemas, namespace, endpoints, and service-linked role names will remain unchanged.

###### Topics

- [What's new?](#rename-changes "#rename-changes")
- [What's staying the same?](#rename-not-changing "#rename-not-changing")
- [Pricing](#updated-pricing "#updated-pricing")
- [FAQs](#FAQS "#FAQS")
- [Updating Slack bot user app mentions when sending messages to chat channels programmatically](#update-slack-bot "#update-slack-bot")

## What's new?

AWS Chatbot is now called Amazon Q Developer. The name change is effective in Microsoft Teams and Slack chat applications, the AWS Management Console, and documentation.
The following sections describe what parts of the service have changed with the rename and what actions you need to take to ensure that your workflows run smoothly after the renaming change.

### Renamed chat applications

The AWS Chatbot for Microsoft Teams and AWS Chatbot for Slack chat applications are renamed Amazon Q Developer.
You don’t need to reinstall or upgrade the chat applications in your Microsoft Teams teams or Slack workspaces.
Notifications and interactions in the chat channels are updated to show Amazon Q Developer as the display name instead of AWS

### Updated @mentions in chat applications

If you run tasks or ask questions in chat channels, you must tag the chat application by entering `Amazon Q` instead of `@aws`.
Tagging the chat application isn’t case sensitive.
For example if you previously entered `@aws Which of my EC2 instances are currently running in us-east-1`?,
Enter `@Amazon Q Which of my EC2 instances are currently running in us-east-1?`.

If you use Slack automation workflows to send commands to the AWS Chatbot chat application, previous references to `@aws`
are automatically updated to `@Amazon Q`. If you're using webhooks to send `@aws` messages to the AWS Chatbot bot app programmatically, you'll need to change how you invoke the bot app programmatically.

###### Tip

Instead of entering `@Amazon Q`, you can enter `@Q` and choose the autocomplete recommendation that matches the app name.

### Renamed console in AWS Management Console

The references to AWS Chatbot in the AWS Management Console are updated with the name Amazon Q Developer in chat applications.
The workflows to create and manage chat configurations remain unchanged in the renamed console.

### Renamed AWS Organizations policies

AWS Chatbot organization policies (Chatbot policies) are now called Amazon Q Developer in chat applications policies (chat applications policies).
These policies allow you to control access to an organization’s accounts from chat applications like Microsoft Teams and Slack.
For more information, see [Amazon Q Developer in chat applications organization policies](chatbot-orgs-policy.md "chatbot-orgs-policy.md").
The schema for the chat application policy remains unchanged. Your existing policies will continue to function as is.

### New service improvements management options

With this launch, the setting to manage how AWS uses your content in chat applications for service improvement are now managed
under Amazon Q Developer. Amazon Q Developer may use certain content from Amazon Q Developer Free tier for service improvement. You can opt-out of this at any time. For more information, see

[Amazon Q Developer service improvement](../../../amazonq/latest/qdeveloper-ug/service-improvement.md "../../../amazonq/latest/qdeveloper-ug/service-improvement.md") in the _Amazon Q Developer User Guide_.

## What's staying the same?

Your existing chat configurations in the chat applications will continue to work as they did previously.
The APIs, SDK, service endpoints, IAM permissions, and Region availability are unaffected by this name change.
You will retain:

- Delivery of notifications for your alarms and operation events
- Ability to run CLI-based tasks using action buttons, aliases, and typed inputs
- Chat channel configurations including configured IAM permissions, channel guardrails, and Amazon SNS topic subscriptions
- Customizations such as custom notifications, actions, and aliases
- AWS Organizations Service control policies (SCPs) and chatbot management policies (now called [Amazon Q Developer in chat applications policies](#renamed-policies "#renamed-policies"))
- Tags

## Pricing

There is no change to your current usage and pricing. Non-generative AI features for sending notifications and running CLI-based commands
using action buttons, aliases, and typed-commands are still available to you at no additional cost after the renaming.
When you use Amazon Q Developer in chat applications, access is limited to the Amazon Q Developer Free tier, even when you are subscribed to Amazon Q Developer Pro tier.
This update doesn't automatically enable identity-aware sessions, which are needed to chat with Amazon Q Developer at the Pro tier. For more information,
see [Amazon Q Developer pricing](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").

## FAQs

### If I use AWS Chatbot today, what changes for me?

The chat application name changes from AWS Chatbot to Amazon Q Developer. Notifications and responses received in channels display the application name as Amazon Q instead of AWS.

When you run tasks or ask questions from your chat channels, use `@Amazon Q` instead of `@aws`.

Your Slack automation workflows that trigger commands within the AWS Chatbot app won't change with this renaming. If you currently send messages to the AWS Chatbot app programmatically using webhooks,
you'll need to change how you invoke the bot app programmatically. To invoke the app, you can use the bot app member ID or change the bot app name in your workspace to `aws`. For more information, see [Updating Slack bot user app mentions when sending messages to chat channels programmatically](#update-slack-bot "#update-slack-bot").

### Do I need an Amazon Q Developer subscription to continue using AWS Chatbot?

No, you don't need a Amazon Q Developer subscription to continue using the non-generative AI features you previously used with AWS Chatbot.

To enable Amazon Q Developer generative AI features in your chat channels, you need to add the `AmazonQDeveloperAccess` managed policy to your IAM role and channel guardrails.

For more information, see [Chatting with Amazon Q Developer in chat channels](asking-questions.md "asking-questions.md").

In chat applications, Amazon Q Developer access is limited to the Free tier only. For customers on Amazon Q Developer Pro tier, access is limited to Free tier usage limits.

### What should I do if I need to disable generative AI features of Amazon Q Developer in chat applications?

To disable Amazon Q Developer generative AI features in a chat channel, you must remove the `AmazonQDeveloperAccess` managed policy from your IAM role or add
restrictions to your channel guardrails. For more information, see [Manage access to Amazon Q Developer with policies](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md")
in the _Amazon Q Developer User Guide_.

You can also control what Amazon Q Developer features are available in your organization by creating a Service Control Policy (SCP) that specifies permissions for some Amazon Q Developer actions.
For more information, see [Manage access with service control policies (SCPs)](../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md#service-control-policies "../../../amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.md#service-control-policies")
in the _Amazon Q Developer User Guide_.

## Updating Slack bot user app mentions when sending messages to chat channels programmatically

If you send messages programmatically to Slack chat channels using webhooks or APIs with messages formated as `<@aws> `message``, you'll need to make a change to continue invoking the Slack
bot user.

### (Recommended) Use member ID in @mention instead of the bot name

Use member IDs instead of instead of `@aws` or `@Amazon Q` when mentioning users and the bot user. A member ID is a unique identifier assigned to each user within a Slack workspace. The member ID for the bot user is unique to each Slack workspace. Member IDs always resolve to the correct chat app, regardless
of the display name. For more information, see [Mentioning Users](https://api.slack.com/reference/surfaces/formatting#mentioning-users "https://api.slack.com/reference/surfaces/formatting#mentioning-users") in the Slack API reference.

###### To update @mentions using a member ID

1. Open Slack
2. Choose the bot user and open the **Profile** sidebar.
3. Choose the vertical ellipses (**⋮**).
4. Choose **Copy member ID**.
5. In your code, update mentions of `<@aws>` to `<@Member-ID>`.

### Workaround: Rename the bot in your workspace

You can change the name of the bot user in your Slack workspace from Amazon Q to aws. This allows your existing programmatic invocations to continue functioning with `@aws` app mentions.

###### Note

This rename applies to your workspace, not just individual channels.

###### To rename the bot in your workspace

1. Open Slack
2. Choose your workspace name in the sidebar.
3. Choose **Tools & settings** from the menu and choose **Manage apps**.
4. Choose the **App Details** tab.
5. In **App Details**, choose the **Configuration** tab.
6. In **Bot User**, choose **Edit**.
7. Change the bot user name from **Amazon Q** to **aws**.
8. Invoke the bot app using `@aws `command`` in your chat channels.
