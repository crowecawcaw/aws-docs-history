

# Slack connector
<a name="connector-slack"></a>

Use the Slack connector to send storefront notifications to your Slack workspace.

## Slack connector
<a name="slack"></a>

The Slack connector sends notifications and alerts from AWS Marketplace Storefront to your Slack workspace channels.

### Prerequisites
<a name="slack-prerequisites"></a>
+ A Slack workspace where you have permission to install apps
+ Owner or Admin role at the organization level

### To connect Slack
<a name="slack-to-connect-slack"></a>

1. In the top-right corner, choose your profile avatar, choose **Organization Settings**, then choose the **Connectors** tab.

1. Find **Slack** and choose **Connect**.

1. After you authorize your Slack workspace, the panel displays a Connected indicator with the workspace name and the granted permissions. Choose **Next Step** to configure channels.

### Configuration
<a name="slack-configuration"></a>

#### Channel assignment
<a name="slack-channel-assignment"></a>

On the channel-configuration step, choose an **Account**, choose a **Notifications** type, choose a **Channel**, and choose a **Sync Frequency** (Instant, Daily, or Weekly). Choose **Add** to create the rule. Repeat for each rule, then choose **Save**.

The rules table displays the following columns:


| Account | Notifications | Channel | Sync Schedule | Sync Hour | Sync Day | Actions | 
| --- | --- | --- | --- | --- | --- | --- | 
| (account name) | (notification type) | (channel name) | (frequency) | (hour) | (day) | (action menu) | 

#### Notification format
<a name="slack-notification-format"></a>

Slack notifications include:
+ Event type and severity
+ Key details (buyer name, amount, product)
+ Direct link to the relevant page in the Storefront console
+ Timestamp

### What triggers Slack notifications
<a name="slack-what-triggers-slack-notifications"></a>

Slack notifications are triggered by the events configured in your organization's notification settings. The Slack connector acts as a delivery channel.

### To disconnect
<a name="slack-to-disconnect"></a>

1. Choose **Disconnect** in the connector settings.

1. Confirm. The Slack app remains in your workspace but stops receiving messages.

To fully remove, also uninstall the app from your Slack workspace settings.

### Related topics
<a name="slack-related-topics"></a>
+ Connector overview
+ Notification settings