# Notification templating

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

The alert notification template feature allows you to take the label value from an
alert query and inject that into alert notifications.

Labels that exist from the evaluation of the alert query can be used in the alert rule
name and in the alert notification message fields. The alert label data is injected into
the notification fields when the alert is in the alerting state. When there are multiple
unique values for the same label, the values are comma-separated.

###### To add alert label data into your alert notification

1. Navigate to the panel that you want to add or edit an alert rule for.
2. Choose the panel title and choose **Edit**.
3. On the **Alert** tab, choose **Create
   Alert**. If an alert already exists for this panel, you can edit it
   directly.
4. Refer to the alert query labels in the alert rule name or the alert
   notification message field by using the `${Label}` syntax. For more
   information about alert query labels, see [Message templating](https://grafana.com/docs/grafana/v8.4/alerting/unified-alerting/message-templating/ "https://grafana.com/docs/grafana/v8.4/alerting/unified-alerting/message-templating/") in the Grafana documentation.
5. Choose **Save** in the upper right corner.
