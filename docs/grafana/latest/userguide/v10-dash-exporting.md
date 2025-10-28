# Exporting dashboards

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can use the Grafana UI or the HTTP API to export dashboards.

The dashboard export action creates a Grafana JSON file that contains everything
you need, including layout, variables, styles, data sources, queries, and so on, so
that you can later import the dashboard.

**Making a dashboard portable**

If you want to export a dashboard for others to use, you can add template
variables for things like a metric prefix (use a constant variable) and server
name.

A template variable of the type `Constant` will automatically be hidden
in the dashboard, and will also be added as a required input when the dashboard is
imported.

###### To export a dashboard

1. Open the dashboard that you want to export.
2. Select the share icon.
3. Choose **Export**.
4. Choose **Save to file.**

###### Note

Grafana downloads a JSON file to your local machine.
