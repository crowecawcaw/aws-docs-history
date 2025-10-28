# Contact points

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Contact points contain the configuration for sending notifications. A contact
point is a list of integrations, each of which sends a notification to a particular
email address, service or URL. Contact points can have multiple integrations of the
same kind, or a combination of integrations of different kinds. For example, a
contact point could contain a Pagerduty integration; an Amazon SNS and Slack
integration; or a Pagerduty integration, a Slack integration, and two Amazon SNS
integrations. You can also configure a contact point with no integrations; in which
case no notifications are sent.

A contact point cannot send notifications until it has been added to a
notification policy. A notification policy can only send alerts to one contact
point, but a contact point can be added to a number of notification policies at the
same time. When an alert matches a notification policy, the alert is sent to the
contact point in that notification policy, which then sends a notification to each
integration in its configuration.

Contact points can be configured for
the Grafana Alertmanager as well as external alertmanagers.

You can also use notification templating to customize notification messages for
contact point types.

**Supported contact point types**

The following table lists the contact point types supported by Grafana.

| Name       | Type        |
| ---------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Amazon SNS | `sns`       |
| OpsGenie   | `opsgenie`  |
| Pager Duty | `pagerduty` |
| Slack      | `slack`     |
| VictorOps  | `victorops` | For more information about contact points, see [Configure contact points](v10-alerting-configure-contactpoints.md "v10-alerting-configure-contactpoints.md") and [Customize notifications](v10-alerting-manage-notifications.md "v10-alerting-manage-notifications.md"). |
