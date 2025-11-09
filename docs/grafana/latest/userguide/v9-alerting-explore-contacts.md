# Contact points

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Use contact points to define how your contacts are notified when an alert rule
fires. A contact point can have one or more contact point types, for example, email,
Slack, webhook, and so on. When an alert rule fires, a notification is sent to all
contact point types listed for a contact point. Contact points can be configured for
the Grafana Alertmanager as well as external alertmanagers.

You can also use notification templating to customize notification messages for
contact point types.

**Supported contact point types**

The following table lists the contact point types supported by Grafana.

| Name       | Type        |
| ---------- | ----------- |
| Amazon SNS | `sns`       |
| OpsGenie   | `opsgenie`  |
| Pager Duty | `pagerduty` |
| Slack      | `slack`     |
| VictorOps  | `victorops` |

For more information about contact points, see [Working with contact points](v9-alerting-contact-points.md "v9-alerting-contact-points.md") and [Customize notifications](v9-alerting-notifications.md "v9-alerting-notifications.md").
