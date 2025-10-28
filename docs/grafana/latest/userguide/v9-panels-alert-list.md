# Alert list panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The alert list panel displays your dashboards alerts. You can configure the list to
show current state or recent state changes. For more information about alerts, see [Alerts in Grafana version 9](v9-alerts.md "v9-alerts.md").

Use these settings to refine your visualization.

## Options

- Group mode – Choose **Default
  grouping** to show alert instances grouped by their alert rule,
  or **Custom grouping** to group alert instances by a
  custom set of labels.
- Max Items – Set the maximum number of
  alerts to list.
- Sort order – Select how to order the
  alerts displayed.
  - Alphabetical (asc) –
    Alphabetical order
  - Alphabetical (desc) – Reverse
    alphabetical order
  - Importance – By importance
    according to the following values, with 1 being the highest:
    - `alerting` or `firing`: 1
    - `no_data`: 2
    - `pending`: 3
    - `ok`: 4
    - `paused` or `inactive`: 5

- Alerts from this dashboard – Show
  alerts only from the dashboard that the alert list is in.

## Filter

Use the following options to filter the alerts to match the query, folder, or
tags that you choose:

- Alert name – Enter an alert name query.
- Alert instance label – Filter alert
  instances using label querying. For example, `{severity="critical",
instance=~"cluster-us-.+"}`.
- Folder – Select a folder. Only alerts
  from dashboards in the selected folder will be displayed.
- **Datasource** – Filter alerts from the
  selected data source.

## State filter

Choose which alert states to display in this panel.

- Alerting / Firing
- Pending
- No data
- Normal
- Error
