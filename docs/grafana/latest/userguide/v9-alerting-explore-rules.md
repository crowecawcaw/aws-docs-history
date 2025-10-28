# About alert rules

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

An alerting rule is a set of evaluation criteria that determines whether an alert
instance will fire. The rule consists of one or more queries and expressions, a
condition, the frequency of evaluation, and optionally, the duration over which the
condition is met.

While queries and expressions select the data set to evaluate, a condition sets
the threshold that an alert must meet or exceed to create an alert.

An interval specifies how frequently an alerting rule is evaluated. Duration, when
configured, indicates how long a condition must be met. The alert rules can also
define alerting behavior in the absence of data.

###### Topics

- [Alert rule types](v9-alerting-explore-rules-types.md "v9-alerting-explore-rules-types.md")
- [Alert instances](v9-alerting-rules-instances.md "v9-alerting-rules-instances.md")
- [Namespaces and groups](v9-alerting-rules-grouping.md "v9-alerting-rules-grouping.md")
- [Notification
  templating](v9-alerting-rules-notification-templates.md "v9-alerting-rules-notification-templates.md")
