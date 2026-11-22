

# Connecting Microsoft Teams

You can connect AWS DevOps Agent to Microsoft Teams in two ways:
+ **One-way notifications**: AWS DevOps Agent posts incident response findings, root cause analyses, and mitigation plans to the Teams channel that you select.
+ **Bidirectional communication**: AWS DevOps Agent also receives and responds to messages in a private or shared Teams channel. Mention the app to start a conversation. AWS DevOps Agent replies in the thread under your message.

You can enable bidirectional communication only in private and shared channels. Standard channels support one-way notifications only.

You connect a channel to an [Agent Space](about-aws-devops-agent-what-are-devops-agent-spaces.html), a logical container that defines the tools and infrastructure that AWS DevOps Agent has access to. For more information, see [About AWS DevOps Agent](about-aws-devops-agent.html).

## Before you begin
<a name="before-you-begin"></a>

To connect AWS DevOps Agent with Microsoft Teams, verify that you have the following:
+ A Microsoft 365 tenant and an account with the Global Administrator or Privileged Role Administrator role in Microsoft Entra ID, to grant tenant-wide consent.
+ Access to [Microsoft Teams](https://teams.cloud.microsoft/) with permission to install apps from the Teams App Store.
+ Permission to configure capability providers and communications integrations in the [AWS DevOps Agent console](https://console.aws.amazon.com/aidevops/home).
+ Permission to create or assign an IAM role from the [AWS DevOps Agent console](https://console.aws.amazon.com/aidevops/home) (required for bidirectional communication).
+ A Microsoft Teams channel where you want to receive notifications. For one-way notifications, the channel can be standard, private, or shared. For bidirectional communication, the channel must be private or shared.
+ A member of the channel who can approve the authorization request that AWS DevOps Agent posts to the channel when you create the association.

## Connecting Microsoft Teams to your Agent Space
<a name="connecting-microsoft-teams-to-your-agent-space"></a>

Follow these steps to register Microsoft Teams, add the app to your channel, associate the channel, optionally enable bidirectional communication, authorize the channel, and verify the integration.

### Step 1: Open the AWS DevOps Agent console
<a name="step-1-open-the-aws-devops-agent-console"></a>

1. Open the [AWS DevOps Agent console](https://console.aws.amazon.com/aidevops/home).

1. In the left navigation panel, choose **Capability Providers**.

1. Check whether a **Microsoft Teams** card appears in the **Currently registered** section. If it does, Microsoft Teams is already registered, and you can skip to [Step 5](#step-5-add-the-app-to-your-teams-channel).

### Step 2: Register Microsoft Teams
<a name="step-2-register-microsoft-teams"></a>

1. In the **Available** section, find the **Microsoft Teams** card and choose **Register**. You can also start from an Agent Space: on the **Capabilities** tab, in the **Communications** section, choose **Add**, then choose **Register** next to **Microsoft Teams**.

1. A new page opens titled **Register Microsoft Teams with DevOps Agent**. It shows two steps that you must complete in order.

![Register Microsoft Teams with DevOps Agent page showing the two registration steps.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step2-register-page.png)


### Step 3: Grant administrator consent
<a name="step-3-grant-administrator-consent"></a>

1. Under **Step 1: Grant administrator consent**, choose **Grant administrator consent**.

1. The browser goes to a Microsoft sign-in page. Sign in with an account that has the Global Administrator or Privileged Role Administrator role in your Microsoft Entra tenant.

1. Microsoft shows a **Permissions requested** dialog that lists the permissions AWS DevOps Agent needs: **Get a list of all teams**, **Read the names and descriptions of all channels**, and **Sign in and read user profile**. Review the permissions and choose **Accept**.

1. You are redirected back to the AWS console. The Step 1 section shows **Complete** with a green checkmark.

The following image shows the **Permissions requested** dialog from step 3.

![Microsoft Permissions requested dialog for AWS DevOps Agent listing the requested permissions and the Accept button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step3-admin-consent.png)


**Note**  
Sign in with a Microsoft Entra ID account that has the Global Administrator or Privileged Role Administrator role. If you sign in with another account, you can't grant the required tenant-wide consent.

### Step 4: Authorize the bot account
<a name="step-4-authorize-the-bot-account"></a>

1. After Step 3 is complete, the **Grant bot account permissions** button becomes active. Choose it.

1. The browser goes to a Microsoft sign-in page. Sign in with an account in the same Microsoft 365 tenant.

1. If Microsoft shows a **Permissions requested** dialog, review the permissions and choose **Accept**.

1. You are redirected back to the AWS console. The Step 2 section shows **Complete** with a green checkmark.

1. After both steps show as complete, choose **Add** at the bottom of the page.

![Register Microsoft Teams with DevOps Agent page with both steps marked Complete and the Add button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step4-complete.png)


**Note**  
Completing **Step 1: Grant administrator consent** and **Step 2: Authorize the bot account** saves the registration. Choose **Add** to return to the console.

Confirm that a **Microsoft Teams** card appears in the **Currently registered** section of the **Capability Providers** page.

### Step 5: Add the app to your Teams channel
<a name="step-5-add-the-app-to-your-teams-channel"></a>

Add the app before you create the association. When you create the association, AWS DevOps Agent posts an authorization request to the channel, and it can post only to a channel that already has the app.

1. Open [Microsoft Teams](https://teams.cloud.microsoft/).

1. In the left sidebar, choose **Apps**.

1. Search for **AWS DevOps Agent** and select it from the [Teams App Store](https://marketplace.microsoft.com/en-us/product/WA200012010).

1. Choose **Add**.

1. In the **Choose a place to use the app** dialog, select the channel that you want to connect and choose **Go**. This installs the app in the team that contains the channel.

1. For a private or shared channel, you must also add the app to the channel itself. Open the channel, choose **More options** next to the channel name, and choose **Manage channel**.

1. On the **Apps** tab, select **AWS DevOps Agent** and choose **Add**. The **Added to Channel** column changes from **No** to **Yes**.

The following image shows the **Choose a place to use the app** dialog, where you select the channel and choose **Go**.

![The AWS DevOps Agent app dialog in Microsoft Teams prompting you to choose a channel, with the Go button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step5-choose-channel.png)


The following image shows the **More options** menu of the channel, where you choose **Manage channel**.

![The channel More options menu in Microsoft Teams with Manage channel highlighted.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step5-manage-channel.png)


The following image shows the **Apps** tab of a private channel, where you select **AWS DevOps Agent** and choose **Add**.

![The Apps tab of a private channel showing AWS DevOps Agent selected, Added to Channel set to No, and the Add button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step5-private-channel-apps.png)


Confirm that you see a message in the Teams channel activity that says AWS DevOps Agent was added to the channel.

### Step 6: Confirm the welcome message
<a name="step-6-confirm-the-welcome-message"></a>

1. Open the channel where you added the app.

1. Wait 15 seconds to 2 minutes for the welcome message to appear.

1. You should see an Adaptive Card titled **Welcome to AWS DevOps Agent**. The card states that the channel is not connected yet and explains how to connect it: enable AWS DevOps Agent in an AWS account and connect the channel to an Agent Space in the [AWS DevOps Agent console](https://console.aws.amazon.com/aidevops/home). It also explains that in private and shared channels with chat enabled, you @mention AWS DevOps Agent with your request and the reply appears in a thread under your message, that you can type **help** after the mention to see what the app can do, or **setup** to see how the channel is connected, and that standard channels receive investigation updates only. The card includes **Get started**, **Documentation**, and **Contact us** action buttons.

![The Welcome to AWS DevOps Agent card in a Teams channel, with the setup and chat instructions and the Get started, Documentation, and Contact us buttons.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step6-welcome-card.png)


If the welcome message does not appear after 2 minutes, see [Troubleshooting](#troubleshooting-microsoft-teams-communication).

### Step 7: Create the Microsoft Teams association
<a name="step-7-create-the-microsoft-teams-association"></a>

When you create the association, the channel receives an authorization request, and any channel member can approve it. Read [Step 9](#step-9-authorize-the-channel) before you continue.

1. In the left navigation panel, choose **Agent Spaces**.

1. Choose the Agent Space that you want to connect to Microsoft Teams.

1. On the **Capabilities** tab, scroll to the **Communications** section and choose **Add**.

1. Find the **Microsoft Teams** row and choose **Add**. The **Associate this Agent Space to your Microsoft Teams channel** page opens.

1. In Microsoft Teams, open the channel where you added the app, choose **More options** next to the channel name, and choose **Copy link**.

1. Paste the link in the **Channel link** field. The channel must be in the Microsoft 365 tenant you registered.

1. To use one-way notifications only, choose **Submit** and continue with [Step 9](#step-9-authorize-the-channel). To enable bidirectional communication, continue with [Step 8](#step-8-optional-enable-bidirectional-communication) before you choose **Submit**.

The following image shows the **More options** menu of the channel in Microsoft Teams, where you choose **Copy link**.

![The channel More options menu in Microsoft Teams with Copy link highlighted.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step7-copy-link.png)


The following image shows the **Channel link** field on the **Associate this Agent Space to your Microsoft Teams channel** page.

![Associate this Agent Space to your Microsoft Teams channel page showing the Channel link field and the Submit button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step7-channel-link.png)


### Step 8: (Optional) Enable bidirectional communication
<a name="step-8-optional-enable-bidirectional-communication"></a>

This step applies only to bidirectional communication. If you chose **Submit** in Step 7 for one-way notifications, skip to [Step 9](#step-9-authorize-the-channel).

To enable bidirectional communication, turn on **Bidirectional mode** and configure the IAM role that AWS DevOps Agent assumes when it handles requests from the channel:

1. Under **Bidirectional communication**, turn on **Bidirectional mode**.

1. Under **IAM role configuration**, choose one of the following options:
   + **Auto-create a new DevOps Agent role**: Enter a role name. The console creates the role in your account with the AIDevOpsChannelAccessPolicy AWS managed policy attached. You can modify the role later.
   + **Assign an existing role**: Select a role from the list of IAM roles that trust the AWS DevOps Agent service. The role needs the permissions in the AIDevOpsChannelAccessPolicy AWS managed policy or equivalent permissions. To enter a role ARN directly, use the policy template option instead.
   + **Create a new DevOps Agent role using a policy template**: Follow the instructions shown to create the role in the IAM console with the provided trust policy and permissions policy, then enter the role ARN.

1. Choose **Submit**.

![The Bidirectional communication section of the association page with Bidirectional mode turned on, the three IAM role configuration options, and the Role name field.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step8-bidirectional.png)


**Note**  
Bidirectional mode is available in private and shared channels. If the channel link is for a standard channel, the console shows an error when you choose **Submit**. Use one-way notifications for a standard channel.

### Step 9: Authorize the channel
<a name="step-9-authorize-the-channel"></a>

When you choose **Submit**, the **Communications** section shows a Microsoft Teams association with the team and channel from your link, and AWS DevOps Agent posts an authorization request card to the channel. The card is titled **AWS DevOps Agent authorization request** and reads: "AWS account *account-id* requested to connect an agent space to this channel. AWS DevOps Agent will not post here until a member of this channel authorizes the request." Below that text, the card lists the Agent Space ID, the AWS account ID, and the AWS Region, and has **Authorize** and **Deny** buttons. Until a channel member chooses **Authorize**, AWS DevOps Agent withholds notifications and does not answer mentions in the channel, and the association shows **Pending** in the console.

The following image shows the authorization request card in the channel.

![Authorization request card in Microsoft Teams with the Authorize and Deny buttons.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step9-authorization-request.png)


1. In Microsoft Teams, open the channel and find the card titled **AWS DevOps Agent authorization request**.

1. Confirm that the AWS account ID and the Agent Space ID on the card are the ones you expect.

1. Choose **Authorize**. The card expands with a **Confirm** button and the text "Allow AWS account *account-id* (agent space *agent-space-id*) to send AWS DevOps Agent notifications to this channel."

1. Choose **Confirm**. The card updates to show who authorized the request, and delivery starts. To refuse the request, choose **Deny**, and then choose **Confirm**. After a denial, remove the association, or create it again to send a new request.

The following image shows the confirmation text and the **Confirm** button from step 3.

![Authorization request card with the confirmation text and the Confirm button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step9-authorization-confirm.png)


The following image shows the card after a channel member authorizes the request. The card reads "Authorized by *name*. AWS DevOps Agent notifications from AWS account *account-id* are enabled in this channel."

![Authorization request card after a channel member authorized it.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step9-authorized-card.png)


**Important**  
Any member of the channel can approve or deny the request, not only the person who created the association or a channel owner. This includes guests in your Microsoft 365 tenant and, in a shared channel, members of other organizations. Approving connects the channel to an Agent Space in the AWS account shown on the card: notifications from that Agent Space post to the channel, and with bidirectional mode, every channel member can send requests to it. We recommend that you associate channels whose members you trust to make this decision, and that channel members choose **Authorize** only for requests from AWS account IDs they recognize.

### Step 10: Verify the association
<a name="step-10-verify-the-association"></a>

1. Return to the [AWS DevOps Agent console](https://console.aws.amazon.com/aidevops/home).

1. Open the Agent Space, and scroll to the **Communications** section.

1. Confirm that the Microsoft Teams association appears in the **Integrations** table, with the team in the **Name** column and the channel in the **Identifier** column.

1. Confirm that the **Status** column shows **Valid**. It shows **Pending** until a channel member approves the authorization request from [Step 9](#step-9-authorize-the-channel).

1. If you enabled bidirectional communication, verify that the **Bidirectional** column shows **Enabled** and the **Bidirectional role** column shows the IAM role ARN.

The following image shows the **Integrations** table with one Microsoft Teams association: the team Example Team with a private channel, **Valid** in the **Status** column, **Enabled** in the **Bidirectional** column, and the IAM role ARN in the **Bidirectional role** column.

![Integrations table with one Microsoft Teams association.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step10-communications.png)


Your Agent Space is now connected to Microsoft Teams.

## Chatting with AWS DevOps Agent in Microsoft Teams
<a name="chatting-with-aws-devops-agent-in-microsoft-teams"></a>

To start a conversation, post a new message in a private or shared channel whose association has **Bidirectional mode** enabled. Type **@**, choose **AWS DevOps Agent** from the suggestions, and enter your request, for example `@AWS DevOps Agent What can you do?`

AWS DevOps Agent replies in the thread under your message and updates the reply while it works. Open the thread to view the response. To continue the conversation, reply in the same thread and mention the app again, for example `@AWS DevOps Agent Tell me more about the Lambda errors`.

Messages that do not mention AWS DevOps Agent are not read. Post a new channel message to start a separate conversation. Each reply is labeled as AI generated.

AWS DevOps Agent can help with tasks supported by your Agent Space, including:
+ Starting, viewing, and guiding investigations into incidents and operational issues
+ Exploring AWS resources, metrics, logs, and topology
+ Reviewing and responding to prevention recommendations
+ Running supported release management and testing workflows

The responses and actions available in Microsoft Teams depend on the configuration and permissions of the associated Agent Space.

Two commands are available after the mention:
+ `help` posts a card that describes what AWS DevOps Agent can do in the channel.
+ `setup` connects the channel to its Agent Space again. With one Agent Space, it confirms that Agent Space. With several, it posts a picker so that you can choose the Agent Space for new conversations. For more information, see [Choosing the Agent Space for a channel](#choosing-the-agent-space-for-a-channel).

## Choosing the Agent Space for a channel
<a name="choosing-the-agent-space-for-a-channel"></a>

You can associate the same Teams channel with more than one [Agent Space](about-aws-devops-agent-what-are-devops-agent-spaces.html). When exactly one association with bidirectional mode serves the channel, AWS DevOps Agent uses that Agent Space, and no setup is needed.

When several associations with bidirectional mode serve the channel, your first mention gets a card that says **Multiple agent spaces can serve this channel**:

1. In the **Choose agent space** list, select the Agent Space that you want the channel to use.

1. Choose **Use this agent space**. AWS DevOps Agent confirms the choice with the Agent Space ID and AWS account.

1. Mention the app again to start chatting.

The choice applies to new conversations. Existing threads keep the Agent Space they started with. To choose again, mention the app with the `setup` command: `@AWS DevOps Agent setup`.

## Switching between bidirectional communication and one-way notifications
<a name="switching-between-bidirectional-communication-and-one-way-notifications"></a>

You can edit the Microsoft Teams association at any time. Bidirectional mode can be enabled only for private and shared channels:

1. Open the Agent Space, and choose **Capabilities**.

1. Under **Communications**, select the Microsoft Teams association and choose **Edit**.

1. Turn **Bidirectional mode** on to allow conversations in the channel, or turn it off to use the channel for one-way notifications only.

1. If you turn **Bidirectional mode** on, configure the role under **IAM role configuration**. For the options, see [Step 8](#step-8-optional-enable-bidirectional-communication).

1. Choose **Submit**.

To stop using a channel with the Agent Space, remove its association. For more information, see [Removing a Microsoft Teams association](#removing-a-microsoft-teams-association). Removing a channel association does not unregister Microsoft Teams from AWS DevOps Agent.

## Viewing investigation results in Microsoft Teams
<a name="viewing-investigation-results-in-microsoft-teams"></a>

While AWS DevOps Agent investigates, it posts Adaptive Cards to the associated Microsoft Teams channel: one when the investigation starts, then cards with observations, findings, causes, and the investigation summary. Each card has a **View Investigation** button that opens the investigation in the AWS DevOps Agent console. Cards for the same investigation are threaded as replies under the first card.

![An Investigation started card in the Teams channel with a View Investigation button and threaded replies.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-results-card.png)


To trigger an investigation and verify notifications:

1. Open the Agent Space in the [AWS DevOps Agent console](https://console.aws.amazon.com/aidevops/home).

1. Choose **Launch via IAM** to open the web app.

1. Start an investigation by entering a request such as:

``` Investigate lambda errors ```

1. Cards start arriving within a few minutes. A full investigation can take longer.

1. Switch to your Microsoft Teams channel. You should see:
   + An **Investigation started** card with the investigation title and a **View Investigation** button.
   + Follow-up cards with observations, findings, causes, and the investigation summary, each with a **View Investigation** button.

## Managing channel associations
<a name="managing-channel-associations"></a>

AWS DevOps Agent posts to Microsoft Teams through a shared app identity. It delivers messages as "AWS DevOps Agent" regardless of which Agent Space produced them. If you have access to the Agent Space, you can associate any channel in the registered Microsoft 365 tenant by entering its channel link. The app can post to a channel only after a team member adds the AWS DevOps Agent app to the team. For a private or shared channel, the team member must also add the app to the channel itself.

Every new association waits for authorization in the channel. When you create an association, AWS DevOps Agent posts an authorization request card to the channel, and it withholds notifications and does not answer mentions until a channel member chooses **Authorize** on the card. The app must be in the channel before you create the association, so that the request can be posted. If you change the channel of an existing association, the new channel receives a new authorization request. For more information, see [Step 9](#step-9-authorize-the-channel).

In a channel with bidirectional mode, every member of the channel can send requests to the associated Agent Space, including guests and, in a shared channel, members of other organizations. Control who can chat with the Agent Space by controlling the channel membership.

To control who can create or modify associations, scope Agent Space permissions with AWS Identity and Access Management (IAM) policies. You can review and remove existing associations at any time from the Agent Space console. AWS CloudTrail records all association changes in the Agent Space's account.

To stop delivery to a channel, remove the AWS DevOps Agent app from that channel or from its team. This stops delivery from all Agent Spaces to that channel. For more information about security, see [AWS DevOps Agent Security](aws-devops-agent-security.html).

## Removing a Microsoft Teams association
<a name="removing-a-microsoft-teams-association"></a>

To disconnect an Agent Space from a Microsoft Teams channel:

1. Open the Agent Space, and choose **Capabilities**.

1. Under **Communications**, select the Microsoft Teams association and choose **Remove**.

Other [Agent Spaces](about-aws-devops-agent-what-are-devops-agent-spaces.html) associated with the same channel stay connected. Removing a channel association does not unregister Microsoft Teams from AWS DevOps Agent. To fully deregister Microsoft Teams, remove all associations first, then go to the **Capability Providers** page. Under **Currently registered**, choose **View all** on the **Microsoft Teams** card. In **Registrations**, select the registration, and then choose **Deregister** from the **Actions** menu.

## Troubleshooting Microsoft Teams communication
<a name="troubleshooting-microsoft-teams-communication"></a>

If AWS DevOps Agent does not send notifications to your Microsoft Teams channel, verify the following:
+ Microsoft Teams is registered with AWS DevOps Agent, the association exists, and the AWS DevOps Agent app is added to the team. For a private or shared channel, the app is also added to the channel itself.
+ The association shows **Valid** in the **Status** column. A new association, or one moved to another channel, shows **Pending** until a channel member chooses **Authorize** on the request card in the channel.
+ The channel in the association link matches the channel where the app is added.
+ Both authorization steps (administrator consent and bot account) completed successfully during registration.
+ A **Microsoft Teams** card appears in the **Currently registered** section of the **Capability Providers** page.
+ The Communications section shows the correct Microsoft Teams association for the Agent Space.

If AWS DevOps Agent does not respond to a message in a bidirectional channel, verify the following:
+ The channel is a private or shared channel. Standard channels receive notifications only.
+ **Bidirectional** is **Enabled** for the association in the AWS DevOps Agent console, and the **Bidirectional role** column shows the IAM role.
+ The AWS DevOps Agent app is added to the channel itself, not only to the team.
+ The association shows **Valid**, not **Pending**, in the **Status** column.
+ Your message mentions **AWS DevOps Agent**. Messages without a mention are not read, including replies in a thread.
+ The channel chats with the Agent Space that you expect. If several Agent Spaces are connected, mention the app with `setup` and choose the Agent Space for new conversations.
+ The response is not already in the thread under your message.


| Symptom | Cause | Fix | 
| --- | --- | --- | 
| No welcome message after 2 minutes | The app was added in a Microsoft 365 tenant that is not registered with AWS DevOps Agent, or the registration did not complete | Confirm that Microsoft Teams shows as Registered for that tenant, then remove the app from the team and add it again, selecting the channel when Teams asks where to use the app | 
| "Service cannot be deregistered" | An association still exists | Remove the association first, then deregister | 
| The channel link is rejected | The link is not a channel link, or the channel is not in the registered Microsoft 365 tenant | In Teams, open the channel, choose More options, choose Copy link, and paste the full link | 
| "AWS DevOps Agent couldn't post the authorization request to the Microsoft Teams channel" when you choose Submit | The app is not in the team, or for a private or shared channel, not in the channel itself | Add the app to the team and, for a private or shared channel, to the channel (Step 5), then create the association again | 
| "Bidirectional chat can be enabled only on a private or shared Microsoft Teams channel" when you choose Submit | The channel link is for a standard channel | Turn off Bidirectional mode for this channel, or associate a private or shared channel instead | 
| The association shows Pending, nothing is posted, and mentions get no reply | The authorization request card in the channel has not been approved | Have a channel member choose Authorize, then Confirm, on the card in the channel | 
| The association shows Invalid right after you created it | A channel member denied the authorization request | Remove the association, or create it again to send a new request | 
| No notifications in a private or shared channel | The app is installed in the team but not added to the channel | In Teams, open the channel, choose Manage channel, and on the Apps tab confirm that Added to Channel is Yes for AWS DevOps Agent | 
| A mention gets a "Set up chat with AWS DevOps Agent" card instead of a reply | The channel has no association with Bidirectional mode enabled | Edit the channel's association and turn on Bidirectional mode, or create an association with Bidirectional mode for a private or shared channel | 
| Investigation does not post to Teams | Wrong channel, or the app is not added to the channel | Verify the channel in the association matches the channel where the app is added. For a private or shared channel, confirm the app is added to the channel itself | 

### AI-generated content
<a name="ai-generated-content"></a>

We use large language models to generate investigation findings, root-cause analyses, mitigation recommendations, and conversational responses. These outputs might be inaccurate or incomplete. Verify AI-generated information before acting on it.

### Data handling and privacy
<a name="data-handling-and-privacy"></a>

We retain data associated with your Agent Space for as long as necessary to provide the service. This data includes investigation journals, chat messages, and operational data. You can delete your Agent Space at any time to remove all associated data.

To request access to or deletion of your data, delete the Agent Space through the AWS Management Console or contact [AWS Support](https://aws.amazon.com/contact-us/).

For information about how we protect your data, see [Security and data protection](aws-devops-agent-security.html). We handle information in accordance with the [AWS Privacy Notice](https://aws.amazon.com/privacy/).