

# Connecting Slack
<a name="connecting-to-ticketing-and-chat-connecting-slack"></a>

You can connect AWS DevOps Agent to Slack in two ways:
+ **One-way notifications** — AWS DevOps Agent posts incident response findings, root cause analyses, and mitigation plans to public or private Slack channels that you select.
+ **Bidirectional communication** — AWS DevOps Agent also receives and responds to messages in a private Slack channel. Mention the app to start a conversation. AWS DevOps Agent replies in a thread.

You can enable bidirectional communication only in private Slack channels. Public channels support one-way notifications only.

## Before you begin
<a name="before-you-begin"></a>

To connect AWS DevOps Agent with Slack, verify that you have the following:
+ Access to a Slack workspace with permission to install and authorize third-party applications.
+ Permission to configure capability providers and communications integrations in AWS DevOps Agent.
+ Permission to create IAM roles from the AWS DevOps Agent console (required for bidirectional communication).
+ The Slack channel ID for each channel that you want to associate.

Each AWS Region has its own AWS DevOps Agent app in the [Slack Marketplace](https://slack.com/marketplace/search?q=AWS+DevOps+Agent). Use the app that matches the AWS Region of your Agent Space. For example, the US East (N. Virginia) AWS Region uses the app named **AWS DevOps Agent - US East (N. Virginia)**. Europe (Frankfurt) uses **AWS DevOps Agent - EU (Frankfurt)**. To find the app for your Region, search for **AWS DevOps Agent** in the Slack Marketplace.

Throughout this guide, references to the **AWS DevOps Agent** app refer to the regional app for your Agent Space. When a command includes `<Region>`, replace it with the Region suffix shown in your app name. For example, use `US East (N. Virginia)` or `EU (Frankfurt)`. The hyphen between the app name and Region suffix is part of the literal Slack app name.

## Connecting Slack to your Agent Space
<a name="connecting-slack-to-your-agent-space"></a>

Follow these steps to register Slack, associate a channel, and optionally enable bidirectional communication.

### Step 1: Open the AWS DevOps Agent console
<a name="step-1-open-the-aws-devops-agent-console"></a>

1. Open the [AWS DevOps Agent console](https://console.aws.amazon.com/devops-agent/).

1. Open an Agent Space, and choose the **Capabilities** tab.

1. Under **Communications**, choose **Add** or **Add integration**.

![The Communications section with the Add integration button.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step1-communications.png)


### Step 2: Register Slack
<a name="step-2-register-slack"></a>

If Slack is already registered with your AWS account, choose **Add** under **Communications**, select the registered Slack workspace, and skip to [Step 5](#step-5-enter-the-slack-channel-id).

1. In the **Add a capability** dialog, search for **Slack** and choose **Register**.

![Add a capability dialog showing Slack under Communication with the Register option.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step2-register.png)


### Step 3: Review registration instructions
<a name="step-3-review-registration-instructions"></a>

1. On the **Register Slack with DevOps Agent** page, review the workspace installation steps.

1. Choose **Next** to begin the Slack authorization flow.

![Register Slack with DevOps Agent page showing the workspace installation steps.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step3-registration-steps.png)


**Note** If you use Slack Enterprise Grid, install the app directly to a workspace. Do not select an Enterprise Grid organization.

### Step 4: Authorize the Slack app
<a name="step-4-authorize-the-slack-app"></a>

1. On the Slack authorization page, choose the workspace that you want to connect from the **Workspace** dropdown.

1. Review the permissions that the app requests, and choose **Allow**.

![Slack authorization page showing the workspace selector, requested permissions, and the Allow button.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step4-authorize.png)


After authorization, Slack redirects you to the AWS DevOps Agent console and displays a success message.

### Step 5: Enter the Slack channel ID
<a name="step-5-enter-the-slack-channel-id"></a>

1. Under **Slack channel for communication**, enter the **Channel ID** of the Slack channel that you want to associate with this Agent Space.

To find the channel ID, open the channel in Slack, choose the channel name at the top, and copy the **Channel ID** from the channel details panel.

![Associate this Agent Space to your Slack channel page showing the Channel ID field and the Bidirectional communication section.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step5-channel-id.png)


### Step 6: (Optional) Enable bidirectional communication
<a name="step-6-optional-enable-bidirectional-communication"></a>

To use one-way notifications only, leave **Bidirectional mode** turned off and skip to [Step 9](#step-9-complete-the-association).

To enable bidirectional communication:

1. Under **Bidirectional communication**, turn on **Bidirectional mode**.

**Note** For private channels, you must invite the AWS DevOps Agent app to the channel before the app can receive messages.

1. Under **IAM role configuration**, choose one of the following options:
   + **Auto-create a new DevOps Agent role** — The console creates the role with the AIDevOpsChannelAccessPolicy AWS managed policy attached. You can modify the role later.
   + **Assign an existing role** — Provide the ARN of a role that AWS DevOps Agent verifies.
   + **Create a new DevOps Agent role using a policy template** — Use the provided details to create the role manually in the IAM console.

1. Choose **Next**.

![Bidirectional communication section with Bidirectional mode enabled and IAM role configuration options.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step6-bidirectional.png)


### Step 7: Invite DevOps Agent to the channel
<a name="step-7-invite-devops-agent-to-the-channel"></a>

For private channels with bidirectional mode enabled, you must add the AWS DevOps Agent app to the channel. You can skip this step for public channels used for one-way notifications only.

1. Go to the private channel in Slack.

1. Add the AWS DevOps Agent app using one of the following methods:
   + Open the channel details, choose the **Integrations** tab, choose **Add** under Apps, and search for **AWS DevOps Agent**.
   + Enter the following command in the channel, replacing `<Region>` with your Region suffix:

```text /invite @AWS DevOps Agent - <Region> ```

For example, for an Agent Space in Europe (Frankfurt):

```text /invite @AWS DevOps Agent - EU (Frankfurt) ```

![Instructions for inviting the AWS DevOps Agent app to a private Slack channel with the /invite command.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step7-invite.png)


### Step 8: Confirm the invite in Slack
<a name="step-8-confirm-the-invite-in-slack"></a>

1. In Slack, verify that you see a confirmation that the app was added to the channel. The message includes the full regional app name.

![Slack message bar showing the /invite command with the regional AWS DevOps Agent app name.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step8-invite-slack.png)


### Step 9: Complete the association
<a name="step-9-complete-the-association"></a>

1. Return to the AWS DevOps Agent console.

1. Choose **Add** to create the channel association.

![Step 2 of the Add Slack channel wizard showing the Invite DevOps Agent instructions and the Add button to complete the association.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step9-add.png)


### Step 10: Verify the association
<a name="step-10-verify-the-association"></a>

1. On the **Communications** page, confirm that the Slack association appears in the **Integrations** table.

1. If you enabled bidirectional communication, verify that the **Bidirectional** column shows **Enabled** and the **Bidirectional role** column shows the IAM role ARN.

![Communications page showing two Slack integrations with Bidirectional Enabled and IAM role ARNs.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step10-success.png)


Your Agent Space is now connected to Slack.

## Setting up bidirectional communication in Slack
<a name="setting-up-bidirectional-communication-in-slack"></a>

After you complete the association with bidirectional mode enabled, set up the channel binding from Slack:

1. In the associated private channel, send this exact app mention as a new top-level message:

```text @AWS DevOps Agent - <Region> setup ```

![A Slack message sending the setup command to the AWS DevOps Agent app.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-setup-command.png)


1. If the channel has one eligible Agent Space association, AWS DevOps Agent configures the binding and posts a confirmation.

1. If the channel has multiple eligible associations, AWS DevOps Agent posts a picker. Select the Agent Space that you want the channel to use, and wait for the confirmation.

Run setup again to repair a stale binding or to select an eligible association again. You don't need the `/setup` slash command.

## Chatting with AWS DevOps Agent in Slack
<a name="chatting-with-aws-devops-agent-in-slack"></a>

To start a conversation, mention the AWS DevOps Agent app in a new top-level message in the associated private channel and include your request. For example:

```
@AWS DevOps Agent - <Region> What can you do?
```

AWS DevOps Agent replies in a thread under your message. Open the thread to view the response, and send follow-up messages in the same thread to continue the conversation.

![A Slack channel showing a message that mentions the AWS DevOps Agent app with a reply indicator.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-chat-channel.png)


![A conversation thread showing the AWS DevOps Agent app responding with a list of capabilities.](http://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-chat-thread.png)


Mention the app in each message, including replies within the thread. Replace `<Region>` with the AWS Region suffix shown in your app name. For example:

```
@AWS DevOps Agent - <Region> Tell me more about the Lambda errors
```

Use separate top-level messages to start separate conversations. AWS DevOps Agent can help with tasks supported by your Agent Space, including:
+ Starting, viewing, and guiding investigations into incidents and operational issues
+ Exploring AWS resources, metrics, logs, and topology
+ Reviewing and responding to prevention recommendations
+ Running supported release management and testing workflows

The responses and actions available in Slack depend on the configuration and permissions of the associated Agent Space.

## Switching between bidirectional communication and one-way notifications
<a name="switching-between-bidirectional-communication-and-one-way-notifications"></a>

You can edit the Slack association at any time. Bidirectional mode can be enabled only for private channel associations:

1. Open the Agent Space, and choose **Capabilities**.

1. Under **Communications**, select the Slack association and choose **Edit**.

1. Turn **Bidirectional mode** on to allow conversations in the private channel, or turn it off to use the channel for one-way notifications only.

1. Save your changes.

To stop using a channel with the Agent Space, select its association and choose **Remove**. Removing a channel association does not unregister the Slack workspace from AWS DevOps Agent.

## Sharing a Slack workspace across multiple AWS accounts
<a name="sharing-a-slack-workspace-across-multiple-aws-accounts"></a>

You can share one Slack workspace across multiple AWS accounts. This works even when an Agent Space uses a customer managed key for encryption. You do not need a separate Slack workspace for each AWS account.

You can register the same Slack workspace with more than one Agent Space or AWS account. Each registration is independent. Registering a workspace again does not overwrite an existing registration.

## Troubleshooting Slack communication
<a name="troubleshooting-slack-communication"></a>

If AWS DevOps Agent does not respond to a message in a bidirectional channel, verify the following:
+ The Slack channel ID matches the private channel associated with the Agent Space.
+ **Bidirectional** is **Enabled** for the association in the AWS DevOps Agent console.
+ The IAM role shown for the association exists and has the permissions created by the console.
+ The regional AWS DevOps Agent app is a member of the private channel.
+ The channel binding is active. Run `@AWS DevOps Agent - <Region> setup` again if the binding appears stale.
+ The correct Agent Space association was selected if setup showed a picker.
+ The first message in a conversation mentions the regional AWS DevOps Agent app.
+ The response is not already available in a thread under the original message.

If the workspace is not available when you create an association, confirm that you registered Slack in the same AWS account and Region as your Agent Space.

**Important** Avoid uninstalling the AWS DevOps Agent app from the Slack workspace. Uninstalling the app might prevent it from being reinstalled. To stop using a channel, remove the channel association in the AWS DevOps Agent console instead.

## Providing feedback through Slack
<a name="providing-feedback-through-slack"></a>

You can submit product feedback directly in a bidirectional Slack channel. Mention the app and describe the feedback you want to file. AWS DevOps Agent summarizes your input, confirms the details with you, and submits it to the product team. Replace `<Region>` with the AWS Region suffix shown in your app name. For example:

```
@AWS DevOps Agent - <Region> I want to share feedback on how notifications work
```

### AI-generated content
<a name="ai-generated-content"></a>

We use large language models to generate investigation findings, root-cause analyses, mitigation recommendations, and conversational responses. These outputs might be inaccurate or incomplete. Verify AI-generated information before acting on it.

### Data handling and privacy
<a name="data-handling-and-privacy"></a>

We retain data associated with your Agent Space for as long as necessary to provide the service. This data includes investigation journals, chat messages, and operational data. You can delete your Agent Space at any time to remove all associated data.

To request access to or deletion of your data, delete the Agent Space through the AWS Management Console or contact [AWS Support](https://aws.amazon.com/contact-us/).

For information about how we protect your data, see [Security and data protection](aws-devops-agent-security.html). We handle information in accordance with the [AWS Privacy Notice](https://aws.amazon.com/privacy/).