

# Connecting Microsoft Teams
<a name="connecting-to-ticketing-and-chat-connecting-microsoft-teams"></a>

You can connect AWS DevOps Agent to Microsoft Teams to receive one-way notifications. AWS DevOps Agent posts incident response findings, root cause analyses, and mitigation plans to the Teams channel that you select.

Microsoft Teams supports one-way notifications only. The app sends proactive notifications to your channel but does not respond to messages.

## Before you begin
<a name="before-you-begin"></a>

To connect AWS DevOps Agent with Microsoft Teams, verify that you have the following:
+ A Microsoft 365 tenant and an account with the Global Administrator or Privileged Role Administrator role in Microsoft Entra ID, to grant tenant-wide consent.
+ Access to [Microsoft Teams](https://teams.cloud.microsoft/) with permission to install apps from the Teams App Store.
+ Permission to configure capability providers and communications integrations in the AWS DevOps Agent console.
+ A Microsoft Teams channel (standard, private, or shared) where you want to receive notifications.

## Connecting Microsoft Teams to your Agent Space
<a name="connecting-microsoft-teams-to-your-agent-space"></a>

Follow these steps to register Microsoft Teams, associate a channel, and verify the integration.

### Step 1: Open the AWS DevOps Agent console
<a name="step-1-open-the-aws-devops-agent-console"></a>

1. Open the [AWS DevOps Agent console](https://console.aws.amazon.com/devops-agent/).

1. In the left navigation panel, choose **Capability Providers**.

1. In the **Communication** section, check whether Microsoft Teams is already registered. If it is, skip to [Step 5](#step-5-create-the-microsoft-teams-association).

![The Communication section on the Capability Providers page showing Microsoft Teams with the Register button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step1-capability-providers.png)


### Step 2: Register Microsoft Teams
<a name="step-2-register-microsoft-teams"></a>

1. In the **Communication** section, find **Microsoft Teams** and choose **Register**. You can also start from an Agent Space: on the **Capabilities** tab, in the **Communications** section, choose **Add**, then choose **Register** next to **Microsoft Teams**.

1. A new page opens titled **Register Microsoft Teams with DevOps Agent**. It shows two steps that you must complete in order.

![Register Microsoft Teams with DevOps Agent page showing the two registration steps.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step2-register-page.png)


### Step 3: Grant administrator consent
<a name="step-3-grant-administrator-consent"></a>

1. Under **Step 1: Grant administrator consent**, choose **Grant administrator consent**.

1. The browser goes to a Microsoft sign-in page. Sign in with an account that has the Global Administrator or Privileged Role Administrator role in your Microsoft Entra tenant.

1. Microsoft shows a **Permissions requested** dialog that lists the permissions AWS DevOps Agent needs: * Get a list of all teams. * Read the names and descriptions of all channels. \* Sign in and read user profile.

Review the permissions and choose **Accept**.

![Microsoft Permissions requested dialog for AWS DevOps Agent listing the requested permissions and the Accept button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step3-admin-consent.png)

+ You are redirected back to the AWS console. The Step 1 section shows **Complete** with a green checkmark.

**Note**  
** Sign in with a Microsoft Entra ID account that has the Global Administrator or Privileged Role Administrator role. If you sign in with another account, you can't grant the required tenant-wide consent.

### Step 4: Authorize the bot account
<a name="step-4-authorize-the-bot-account"></a>

1. After Step 3 is complete, the **Grant bot account permissions** button becomes active. Choose it.

1. The browser goes to a Microsoft sign-in page. Sign in with an account in the same Microsoft 365 tenant.

1. If Microsoft shows a **Permissions requested** dialog, review the permissions and choose **Accept**.

1. You are redirected back to the AWS console. The Step 2 section shows **Complete** with a green checkmark.

1. After both steps show as complete, choose **Add** at the bottom of the page.

![Register Microsoft Teams with DevOps Agent page with both steps marked Complete and the Add button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step4-complete.png)


**Note**  
** Completing both steps saves the registration. Choose ** Add ** to return to the console.

Confirm that Microsoft Teams appears as **Registered** in the **Communication** section of the **Capability Providers** page.

### Step 5: Create the Microsoft Teams association
<a name="step-5-create-the-microsoft-teams-association"></a>

1. In the left navigation panel, choose **Agent Spaces**.

1. Choose the Agent Space that you want to connect to Microsoft Teams.

1. On the **Capabilities** tab, scroll to the **Communications** section and choose **Add**.

1. Find the **Microsoft Teams** row and choose **Add**. The **Associate this Agent Space to your Microsoft Teams channel** page opens.

1. In Microsoft Teams, open the channel, choose **More options (…)** next to the channel name, and choose **Copy link**.

![The channel More options menu in Microsoft Teams with Copy link highlighted.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step5-copy-link.png)


1. Paste the link in the **Channel link** field. The channel must be in the Microsoft 365 tenant you registered.

![Associate this Agent Space to your Microsoft Teams channel page showing the Channel link field and the Submit button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step5-channel-link.png)


1. Note the team and channel in the link. You add the AWS DevOps Agent app to that team, and for a private or shared channel to the channel itself, in [Step 6](#step-6-add-the-app-to-your-teams-channel).

1. Choose **Submit**.

Confirm that the Communications section shows a Microsoft Teams association with the team and channel from your link.

### Step 6: Add the app to your Teams channel
<a name="step-6-add-the-app-to-your-teams-channel"></a>

1. Open [Microsoft Teams](https://teams.cloud.microsoft/).

1. In the left sidebar, choose **Apps**.

1. Search for **AWS DevOps Agent** and select it from the [Teams App Store](https://marketplace.microsoft.com/en-us/product/WA200012010).

1. Choose **Add**.

1. In the **Choose a place to use the app** dialog, select the channel from [Step 5](#step-5-create-the-microsoft-teams-association) and choose **Go**. This installs the app in the team that contains the channel.

![The AWS DevOps Agent app dialog in Microsoft Teams prompting you to choose a channel, with the Go button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step6-choose-channel.png)


1. For a private or shared channel, after you install the app in the team, you must also add it to the channel itself. Open the channel, choose **More options (…)**, and choose **Manage channel**. On the **Apps** tab, select **AWS DevOps Agent** and choose **Add**. The **Added to Channel** column changes from **No** to **Yes**.

![The channel More options menu in Microsoft Teams with Manage channel highlighted.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step6-manage-channel.png)


![The Apps tab of a private channel showing AWS DevOps Agent selected, Added to Channel set to No, and the Add button.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step6-private-channel-apps.png)


Confirm that you see a message in the Teams channel activity that says AWS DevOps Agent was added to the channel.

### Step 7: Confirm the welcome message
<a name="step-7-confirm-the-welcome-message"></a>

1. Open the channel where you added the app.

1. Wait 15 seconds to 2 minutes for the welcome message to appear.

1. You should see an Adaptive Card with the following message:

**Welcome to AWS DevOps Agent**
+ AWS DevOps Agent delivers incident notifications and investigation results to this conversation.
+ This bot sends proactive notifications — it does not respond to messages.
+ Notifications require an active AWS account with the AWS DevOps Agent service configured.

The card includes **Get started**, **Documentation**, and **Contact us** action buttons.

![The Welcome to AWS DevOps Agent card in the Teams channel with the Get started, Documentation, and Contact us buttons.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step7-welcome.png)


If the welcome message does not appear after 2 minutes, see [Troubleshooting](#troubleshooting-microsoft-teams-communication).

### Step 8: Verify the association
<a name="step-8-verify-the-association"></a>

1. Return to the AWS DevOps Agent console.

1. Open the Agent Space, and scroll to the **Communications** section.

1. Confirm that the Microsoft Teams association appears in the **Integrations** table, with the team in the **Name** column and the channel in the **Identifier** column.

![The Communications section of an Agent Space showing a Microsoft Teams integration with the team name and channel name.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-step8-communications.png)


Your Agent Space is now connected to Microsoft Teams.

## Viewing investigation results in Microsoft Teams
<a name="viewing-investigation-results-in-microsoft-teams"></a>

While AWS DevOps Agent investigates, it posts Adaptive Cards to the associated Microsoft Teams channel: one when the investigation starts, then cards with observations, findings, causes, and the investigation summary. Each card has a **View Investigation** button that opens the investigation in the AWS DevOps Agent console. Cards for the same investigation are threaded as replies under the first card.

![An Investigation started card in the Teams channel with a View Investigation button and threaded replies.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/teams-results-card.png)


To trigger an investigation and verify notifications:

1. Open the Agent Space in the [AWS DevOps Agent console](https://console.aws.amazon.com/devops-agent/).

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

To control who can create or modify associations, scope Agent Space permissions with AWS Identity and Access Management (IAM) policies. You can review and remove existing associations at any time from the Agent Space console. AWS CloudTrail records all association changes in the Agent Space's account.

To stop delivery to a channel, remove the AWS DevOps Agent app from that channel or from its team. This stops delivery from all Agent Spaces to that channel. For more information about security, see [AWS DevOps Agent Security](aws-devops-agent-security.html).

## Removing a Microsoft Teams association
<a name="removing-a-microsoft-teams-association"></a>

To stop receiving notifications in a Microsoft Teams channel:

1. Open the Agent Space, and choose **Capabilities**.

1. Under **Communications**, select the Microsoft Teams association and choose **Remove**.

Removing a channel association does not unregister Microsoft Teams from AWS DevOps Agent. To fully deregister Microsoft Teams, remove all associations first, then choose **Deregister** for Microsoft Teams in the **Communication** section of the **Capability Providers** page.

## Troubleshooting Microsoft Teams communication
<a name="troubleshooting-microsoft-teams-communication"></a>

If AWS DevOps Agent does not send notifications to your Microsoft Teams channel, verify the following:
+ Microsoft Teams is registered with AWS DevOps Agent, the association exists, and the AWS DevOps Agent app is added to the team. For a private or shared channel, the app is also added to the channel itself. You can create the association and add the app in either order.
+ The channel in the association link matches the channel where the app is added.
+ Both authorization steps (administrator consent and bot account) completed successfully during registration.
+ Microsoft Teams appears as **Registered** in the **Communication** section of the **Capability Providers** page.
+ The Communications section shows the correct Microsoft Teams association for the Agent Space.


| Symptom | Cause | Fix | 
| --- | --- | --- | 
| No welcome message after 2 minutes | The app was added in a Microsoft 365 tenant that is not registered with AWS DevOps Agent, or the registration did not complete | Confirm that Microsoft Teams shows as Registered for that tenant, then remove the app from the team and add it again, selecting the associated channel when Teams asks where to use the app | 
| "Service cannot be deregistered" | An association still exists | Remove the association first, then deregister | 
| The channel link is rejected | The link is not a channel link, or the channel is not in the registered Microsoft 365 tenant | In Teams, open the channel, choose More options (…), choose Copy link, and paste the full link | 
| No notifications in a private or shared channel | The app is installed in the team but not added to the channel | In Teams, open the channel, choose Manage channel, and on the Apps tab confirm that Added to Channel is Yes for AWS DevOps Agent | 
| Investigation does not post to Teams | Wrong channel, or the app is not added to the channel | Verify the channel in the association matches the channel where the app is added. For a private or shared channel, confirm the app is added to the channel itself | 

### AI-generated content
<a name="ai-generated-content"></a>

We use large language models to generate investigation findings, root-cause analyses, mitigation recommendations, and conversational responses. These outputs might be inaccurate or incomplete. Verify AI-generated information before acting on it.

### Data handling and privacy
<a name="data-handling-and-privacy"></a>

We retain data associated with your Agent Space for as long as necessary to provide the service. This data includes investigation journals, chat messages, and operational data. You can delete your Agent Space at any time to remove all associated data.

To request access to or deletion of your data, delete the Agent Space through the AWS Management Console or contact [AWS Support](https://aws.amazon.com/contact-us/).

For information about how we protect your data, see [Security and data protection](aws-devops-agent-security.html). We handle information in accordance with the [AWS Privacy Notice](https://aws.amazon.com/privacy/).