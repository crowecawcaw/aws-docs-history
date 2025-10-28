# Namespaces and groups

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Alerts can be organized using Folders for Grafana-managed rules and namespaces
for Mimir, Loki, or Prometheus rules and group names.

**Namespaces**

When creating Grafana-managed rules, the folder can be used to perform
access control and grant or deny access to all rules within a specific
folder.

**Groups**

All rules within a group are evaluated at the same **interval**.

Alert rules and recording rules within a group will always be evaluated
**sequentially**, meaning no rules will be
evaluated at the same time and in order of appearance.

###### Tip

If you want rules to be
evaluated concurrently and with different intervals, consider storing
them in different groups.
