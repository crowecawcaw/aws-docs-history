# Manage your alert rules

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

An alert rule is a set of evaluation criteria that determines whether an alert will
fire. The alert rule consists of one or more queries and expressions, a condition, the
frequency of evaluation, and optionally, the duration over which the condition is
met.

While queries and expressions select the data set to evaluate, a condition sets the
threshold that an alert must meet or exceed to create an alert. An interval specifies
how frequently an alert rule is evaluated. Duration, when configured, indicates how long
a condition must be met. Alert rules can also define alerting behavior in the absence of
data.

###### Note

Grafana managed alert rules can only be edited
or deleted by users with Edit permissions for the folder storing the rules.

Alert rules for an external Grafana Mimir or Loki instance can be edited or
deleted by users with Editor or Admin roles.

###### Topics

- [Creating Grafana managed
  alert rules](v9-alerting-managerules-grafana.md "v9-alerting-managerules-grafana.md")
- [Creating Grafana Mimir
  or Loki managed alert rules](v9-alerting-managerules-mimir-loki.md "v9-alerting-managerules-mimir-loki.md")
- [Creating Grafana
  Mimir or Loki managed recording rules](v9-alerting-managerules-mimir-loki-recording.md "v9-alerting-managerules-mimir-loki-recording.md")
- [Grafana Mimir or
  Loki rule groups and namespaces](v9-alerting-managerules-mimir-loki-groups.md "v9-alerting-managerules-mimir-loki-groups.md")
- [View and edit alerting rules](v9-alerting-managerules-view-edit.md "v9-alerting-managerules-view-edit.md")
