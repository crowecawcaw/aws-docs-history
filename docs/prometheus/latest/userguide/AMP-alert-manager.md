# Managing and forwarding alerts in Amazon Managed Service for Prometheus with alert

manager

When the [alerting rules](AMP-ruler-rulesfile.md "AMP-ruler-rulesfile.md") that Amazon Managed Service for Prometheus runs are
firing, alert manager handles the alerts that are sent. It de-duplicates, groups, and routes
the alerts to downstream receivers. Amazon Managed Service for Prometheus supports only Amazon Simple Notification Service as a receiver, and can
route messages to Amazon SNS topics in the same account. You can also use alert manager to
silence and inhibit alerts.

Alert manager provides similar functionality to Alertmanager in Prometheus.

You can use alert manager's configuration file for the following:

- **Grouping** – Grouping collects similar
  alerts into a single notification. This is especially useful during larger outages
  when many systems fail at once and hundreds of alerts might fire simultaneously. For
  example, suppose that a network failure causes many of your nodes to fail at the
  same time. If these types of alerts are grouped, alert manager sends you a single
  notification.

Alert grouping and the timing for the grouped notifications are configured by a
routing tree in the alert manager configuration file. For more information, see
[<route>](https://prometheus.io/docs/alerting/latest/configuration/#route "https://prometheus.io/docs/alerting/latest/configuration/#route").

- **Inhibition** – Inhibition suppresses
  notifications for certain alerts if certain other alerts are already firing. For
  example, if an alert is firing about a cluster being unreachable, you can configure
  alert manager to mute all other alerts concerning this cluster. This prevents
  notifications for hundreds or thousands of firing alerts that are unrelated to the
  actual issue. For more information about how to write inhibition rules, see [<inhibit_rule>](https://prometheus.io/docs/alerting/latest/configuration/#inhibit_rule "https://prometheus.io/docs/alerting/latest/configuration/#inhibit_rule").
- **Silences** – Silences mute alerts for a
  specified time, such as during a maintenance window. Incoming alerts are checked for
  whether they match all the equality or regular expression matchers of an active
  silence. If they do, no notifications are sent for that alert.

To create a silence, you use the `PutAlertManagerSilences` API. For
more information, see [PutAlertManagerSilences](AMP-APIReference-PutAlertManagerSilences.md "AMP-APIReference-PutAlertManagerSilences.md").
**Prometheus templating**

Standalone Prometheus supports templating, using separate template files. Templates can
use conditionals and format data, among other things.

In Amazon Managed Service for Prometheus, you put your templating in the same alert manager configuration file as your
[alert manager configuration](AMP-alertmanager-config.md "AMP-alertmanager-config.md").

###### Topics

- [Understanding IAM permissions
  needed for working with alert manager](AMP-alertmanager-IAM-permissions.md "AMP-alertmanager-IAM-permissions.md")
- [Create an alert manager configuration in
  Amazon Managed Service for Prometheus to manage and route alerts](AMP-alertmanager-config.md "AMP-alertmanager-config.md")
- [Forward alerts to an alert receiver with
  alert manager in Amazon Managed Service for Prometheus](AMP-alertmanager-receiver.md "AMP-alertmanager-receiver.md")
- [Upload your alert manager configuration file
  to Amazon Managed Service for Prometheus](AMP-alertmanager-upload.md "AMP-alertmanager-upload.md")
- [Integrate alerts with Amazon Managed Grafana or open source
  Grafana](integrating-grafana.md "integrating-grafana.md")
- [Troubleshoot alert manager with CloudWatch Logs](Troubleshooting-alerting.md "Troubleshooting-alerting.md")
