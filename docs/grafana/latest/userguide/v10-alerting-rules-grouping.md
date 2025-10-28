# Namespaces, folders and groups

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Alerts can be organized using folders for Grafana managed rules and namespaces
for Mimir, Loki, or Prometheus rules and group names.

**Namespaces and folders**

When creating Grafana-managed rules, the folder can be used to perform
access control and grant or deny access to all rules within a specific
folder.

A namespace contains one or more groups. The rules within a group are run
sequentially at a regular interval. The default interval is one minute. You can
rename Grafana Mimi or Loki rule namespaces and groups, and edit group
evaluation intervals.

**Groups**

The rules within a group are run sequentially at a regular interval, meaning
no rules will be evaluated at the same time, and in order of appearance. The
default interval is one minute. You can rename Grafana Mimir or Loki rule
namespaces or Loki rule namespaces and groups, and edit group evaluation
intervals.

###### Tip

If you want rules to be
evaluated concurrently and with different intervals, consider storing
them in different groups.

###### Note

Grafana managed alert rules are evaluated concurrently instead of
sequentially.
