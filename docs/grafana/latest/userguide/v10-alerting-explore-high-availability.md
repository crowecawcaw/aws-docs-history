# Alerting high availability

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Amazon Managed Grafana is configured for high availability, including running multiple
instances across multiple availability zones for each workspace that you create.

Grafana Alerting uses the Prometheus model of separating the evaluation of alert
rules from the delivering of notifications. In this model the evaluation of alert
rules is done in the alert generator and the delivering of notifications is done in
the alert receiver. In Grafana Alerting, the alert generator is the Scheduler and
the receiver is the Alertmanager.

With high availability configurations, all alert rules are evaluated on all
instances. You can think of the evaluation of alert rules as being duplicated. This
is how Grafana Alerting makes sure that as long as at least one Grafana instance is
working, alert rules will still be evaluated and notifications for alerts will
still be sent. You will see this duplication in state history, and is a good way to
tell if you are using high availability.
