

# Connect Slack
<a name="omni-connect-slack"></a>

An integration connects CloudWatch Omni to a tool your team already uses. Slack delivers alert notifications to your team's channels, and lets your team mention the Omni agent there. You manage it in **Settings**, on the **Integrations** page, and a connection applies to your whole space.

With Slack connected, an alert's notification rules can deliver to Slack channels. You choose the channels on each alert when you set its destinations. See [Alerts](omni-alerts.md).

Connecting the integration is not enough: delivery also requires the alert's access profile to grant this integration and the channels the alert posts to. Omni checks the grant when you create the alert and again on every delivery, so revoking it stops notifications for alerts that were already working. If an alert fires but nothing reaches Slack, check the profile. See [Access profiles](omni-access-profiles.md).

To connect:

1. In **Settings**, choose **Integrations**.

1. On the **Slack** card, choose **Enable**. Slack's authorization page opens in a new tab.

1. Review the requested permissions and choose **Allow**.

Back in Omni, the **Slack** card shows the connected integration: its ID and name. If your Slack workspace requires administrator approval for new apps, ask a workspace administrator to approve the request, then connect again.

**What the Slack connection can do.** The authorization page lists the exact permissions requested. The connection lets Omni post and reply to messages, read the names of your workspace's public and bot-added private channels so it can offer them as destinations, receive messages that mention the Omni app, and hold direct-message conversations with the Omni app. It does not include your workspace's message history. A private channel appears in the channel list only after the Omni app has been added to it.

**Bring the Omni agent into Slack.** With the integration connected, your team can mention the Omni agent in a Slack channel and get answers there. Connecting the workspace is not enough: the `DefaultAccessProfileForAsyncWorkflows` access profile must also grant the agent permission to post to the integration. Without that grant, a mention is received but the agent cannot respond. For what the agent can do, see [Ask the Omni agent](omni-ask-the-omni-agent.md). For profiles and grants, see [Access profiles](omni-access-profiles.md).

On the connected **Slack** card, choose **Set up Omni permissions for Slack**. This opens the add-grant form already filled in for the `DefaultAccessProfileForAsyncWorkflows` profile, where you choose the channels the agent may post to. Give the profile a viewer grant as well, so the agent can read the resources it answers about.

The grant covers three things:
+ **Reply through the Slack integration** — `cloudwatch:InvokeIntegration`, scoped to the Slack integration's ARN and the channels you choose.
+ **Work with conversation threads** — `cloudwatch:GetOmniThread` and `cloudwatch:CreateOmniThread`. A viewer grant already includes both, so a profile that has one does not need them listed separately.
+ **Read the resources it answers about** — a viewer grant.

If you author grants through the API instead of the console, use your own integration ARN and channel names:

```
{
  "name": "slack-agent-integration",
  "permission": "CUSTOM",
  "scopedActions": [
    {
      "actions": ["cloudwatch:InvokeIntegration"],
      "resources": [
        {
          "resourceType": "Integration",
          "resourceArns": ["arn:aws:cloudwatch:region:account-id:integration/integration-id"]
        }
      ],
      "contextConditions": { "channelNames": ["#oncall-alerts", "#incidents"] }
    },
    { "actions": ["cloudwatch:GetOmniThread", "cloudwatch:CreateOmniThread"] }
  ]
}
```

Pair it with a viewer grant:

```
{ "name": "slack-agent-viewer", "permission": "READ" }
```

**Regional Slack apps.** The Slack app is Region-specific, and you do not choose it: **Enable** directs you to the Amazon CloudWatch Slack app for the Region your space is in. It appears in your workspace as a bot with a matching name. Within one Region, a Slack workspace can be connected to only one space. The same workspace can be connected to spaces in different Regions. Each Region installs its own bot, so mention the bot whose name matches the Region of the space you want to reach.

**Invite the bot to each channel.** Connecting the workspace does not add the bot to any channel. Before an alert can deliver notifications to a channel, or a mention in that channel can reach the agent, invite the Region's bot to it from Slack:

```
/invite @Amazon CloudWatch - USEast Virginia
```


| Region | Bot name | 
| --- | --- | 
| US East (N. Virginia), us-east-1 | Amazon CloudWatch - USEast Virginia | 
| US East (Ohio), us-east-2 | Amazon CloudWatch - US East (Ohio) | 
| US West (Oregon), us-west-2 | Amazon CloudWatch - US West Oregon | 
| Europe (Ireland), eu-west-1 | Amazon CloudWatch - EU (Ireland) | 

**Disconnect an integration**

On the integration's card in **Settings**, on the **Integrations** page, choose **Disable**. Disconnecting Slack stops alert notifications to Slack. The alerts themselves keep evaluating, and their other destinations keep working. You can reconnect with **Enable**.

**Who can manage integrations**

Integrations apply to the whole space. One person connects, and the connection works for everyone in the space. Whether a member can connect, change, or disconnect an integration is governed by their grants: the integration create, update, and delete actions. See [Custom grant actions](omni-custom-grant-actions.md).