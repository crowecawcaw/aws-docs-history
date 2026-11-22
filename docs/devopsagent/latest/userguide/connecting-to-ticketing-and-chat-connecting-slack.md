

# Connecting Slack

You can connect AWS DevOps Agent to Slack in two ways:
+ **One-way notifications** – AWS DevOps Agent posts incident response findings, root cause analyses, and mitigation plans to public or private Slack channels that you select.
+ **Bidirectional communication** – AWS DevOps Agent also receives and responds to messages in a private Slack channel. Mention the app to start a conversation. AWS DevOps Agent replies in a thread. You can also move an investigation into its own Slack code channel. For more information, see [Using Slack code channels](connecting-to-ticketing-and-chat-using-slack-code-channels.html).

You can enable bidirectional communication only in private Slack channels. Public channels support one-way notifications only.

## Before you begin
<a name="before-you-begin"></a>

To connect AWS DevOps Agent with Slack, verify that you have the following:
+ Access to a Slack workspace with permission to install and authorize third-party applications.
+ Permission to configure capability providers and communications integrations in AWS DevOps Agent.
+ Permission to create IAM roles from the AWS DevOps Agent console (required for bidirectional communication).
+ The Slack channel ID for each channel that you want to associate.
+ A member of the channel who can approve the authorization request that AWS DevOps Agent posts to the channel when you create the association.

Each AWS Region has its own AWS DevOps Agent app in the [Slack Marketplace](https://slack.com/marketplace/search?q=AWS+DevOps+Agent). Use the app that matches the AWS Region of your Agent Space. For example, the US East (N. Virginia) AWS Region uses the app named **AWS DevOps Agent - US East (N. Virginia)**. Europe (Frankfurt) uses **AWS DevOps Agent - EU (Frankfurt)**. To find the app for your Region, search for **AWS DevOps Agent** in the Slack Marketplace.

Throughout this guide, references to the **AWS DevOps Agent** app refer to the regional app for your Agent Space. When a command includes `<Region>`, replace it with the Region suffix shown in your app name. For example, use `US East (N. Virginia)` or `EU (Frankfurt)`. The hyphen between the app name and Region suffix is part of the literal Slack app name.

## Connecting Slack to your Agent Space
<a name="connecting-slack-to-your-agent-space"></a>

Follow these steps to register Slack, associate a channel, optionally enable bidirectional communication, and authorize the channel.

### Step 1: Open the AWS DevOps Agent console
<a name="step-1-open-the-aws-devops-agent-console"></a>

1. Open the [AWS DevOps Agent console](https://console.aws.amazon.com/aidevops/home).

1. Open an Agent Space, and choose the **Capabilities** tab.

1. Under **Communications**, choose **Add** or **Add integration**.

![The Communications section with the Add integration button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step1-communications.png)


### Step 2: Register Slack
<a name="step-2-register-slack"></a>

If Slack is already registered with your AWS account, choose **Add** under **Communications**, select the registered Slack workspace, and skip to [Step 5](#step-5-enter-the-slack-channel-id).

1. In the **Add a capability** dialog, search for **Slack** and choose **Register**.

![Add a capability dialog showing Slack under Communication with the Register option.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step2-register.png)


### Step 3: Review registration instructions
<a name="step-3-review-registration-instructions"></a>

1. On the **Register Slack with DevOps Agent** page, review the workspace installation steps.

1. Choose **Next** to begin the Slack authorization flow.

![Register Slack with DevOps Agent page showing the workspace installation steps.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step3-registration-steps.png)


**Note** If you use Slack Enterprise Grid, install the app directly to a workspace. Do not select an Enterprise Grid organization.

### Step 4: Authorize the Slack app
<a name="step-4-authorize-the-slack-app"></a>

1. On the Slack authorization page, choose the workspace that you want to connect from the **Workspace** dropdown.

1. Review the permissions that the app requests, and choose **Allow**.

![Slack authorization page showing the workspace selector, requested permissions, and the Allow button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step4-authorize.png)


After authorization, Slack redirects you to the AWS DevOps Agent console and displays a success message.

### Step 5: Enter the Slack channel ID
<a name="step-5-enter-the-slack-channel-id"></a>

1. Under **Slack channel for communication**, enter the **Channel ID** of the Slack channel that you want to associate with this Agent Space.

To find the channel ID, open the channel in Slack, choose the channel name at the top, and copy the **Channel ID** from the channel details panel.

![Associate this Agent Space to your Slack channel page showing the Channel ID field and the Bidirectional communication section.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step5-channel-id.png)


### Step 6: (Optional) Enable bidirectional communication
<a name="step-6-optional-enable-bidirectional-communication"></a>

To use one-way notifications only, leave **Bidirectional mode** turned off and skip to [Step 9](#step-9-complete-the-association).

To use bidirectional mode, give the channel a role that has the permissions of the `AIDevOpsChannelAccessPolicy` AWS managed policy. If you choose **Assign an existing role** or create a role from the policy template, attach this policy to the role. You can also add the statements of this policy to the permissions policy of the role. For more information, see [AIDevOpsChannelAccessPolicy](aws-devops-agent-security-devops-agent-iam-permissions.html#aidevopschannelaccesspolicy).

To enable bidirectional communication:

1. Under **Bidirectional communication**, turn on **Bidirectional mode**.

**Note** Invite the AWS DevOps Agent app to the channel so that the app can receive messages. Use a private channel for bidirectional mode. If you use a public channel, the app cannot send or receive bidirectional messages.

1. Under **IAM role configuration**, choose one of the following options:
   + **Auto-create a new DevOps Agent role** — The console creates the role with the AIDevOpsChannelAccessPolicy AWS managed policy attached. You can modify the role later.
   + **Assign an existing role** — Provide the ARN of a role that AWS DevOps Agent verifies.
   + **Create a new DevOps Agent role using a policy template** — Use the provided details to create the role manually in the IAM console.

1. Choose **Next**.

![Bidirectional communication section with Bidirectional mode enabled and IAM role configuration options.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step6-bidirectional.png)


### Step 7: Invite DevOps Agent to the channel
<a name="step-7-invite-devops-agent-to-the-channel"></a>

Add the AWS DevOps Agent app to the channel. For bidirectional mode, the channel must be private. Invite the app before you complete the association in [Step 9](#step-9-complete-the-association). When you create the association, AWS DevOps Agent posts an authorization request to the channel, and it can post only to a channel that the app is in.

1. Open your Slack channel.

1. Add the AWS DevOps Agent app using one of the following methods:
   + Open the channel details, choose the **Integrations** tab, choose **Add** under Apps, and search for **AWS DevOps Agent**.
   + Enter the following command in the channel, replacing `<Region>` with your Region suffix:

``` /invite @AWS DevOps Agent - <Region> ```

For example, for an Agent Space in Europe (Frankfurt):

``` /invite @AWS DevOps Agent - EU (Frankfurt) ```

### Step 8: Confirm the invite in Slack
<a name="step-8-confirm-the-invite-in-slack"></a>

1. In Slack, verify that you see a confirmation that the app was added to the channel. The message includes the full regional app name.

![Slack message bar showing the /invite command with the regional AWS DevOps Agent app name.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step8-invite-slack.png)


### Step 9: Complete the association
<a name="step-9-complete-the-association"></a>

When you create the association, AWS DevOps Agent posts an authorization request to the channel, and any channel member can approve it. Read [Step 10](#step-10-authorize-the-channel) before you continue.

1. Return to the AWS DevOps Agent console.

1. Choose **Add** to create the channel association.

![Step 2 of the Add Slack channel wizard showing the Invite DevOps Agent instructions and the Add button to complete the association.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step9-add.png)


### Step 10: Authorize the channel
<a name="step-10-authorize-the-channel"></a>

When you choose **Add**, AWS DevOps Agent posts an authorization request to the channel. The message is titled **AWS DevOps Agent authorization request** and reads: "AWS account *account-id* requested to connect an agent space to this channel. AWS DevOps Agent will not post here until a member of this channel authorizes the request." Below that text, the message lists the Agent Space ID, the AWS account ID, and the AWS Region, and has **Authorize** and **Deny** buttons. Until a channel member chooses **Authorize**, AWS DevOps Agent withholds notifications and does not answer mentions in the channel, and the association shows **Pending** in the console.

The following image shows the authorization request in the channel.

![Authorization request message in Slack with the Authorize and Deny buttons.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step10-authorization-request.png)


1. In Slack, open the channel and find the message titled **AWS DevOps Agent authorization request**.

1. Confirm that the AWS account ID and the Agent Space ID in the message are the ones you expect.

1. Choose **Authorize**. Slack opens the **Authorize notifications?** dialog with the **Cancel** and **Authorize** buttons and the text "Allow AWS account *account-id* (agent space *agent-space-id*) to send AWS DevOps Agent notifications to this channel."

1. Choose **Authorize** in the dialog. The message updates to show who authorized the request, and delivery starts. To refuse the request, choose **Deny**, and then choose **Deny** in the confirmation dialog. After a denial, remove the association, or create it again to send a new request.

The following image shows the **Authorize notifications?** dialog from step 3.

![Authorize notifications dialog in Slack with the Cancel and Authorize buttons.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step10-authorization-confirm.png)


The following image shows the message after a channel member authorizes the request. The message reads "Authorized by *name*. AWS DevOps Agent notifications from AWS account *account-id* are enabled in this channel."

![Authorization request message in Slack after a channel member authorized it.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step10-authorized-message.png)


**Important**  
Any member of the channel can approve or deny the request, not only the person who created the association or a workspace admin. In a Slack Connect channel, this includes members from other organizations. Approving connects the channel to an Agent Space in the AWS account shown in the message: notifications from that Agent Space post to the channel, and with bidirectional communication, every channel member can send requests to it. We recommend that you associate channels whose members you trust to make this decision, and that channel members choose **Authorize** only for requests from AWS account IDs they recognize.

### Step 11: Verify the association
<a name="step-11-verify-the-association"></a>

1. On the **Communications** page, confirm that the Slack association appears in the **Integrations** table.

1. Confirm that the **Status** column shows **Valid**. It shows **Pending** until a channel member approves the authorization request from [Step 10](#step-10-authorize-the-channel).

1. If you enabled bidirectional communication, verify that the **Bidirectional** column shows **Enabled** and the **Bidirectional role** column shows the IAM role ARN.

The following image shows the **Integrations** table with two Slack associations. The first row is a channel whose authorization request a member approved, so its **Status** is **Valid**. The second row is a channel whose request is still open, so its **Status** is **Pending**. Both rows show **Enabled** in the **Bidirectional** column and an IAM role ARN in the **Bidirectional role** column.

![Integrations table with two Slack associations, one Valid and one Pending.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-step11-success.png)


Your Agent Space is now connected to Slack.

## Setting up bidirectional communication in Slack
<a name="setting-up-bidirectional-communication-in-slack"></a>

After you complete the association with bidirectional mode enabled and a channel member authorizes the channel ([Step 10](#step-10-authorize-the-channel)), set up the channel binding from Slack:

1. In the associated private channel, send this exact app mention as a new top-level message:

``` @AWS DevOps Agent - <Region> setup ```

![A Slack message sending the setup command to the AWS DevOps Agent app.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-setup-command.png)


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

![A Slack channel showing a message that mentions the AWS DevOps Agent app with a reply indicator.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-chat-channel.png)


![A conversation thread showing the AWS DevOps Agent app responding with a list of capabilities.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-chat-thread.png)


Mention the app in each message, including replies within the thread. Replace `<Region>` with the AWS Region suffix shown in your app name. For example:

```
@AWS DevOps Agent - <Region> Tell me more about the Lambda errors
```

**Note** In a Slack code channel for an investigation, you don't need to mention the app.

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

## Updating Slack permissions for an existing workspace
<a name="updating-slack-permissions-for-an-existing-workspace"></a>

Update your workspace's Slack permissions so that you can open Slack code channels for investigations. The update doesn't change your channel associations or Agent Spaces.

Slack code channels need two Slack permissions. With `code_channels:manage`, AWS DevOps Agent can create and manage code channels. With `groups:history`, it can read messages in the private channels that it's in. If you connected your Slack workspace before code channels were available, make sure to update its permissions.

If your Slack workspace requires app approval, a Slack admin must approve the new permissions before the update can complete.

**To start the update in the AWS DevOps Agent console**

1. Open the [AWS DevOps Agent console](https://console.aws.amazon.com/aidevops/home), and in the navigation pane, choose **Capability Providers**.

1. In the **Slack** section, select the workspace. Then, on the **Actions** menu, choose **Update**.

1. On the **Update Slack permissions for workspace** page, choose **Update**. Slack opens its authorization page.

**To allow the new permissions in Slack**

1. On the Slack authorization page, confirm that the **Workspace** dropdown shows the workspace that you registered, and choose **Allow**. If you allow the update in a different workspace, Slack declines it.

When the update completes, the console returns you to the **Capability Providers** page and shows a green banner that reads **Slack updated successfully.** If the console shows **Slack permissions were not updated**, verify that you chose the registered workspace and that a Slack admin approved the app, and then update the permissions again.

On the **Actions** menu for a Slack workspace, **Update** reauthorizes AWS DevOps Agent in the workspace with the new permissions, and **Deregister** removes the workspace registration. The following image shows the **Actions** menu for the AnyCompany workspace on the **Capability Providers** page.

![Actions menu open for a Slack workspace on the Capability Providers page.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-update-permissions-1-actions.png)


The **Update Slack permissions for workspace** page names the workspace that you're updating. It explains that choosing **Update** opens the Slack authorization page, that choosing **Cancel** in Slack makes no changes, and that Slack declines the update if it opens a different workspace. The following image shows the **Update Slack permissions for workspace** page.

![The Update Slack permissions for workspace page in the AWS DevOps Agent console.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-update-permissions-2-update-page.png)


On the Slack authorization page, review the requested permissions, and then choose **Allow**. The list includes the permission to manage code channels. The following image shows the authorization page for the AnyCompany workspace. Under the heading "Actions AWS DevOps Agent - US East (N. Virginia) can take", the page lists these permissions:
+ **View messages that directly mention @AWS DevOps Agent - US East (N. Virginia) in conversations that the app is in**
+ **Send messages as @AWS DevOps Agent - US East (N. Virginia)**
+ **Send messages to channels @AWS DevOps Agent - US East (N. Virginia) isn't a member of**
+ **Allows AWS DevOps Agent - US East (N. Virginia) to manage code channels**

![The requested permissions and Allow on the Slack authorization page.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/slack-update-permissions-3-authorize.png)


## Managing channel associations
<a name="managing-channel-associations"></a>

AWS DevOps Agent posts to Slack through a shared app identity. It delivers messages as "AWS DevOps Agent" regardless of which Agent Space produced them. If you have access to the Agent Space, you can associate any channel in the connected workspace by entering its channel ID. The app can post to a channel only after a channel member adds the AWS DevOps Agent app to that channel.

Every new association waits for authorization in the channel. When you create an association, AWS DevOps Agent posts an authorization request to the channel, and it withholds notifications and does not answer mentions until a channel member chooses **Authorize** on the message. Add the app to the channel before you create the association, so that the request can be posted. If you change the channel of an existing association, the new channel receives a new authorization request. For more information, see [Step 10](#step-10-authorize-the-channel).

To control who can create or modify associations, scope Agent Space permissions with AWS Identity and Access Management (IAM) policies. You can review and remove existing associations at any time from the Agent Space console. AWS CloudTrail records all association changes in the Agent Space's account.

To stop delivery to a channel, remove the AWS DevOps Agent app from that channel. This stops delivery from all Agent Spaces to that channel. For more information about security, see [AWS DevOps Agent Security](aws-devops-agent-security.html).

## Troubleshooting Slack communication
<a name="troubleshooting-slack-communication"></a>

If the console shows "AWS DevOps Agent couldn't post the authorization request to the Slack channel" when you choose **Add**, invite the AWS DevOps Agent app to the channel, confirm the channel ID, and choose **Add** again.

If AWS DevOps Agent does not post notifications to a channel, confirm that the association shows **Valid** in the **Status** column. A new association, or one moved to another channel, shows **Pending** until a channel member chooses **Authorize** on the authorization request in the channel. If a channel member denied the request, the association shows **Invalid**; remove it, or create it again to send a new request.

If AWS DevOps Agent does not respond to a message in a bidirectional channel, verify the following:
+ The Slack channel ID matches the private channel associated with the Agent Space.
+ The association shows **Valid**, not **Pending**, in the **Status** column.
+ **Bidirectional** is **Enabled** for the association in the AWS DevOps Agent console.
+ The IAM role shown for the association exists and has the permissions created by the console.
+ The regional AWS DevOps Agent app is a member of the private channel.
+ The channel binding is active. Run `@AWS DevOps Agent - <Region> setup` again if the binding appears stale.
+ The correct Agent Space association was selected if setup showed a picker.
+ The first message in a conversation mentions the regional AWS DevOps Agent app.
+ The response is not already available in a thread under the original message.

If the workspace is not available when you create an association, confirm that you registered Slack in the same AWS account and Region as your Agent Space.

For information about problems with code channels, see [Troubleshooting code channels](connecting-to-ticketing-and-chat-using-slack-code-channels.html#troubleshooting-code-channels).

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

Deleting an Agent Space also removes the records that AWS DevOps Agent keeps for the code channels in that Agent Space. The Slack channels themselves stay in your workspace.

To request access to or deletion of your data, delete the Agent Space through the AWS Management Console or contact [AWS Support](https://aws.amazon.com/contact-us/).

For information about how we protect your data, see [Security and data protection](aws-devops-agent-security.html). We handle information in accordance with the [AWS Privacy Notice](https://aws.amazon.com/privacy/).