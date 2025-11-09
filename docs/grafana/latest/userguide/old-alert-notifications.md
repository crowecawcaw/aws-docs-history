# Alert notifications

This documentation topic discusses
legacy alerting in Grafana. This will not be supported in future versions
of Amazon Managed Grafana. You can migrate to Grafana alerting to use the latest
alerting features. For more information, see one of the following
topics.

For Grafana workspaces that support Grafana version 10.x, see
[Alerts in Grafana version 10](v10-alerts.md "v10-alerts.md").

For Grafana workspaces that support Grafana version 9.x, see
[Alerts in Grafana version 9](v9-alerts.md "v9-alerts.md").

For Grafana workspaces that support Grafana version 8.x, see
[Grafana alerting](alerts-overview.md "alerts-overview.md").

When an alert changes state, it sends out notifications. Each alert rule can have
multiple notifications. To add a notification to an alert rule, you first must add and
configure a `notification` channel.

This is done from the Notification channels page.

## Adding a notification

channel

1. In the side bar, pause on the **Alerting**
   (bell) icon, and then choose **Notification
   channels**.
2. Choose **Add channel**.
3. Fill out the fields or select options described in the following
   sections.

## New notification channel

fields

### Default (send on all

alerts)

- **Name** – Enter a name for this
  channel. It will be displayed when users add notifications to alert
  rules.
- **Type** – Select the channel type.
  For more information, see [List of supported
  notifiers](#old-list-of-supported-notifiers "#old-list-of-supported-notifiers").
- **Default (send on all alerts)** –
  When selected, this option sends a notification on this channel for all
  alert rules.
- **Disable Resolve Message** – When
  selected, this option disables the resolve message [OK] that is sent
  when the alerting state returns to false.
- **Send reminders** – When this option
  is selected, additional notifications (reminders) will be sent for
  alerts. You can specify how often reminders should be sent by using the
  number of seconds (s), minutes (m), or hours (h); for example,
  `30s`, `3m`, `5m` or
  `1h`.

###### Important

Alert reminders are sent after rules are evaluated. Therefore, a reminder
can't be sent more frequently than a configured alert rule evaluation
interval.

The following examples show how often and when reminders are sent for a
triggered alert.

| Alert rule evaluation interval | Send reminders every | Reminder sent every (after last alert notification) |
| ------------------------------ | -------------------- | --------------------------------------------------- |
| `30s`                          | `15s`                | ~30 seconds                                         |
| `1m`                           | `5m`                 | ~5 minutes                                          |
| `5m`                           | `15m`                | ~15 minutes                                         |
| `6m`                           | `20m`                | ~24 minutes                                         |
| `1h`                           | `15m`                | ~1 hour                                             |
| `1h`                           | `2h`                 | ~2 hours                                            |

## List of supported

notifiers

| Name                                                                    | Type        | Supports images | Supports alert rule tags |
| ----------------------------------------------------------------------- | ----------- | --------------- | ------------------------ |
| [Amazon Simple Notification Service](#old-amazon-sns "#old-amazon-sns") | sns         | No              | Yes                      |
| OpsGenie                                                                | `opsgenie`  | No              | Yes                      |
| [PagerDuty](#old-pagerduty "#old-pagerduty")                            | `pagerduty` | No              | Yes                      |
| [Slack](#old-slack "#old-slack")                                        | `slack`     | No              | No                       |
| VictorOps                                                               | `victorops` | No              | No                       |

### Amazon Simple Notification Service

If you have enabled service-managed permissions and included Amazon SNS as a
notification channel for your workspace, you only need to provide the SNS Topic
ARN when you create your notification channel. In the **Name**
field, provide the name of the SNS topic that you have created. If you created
the workspace using service-managed permissions, the SNS topic name must be
prefixed with `grafana` for notifications to successfully publish to
the topic. If you selected customer-managed permissions when you created the
workspace, the SNS Topic name does not need to be prefixed with
`grafana`.

In the **Topic** field, copy and paste the ARN of the SNS
topic. In the **Message body format**, you can choose either
the JSON or the text option.

In the **Optional AWS SNS Settings** field, check the
checkbox **Include all tags in the message** to see all the
Grafana tags in the message body.

If you use customer-managed permissions for the workplace, the IAM role that
you supply should include SNS Publish permissions for your SNS Topic.

### Slack

To set up Slack, you must configure an incoming Slack webhook URL. For more
information, see [Sending
messages using Incoming Webhooks](https://api.slack.com/incoming-webhooks "https://api.slack.com/incoming-webhooks").

For more information about setting up a Slack bot integration,
see [Follow Slack’s guide to set up
a bot integration](https://api.slack.com/bot-users "https://api.slack.com/bot-users"). Use the token provided, which starts with
"xoxb".

| Setting         | Description                                                                                                                                                                                                                                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Url             | Slack incoming webhook URL, or eventually the [chat.postMessage](https://api.slack.com/methods/chat.postMessage "https://api.slack.com/methods/chat.postMessage") Slack API endpoint.                                                                                                                                            |
| Username        | Set the user name for the bot’s message.                                                                                                                                                                                                                                                                                         |
| Recipient       | Use this to override the Slack recipient. You must provide<br>either a channel Slack ID, a user Slack ID, a user name<br>reference (@<user>, all lowercase, no whitespace), or a<br>channel reference (#<channel>, all lowercase, no white<br>space). If you use the `chat.postMessage` Slack API<br>endpoint, this is required. |
| Icon emoji      | Provide an emoji to use as the icon for the bot’s message.<br>For example, :smile:                                                                                                                                                                                                                                               |
| Icon URL        | Provide a URL to an image to use as the icon for the bot’s<br>message.                                                                                                                                                                                                                                                           |
| Mention Users   | Optionally mention one or more users in the Slack<br>notification sent by Grafana. To see users, comma-separated, via<br>their corresponding Slack IDs, choose the overflow button on<br>each user’s Slack profile.                                                                                                              |
| Mention Groups  | Optionally mention one or more groups in the Slack<br>notification sent by Grafana. You can see groups,<br>comma-separated, via their corresponding Slack IDs (which you<br>can get from each group’s Slack profile URL).                                                                                                        |
| Mention Channel | Optionally mention either all channel members or only active<br>ones.                                                                                                                                                                                                                                                            |
| Token           | If provided, Amazon Managed Grafana will upload the generated image via<br>the Slack file.upload API operation, not the external image<br>destination. If you use the `chat.postMessage` Slack<br>API endpoint, this is required.                                                                                                |

If you are using the token for a slack bot, you have to invite the bot to the
channel that you want to send notifications. Then add the channel to the
recipient field.

### PagerDuty

To set up PagerDuty, provide an integration key.

| Setting                | Description                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| Integration Key        | Integration key for PagerDuty.                                                                      |
| Severity               | Level for dynamic notifications; default is<br>`critical` (1) .                                     |
| Auto resolve incidents | Resolve incidents in PagerDuty after the alert goes back to<br>ok.                                  |
| Message in details     | Removes the Alert message from the PD summary field and puts<br>it into custom details instead (2). |

###### Note

The tags `Severity`, `Class`, `Group`,
`dedup_key`, and `Component` have special meaning
in the [PagerDuty
Common Event Format – PD-CEF](https://support.pagerduty.com/docs/pd-cef "https://support.pagerduty.com/docs/pd-cef"). If an alert panel defines
these tag keys, they are transposed to the root of the event sent to
PagerDuty. This means they will be available within the PagerDuty UI and
Filtering tools. A Severity tag set on an alert overrides the global
Severity set on the notification channel if it’s a valid level.

###### Note

Using Message In Details will change the structure of the
`custom_details` field in the PagerDuty Event. This might
break custom event rules in your PagerDuty rules if you rely on the fields
in `payload.custom_details`. Move any existing rules that use
`custom_details.myMetric` to
`custom_details.queries.myMetric`.

###### Note

Using `dedup_key` tag will override the Grafana generated
`dedup_key` with a custom key.

## Configuring the link back to Grafana from alert notifications

All alert notifications contain a link back to the triggered alert in the Grafana
workspace.
