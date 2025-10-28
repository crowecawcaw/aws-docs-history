# Exporting and importing dashboards

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Amazon Managed Grafana Dashboards can easily be exported and imported, either from the UI or from
the [HTTP API]

## Exporting a dashboard

Dashboards are exported in Amazon Managed Grafana JSON format, and contain everything you
need, including layout, variables, styles, data sources, and queries, to import the
dashboard at a later time.

The export feature is accessed in the share window, which you open by choosing
the share button in the dashboard menu.

### Making a dashboard

portable

When you export a dashboard for others to use, it's good to add template
variables for values such as a metric prefix (use a constant variable) and a
server name.

A template variable of the type `Constant` is automatically hidden
in the dashboard. It is also added as a required input when the dashboard is
imported. For more information about templating and template variables, see
[Templates and variables](templates-and-variables.md "templates-and-variables.md").

## Importing a dashboard

To import a dashboard, choose the + icon in the side menu, and then choose
**Import**.

You can upload a dashboard JSON file, paste a dashboard URL or paste dashboard
JSON text directly into the text area.

In step 2 of the import process, you can change the name of the dashboard,
specify the data source that you want the dashboard to use, and specify any metric
prefixes (if the dashboard uses any).

## Discover dashboards on

Grafana.com

Find dashboards for common server applications at [Grafana.com/dashboards](https://grafana.com/dashboards "https://grafana.com/dashboards").
