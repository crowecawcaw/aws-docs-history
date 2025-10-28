# Grafana Mimir or

Loki rule groups and namespaces

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can organize your rules. Rules are created within rule groups, and rule groups
are organized into namespaces. The rules within a rule group are run sequentially at
a regular interval. The default interval is one minute. You can rename Grafana Mimir
or Loki namespaces and rule groups, and edit rule group evaluation intervals.

###### To edit a rule group or namespace

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page.
2. Navigate to a rule within the rule group or namespace you want to
   edit.
3. Choose the **Edit** (pen) icon.
4. Make changes to the rule group or namespace.

###### Note

For namespaces, you can only edit the name. For rule groups, you
change the name, or the evaluation interval for rules in the group. For
example, you can choose `1m` to have the rules be evaluated
once per minute, or `30s` to evaluate once every 30
seconds. 5. Choose **Save changes**.
