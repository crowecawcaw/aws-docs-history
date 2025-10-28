# Pausing an alert rule

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

Pausing the evaluation of an alert rule can sometimes be useful. For example, during
a maintenance window, pausing alert rules can avoid initiating a flood of alerts.

1. In the Grafana side bar, pause on the **Alerting** (bell)
   icon and then choose **Alert Rules**. All
   configured alert rules are listed, along with their current state.
2. Find your alert in the list, and choose the **Pause** icon on the right. The **Pause** icon turns into a **Play**
   icon.
3. Choose the **Play** icon to resume evaluation of
   your alert.
