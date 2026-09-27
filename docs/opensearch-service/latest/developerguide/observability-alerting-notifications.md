

# Notifications
<a name="observability-alerting-notifications"></a>

Notifications deliver your alerts to external destinations such as Amazon SNS, Slack, Microsoft Teams, email, and custom webhooks. Classic monitors send notifications through actions on their triggers. This page describes how to configure notification channels and actions.

## Notification channels
<a name="observability-alerting-notifications-channels"></a>

A *channel* defines a destination that receives alert notifications. You manage channels in the **Notifications** area of OpenSearch UI. To create a channel:

1. Choose **Notifications**, **Channels**, and then **Create channel**.

1. Choose a channel type, such as Amazon SNS, Slack, Microsoft Teams, email (through an Amazon SES or SMTP sender), or a custom webhook.

1. Configure the destination, and then save the channel.

1. (Optional) Choose **Send test message** to confirm that the channel delivers.

For email channels, first create a sender (SMTP or Amazon SES) and one or more recipient groups, and then reference them from the channel.

To manage existing channels, use the **Channels** list, where you can search and filter channels, open a channel to view its details, edit or delete a channel, or mute a channel to temporarily stop its notifications.

**Tip**  
You're responsible for securing access to the destination that a channel delivers to, such as the Slack channel or webhook endpoint that receives the message.

## Actions
<a name="observability-alerting-notifications-actions"></a>

To send notifications, add one or more actions to a trigger. Each action sends to a notification channel, such as an Amazon SNS channel. A single trigger can have multiple actions, so one alert can notify several channels. For each action, you configure:
+ The notification channel and the message. You write the message subject and body with a Mustache template that can include variables such as `ctx.monitor.name`, `ctx.trigger.name`, `ctx.trigger.severity`, `ctx.periodStart`, and `ctx.periodEnd`.
+ Throttling, to limit how often the action sends notifications. For example, if the monitor runs every minute, setting throttling to 60 minutes sends at most one notification per hour, even if the condition is met on every run.
+ For a per-bucket monitor, whether the action runs for each execution or for each alert.

The following example message body uses a Mustache template:

```
Monitor {{ctx.monitor.name}} entered alert status.
Trigger: {{ctx.trigger.name}}
Severity: {{ctx.trigger.severity}}
Period: {{ctx.periodStart}} to {{ctx.periodEnd}}
```

For the template syntax, see the [Mustache manual](https://mustache.github.io/mustache.5.html) on the Mustache website. For the variables available to actions, see [Actions](https://docs.opensearch.org/latest/observing-your-data/alerting/actions/) on the OpenSearch website.