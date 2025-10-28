# Sharing a dashboard

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

To share a dashboard, choose **Share dashboard** (the share icon) in
the top navigation bar. This opens the **Share** dialog box, where you
can get a link to the current dashboard with the current selected time range and
template variables. If you have made changes to the dashboard, be sure to save those
changes before you copy the link.

## Dashboard snapshot

A dashboard snapshot is an instant way to share an interactive dashboard
publicly. When creating the snapshot, Amazon Managed Grafana strips sensitive data such as
queries (metric, template, and annotation) and panel links, leaving only the visible
metric data and series names embedded in your dashboard. Dashboard snapshots can be
accessed by anyone who has the link and can reach the URL.

## Publish snapshots

You can publish snapshots to your local instance.
