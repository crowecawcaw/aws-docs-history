# Alertmanager

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Alertmanager enables you to quickly and efficiently manage and respond to alerts.
It receives alerts, handles mutings, inhibition, grouping, and routing by sending
notifications out via your channel of choice, for example, email or Slack.

In Grafana, you can use the Grafana Alertmanager
or an external Alertmanager. You can also run multiple alertmanagers; your
decision depends on your set up and where your alerts are being generated.

**Grafana Alertmanager**

Grafana Alertmanager is an internal Alertmanager that is pre-configured and
available for selection by default.

The Grafana Alertmanager can receive alerts from Grafana, but it cannot receive
alerts from outside Grafana, for example, from Mimir or Loki.

###### Note

Inhibition rules are not supported in the Grafana
Alertmanager.

**External Alertmanager**

If you want to use a single alertmanager to receive all your Grafana, Loki, Mimir,
and Prometheus alerts, you can set up Grafana to use an external Alertmanager. This
external Alertmanager can be configured and administered from within Grafana
itself.

Here are two examples of when you might want to configure your own external
alertmanager and send your alerts there instead of the Grafana Alertmanager:

1. You already have alertmanagers on-premise in your own Cloud
   infrastructure that you have set up and still want to use, because you
   have other alert generators, such as Prometheus.
2. You want to use both Prometheus on-premise and hosted Grafana to send
   alerts to the same alertmanager that runs in your Cloud
   infrastructure.
   Alertmanagers are visible from the dropdown menu on the Alerting Contact
   Points, and Notification Policies pages.

If you are provisioning your data source, set the flag
`handleGrafanaManagedAlerts` in the `jsonData` field to
`true` to send Grafana-managed alerts to this Alertmanager.
